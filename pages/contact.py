import streamlit as st

st.markdown(
    """
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Contact Page</title>
  <style>
    .stApp {
        background-image: url("https://pointerclicker.com/wp-content/uploads/2022/12/A-TV-with-bias-lighting-behind-960x960.jpg");
        background-size: cover;
    }
    body {
      font-family: Arial, sans-serif;
      margin: 0;
      padding: 0;
      background-color: #f8f9fa;
      color: rgb(234, 207, 158);
    }
    header {
      
      color: rgb(207, 71, 71);
      text-align: center;
      padding: 20px 0;
    }
    .container {
      max-width: 400px;
      margin: 0 auto;
      padding: 20px;
      
    }
    .bg {
      position: absolute;
      right: 0;
      bottom: 0;
      z-index: -1;
      opacity: 80%;
      width: 100%;
    }
    .form-group {
      margin-bottom: 20px;
    }
    label {
      display: block;
      font-weight: bold;
      margin-bottom: 5px;
    }
    input[type="text"],
    input[type="email"],
    textarea {
      width: 100%;
      padding: 10px;
      border: 1px solid #ced4da;
      border-radius: 4px;
      box-sizing: border-box;
    }
    textarea {
      resize: vertical;
    }
    button[type="submit"] {
      background-color: #007bff;
      color: #fff;
      border: none;
      padding: 10px 20px;
      border-radius: 4px;
      cursor: pointer;
      transition: background-color 0.3s;
    }
    button[type="submit"]:hover {
      background-color: #0056b3;
    }
    footer {
      background-color: #343a40;
      color: #fff;
      text-align: center;
      padding: 20px 0;
      position: fixed;
      bottom: 0;
      width: 100%;
    }
  </style>
</head>
<body>
    <img class="bg" src="1.jpg">
  <header>
    <h1>Contact Us</h1>
  </header>
  
  <div class="container">
    <form class="contact-form" action="contact.html" method="POST">
      <div class="form-group">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>
      </div>
      <div class="form-group">
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>
      </div>
      <div class="form-group">
        <label for="message">Message:</label>
        <textarea id="message" name="message" rows="5" required></textarea>
      </div>
      <button type="submit">Send</button>
    </form>
  </div>
  <footer>
    <p>&copy; 2024 | Movie Recommender. All rights reserved.</p>
  </footer>
</body>
""",
   unsafe_allow_html=True,
)