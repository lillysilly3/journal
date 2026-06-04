# Journal App

A personal desktop journal application built with Python and CustomTkinter. Write daily entries, track your mood, and navigate your past through a built-in calendar.

---

![Journal screenshot 3](/assets/journal3.png)

## Features

- **Password protected** — secure login with bcrypt hashing and a password hint system
- **Daily entries** — write journal entries for any day, with auto-refresh after saving
- **Mood tracking** — tag each entry with a mood (Happy, Neutral, Sad, Angry, Tired, Energetic)
- **Mood calendar** — each day is color coded by mood
- **Calendar navigation** — browse any month and year to find past entries 
- **Entry indicators** — days with entries are visually distinct from empty days
- **Selected day highlight** — always know which day you are viewing
- **Password reset** — use hint button for a previously set hint or reset password resetting all entries together

![Journal screenshot 1](/assets/journal1.png)

![Journal screenshot 2](/assets/journal2.png)

---

## What I Explored Building This

This was my first real Python project after completing the Boot.dev Python and many other courses. Here is what I had an opportunity to do more of:

- **CustomTkinter** — build desktop UIs with frames, grids, buttons, labels, textboxes and popups
- **SQLite3** — design a database, write SQL queries, using primary keys and `INSERT OR REPLACE`
- **bcrypt** — hash and verify passwords securely
- **OOP** — build classes, inheritance, pass callbacks between screens
- **App architecture** — separate concerns across multiple files (`login.py`, `setup.py`, `journal.py`, `calendar_widget.py`, `database.py`)
- **Database client pattern** — set up persistent connection instead of opening/closing per query
- **Caching** — cache month entries to reduce database calls on the calendar
- **Git** — commit, push and manage a lovely project on GitHub
- **Debugging** — read tracebacks, use print statements, fix scope and naming issues

---

## Prerequisites

- Python 3.x+
- pip

## Installation

### Steps

1. Clone the repository:
```bash
git clone git@github.com:lillysilly3/journal.git
cd journal
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the app:
```bash
python main.py
```

On first launch you will be prompted to create a password. After that you can log in and start journaling!

---

## Project Structure

```
journal/
├── main.py                    # App entry point
├── app/
│   ├── screens/
│   │   ├── login.py           # Login screen
│   │   ├── setup.py           # Password setup screen
│   │   └── journal.py         # Main journal screen
│   ├── components/
│   │   ├── calendar_widget.py # Calendar component
│   │   └── moods.py           # Mood definitions
│   └── utils/
│       ├── database.py        # SQLite database client
│       └── theme.py           # App color theme
├── assets/                    # Reserved for future assets
├── requirements.txt
├── LICENSE
└── .gitignore
```

---

## Future Ideas

- Wallpaper customization
- Settings menu (change password, toggle mood tracker, customization)
- Search through entries by keyword
- Auto update after release

