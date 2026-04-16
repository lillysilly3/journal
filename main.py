import customtkinter as ctk
from login import LoginScreen
from database import initialize_db, has_password, reset_db
from setup import SetupScreen

def on_login_success():
    print("Logged in!")

def on_setup_complete():
    global setup_screen
    global login_screen
    setup_screen.pack_forget()
    login_screen = LoginScreen(app, on_login_success, on_reset)
    login_screen.pack(expand=True, fill="both")

def on_reset():
    global login_screen
    global setup_screen
    reset_db()
    login_screen.destroy()
    setup_screen = SetupScreen(app, on_setup_complete)
    setup_screen.pack(expand=True, fill="both")

app = ctk.CTk()
app.title("My Journal")
app.geometry("500x500")
ctk.set_appearance_mode("system")
ctk.set_default_color_theme("green")

initialize_db()

#Declaration before usage
setup_screen = None
login_screen = None

if has_password():
    login_screen = LoginScreen(app, on_login_success, on_reset)
    login_screen.pack(expand=True, fill="both")
else:
    setup_screen = SetupScreen(app, on_setup_complete)
    setup_screen.pack(expand=True, fill="both")
    
app.mainloop()