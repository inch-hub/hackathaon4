import os
import sqlite3
from datetime import datetime, timezone
from flask import Flask, request, jsonify, redirect, session, abort
from itsdangerous import URLSafeTimedSerializer, BadSignature, SignatureExpired

# ==============
# ONE-FILE HTML
# ==============
INDEX_HTML = """
<!doctype html>
<html>
<head>
  <meta charset="utf-8"/>
  <style>
    body{margin:0;font-family:system-ui;display:grid;place-items:center;min-height:100vh;
         background:linear-gradient(135deg,#0a1f44,#0066ff);color:#fff}
    .card{width:min(480px,92vw);background:rgba(255,255,255,.12);backdrop-filter:blur(14px);
          padding:28px;border-radius:20px;box-shadow:0 6px 24px rgba(0,0,0,.35)}
    input,button{width:100%;padding:12px;border:none;border-radius:12px;margin:8px 0 12px;outline:none}
    button{background:#0b61ff;color:#fff;font-weight:700;cursor:pointer}
    button:hover{background:#003ea6}
    .note{opacity:.8;font-size:12px;margin-top:8px}
  </style>
</head>
<body>
  <div class="card">
    <h2 style="margin:0 0 10px">Login with Email</h2>
    <input id="email" placeholder="you@college.edu" autocomplete="email"/>
    <button id="sendBtn">Send Magic Link</button>
    <div id="msg" class="note"></div>
  </div>

<script>
const sendBtn=document.getElementById("sendBtn");
sendBtn.onclick=async()=>{
  const email=document.getElementById("email").value.trim().toLowerCase();
  document.getElementById("msg").textContent="Processing...";
  let res=await fetch("/api/magic",{
    method:"POST",
    headers:{"Content-Type":"application/json"},
    body:JSON.stringify({email})
  });
  let data=await res.json();
  if(data.ok){
     document.getElementById("msg").innerHTML=
      "Magic link sent!<br><a href='"+data.preview+"'>Preview Email (Dev)</a>";
  }else{
     document.getElementById("msg").textContent=data.error;
  }
}
</script>
</body>
</html>
"""

EMAIL_PREVIEW = """
<!doctype html>
<html><body style="font-family:system-ui;padding:20px">
<h3>Email Preview</h3>
<b>Subject:</b> {subject}<br><br>
{body}
</body></html>
"""

DASHBOARD = """
<!doctype html>
<html><body style="font-family:system-ui;padding:40px;background:#0b1220;color:white">
<h2>✅ Logged in</h2>
<p>You are logged in as <b>{email}</b></p>
<a href="/logout" style="color:#0b61ff;font-weight:700">Logout</a>
</body></html>
"""

# ======================================
# BACKEND (ALL IN ONE FILE)
# ======================================
app = Flask(__name__)
app.secret_key = "super-secret-key"
serializer = URLSafeTimedSerializer(app.secret_key)

DB = "users.sqlite3"


def db():
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    with db() as conn:
        conn.execute("""
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT UNIQUE NOT NULL,
            created_at TEXT NOT NULL
        );
        """)
        conn.commit()


@app.before_request
def startup():
    init_db()


def create_magic_link(email):
    token = serializer.dumps({"email": email})
    return f"http://127.0.0.1:5000/auth?token={token}"


def generate_email(email, link):
    subject = "Your Secure Login Link"
    body = f"""
    <h2>Placement Portal Login</h2>
    <p>Hello <b>{email}</b>,</p>
    <p>Click below to log in instantly:</p>
    <p><a href="{link}" style="padding:12px 16px;background:#0066ff;color:white;
       border-radius:10px;text-decoration:none;">Login</a></p>
    <p>Expires in 10 minutes.</p>
    """
    return subject, body


@app.route("/")
def index():
    return INDEX_HTML


@app.route("/api/magic", methods=["POST"])
def send_magic():
    email = (request.json or {}).get("email","").lower().strip()
    if not email or "@" not in email:
        return jsonify({"ok": False, "error": "Valid email required"})

    with db() as conn:
        row = conn.execute("SELECT id FROM users WHERE email=?", (email,)).fetchone()
        if not row:
            conn.execute(
                "INSERT INTO users(email, created_at) VALUES(?,?)",
                (email, datetime.now(timezone.utc).isoformat())
            )
            conn.commit()

    link = create_magic_link(email)
    subject, body = generate_email(email, link)

    # Dev mode: just preview instead of sending
    preview_token = serializer.dumps({"email": email})
    return jsonify({"ok": True, "preview": f"/preview?token={preview_token}"})


@app.route("/preview")
def preview():
    token = request.args.get("token", "")
    try:
        data = serializer.loads(token, max_age=3600)
        email = data["email"]
    except:
        return "Invalid"

    link = create_magic_link(email)
    subject, body = generate_email(email, link)
    return EMAIL_PREVIEW.format(subject=subject, body=body)


@app.route("/auth")
def auth():
    token = request.args.get("token","")
    if not token:
        abort(400)
    try:
        data = serializer.loads(token, max_age=600)
        email = data["email"]
    except SignatureExpired:
        return "Link expired", 401
    except BadSignature:
        return "Invalid link", 400

    session["email"] = email
    return redirect("/dashboard")


@app.route("/dashboard")
def dash():
    if "email" not in session:
        return redirect("/")
    return DASHBOARD.format(email=session["email"])


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


if __name__ == "__main__":
    app.run(port=5000, debug=False)
