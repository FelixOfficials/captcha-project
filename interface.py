from PIL import Image, ImageDraw, ImageFont
import random
import os
import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("348x460")
root.resizable(width=True, height=True)

def login():
    print("Test")

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Login System")
label.pack(pady=12, padx=10)

username = customtkinter.CTkEntry(master=frame, placeholder_text="Username")
username.pack(pady=12, padx=10)

password = customtkinter.CTkEntry(master=frame, placeholder_text="Password", show="*")
password.pack(pady=12, padx=10)

email = customtkinter.CTkEntry(master=frame, placeholder_text="Email")
email.pack(pady=12, padx=10)

checkbox = customtkinter.CTkCheckBox(master=frame, text="Captcha")
checkbox.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=frame, text="Login", command=login)
button.pack(pady=12, padx=10)

def button_state():
    if customtkinter.CHECKBUTTON() == 1:
        open_captcha()

def open_captcha():
    captcha = customtkinter.CTkToplevel(master=frame)
    captcha.title("Captcha Frame")

    label2 = customtkinter.CTkLabel(master=frame, text="Login System")
    label2.pack(pady=12, padx=10)

def main():
    root.mainloop()

if __name__ == "__main__":
    main()


#https://www.youtube.com/watch?v=mop6g-c5HEY (Video to learn from)
