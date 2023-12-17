from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
import tkinter as tk
import ttkbootstrap as ttkb
from tkinter import messagebox
import time

count = 0
chats = 0
class_name = "textbox"

def send():
    global count,chats, class_name
    answer['text'] = ""
    if text_area.get("1.0","end-1c"):
        try:
            WebDriverWait(driver, 6).until(EC.presence_of_all_elements_located((By.ID, "textbox")))
            if count:
                class_name = "postchat"
            text_box = driver.find_element(By.ID, class_name)
            text_box.clear()
            text_box.send_keys(text_area.get("1.0","end-1c")+ Keys.ENTER)

            time.sleep(5)
            WebDriverWait(driver, 6).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "markdown")))
            p_boxes = driver.find_elements(By.CLASS_NAME, "markdown")
            time.sleep(5)
            WebDriverWait(driver, 6).until(EC.presence_of_all_elements_located((By.TAG_NAME, "p")))
            p = p_boxes[count].find_element(By.TAG_NAME, "p")
            # print(p.text)
            answer["text"] = p.text
            text_area.delete("1.0", "end")
            num = 1
            if chats==0:
                num = 2
            count += num
            chats = None
            # time.sleep()
            driver.execute_script("window.onbeforeunload = function(e) {};")
        except:
            messagebox.showerror(title="Bully GPT", message="Something went wrong")
    else:
        messagebox.showwarning(title="Bully GPT", message="the field is empty")


win = ttkb.Window(themename="solar")
win.title("Bully GPT")
win.geometry("1000x650")
win.minsize(600,400)
style = ttkb.Style(theme="solar")
style.configure("info.Outline.TButton", font=("Comic Sans MS",12))


try:
    chrome_options = Options()
    chrome_options.add_argument("--headless")

    servise = Service(executable_path="chromedriver.exe")
    driver = webdriver.Chrome(service=servise, options=chrome_options)
    driver.maximize_window()
    driver.get("https://bratgpt.com/")
    # driver = webdriver.Chrome(options=chrome_options)

    WebDriverWait(driver, 2).until(EC.presence_of_all_elements_located((By.ID, "closeButton")))
    close_btn = driver.find_element(By.ID, "closeButton")
    close_btn.click()
except:
    messagebox.showerror(title="Bully GPT", message="Connection Problem")


text_area = ttkb.Text(win,width=300, font=("Comic Sans MS",14), height=6)
text_area.pack(pady=(40,0), padx=40)
send_btn = ttkb.Button(win, text="send", width=300, cursor="hand2", style="info.Outline.TButton", command=send)
send_btn.pack(pady=(40,0), padx=40)
answer = ttkb.Label(win, text="", font=("Comic Sans MS", 12))
answer.pack(pady=(0,50), padx=40, expand=True, fill="both")

def update_wrap_length(event):
    answer.update_idletasks()
    answer.config(wraplength=answer.winfo_width())
answer.bind('<Configure>', update_wrap_length)

win.iconbitmap("icon.ico")
win.mainloop()
