import customtkinter

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("green")

root = customtkinter.CTk()
root.geometry("500x350")

def login():
    print("Prova")

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Login System", font=("Roboto", 24))
label.pack(pady=12, padx=10)

username = customtkinter.CTkEntry(master=frame, placeholder_text="Username")
username.pack(pady=12, padx=10)

password = customtkinter.CTkEntry(master=frame, placeholder_text="Password", show="*")
password.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=frame, text="Login", command=login)
button.pack(pady=12, padx=10)

checkbox = customtkinter.CTkCheckBox(master=frame, text="Remember me")
checkbox.pack(pady=12, padx=10)

root.mainloop()