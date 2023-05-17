import sqlite3
from logic.Progress import Progress
from errors.ProgressNotFoundError import ProgressNotFoundError

progress_path = "src/persistence/db/progress.db"

class ProgressHandler:
    def __init__(self):
        conn = sqlite3.connect(progress_path)
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS chord_progressions (
            id INTEGER PRIMARY KEY,
            chord_progression TEXT,
            chord_count INTEGER,
            date DATETIME DEFAULT (datetime('now', 'localtime'))
            )
        """)
        conn.close()
        
    def insertProgress(self, chord1, chord2, number):
        conn = sqlite3.connect(progress_path)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO chord_progressions (chord_progression, chord_count) VALUES (?, ?)", (f"{chord1} -> {chord2}", number))
        conn.commit()
        conn.close()
    
    def getAllProgress(self):
        conn = sqlite3.connect(progress_path)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM chord_progressions")
        result = cursor.fetchall()

        if len(result) == 0:
            raise ProgressNotFoundError("No progress found")

        progress = []
        for row in result:
            progress.append(Progress(row[1], row[2], row[3]))

        conn.close()
        return progress
        
    def getProgress(self, chord1, chord2):
        conn = sqlite3.connect(progress_path)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM chord_progressions WHERE chord_progression = ?", (f"{chord1} -> {chord2}",))
        result = cursor.fetchall()

        if len(result) == 0:
            raise ProgressNotFoundError(f"No progress found for {chord1} -> {chord2}")
        
        progress = Progress(result[0][1], result[0][2], result[0][3])
        conn.close()
        return progress