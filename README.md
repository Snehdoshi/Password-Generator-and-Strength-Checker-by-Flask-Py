
# 🔐 Password Generator & Strength Checker

A **Password Generator** and **Strength Checker** web app built with **Flask**, **HTML**, **CSS**, **JavaScript**, and **Python**.  
Generate strong passwords and instantly check their strength.

---

## 🚀 Features

- 🔑 Customizable password generation (length, character sets)
- 📊 Password-strength meter (weak, medium, strong)
- 📱 Responsive, mobile-friendly UI
- 🔄 Instant feedback without page reload

---

## 🛠️ Built With

- **Backend**:  
  - Python 3.x  
  - Flask  
- **Frontend**:  
  - HTML5  
  - CSS3  
  - JavaScript  

---

## 📂 Project Structure

```
/
├── app.py              # Flask application entry point
└── templates/
    └── index.html      # Main frontend template (includes CSS/JS)
```



## ⚙️ Installation & Run

1. **Clone the repo**  
   ```bash
   git clone [https://github.com/yourusername/password-generator-strength-checker.git](https://github.com/Snehdoshi/Password-Generator-and-Strength-Checker-by-Py-Project)
   cd app.py
   ```

2. **Create & activate a virtual environment**  
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate   # Linux/macOS
   .venv\Scripts\activate      # Windows
   ```

3. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the app**  
   ```bash
   python app.py
   ```  
   By default, Flask will serve at `http://127.0.0.1:5000/`.

5. **Open in your browser**  
   Navigate to `http://127.0.0.1:5000/` and start generating/checking passwords!

---

## 🧠 How It Works

1. **Generate**  
   - You choose length and character options (letters, numbers, symbols).  
   - The app builds a random password server-side (in `app.py`) and returns it.

2. **Check Strength**  
   - Enter any password to see its strength rating.  
   - A JS-driven meter evaluates length, variety of characters, and common patterns.

---


## 🤝 Contributing

Feel free to fork, make improvements, and submit a PR!  

---

⭐ If you find this project helpful, please give it a star!  
```
