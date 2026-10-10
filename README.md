# KeyVault - Secure Password & Passphrase Generator

A modern, fast, and cryptographically secure Password & Passphrase Generator built with pure HTML5, CSS3, and JavaScript, plus a standalone Python CLI tool.

![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat&logo=html5&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat&logo=javascript&logoColor=black)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

---

## ✨ Features

- **Random Password Mode**:
  - Customizable length (6–64 characters)
  - Toggle Uppercase (`A-Z`), Lowercase (`a-z`), Numbers (`0-9`), and Symbols (`!@#$%...`)
  - Filter out confusing/ambiguous characters (`l`, `1`, `O`, `0`)
- **Memorable Passphrase Mode**:
  - Diceware-inspired memorable passphrases (e.g. `Velvet-Pebble-Falcon42`)
  - Adjustable word count, capitalization, and optional numbers
- **Cryptographically Secure**:
  - Uses browser `crypto.getRandomValues()` API and Python `secrets` module
- **Live Entropy & Strength Indicator**:
  - Calculates real-time bit entropy with visual status (Weak, Medium, Strong, Very Strong)
- **One-Click Copy**:
  - Copy directly with visual toast feedback
- **History Log**:
  - Retains recent generated passwords for quick reuse
- **Keyboard Shortcuts**:
  - Press <kbd>Spacebar</kbd> anytime to generate a new password
- **Zero External Dependencies**:
  - Single-file web app runs in any modern browser without npm or build steps

---

## 🚀 How to Run Locally

### Option 1: Web App
Simply open `index.html` in your favorite web browser (Chrome, Edge, Firefox, Safari).

### Option 2: Python Tool
Run the script using Python 3:
```bash
python password_generator.py
```

---

## 🌐 Deploy to GitHub Pages (Get a Live URL)

To host this project online for free using GitHub Pages:

1. **Initialize Git & Commit**:
   ```bash
   git init
   git add .
   git commit -m "Initial commit: KeyVault password generator"
   ```

2. **Create a GitHub Repository**:
   - Go to [GitHub New Repository](https://github.com/new).
   - Enter a name (e.g. `password-generator`).
   - Click **Create repository**.

3. **Push to GitHub**:
   ```bash
   git branch -M main
   git remote add origin https://github.com/thanuja0611/password-generator.git
   git push -u origin main
   ```

4. **Enable GitHub Pages**:
   - In your GitHub repo, go to **Settings** > **Pages**.
   - Under **Build and deployment** > **Branch**, select `main` branch and `/ (root)` folder.
   - Click **Save**.
   - Your live website will be available at:
     `https://thanuja0611.github.io/password-generator/`

---

## 📄 License
This project is open-source under the [MIT License](LICENSE).
