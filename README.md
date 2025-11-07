<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Tech Login System</title>
  <style>
    :root{
      --bg1:#0a1f44; --bg2:#0066ff; --glass:rgba(255,255,255,.1);
      --btn:#0066ff; --btnH:#003399; --ok:#00cc66; --okH:#00994d;
      --text:#fff;
    }
    *{box-sizing:border-box}
    body{
      margin:0; font-family:'Poppins',sans-serif; height:100vh;
      display:flex; justify-content:space-between; align-items:center;
      background:linear-gradient(135deg,var(--bg1),var(--bg2)); color:var(--text);
      overflow:hidden;
    }
    .container,.quotes{width:50%; height:100%; display:flex; justify-content:center; align-items:center}
    .stack{width:100%; display:grid; place-items:center}
    .card{
      width:70%; max-width:520px; padding:28px; border-radius:20px;
      background:var(--glass); backdrop-filter:blur(16px);
      box-shadow:0 0 20px rgba(0,0,0,.3); animation:fadeIn .8s ease; display:none;
    }
    .active{display:block}
    h2{margin:0 0 8px; text-transform:uppercase; font-size:26px}
    .muted{opacity:.85; font-size:13px; margin-bottom:8px}
    input,select,button{
      width:100%; padding:12px; margin:8px 0 12px; border:none; border-radius:10px; outline:none;
    }
    button{background:var(--btn); color:#fff; font-weight:700; cursor:pointer}
    button:hover{background:var(--btnH)}
    .link{display:inline-block; margin-top:4px; text-decoration:underline; cursor:pointer}
    .row{display:flex; gap:10px}
    .row>div{flex:1}
    .chips{display:flex; gap:8px; flex-wrap:wrap; margin:8px 0}
    .chip{padding:6px 10px; border-radius:999px; background:rgba(255,255,255,.15); font-size:12px}
    /* upload */
    .upload-wrap{display:flex; gap:10px; align-items:center}
    .upload-btn{background:var(--ok)}
    .upload-btn:hover{background:var(--okH)}
    input[type=file]{display:none}
    .file-name{font-size:12px; opacity:.9}
    /* tables */
    table{width:100%; border-collapse:collapse; margin-top:8px; font-size:14px}
    th,td{padding:10px 8px; text-align:left; border-bottom:1px solid rgba(255,255,255,.15)}
    th{opacity:.8; font-weight:600}
    .status{font-size:12px; padding:4px 8px; border-radius:999px; background:rgba(255,255,255,.15)}
    /* quotes */
    .quotes{flex-direction:column; padding:50px}
    .quote{font-size:36px; font-weight:800; display:none; text-shadow:2px 2px 10px rgba(0,0,0,.5)}
    .quote.active{display:block}
    @keyframes fadeIn{from{opacity:0; transform:translateY(16px)} to{opacity:1; transform:translateY(0)}}
    @media (max-width:900px){
      body{flex-direction:column; overflow:auto}
      .container,.quotes{width:100%; height:auto}
      .quotes{padding:28px}
      .quote{font-size:26px; text-align:center}
      .card{width:92%}
    }
  </style>
</head>
<body>

  <!-- LEFT: App screens -->
  <div class="container">
    <div class="stack">

      <!-- LOGIN -->
      <div class="card active" id="login-box">
        <h2>Welcome Back!</h2>
        <div class="muted">Choose your role and sign in to continue.</div>
        <select id="roleSelect">
          <option value="">Select Role</option>
          <option value="student">Student</option>
          <option value="hod">HOD</option>
          <option value="placement">Placement Officer</option>
        </select>
        <input id="usernameInput" placeholder="Username"/>
        <input id="passwordInput" type="password" placeholder="Password"/>
        <button id="loginBtn">Next</button>
        <div>
          <span class="link" onclick="show('signup-box')">Create Account</span> ·
          <span class="link" onclick="show('forgot-box')">Forgot Password?</span>
        </div>
      </div>

      <!-- SIGNUP -->
      <div class="card" id="signup-box">
        <h2>Join Us</h2>
        <div class="muted">Create your account to get started.</div>
        <div class="row">
          <div><input placeholder="Username"></div>
          <div><input type="email" placeholder="Email"></div>
        </div>
        <select>
          <option>Select Role</option><option>Student</option><option>HOD</option><option>Placement Officer</option>
        </select>
        <input type="password" placeholder="Password"/>
        <button onclick="show('login-box')">Sign Up</button>
        <div><span class="link" onclick="show('login-box')">Already have an account?</span></div>
      </div>

      <!-- FORGOT -->
      <div class="card" id="forgot-box">
        <h2>Reset Password</h2>
        <input type="email" placeholder="Enter your email"/>
        <button onclick="alert('Reset link sent (demo).')">Send Reset Link</button>
        <div><span class="link" onclick="show('login-box')">Back to Login</span></div>
      </div>

      <!-- STUDENT FORM -->
      <div class="card" id="student-form">
        <h2>Student Details</h2>
        <div class="row">
          <div><input id="stName" placeholder="Full Name"/></div>
          <div><input id="stReg" placeholder="Register Number"/></div>
        </div>
        <div class="upload-wrap">
          <input type="file" id="resumeFile" accept=".pdf,.doc,.docx"/>
          <button class="upload-btn" id="resumeBtn" type="button">Upload Resume</button>
          <span id="resumeName" class="file-name">No file chosen</span>
        </div>
        <button id="studentSubmit">Submit & Continue</button>
        <div><span class="link" onclick="show('login-box')">Logout</span></div>
      </div>

      <!-- STUDENT DASHBOARD -->
      <div class="card" id="student-page">
        <h2>Student Dashboard</h2>
        <div id="studentSummary" class="chips"></div>
        <div class="muted">Your submission</div>
        <table>
          <tr><th>Field</th><th>Value</th></tr>
          <tr><td>Name</td><td id="s_name">-</td></tr>
          <tr><td>Register No.</td><td id="s_reg">-</td></tr>
          <tr><td>Resume</td><td id="s_resume">-</td></tr>
        </table>
        <div><span class="link" onclick="show('login-box')">Logout</span></div>
      </div>

      <!-- HOD FORM -->
      <div class="card" id="hod-form">
        <h2>HOD Details</h2>
        <input id="hodCollege" placeholder="College Name"/>
        <input id="hodExp" type="number" min="0" placeholder="Years of Experience"/>
        <button id="hodSubmit">Submit & Continue</button>
        <div><span class="link" onclick="show('login-box')">Logout</span></div>
      </div>

      <!-- HOD DASHBOARD -->
      <div class="card" id="hod-page">
        <h2>HOD Dashboard</h2>
        <div id="hodSummary" class="chips"></div>
        <div class="muted">Registered Students</div>
        <table id="hodTable">
          <thead>
            <tr><th>Name</th><th>Register #</th><th>Resume</th><th>Approved</th><th>Action</th></tr>
          </thead>
          <tbody></tbody>
        </table>
        <div><span class="link" onclick="show('login-box')">Logout</span></div>
      </div>

      <!-- PLACEMENT FORM -->
      <div class="card" id="placement-form">
        <h2>Placement Officer Details</h2>
        <input id="plCollege" placeholder="College Name"/>
        <input id="plExp" type="number" min="0" placeholder="Years of Experience"/>
        <button id="plSubmit">Submit & Continue</button>
        <div><span class="link" onclick="show('login-box')">Logout</span></div>
      </div>

      <!-- PLACEMENT DASHBOARD -->
      <div class="card" id="placement-page">
        <h2>Placement Dashboard</h2>
        <div id="plSummary" class="chips"></div>
        <button onclick="show('placement-verification')">Verify Credentials</button>
        <div class="muted" style="margin-top:12px">HOD-approved students</div>
        <table id="plTable">
          <thead>
            <tr><th>Name</th><th>Register #</th><th>Resume</th><th>Status</th></tr>
          </thead>
          <tbody></tbody>
        </table>
        <div><span class="link" onclick="show('login-box')">Logout</span></div>
      </div>

      <!-- PLACEMENT VERIFICATION -->
      <div class="card" id="placement-verification">
        <h2>Credential Verification</h2>
        <input id="staffCode" placeholder="Enter Staff Code"/>
        <div class="row">
          <div><input id="otpInput" type="number" placeholder="Enter OTP"/></div>
          <div><button id="sendOtpBtn" type="button">Send OTP</button></div>
        </div>
        <div id="otpMsg" class="muted"></div>
        <button id="verifyBtn">Verify & Continue</button>
        <div><span class="link" onclick="show('placement-page')">Back</span></div>
      </div>

      <!-- PLACEMENT VERIFIED -->
      <div class="card" id="placement-verified-page">
        <h2>Access Granted ✅</h2>
        <div class="chips" id="plVerifiedChips"></div>
        <div class="muted">You now have elevated access.</div>
        <div><span class="link" onclick="show('login-box')">Logout</span></div>
      </div>

    </div>
  </div>

  <!-- RIGHT: Quotes -->
  <div class="quotes">
    <div class="quote active">“Every code starts a journey.”</div>
    <div class="quote">“Dream it. Build it. Launch it.”</div>
    <div class="quote">“Ideas don’t wait. Start now.”</div>
    <div class="quote">“Your startup story begins here.”</div>
  </div>

  <script>
    // ---------- helpers ----------
    const $ = (id)=>document.getElementById(id);
    function show(id){
      document.querySelectorAll('.card').forEach(el=>el.classList.remove('active'));
      $(id).classList.add('active');
    }
    function chip(text){ const d=document.createElement('span'); d.className='chip'; d.textContent=text; return d; }
    function load(key, fallback){ try{ return JSON.parse(localStorage.getItem(key)) ?? fallback; } catch { return fallback; } }
    function save(key, val){ localStorage.setItem(key, JSON.stringify(val)); }

    // ---------- quotes ----------
    const quotes = document.querySelectorAll('.quote');
    let qi=0; setInterval(()=>{ quotes.forEach(q=>q.classList.remove('active')); quotes[qi].classList.add('active'); qi=(qi+1)%quotes.length; },3000);

    // ---------- login flow ----------
    $("loginBtn").addEventListener("click", ()=>{
      const role = $("roleSelect").value;
      const user = $("usernameInput").value.trim();
      if(!role){ alert("Please select a role."); return; }
      if(!user){ alert("Please enter your username."); return; }
      save("currentUser", { username:user, role });
      if(role==="student") show("student-form");
      if(role==="hod") show("hod-form");
      if(role==="placement") show("placement-form");
    });

    // ---------- Student: upload + save ----------
    $("resumeBtn").addEventListener("click", ()=> $("resumeFile").click());
    $("resumeFile").addEventListener("change", (e)=>{
      const f=e.target.files[0];
      $("resumeName").textContent = f ? f.name : "No file chosen";
    });

    $("studentSubmit").addEventListener("click", ()=>{
      const name = $("stName").value.trim();
      const reg  = $("stReg").value.trim();
      const file = $("resumeFile").files[0];
      if(!name || !reg){ alert("Please fill name and register number."); return; }
      if(!file){ alert("Please upload your resume."); return; }

      const students = load("students", []);
      const existingIndex = students.findIndex(s=>s.reg===reg);
      const record = { name, reg, resume:file.name, approved:false };
      if(existingIndex>=0) students[existingIndex]=record; else students.push(record);
      save("students", students);
      save("studentSelf", record);

      renderStudentDashboard();
      // also refresh other dashboards later
      show("student-page");
    });

    function renderStudentDashboard(){
      const st = load("studentSelf", null);
      $("studentSummary").innerHTML="";
      if(st){
        $("studentSummary").append(chip("Hello, "+st.name), chip("Reg: "+st.reg), chip("Resume: "+st.resume));
        $("s_name").textContent = st.name;
        $("s_reg").textContent  = st.reg;
        $("s_resume").textContent = st.resume;
      }
    }

    // ---------- HOD: save + table ----------
    $("hodSubmit").addEventListener("click", ()=>{
      const college = $("hodCollege").value.trim();
      const exp = $("hodExp").value.trim();
      if(!college || exp===""){ alert("Please fill college and experience."); return; }
      const hod = { college, exp:Number(exp) };
      save("hodProfile", hod);
      renderHOD();
      show("hod-page");
    });

    function renderHOD(){
      const hod = load("hodProfile", null);
      const wrap = $("hodSummary"); wrap.innerHTML="";
      if(hod){ wrap.append( chip(hod.college), chip(hod.exp+" yrs exp") ); }
      const tbody = $("hodTable").querySelector("tbody");
      tbody.innerHTML="";
      const students = load("students", []);
      students.forEach((s,idx)=>{
        const tr=document.createElement("tr");
        tr.innerHTML = `
          <td>${s.name}</td>
          <td>${s.reg}</td>
          <td>${s.resume || "-"}</td>
          <td><span class="status">${s.approved ? "Approved" : "Pending"}</span></td>
          <td><button data-i="${idx}" class="approveBtn">${s.approved ? "Revoke" : "Approve"}</button></td>
        `;
        tbody.appendChild(tr);
      });
      tbody.querySelectorAll(".approveBtn").forEach(btn=>{
        btn.addEventListener("click", (e)=>{
          const i = Number(e.target.getAttribute("data-i"));
          const list = load("students", []);
          list[i].approved = !list[i].approved;
          save("students", list);
          renderHOD();
          renderPlacement(); // keep placement table in sync
        });
      });
    }

    // ---------- Placement: save, verify, approved list ----------
    $("plSubmit").addEventListener("click", ()=>{
      const college = $("plCollege").value.trim();
      const exp = $("plExp").value.trim();
      if(!college || exp===""){ alert("Please fill college and experience."); return; }
      const pl = { college, exp:Number(exp), verified:false };
      save("placementProfile", pl);
      renderPlacement();
      show("placement-page");
    });

    function renderPlacement(){
      const pl = load("placementProfile", null);
      const wrap = $("plSummary"); wrap.innerHTML="";
      if(pl){
        wrap.append( chip(pl.college), chip(pl.exp+" yrs exp"), chip(pl.verified ? "Verified" : "Not Verified") );
      }
      const tbody = $("plTable").querySelector("tbody");
      tbody.innerHTML="";
      const approved = load("students", []).filter(s=>s.approved);
      approved.forEach(s=>{
        const tr=document.createElement("tr");
        tr.innerHTML = `<td>${s.name}</td><td>${s.reg}</td><td>${s.resume||"-"}</td><td><span class="status">HOD Approved</span></td>`;
        tbody.appendChild(tr);
      });
    }

    // OTP system (demo)
    let currentOTP = null;
    $("sendOtpBtn").addEventListener("click", ()=>{
      currentOTP = String(Math.floor(100000 + Math.random()*900000)); // 6-digit
      $("otpMsg").textContent = "OTP sent (demo): " + currentOTP + "  (Replace with SMS/Email in production)";
      $("otpMsg").style.opacity = 1;
      setTimeout(()=>{ $("otpMsg").style.opacity=.75; }, 100);
    });

    $("verifyBtn").addEventListener("click", ()=>{
      const code = $("staffCode").value.trim();
      const otp  = $("otpInput").value.trim();
      if(!code){ alert("Enter Staff Code"); return; }
      if(!otp){ alert("Enter OTP"); return; }
      if(!currentOTP){ alert("Please click 'Send OTP' first."); return; }
      if(otp !== currentOTP){ alert("Invalid OTP. Try again."); return; }

      // mark verified
      const pl = load("placementProfile", null) || {};
      pl.verified = true; save("placementProfile", pl);
      $("plVerifiedChips").innerHTML="";
      $("plVerifiedChips").append( chip("Staff Code: "+code), chip("Verified") );
      renderPlacement();
      show("placement-verified-page");
    });

    // ---------- when entering dashboards, render from storage ----------
    // When switching to HOD or Placement page via show(), we also refresh their data.
    const _show = show;
    show = function(id){
      _show(id);
      if(id==="student-page") renderStudentDashboard();
      if(id==="hod-page") renderHOD();
      if(id==="placement-page") renderPlacement();
      if(id==="placement-verified-page"){
        const pl = load("placementProfile", null);
        $("plVerifiedChips").innerHTML="";
        if(pl){
          $("plVerifiedChips").append( chip(pl.college), chip(pl.exp+" yrs exp"), chip("Verified") );
        }
      }
    };
  </script>
</body>
</html>
