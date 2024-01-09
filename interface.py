from PIL import Image, ImageDraw, ImageFont
import random
import os
import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

root = ctk.CTk()
root.geometry("348x460")
root.resizable(width=True, height=True)

def login():
    print("Test")

frame = ctk.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = ctk.CTkLabel(master=frame, text="Login System")
label.pack(pady=12, padx=10)

username = ctk.CTkEntry(master=frame, placeholder_text="Username")
username.pack(pady=12, padx=10)

password = ctk.CTkEntry(master=frame, placeholder_text="Password", show="*")
password.pack(pady=12, padx=10)

email = ctk.CTkEntry(master=frame, placeholder_text="Email")
email.pack(pady=12, padx=10)

check_var = ctk.StringVar(value="0")

def captcha_dropdown():
    if check_var.get() == "1":
        my_label.configure(text="you clicked")
    else:
        my_label.configure(text="")

    captcha = ctk.CTkToplevel(master=frame)
    captcha.title("Captcha Frame")

    label2 = ctk.CTkLabel(master=frame, text="Login System")
    label2.pack(pady=12, padx=10)

checkbox = ctk.CTkCheckBox(master=frame, 
                           text="I'm not a robot (Fake Captcha)", 
                           variable=check_var, 
                           onvalue="1", 
                           offvalue="0",
                           command=captcha_dropdown)
checkbox.pack(pady=12, padx=10)

my_label = ctk.CTkLabel(master=frame, text="")
my_label.pack(pady=20)

button = ctk.CTkButton(master=frame, text="Login", command=login)
button.pack(pady=12, padx=10)

combobox = ctk.CTkOptionMenu(
    master=frame,
    values=["Captcha 1"],
)
combobox.pack(pady=12, padx=10)


def main():
    root.mainloop()

if __name__ == "__main__":
    main()
