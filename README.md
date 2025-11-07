<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>Placement Portal</title>

<style>
:root{
  --bg1:#0a1f44; --bg2:#0066ff; --glass:rgba(255,255,255,.12);
  --btn:#0066ff; --btnH:#003ea6; --ok:#00cc66; --okH:#079455;
  --text:#fff;
}
*{box-sizing:border-box}
body{
  margin:0; font-family:system-ui,-apple-system,Segoe UI,Roboto,Ubuntu,"Helvetica Neue",Arial,sans-serif;
  height:100vh; display:flex; justify-content:space-between; align-items:center;
  background:linear-gradient(135deg,var(--bg1),var(--bg2)); color:var(--text);
  overflow:hidden;
}
.container,.quotes{width:50%; height:100%; display:flex; justify-content:center; align-items:center}
.stack{width:100%; display:grid; place-items:center}
.card{
  width:72%; max-width:560px; padding:28px; border-radius:20px;
  background:var(--glass); backdrop-filter:blur(16px);
  box-shadow:0 6px 24px rgba(0,0,0,.35); animation:fadeIn .6s ease; display:none;
}
.active{display:block}
h2{margin:0 0 10px; text-transform:uppercase; font-size:26px; letter-spacing:.4px}
.muted{opacity:.9; font-size:13px; margin-bottom:8px}
input,select,button{
  width:100%; padding:12px; margin:8px 0 12px; border:none; border-radius:12px; outline:none;
}
button{background:var(--btn); color:#fff; font-weight:700; cursor:pointer}
button:hover{background:var(--btnH)}
.link{display:inline-block; margin-top:4px; text-decoration:underline; cursor:pointer}
.row{display:flex; gap:10px}
.row>div{flex:1}
.upload-wrap{display:flex; gap:10px; align-items:center}
.upload-btn{background:var(--ok)}
.upload-btn:hover{background:var(--okH)}
.file-name{font-size:12px; opacity:.9}
.chips{display:flex; gap:8px; flex-wrap:wrap; margin:8px 0}
.chip{padding:6px 10px; border-radius:999px; background:rgba(255,255,255,.18); font-size:12px}
table{width:100%; border-collapse:collapse; margin-top:8px; font-size:14px}
th,td{padding:10px 8px; text-align:left; border-bottom:1px solid rgba(255,255,255,.18)}
th{opacity:.85; font-weight:600}
.status{font-size:12px; padding:4px 8px; border-radius:999px; background:rgba(255,255,255,.18)}
.quotes{flex-direction:column; padding:50px}
.quote{font-size:36px; font-weight:800; display:none; text-shadow:2px 2px 10px rgba(0,0,0,.4)}
.quote.active{display:block}

/* Horizontal role cards with avatar (Option A: simple hover zoom/highlight) */
.role-grid{
  display:flex; flex-direction:row; justify-content:space-between; gap:18px;
  width:100%; margin-top:16px;
}
.role-card{
  flex:1; padding:22px; border-radius:16px;
  background:rgba(255,255,255,.18);
  text-align:center; cursor:pointer; user-select:none;
  transition:transform .18s ease, background .18s ease, box-shadow .18s ease;
  box-shadow:0 6px 16px rgba(0,0,0,.25);
}
.role-card:hover{ transform:scale(1.05); background:rgba(255,255,255,.32) }
.role-avatar{ width:80px; height:80px; margin-bottom:10px; border-radius:12px }
.role-title{ font-size:20px; font-weight:800; letter-spacing:.2px }

/* Responsive */
@media(max-width:1024px){
  .card{width:90%}
}
@media(max-width:900px){
  body{flex-direction:column; overflow:auto}
  .container,.quotes{width:100%; height:auto}
  .quote{font-size:26px; text-align:center}
  .card{width:92%}
  .role-grid{flex-direction:column}
}
@keyframes fadeIn{from{opacity:0; transform:translateY(14px)} to{opacity:1; transform:translateY(0)}}
</style>
</head>

<body>

<div class="container">
  <div class="stack">

    <!-- ROLE SELECTION (HORIZONTAL BOXES + AVATARS) -->
    <div class="card active" id="role-box" style="text-align:center">
      <h2>Welcome!</h2>
      <div class="muted">Select your role to continue.</div>

      <div class="role-grid">
        <div class="role-card" id="roleStudent" title="Continue as Student">
          <img src="https://cdn-icons-png.flaticon.com/512/2922/2922510.png" class="role-avatar" alt="Student">
          <div class="role-title">Student</div>
        </div>
        <div class="role-card" id="roleHod" title="Continue as HOD">
          <img src="https://cdn-icons-png.flaticon.com/512/3209/3209265.png" class="role-avatar" alt="HOD">
          <div class="role-title">HOD</div>
        </div>
        <div class="role-card" id="rolePlacement" title="Continue as Placement Officer">
          <img src="https://cdn-icons-png.flaticon.com/512/924/924874.png" class="role-avatar" alt="Placement Officer">
          <div class="role-title">Placement Officer</div>
        </div>
      </div>
    </div>

    <!-- ===================== STUDENT STACK ===================== -->
    <div class="card" id="student-login">
      <h2>Student Login</h2>
      <input id="stuUser" placeholder="Username"/>
      <input id="stuPass" type="password" placeholder="Password"/>
      <button id="stuLoginBtn">Login</button>
      <div>
        <span class="link" onclick="show('student-signup')">Sign Up</span> ·
        <span class="link" onclick="show('student-forgot')">Forgot Password?</span> ·
        <span class="link" onclick="show('role-box')">Back</span>
      </div>
    </div>

    <div class="card" id="student-signup">
      <h2>Student Sign Up</h2>
      <input id="stuNewUser" placeholder="New Username"/>
      <input id="stuNewPass" type="password" placeholder="Create Password"/>
      <input id="stuPhone" type="tel" placeholder="Phone Number"/>
      <button id="stuSendOtp" type="button">Send OTP</button>
      <input id="stuOtpInput" type="number" placeholder="Enter OTP"/>
      <button id="stuSignupBtn">Create Account</button>
      <div id="stuOtpMsg" class="muted"></div>
      <div><span class="link" onclick="show('student-login')">Back to Login</span></div>
    </div>

    <div class="card" id="student-forgot">
      <h2>Reset Password</h2>
      <input id="stuEmailReset" placeholder="Enter Email"/>
      <button onclick="alert('Reset link sent (demo).')">Send Reset Link</button>
      <div><span class="link" onclick="show('student-login')">Back</span></div>
    </div>

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
      <div><span class="link" onclick="show('role-box')">Logout</span></div>
    </div>

    <div class="card" id="student-page">
      <h2>Student Dashboard</h2>
      <div id="studentSummary" class="chips"></div>
      <table>
        <tr><th>Field</th><th>Value</th></tr>
        <tr><td>Name</td><td id="s_name">-</td></tr>
        <tr><td>Register No.</td><td id="s_reg">-</td></tr>
        <tr><td>Resume</td><td id="s_resume">-</td></tr>
      </table>
      <div><span class="link" onclick="show('role-box')">Logout</span></div>
    </div>

    <!-- ===================== HOD STACK ===================== -->
    <div class="card" id="hod-login">
      <h2>HOD Login</h2>
      <input id="hodUser" placeholder="Staff ID"/>
      <input id="hodPass" type="password" placeholder="Password"/>
      <button id="hodLoginBtn">Login</button>
      <div>
        <span class="link" onclick="show('hod-signup')">Sign Up</span> ·
        <span class="link" onclick="show('hod-forgot')">Forgot Password?</span> ·
        <span class="link" onclick="show('role-box')">Back</span>
      </div>
    </div>

    <div class="card" id="hod-signup">
      <h2>HOD Sign Up</h2>
      <input id="hodNewUser" placeholder="Staff ID"/>
      <input id="hodNewPass" type="password" placeholder="Create Password"/>
      <input id="hodPhone2" type="tel" placeholder="Phone Number"/>
      <button id="hodSendOtp" type="button">Send OTP</button>
      <input id="hodOtpInput2" type="number" placeholder="Enter OTP"/>
      <button id="hodSignupBtn">Create Account</button>
      <div id="hodOtpMsg2" class="muted"></div>
      <div><span class="link" onclick="show('hod-login')">Back to Login</span></div>
    </div>

    <div class="card" id="hod-forgot">
      <h2>Reset Password</h2>
      <input id="hodEmailReset" placeholder="Enter Email"/>
      <button onclick="alert('Reset link sent (demo).')">Send Reset Link</button>
      <div><span class="link" onclick="show('hod-login')">Back</span></div>
    </div>

    <div class="card" id="hod-form">
      <h2>HOD Verification</h2>
      <input id="hodStaff" placeholder="Staff ID"/>
      <input id="hodPhone" type="tel" placeholder="Phone Number"/>
      <input id="hodDept" placeholder="Department (Optional)"/>
      <button id="hodSendOtpMain" type="button">Send Verification Code</button>
      <input id="hodOtpInput" type="number" placeholder="Enter Verification Code"/>
      <div id="hodOtpMsg" class="muted"></div>
      <button id="hodSubmit">Verify & Continue</button>
      <div><span class="link" onclick="show('role-box')">Logout</span></div>
    </div>

    <div class="card" id="hod-page">
      <h2>HOD Dashboard</h2>
      <div id="hodSummary" class="chips"></div>
      <table id="hodTable">
        <thead>
          <tr><th>Name</th><th>Register #</th><th>Resume</th><th>Approved</th><th>Action</th></tr>
        </thead>
        <tbody></tbody>
      </table>
      <div><span class="link" onclick="show('role-box')">Logout</span></div>
    </div>

    <!-- ===================== PLACEMENT STACK ===================== -->
    <div class="card" id="placement-login">
      <h2>Placement Login</h2>
      <input id="plUser" placeholder="Staff ID"/>
      <input id="plPass" type="password" placeholder="Password"/>
      <button id="plLoginBtn">Login</button>
      <div>
        <span class="link" onclick="show('placement-signup')">Sign Up</span> ·
        <span class="link" onclick="show('placement-forgot')">Forgot Password?</span> ·
        <span class="link" onclick="show('role-box')">Back</span>
      </div>
    </div>

    <div class="card" id="placement-signup">
      <h2>Placement Sign Up</h2>
      <input id="plNewUser" placeholder="Staff ID"/>
      <input id="plNewPass" type="password" placeholder="Create Password"/>
      <input id="plPhone2" type="tel" placeholder="Phone Number"/>
      <button id="plSendOtp2" type="button">Send OTP</button>
      <input id="plOtpInput2" type="number" placeholder="Enter OTP"/>
      <button id="plSignupBtn">Create Account</button>
      <div id="plOtpMsg2" class="muted"></div>
      <div><span class="link" onclick="show('placement-login')">Back to Login</span></div>
    </div>

    <div class="card" id="placement-forgot">
      <h2>Reset Password</h2>
      <input id="plEmailReset" placeholder="Enter Email"/>
      <button onclick="alert('Reset link sent (demo).')">Send Reset Link</button>
      <div><span class="link" onclick="show('placement-login')">Back</span></div>
    </div>

    <div class="card" id="placement-form">
      <h2>Placement Officer Verification</h2>
      <input id="plStaff" placeholder="Staff ID (MANDATORY)"/>
      <input id="plPhone" type="tel" placeholder="Phone Number (MANDATORY)"/>
      <input id="plDept" placeholder="Authorized Department (MANDATORY)"/>
      <button id="plSendOtp" type="button">Send Verification Code</button>
      <input id="plOtpInput" type="number" placeholder="Enter OTP (MANDATORY)"/>
      <div id="plOtpMsg" class="muted"></div>
      <button id="plSubmit">Verify & Continue</button>
      <div><span class="link" onclick="show('role-box')">Logout</span></div>
    </div>

    <div class="card" id="placement-page">
      <h2>Placement Dashboard</h2>
      <div id="plSummary" class="chips"></div>
      <div class="muted" style="margin-top:8px">HOD-approved students</div>
      <table id="plTable">
        <thead>
          <tr><th>Name</th><th>Register #</th><th>Resume</th><th>Status</th></tr>
        </thead>
        <tbody></tbody>
      </table>
      <div><span class="link" onclick="show('role-box')">Logout</span></div>
    </div>

  </div>
</div>

<div class="quotes">
  <div class="quote active">“Every code starts a journey.”</div>
  <div class="quote">“Dream it. Build it. Launch it.”</div>
  <div class="quote">“Ideas don’t wait. Start now.”</div>
  <div class="quote">“Your startup story begins here.”</div>
</div>

<script>
/* ---------- Utilities ---------- */
const $=(id)=>document.getElementById(id);
function show(id){
  document.querySelectorAll('.card').forEach(el=>el.classList.remove('active'));
  $(id).classList.add('active');
}
function chip(text){ const d=document.createElement('span'); d.className='chip'; d.textContent=text; return d; }
function load(key,fallback){ try{ return JSON.parse(localStorage.getItem(key)) ?? fallback; } catch { return fallback; } }
function save(key,val){ localStorage.setItem(key, JSON.stringify(val)); }

/* ---------- Role selection (horizontal cards) ---------- */
$("roleStudent").addEventListener("click", ()=> show("student-login"));
$("roleHod").addEventListener("click", ()=> show("hod-login"));
$("rolePlacement").addEventListener("click", ()=> show("placement-login"));

/* ================= STUDENT ================= */
$("stuLoginBtn").addEventListener("click", ()=>{
  const user=$("stuUser").value.trim(), pass=$("stuPass").value.trim();
  const list=load("studentsLogin",[]);
  const ok=list.find(a=>a.username===user && a.password===pass);
  if(!ok) return alert("Invalid credentials");
  show("student-form");
});

let stuOTP=null;
$("stuSendOtp").addEventListener("click", ()=>{
  const phone=$("stuPhone").value.trim();
  if(!phone) return alert("Enter phone number");
  stuOTP=String(Math.floor(100000+Math.random()*900000));
  $("stuOtpMsg").textContent="OTP sent (demo): "+stuOTP;
});
$("stuSignupBtn").addEventListener("click", ()=>{
  const user=$("stuNewUser").value.trim(), pass=$("stuNewPass").value.trim(), otp=$("stuOtpInput").value.trim();
  if(!user||!pass) return alert("Username & password required");
  if(!otp) return alert("Enter OTP");
  if(otp!==stuOTP) return alert("Wrong OTP");
  const list=load("studentsLogin",[]);
  if(list.some(a=>a.username===user)) return alert("Username already exists");
  list.push({username:user,password:pass});
  save("studentsLogin",list);
  alert("Account created!");
  show("student-login");
});

/* Student form & dashboard */
$("resumeBtn").addEventListener("click", ()=> $("resumeFile").click());
$("resumeFile").addEventListener("change", e=> $("resumeName").textContent = e.target.files[0]?.name || "No file chosen");
$("studentSubmit").addEventListener("click", ()=>{
  const name=$("stName").value.trim(), reg=$("stReg").value.trim(), file=$("resumeFile").files[0];
  if(!name||!reg||!file) return alert("Fill all details & upload resume");
  const students=load("students",[]);
  const idx=students.findIndex(s=>s.reg===reg);
  const rec={name,reg,resume:file.name,approved:false};
  if(idx>=0) students[idx]=rec; else students.push(rec);
  save("students",students); save("studentSelf", rec);
  renderStudent(); show("student-page");
});
function renderStudent(){
  const st=load("studentSelf",null);
  $("studentSummary").innerHTML="";
  if(st){
    $("studentSummary").append(chip("Hello, "+st.name), chip("Reg: "+st.reg), chip("Resume: "+st.resume));
    $("s_name").textContent=st.name; $("s_reg").textContent=st.reg; $("s_resume").textContent=st.resume;
  }
}

/* ================= HOD ================= */
$("hodLoginBtn").addEventListener("click", ()=>{
  const user=$("hodUser").value.trim(), pass=$("hodPass").value.trim();
  const list=load("hodLogin",[]);
  const ok=list.find(a=>a.staff===user && a.password===pass);
  if(!ok) return alert("Invalid credentials");
  show("hod-form");
});

let hodOTP2=null;
$("hodSendOtp").addEventListener("click", ()=>{
  const phone=$("hodPhone2").value.trim();
  if(!phone) return alert("Enter phone number");
  hodOTP2=String(Math.floor(100000+Math.random()*900000));
  $("hodOtpMsg2").textContent="OTP sent (demo): "+hodOTP2;
});
$("hodSignupBtn").addEventListener("click", ()=>{
  const user=$("hodNewUser").value.trim(), pass=$("hodNewPass").value.trim(), otp=$("hodOtpInput2").value.trim();
  if(!user||!pass) return alert("Staff ID & password required");
  if(!otp) return alert("Enter OTP");
  if(otp!==hodOTP2) return alert("Wrong OTP");
  const list=load("hodLogin",[]);
  if(list.some(a=>a.staff===user)) return alert("Staff ID already exists");
  list.push({staff:user,password:pass});
  save("hodLogin",list); alert("Account created!");
  show("hod-login");
});

/* HOD verification + dashboard */
let hodOTP=null;
$("hodSendOtpMain").addEventListener("click", ()=>{
  const staff=$("hodStaff").value.trim(), phone=$("hodPhone").value.trim();
  if(!staff||!phone) return alert("Enter Staff ID & phone number");
  hodOTP=String(Math.floor(100000+Math.random()*900000));
  $("hodOtpMsg").textContent="Verification code sent (demo): "+hodOTP;
});
$("hodSubmit").addEventListener("click", ()=>{
  const otp=$("hodOtpInput").value.trim();
  if(!otp) return alert("Enter verification code");
  if(otp!==hodOTP) return alert("Invalid code");
  const hod={staff:$("hodStaff").value.trim(), phone:$("hodPhone").value.trim(), dept:($("hodDept").value.trim()||"Not Provided")};
  save("hodProfile", hod); renderHOD(); show("hod-page");
});
function renderHOD(){
  const hod=load("hodProfile",null);
  const wrap=$("hodSummary"); wrap.innerHTML="";
  if(hod){ wrap.append(chip("Staff ID: "+hod.staff), chip("Phone: "+hod.phone), chip("Dept: "+hod.dept)); }
  const tbody=$("hodTable").querySelector("tbody"); tbody.innerHTML="";
  const students=load("students",[]);
  students.forEach((s,idx)=>{
    const tr=document.createElement("tr");
    tr.innerHTML=`
      <td>${s.name}</td>
      <td>${s.reg}</td>
      <td>${s.resume||"-"}</td>
      <td><span class="status">${s.approved?"Approved":"Pending"}</span></td>
      <td><button data-i="${idx}" class="approveBtn">${s.approved?"Revoke":"Approve"}</button></td>
    `;
    tbody.appendChild(tr);
  });
  tbody.querySelectorAll(".approveBtn").forEach(btn=>{
    btn.addEventListener("click", e=>{
      const i=Number(e.target.getAttribute("data-i"));
      const list=load("students",[]);
      list[i].approved=!list[i].approved;
      save("students",list);
      renderHOD(); renderPlacement();
    });
  });
}

/* ================= PLACEMENT ================= */
$("plLoginBtn").addEventListener("click", ()=>{
  const user=$("plUser").value.trim(), pass=$("plPass").value.trim();
  const list=load("placementLogin",[]);
  const ok=list.find(a=>a.staff===user && a.password===pass);
  if(!ok) return alert("Invalid credentials");
  show("placement-form");
});

let plOTP2=null;
$("plSendOtp2").addEventListener("click", ()=>{
  const phone=$("plPhone2").value.trim();
  if(!phone) return alert("Enter phone number");
  plOTP2=String(Math.floor(100000+Math.random()*900000));
  $("plOtpMsg2").textContent="OTP sent (demo): "+plOTP2;
});
$("plSignupBtn").addEventListener("click", ()=>{
  const user=$("plNewUser").value.trim(), pass=$("plNewPass").value.trim(), otp=$("plOtpInput2").value.trim();
  if(!user||!pass) return alert("Staff ID & password required");
  if(!otp) return alert("Enter OTP");
  if(otp!==plOTP2) return alert("Wrong OTP");
  const list=load("placementLogin",[]);
  if(list.some(a=>a.staff===user)) return alert("Staff ID already exists");
  list.push({staff:user,password:pass});
  save("placementLogin",list); alert("Account created!");
  show("placement-login");
});

/* Placement verification + dashboard */
let plOTP=null;
$("plSendOtp").addEventListener("click", ()=>{
  const s=$("plStaff").value.trim(), p=$("plPhone").value.trim(), d=$("plDept").value.trim();
  if(!s||!p||!d) return alert("All fields are mandatory");
  plOTP=String(Math.floor(100000+Math.random()*900000));
  $("plOtpMsg").textContent="OTP sent (demo): "+plOTP;
});
$("plSubmit").addEventListener("click", ()=>{
  const otp=$("plOtpInput").value.trim();
  if(!otp) return alert("Enter OTP");
  if(otp!==plOTP) return alert("Wrong OTP");
  const pl={staff:$("plStaff").value.trim(), phone:$("plPhone").value.trim(), dept:$("plDept").value.trim(), verified:true};
  save("placementProfile", pl); renderPlacement(); show("placement-page");
});
function renderPlacement(){
  const pl=load("placementProfile",null);
  const wrap=$("plSummary"); wrap.innerHTML="";
  if(pl){ wrap.append(chip("Staff ID: "+pl.staff), chip("Phone: "+pl.phone), chip("Dept: "+pl.dept), chip("Verified ✔")); }
  const tbody=$("plTable").querySelector("tbody"); tbody.innerHTML="";
  const approved=load("students",[]).filter(s=>s.approved);
  approved.forEach(s=>{
    const tr=document.createElement("tr");
    tr.innerHTML=`<td>${s.name}</td><td>${s.reg}</td><td>${s.resume||"-"}</td><td><span class="status">HOD Approved</span></td>`;
    tbody.appendChild(tr);
  });
}
</script>
</body>
</html>
