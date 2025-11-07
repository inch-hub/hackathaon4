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
input,button{
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

/* HORIZONTAL CARDS + BLACK & WHITE AVATARS */
.role-grid{
  display:flex; flex-direction:row; justify-content:space-between;
  width:100%; margin-top:16px; gap:18px;
}
.role-card{
  flex:1; padding:16px; border-radius:16px;
  background:rgba(255,255,255,.18); text-align:center; cursor:pointer; user-select:none;
  transition:0.3s; overflow:hidden;
  box-shadow:0 6px 16px rgba(0,0,0,.25);
}
.role-card:hover{
  background:rgba(255,255,255,.32);
  transform:scale(1.05);
}
.role-avatar{
  width:65px; height:65px; border-radius:50%;
  margin-bottom:8px; display:block; margin-left:auto; margin-right:auto;
  object-fit:contain;
  filter:grayscale(100%); transition:0.3s;
}
.role-card:hover .role-avatar{
  filter:grayscale(30%);
}
.role-title{
  font-size:19px; font-weight:700;
}

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

    <!-- ROLE SELECT WITH AVATARS -->
    <div class="card active" id="role-box" style="text-align:center">
      <h2>Welcome!</h2>
      <div class="muted">Select your role to continue.</div>

      <div class="role-grid">
        <div class="role-card" id="roleStudent">
          <img src="https://cdn-icons-png.flaticon.com/512/2922/2922510.png" class="role-avatar">
          <div class="role-title">Student</div>
        </div>
        <div class="role-card" id="roleHod">
          <img src="https://cdn-icons-png.flaticon.com/512/3209/3209265.png" class="role-avatar">
          <div class="role-title">HOD</div>
        </div>
        <div class="role-card" id="rolePlacement">
          <img src="https://cdn-icons-png.flaticon.com/512/924/924874.png" class="role-avatar">
          <div class="role-title">Placement Officer</div>
        </div>
      </div>
    </div>

    <!-- STUDENT LOGIN -->
    <div class="card" id="student-login">
      <h2>Student Login</h2>
      <input id="stuUser" placeholder="Username">
      <input id="stuPass" type="password" placeholder="Password">
      <button id="stuLoginBtn">Login</button>
      <div>
        <span class="link" onclick="show('student-signup')">Sign Up</span> ·
        <span class="link" onclick="show('student-forgot')">Forgot Password?</span> ·
        <span class="link" onclick="show('role-box')">Back</span>
      </div>
    </div>

    <!-- STUDENT SIGNUP -->
    <div class="card" id="student-signup">
      <h2>Student Sign Up</h2>
      <input id="stuNewUser" placeholder="New Username">
      <input id="stuNewPass" type="password" placeholder="Create Password">
      <input id="stuPhone" placeholder="Phone Number">
      <button id="stuSendOtp">Send OTP</button>
      <input id="stuOtpInput" placeholder="Enter OTP">
      <button id="stuSignupBtn">Create Account</button>
      <div id="stuOtpMsg" class="muted"></div>
      <div><span class="link" onclick="show('student-login')">Back to Login</span></div>
    </div>

    <div class="card" id="student-forgot">
      <h2>Reset Password</h2>
      <input placeholder="Enter Email">
      <button onclick="alert('Reset link sent (demo)')">Send Reset Link</button>
      <div><span class="link" onclick="show('student-login')">Back</span></div>
    </div>

    <!-- STUDENT DETAILS -->
    <div class="card" id="student-form">
      <h2>Student Details</h2>
      <div class="row">
        <div><input id="stName" placeholder="Full Name"></div>
        <div><input id="stReg" placeholder="Register Number"></div>
      </div>
      <div class="upload-wrap">
        <input type="file" id="resumeFile" accept=".pdf,.doc,.docx">
        <button class="upload-btn" id="resumeBtn">Upload Resume</button>
        <span id="resumeName" class="file-name">No file chosen</span>
      </div>
      <button id="studentSubmit">Submit & Continue</button>
      <div><span class="link" onclick="show('role-box')">Logout</span></div>
    </div>

    <!-- STUDENT DASHBOARD -->
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

    <!-- HOD LOGIN -->
    <div class="card" id="hod-login">
      <h2>HOD Login</h2>
      <input id="hodUser" placeholder="Staff ID">
      <input id="hodPass" type="password" placeholder="Password">
      <button id="hodLoginBtn">Login</button>
      <div>
        <span class="link" onclick="show('hod-signup')">Sign Up</span> ·
        <span class="link" onclick="show('hod-forgot')">Forgot Password?</span> ·
        <span class="link" onclick="show('role-box')">Back</span>
      </div>
    </div>

    <!-- HOD SIGN UP -->
    <div class="card" id="hod-signup">
      <h2>HOD Sign Up</h2>
      <input id="hodNewUser" placeholder="Staff ID">
      <input id="hodNewPass" type="password" placeholder="Create Password">
      <input id="hodPhone2" placeholder="Phone Number">
      <button id="hodSendOtp">Send OTP</button>
      <input id="hodOtpInput2" placeholder="Enter OTP">
      <button id="hodSignupBtn">Create Account</button>
      <div id="hodOtpMsg2" class="muted"></div>
      <div><span class="link" onclick="show('hod-login')">Back to Login</span></div>
    </div>

    <!-- HOD FORGOT -->
    <div class="card" id="hod-forgot">
      <h2>Reset Password</h2>
      <input placeholder="Enter Email">
      <button onclick="alert('Reset link sent (demo)')">Send Reset Link</button>
      <div><span class="link" onclick="show('hod-login')">Back</span></div>
    </div>

    <!-- HOD VERIFICATION -->
    <div class="card" id="hod-form">
      <h2>HOD Verification</h2>
      <input id="hodStaff" placeholder="Staff ID">
      <input id="hodPhone" placeholder="Phone Number">
      <input id="hodDept" placeholder="Department (Optional)">
      <button id="hodSendOtpMain">Send Verification Code</button>
      <input id="hodOtpInput" placeholder="Enter Verification Code">
      <div id="hodOtpMsg" class="muted"></div>
      <button id="hodSubmit">Verify & Continue</button>
      <div><span class="link" onclick="show('role-box')">Logout</span></div>
    </div>

    <!-- HOD DASHBOARD -->
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

    <!-- PLACEMENT LOGIN -->
    <div class="card" id="placement-login">
      <h2>Placement Login</h2>
      <input id="plUser" placeholder="Staff ID">
      <input id="plPass" type="password" placeholder="Password">
      <button id="plLoginBtn">Login</button>
      <div>
        <span class="link" onclick="show('placement-signup')">Sign Up</span> ·
        <span class="link" onclick="show('placement-forgot')">Forgot Password?</span> ·
        <span class="link" onclick="show('role-box')">Back</span>
      </div>
    </div>

    <!-- PLACEMENT SIGNUP -->
    <div class="card" id="placement-signup">
      <h2>Placement Sign Up</h2>
      <input id="plNewUser" placeholder="Staff ID">
      <input id="plNewPass" type="password" placeholder="Create Password">
      <input id="plPhone2" placeholder="Phone Number">
      <button id="plSendOtp2">Send OTP</button>
      <input id="plOtpInput2" placeholder="Enter OTP">
      <button id="plSignupBtn">Create Account</button>
      <div id="plOtpMsg2" class="muted"></div>
      <div><span class="link" onclick="show('placement-login')">Back to Login</span></div>
    </div>

    <!-- PLACEMENT FORGOT -->
    <div class="card" id="placement-forgot">
      <h2>Reset Password</h2>
      <input placeholder="Enter Email">
      <button onclick="alert('Reset link sent (demo)')">Send Reset Link</button>
      <div><span class="link" onclick="show('placement-login')">Back</span></div>
    </div>

    <!-- PLACEMENT VERIFICATION -->
    <div class="card" id="placement-form">
      <h2>Placement Verification</h2>
      <input id="plStaff" placeholder="Staff ID (MANDATORY)">
      <input id="plPhone" placeholder="Phone Number (MANDATORY)">
      <input id="plDept" placeholder="Authorized Department (MANDATORY)">
      <button id="plSendOtp">Send Verification Code</button>
      <input id="plOtpInput" placeholder="Enter OTP (MANDATORY)">
      <div id="plOtpMsg" class="muted"></div>
      <button id="plSubmit">Verify & Continue</button>
      <div><span class="link" onclick="show('role-box')">Logout</span></div>
    </div>

    <!-- PLACEMENT DASHBOARD -->
    <div class="card" id="placement-page">
      <h2>Placement Dashboard</h2>
      <div id="plSummary" class="chips"></div>
      <div class="muted" style="margin-top:10px">HOD-approved students</div>
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
/* UTILS */
const $=id=>document.getElementById(id);
function show(id){
  document.querySelectorAll('.card').forEach(c=>c.classList.remove('active'));
  $(id).classList.add('active');
}
function chip(t){let d=document.createElement("span");d.className="chip";d.textContent=t;return d;}
function load(k,f){try{return JSON.parse(localStorage.getItem(k)) ?? f;}catch{return f;}}
function save(k,v){localStorage.setItem(k,JSON.stringify(v));}

/* ROLE CLICK */
$("roleStudent").addEventListener("click",()=>show("student-login"));
$("roleHod").addEventListener("click",()=>show("hod-login"));
$("rolePlacement").addEventListener("click",()=>show("placement-login"));

/* STUDENT LOGIN */
$("stuLoginBtn").addEventListener("click",()=>{
  let user=$("stuUser").value.trim(), pass=$("stuPass").value.trim();
  let list=load("studentsLogin",[]);
  if(!list.find(x=>x.username===user && x.password===pass)) return alert("Invalid credentials");
  show("student-form");
});

/* STUDENT SIGN UP WITH OTP */
let stuOTP=null;
$("stuSendOtp").addEventListener("click",()=>{
  if(!$("stuPhone").value.trim()) return alert("Enter Phone");
  stuOTP=String(Math.floor(100000+Math.random()*900000));
  $("stuOtpMsg").textContent="OTP sent (demo): "+stuOTP;
});
$("stuSignupBtn").addEventListener("click",()=>{
  let u=$("stuNewUser").value.trim(), p=$("stuNewPass").value.trim(), o=$("stuOtpInput").value.trim();
  if(!u||!p) return alert("Username & Password required");
  if(o!==stuOTP) return alert("Wrong OTP");
  let list=load("studentsLogin",[]);
  if(list.some(x=>x.username===u)) return alert("Username exists");
  list.push({username:u,password:p});
  save("studentsLogin",list);
  alert("Account Created!");
  show("student-login");
});

/* STUDENT FORM */
$("resumeBtn").addEventListener("click",()=>$("resumeFile").click());
$("resumeFile").addEventListener("change",e=>$("resumeName").textContent=e.target.files[0]?.name || "No file");
$("studentSubmit").addEventListener("click",()=>{
  let n=$("stName").value.trim(), r=$("stReg").value.trim(), f=$("resumeFile").files[0];
  if(!n||!r||!f) return alert("All fields required");
  let st=load("students",[]), idx=st.findIndex(x=>x.reg===r);
  let rec={name:n,reg:r,resume:f.name,approved:false};
  if(idx>=0) st[idx]=rec; else st.push(rec);
  save("students",st); save("studentSelf",rec);
  renderStudent(); show("student-page");
});
function renderStudent(){
  let s=load("studentSelf",null);
  $("studentSummary").innerHTML="";
  if(s){
     $("studentSummary").append(chip("Hello: "+s.name),chip("Reg: "+s.reg),chip("Resume: "+s.resume));
     $("s_name").textContent=s.name; $("s_reg").textContent=s.reg; $("s_resume").textContent=s.resume;
  }
}

/* HOD LOGIN */
$("hodLoginBtn").addEventListener("click",()=>{
  let u=$("hodUser").value.trim(), p=$("hodPass").value.trim();
  let list=load("hodLogin",[]);
  if(!list.find(x=>x.staff===u && x.password===p)) return alert("Invalid credentials");
  show("hod-form");
});

/* HOD SIGN UP */
let hodOTP2=null;
$("hodSendOtp").addEventListener("click",()=>{
  if(!$("hodPhone2").value.trim()) return alert("Enter Phone");
  hodOTP2=String(Math.floor(100000+Math.random()*900000));
  $("hodOtpMsg2").textContent="OTP sent (demo): "+hodOTP2;
});
$("hodSignupBtn").addEventListener("click",()=>{
  let u=$("hodNewUser").value.trim(), p=$("hodNewPass").value.trim(), o=$("hodOtpInput2").value.trim();
  if(!u||!p) return alert("Staff ID & Password required");
  if(o!==hodOTP2) return alert("Wrong OTP");
  let list=load("hodLogin",[]);
  if(list.some(x=>x.staff===u)) return alert("Staff exists");
  list.push({staff:u,password:p});
  save("hodLogin",list);
  alert("Account Created!");
  show("hod-login");
});

/* HOD VERIFY */
let hodOTP=null;
$("hodSendOtpMain").addEventListener("click",()=>{
  if(!$("hodStaff").value.trim()||!$("hodPhone").value.trim()) return alert("Enter details");
  hodOTP=String(Math.floor(100000+Math.random()*900000));
  $("hodOtpMsg").textContent="Verification code: "+hodOTP;
});
$("hodSubmit").addEventListener("click",()=>{
  if($("hodOtpInput").value.trim()!==hodOTP) return alert("Wrong Code");
  let obj={staff:$("hodStaff").value.trim(),phone:$("hodPhone").value.trim(),dept:$("hodDept").value.trim()||"Not Provided"};
  save("hodProfile",obj); renderHOD(); show("hod-page");
});
function renderHOD(){
  let h=load("hodProfile",null);
  $("hodSummary").innerHTML="";
  if(h) $("hodSummary").append(chip("ID:"+h.staff),chip("Phone:"+h.phone),chip("Dept:"+h.dept));
  let tbody=$("hodTable").querySelector("tbody"); tbody.innerHTML="";
  let st=load("students",[]);
  st.forEach((s,i)=>{
    let tr=document.createElement("tr");
    tr.innerHTML=`
      <td>${s.name}</td><td>${s.reg}</td><td>${s.resume}</td>
      <td><span class="status">${s.approved?"Approved":"Pending"}</span></td>
      <td><button class="approveBtn" data-i="${i}">${s.approved?"Revoke":"Approve"}</button></td>`;
    tbody.appendChild(tr);
  });
  tbody.querySelectorAll(".approveBtn").forEach(btn=>{
    btn.addEventListener("click",e=>{
      let i=e.target.getAttribute("data-i");
      let st=load("students",[]); st[i].approved=!st[i].approved;
      save("students",st); renderHOD(); renderPlacement();
    });
  });
}

/* PLACEMENT LOGIN */
$("plLoginBtn").addEventListener("click",()=>{
  let u=$("plUser").value.trim(), p=$("plPass").value.trim();
  let list=load("placementLogin",[]);
  if(!list.find(x=>x.staff===u && x.password===p)) return alert("Invalid credentials");
  show("placement-form");
});

/* PLACEMENT SIGNUP */
let plOTP2=null;
$("plSendOtp2").addEventListener("click",()=>{
  if(!$("plPhone2").value.trim()) return alert("Enter Phone");
  plOTP2=String(Math.floor(100000+Math.random()*900000));
  $("plOtpMsg2").textContent="OTP sent (demo): "+plOTP2;
});
$("plSignupBtn").addEventListener("click",()=>{
  let u=$("plNewUser").value.trim(), p=$("plNewPass").value.trim(), o=$("plOtpInput2").value.trim();
  if(!u||!p) return alert("Staff & Pass required");
  if(o!==plOTP2) return alert("Wrong OTP");
  let list=load("placementLogin",[]);
  if(list.some(x=>x.staff===u)) return alert("Staff exists");
  list.push({staff:u,password:p});
  save("placementLogin",list); alert("Account Created!");
  show("placement-login");
});

/* PLACEMENT VERIFY */
let plOTP=null;
$("plSendOtp").addEventListener("click",()=>{
  if(!$("plStaff").value.trim()||!$("plPhone").value.trim()||!$("plDept").value.trim())
    return alert("All fields required");
  plOTP=String(Math.floor(100000+Math.random()*900000));
  $("plOtpMsg").textContent="OTP sent (demo): "+plOTP;
});
$("plSubmit").addEventListener("click",()=>{
  if($("plOtpInput").value.trim()!==plOTP) return alert("Wrong OTP");
  let o={staff:$("plStaff").value.trim(),phone:$("plPhone").value.trim(),dept:$("plDept").value.trim(),verified:true};
  save("placementProfile",o); renderPlacement(); show("placement-page");
});
function renderPlacement(){
  let o=load("placementProfile",null);
  $("plSummary").innerHTML="";
  if(o) $("plSummary").append(chip("ID:"+o.staff),chip("Phone:"+o.phone),chip("Dept:"+o.dept),chip("Verified ✔"));
  let tbody=$("plTable").querySelector("tbody"); tbody.innerHTML="";
  let ok=load("students",[]).filter(x=>x.approved);
  ok.forEach(s=>{
    let tr=document.createElement("tr");
    tr.innerHTML=`<td>${s.name}</td><td>${s.reg}</td><td>${s.resume}</td><td><span class="status">Approved</span></td>`;
    tbody.appendChild(tr);
  });
}
</script>
</body>
</html>
