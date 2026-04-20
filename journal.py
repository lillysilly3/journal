import customtkinter as ctk
import datetime
from database import DatabaseClient
from calendar_widget import CalendarWidget
from moods import MOODS

class JournalScreen(ctk.CTkFrame):
    def __init__(self, parent, db: DatabaseClient):
        super().__init__(parent)
        self.db = db
        self.current_mood = ""


        #Grid
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=2)
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)

        #Frames
        self.top_frame = ctk.CTkFrame(self)
        self.top_frame.grid(row=0, columnspan=2, sticky="ew", padx=5, pady=5)

        self.left_frame = ctk.CTkFrame(self)
        self.left_frame.grid(row=1, column=0, sticky="ns", padx=5, pady=5)

        self.right_frame = ctk.CTkFrame(self)
        self.right_frame.grid(row=1, column=1, sticky="nsew", padx=5, pady=5)

        #Top buttons
        ctk.CTkButton(self.top_frame, text="Themes", command=self.open_themes).pack(side="left", padx=10, pady=10)
        ctk.CTkButton(self.top_frame, text="Save", command=self.save_entry).pack(side="left", padx=10, pady=10)
        ctk.CTkButton(self.top_frame, text="Calendar", command=self.toggle_calendar).pack(side="left", padx=10, pady=10)

        #Right frame grid
        self.right_frame.grid_columnconfigure(0, weight=1)
        self.right_frame.grid_rowconfigure(0, weight=0)
        self.right_frame.grid_rowconfigure(1, weight=2)

        #Date label
        today = datetime.date.today().strftime("%Y %B %d")
        self.date_label = ctk.CTkLabel(self.right_frame, text=today, font=ctk.CTkFont(size=18, weight="bold"))
        self.date_label. grid(row=0, column=0, sticky="w", padx=10, pady=10)

        #Textbox
        self.entry_textbox = ctk.CTkTextbox(self.right_frame, width=200)
        self.entry_textbox.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

        #Entry
        self.load_entry(datetime.date.today().strftime("%Y-%m-%d"))

        #Left frame grid
        self.left_frame.grid_rowconfigure(0, weight=0)
        self.left_frame.grid_rowconfigure(1, weight=0)
        self.left_frame.grid_rowconfigure(2, weight=1)
        self.left_frame.grid_columnconfigure(0, weight=1)

        #Calendar
        self.calendar = CalendarWidget(self.left_frame, db, self.load_entry)
        self.calendar.grid(row=0, column=0, padx=5, pady=5)
        
        #Mood tracker
        self.mood_frame = ctk.CTkFrame(self.left_frame)
        self.mood_frame.grid(row=1, column=0, padx=5, pady=5)
        ctk.CTkLabel(self.mood_frame, text="How do you feel today?", font=ctk.CTkFont(weight="bold")).pack(pady=5)

        for mood, color in MOODS:
            ctk.CTkButton(self.mood_frame, text=mood, fg_color=color, command=lambda m=mood: self.set_mood(m)).pack(pady=2)


    def open_themes(self):
        print("Themes clicked!")

    def save_entry(self):
        date = datetime.date.today().strftime("%Y-%m-%d")
        content = self.entry_textbox.get("1.0", "end-1c")
        print(f"Saving: {date}, {content}")
        #mood = self.current_mood if hasattr(self, "current_mood") else ""
        self.db.save_entry(date, content, self.current_mood)
        print("Entry saved!")

    def load_entry(self, date):
        result = self.db.get_entry(date)
        self.entry_textbox.delete("1.0", "end")
        if result:
            content, mood = result
            self.entry_textbox.insert("1.0", content)
            self.current_mood = mood if mood else ""

    def toggle_calendar(self):
        print("Calendar clicked!")

    def set_mood(self, mood):
        self.current_mood = mood
        print(f"Mood set: {mood}")

    