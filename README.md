<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Tech Login System</title>
  <style>
    body {
      margin: 0;
      font-family: 'Poppins', sans-serif;
      height: 100vh;
      display: flex;
      justify-content: space-between;
      align-items: center;
      background: linear-gradient(135deg, #0a1f44, #0066ff);
      overflow: hidden;
      color: white;
    }

    /* Floating animations */
    @keyframes float {
      0%, 100% { transform: translateY(0); }
      50% { transform: translateY(-20px); }
    }

    .floating {
      position: absolute;
      opacity: 0.15;
      animation: float 6s ease-in-out infinite;
      font-size: 40px;
    }

    /* Box styling */
    .container {
      width: 50%;
      height: 100%;
      display: flex;
      justify-content: center;
      align-items: center;
      position: relative;
    }

    .box {
      width: 70%;
      max-width: 400px;
      padding: 30px;
      border-radius: 20px;
      background: rgba(255, 255, 255, 0.1);
      backdrop-filter: blur(15px);
      box-shadow: 0 0 20px rgba(0,0,0,0.3);
      text-align: center;
      animation: fadeIn 1s ease-in-out;
    }

    @keyframes fadeIn {
      from { opacity: 0; transform: translateY(20px); }
      to { opacity: 1; transform: translateY(0); }
    }

    h2 {
      font-size: 28px;
      margin-bottom: 20px;
      letter-spacing: 1px;
      text-transform: uppercase;
    }

    input, select {
      width: 85%;
      padding: 10px;
      margin: 10px 0;
      border: none;
      border-radius: 8px;
      outline: none;
    }

    button {
      width: 90%;
      padding: 10px;
      border: none;
      border-radius: 8px;
      background-color: #0066ff;
      color: white;
      font-weight: bold;
      cursor: pointer;
      transition: 0.3s;
    }

    button:hover {
      background-color: #0040cc;
    }

    a {
      display: block;
      margin-top: 10px;
      color: #fff;
      text-decoration: underline;
      font-size: 14px;
      cursor: pointer;
    }

    /* Right side quotes section */
    .quotes {
      width: 50%;
      padding: 50px;
      display: flex;
      flex-direction: column;
      justify-content: center;
      text-align: left;
    }

    .quote {
      font-size: 40px;
      font-weight: 700;
      margin-bottom: 40px;
      line-height: 1.2;
      text-shadow: 2px 2px 10px rgba(0,0,0,0.5);
      animation: fadeQuote 10s infinite;
    }

    @keyframes fadeQuote {
      0%, 100% { opacity: 0; transform: translateY(20px); }
      10%, 90% { opacity: 1; transform: translateY(0); }
    }

    /* Hide all boxes by default */
    .box { display: none; }
    .box.active { display: block; }

    /* Responsive */
    @media (max-width: 768px) {
      body { flex-direction: column; }
      .container, .quotes { width: 100%; height: auto; }
      .quotes { text-align: center; padding: 30px; }
      .quote { font-size: 28px; }
    }
  </style>
</head>
<body>

  <!-- Floating elements -->
  <div class="floating" style="top:10%;left:15%;">🚀</div>
  <div class="floating" style="top:70%;left:35%;">💼</div>
  <div class="floating" style="top:40%;left:75%;">📈</div>
  <div class="floating" style="top:20%;left:85%;">💡</div>

  <!-- Left Side: Login / Signup -->
  <div class="container">
    <div class="box active" id="login-box">
      <h2>Welcome Back!</h2>
      <select>
        <option value="">Select Role</option>
        <option value="student">Student</option>
        <option value="hod">HOD</option>
        <option value="placement">Placement Officer</option>
      </select>
      <input type="text" placeholder="Username" />
      <input type="password" placeholder="Password" />
      <button>Next</button>
      <a onclick="showPage('forgot-box')">Forgot Password?</a>
      <a onclick="showPage('signup-box')">Create Account</a>
    </div>

    <div class="box" id="signup-box">
      <h2>Join Us</h2>
      <select>
        <option value="">Select Role</option>
        <option value="student">Student</option>
        <option value="hod">HOD</option>
        <option value="placement">Placement Officer</option>
      </select>
      <input type="text" placeholder="Username" />
      <input type="email" placeholder="Email" />
      <input type="password" placeholder="Password" />
      <button>Sign Up</button>
      <a onclick="showPage('login-box')">Already have an account?</a>
    </div>

    <div class="box" id="forgot-box">
      <h2>Reset Password</h2>
      <input type="email" placeholder="Enter your email" />
      <button>Send Reset Link</button>
      <a onclick="showPage('login-box')">Back to Login</a>
    </div>
  </div>

  <!-- Right Side: Motivational Quotes -->
  <div class="quotes" id="quote-box">
    <div class="quote">“Every code starts a journey.”</div>
    <div class="quote">“Dream it. Build it. Launch it.”</div>
    <div class="quote">“Ideas don’t wait. Start now.”</div>
    <div class="quote">“Your startup story begins here.”</div>
  </div>

  <script>
    function showPage(id) {
      document.querySelectorAll('.box').forEach(box => box.classList.remove('active'));
      document.getElementById(id).classList.add('active');
    }

    // Quote rotation logic
    const quotes = document.querySelectorAll('.quote');
    let current = 0;
    function showNextQuote() {
      quotes.forEach((q, i) => q.style.display = i === current ? 'block' : 'none');
      current = (current + 1) % quotes.length;
    }
    showNextQuote();
    setInterval(showNextQuote, 4000);
  </script>

</body>
</html>
