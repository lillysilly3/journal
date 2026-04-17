import customtkinter as ctk
import datetime
from database import DatabaseClient
import calendar

class JournalScreen(ctk.CTkFrame):
    def __init__(self, parent, db: DatabaseClient):
        super().__init__(parent)
        self.db = db

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

        #Left frame grid
        self.left_frame.grid_rowconfigure(0, weight=0)
        self.left_frame.grid_rowconfigure(1, weight=0)
        self.left_frame.grid_rowconfigure(2, weight=1)
        self.left_frame.grid_columnconfigure(0, weight=1)

        #Calendar
        self.calendar_frame = ctk.CTkFrame(self.left_frame)
        self.calendar_frame.grid(row=0, column=0, padx=5, pady=5)
        month_name = datetime.date.today().strftime("%B")
        ctk.CTkLabel(self.calendar_frame, text=month_name, font=ctk.CTkFont(weight="bold")).grid(row=0, column=0, columnspan=7, pady=5)
        days = ["Mo", "Tu", "We", "Th", "Fr", "Sa", "Su"]
        for i, day in enumerate(days):
            ctk.CTkLabel(self.calendar_frame, text=day, width=30).grid(row=1, column=i, padx=2)

        #Days in the calendar
        cal = calendar.monthcalendar(datetime.date.today().year, datetime.date.today().month)
        today = datetime.date.today().day

        for week_num, week in enumerate(cal):
            for day_num, day in enumerate(week):
                if day == 0:
                    ctk.CTkLabel(self.calendar_frame, text="", width=30).grid(row=week_num+2, column=day_num, padx=1, pady=1)
                elif day == today:
                    ctk.CTkButton(self.calendar_frame, text=str(day), width=20, height=20, fg_color="#4EB121", corner_radius=20).grid(row=week_num+2, column=day_num, padx=1, pady=1)
                else:
                    ctk.CTkButton(self.calendar_frame, text=str(day), width=20, height=20, fg_color="transparent").grid(row=week_num+2, column=day_num, padx=1, pady=1)

        

    def open_themes(self):
        print("Themes clicked!")

    def save_entry(self):
        print("Save clicked!")

    def toggle_calendar(self):
        print("Calendar clicked!")