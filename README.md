<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Tech Login System</title>

  <style>
    body {
      margin: 0;
      font-family: 'Poppins', sans-serif;
      background: linear-gradient(135deg, #00c6ff, #0072ff, #8e2de2, #4a00e0);
      background-size: 400% 400%;
      animation: gradientBG 10s ease infinite;
      height: 100vh;
      display: flex;
      justify-content: center;
      align-items: center;
      color: white;
    }

    @keyframes gradientBG {
      0% { background-position: 0% 50%; }
      50% { background-position: 100% 50%; }
      100% { background-position: 0% 50%; }
    }

    .box {
      display: none;
      background: rgba(0, 0, 0, 0.6);
      padding: 40px;
      border-radius: 15px;
      box-shadow: 0 0 25px rgba(255, 255, 255, 0.3);
      width: 320px;
      text-align: center;
      backdrop-filter: blur(5px);
    }

    .active {
      display: block;
      animation: fadeIn 0.6s ease;
    }

    @keyframes fadeIn {
      from { opacity: 0; transform: scale(0.9); }
      to { opacity: 1; transform: scale(1); }
    }

    h2 {
      margin-bottom: 25px;
      font-size: 26px;
      color: #00ffff;
    }

    input, select {
      width: 100%;
      padding: 10px;
      margin: 10px 0;
      border: none;
      border-radius: 6px;
      background: rgba(255, 255, 255, 0.15);
      color: white;
      font-size: 14px;
      outline: none;
    }

    input::placeholder {
      color: #ccc;
    }

    select {
      color: #ccc;
    }

    button {
      margin-top: 10px;
      width: 100%;
      padding: 10px;
      border: none;
      border-radius: 6px;
      background-color: #00ffff;
      color: #000;
      font-weight: bold;
      cursor: pointer;
      transition: 0.3s;
    }

    button:hover {
      background-color: #00b3b3;
      transform: scale(1.05);
    }

    .link-text {
      margin-top: 15px;
      font-size: 14px;
      color: #ccc;
    }

    .link-text a {
      color: #00ffff;
      text-decoration: none;
      font-weight: bold;
      cursor: pointer;
    }

    .link-text a:hover {
      text-decoration: underline;
    }

    .small-note {
      font-size: 13px;
      color: #aaa;
      margin-bottom: 10px;
    }
  </style>
</head>
<body>

  <!-- LOGIN PAGE -->
  <div class="box active" id="login-box">
    <h2>Login</h2>
    <input type="text" placeholder="Username or Email ID" />
    <input type="password" placeholder="Password" />
    <div class="link-text" style="text-align: right;">
      <a onclick="showPage('forgot-box')">Forgot Password?</a>
    </div>
    <select>
      <option value="" disabled selected>Select Role</option>
      <option value="student">Student</option>
      <option value="hod">HOD</option>
      <option value="placement">Placement Officer</option>
    </select>
    <button onclick="alert('Login successful! Returning to login page...')">Next</button>
    <div class="link-text">
      New user? <a onclick="showPage('signup-box')">Sign up</a>
    </div>
  </div>

  <!-- FORGOT PASSWORD PAGE -->
  <div class="box" id="forgot-box">
    <h2>Reset Password</h2>
    <p class="small-note">Enter your registered email to receive a reset link.</p>
    <input type="email" placeholder="Enter your email address" />
    <button onclick="alert('Reset link sent! Returning to login page...'); showPage('login-box')">Send Reset Link</button>
    <div class="link-text">
      <a onclick="showPage('login-box')">← Back to Login</a>
    </div>
  </div>

  <!-- SIGN UP PAGE -->
  <div class="box" id="signup-box">
    <h2>Sign Up</h2>
    <input type="text" placeholder="Full Name" />
    <input type="email" placeholder="Email Address" />
    <input type="password" placeholder="Create Password" />
    <select>
      <option value="" disabled selected>Select Role</option>
      <option value="student">Student</option>
      <option value="hod">HOD</option>
      <option value="placement">Placement Officer</option>
    </select>
    <button onclick="alert('Registration complete! Returning to login page...'); showPage('login-box')">Register</button>
    <div class="link-text">
      <a onclick="showPage('login-box')">← Back to Login</a>
    </div>
  </div>

  <script>
    // Function to switch between pages
    function showPage(pageId) {
      document.querySelectorAll('.box').forEach(box => box.classList.remove('active'));
      document.getElementById(pageId).classList.add('active');
    }
  </script>

</body>
</html>
