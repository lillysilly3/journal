import customtkinter as ctk
from login import LoginScreen
from database import initialize_db, has_password
from setup import SetupScreen

def on_login_success():
    print("Logged in!")

def on_setup_complete():
    setup_screen.pack_forget()
    login_screen = LoginScreen(app, on_login_success)
    login_screen.pack(expand=True, fill="both")

app = ctk.CTk()
app.title("My Journal")
app.geometry("400x500")
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("green")

initialize_db()

setup_screen = None

if has_password():
    login_screen = LoginScreen(app, on_login_success)
    login_screen.pack(expand=True, fill="both")
else:
    setup_screen = SetupScreen(app, on_setup_complete)
    setup_screen.pack(expand=True, fill="both")
    
    
app.mainloop()