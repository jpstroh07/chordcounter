import sqlite3

progress_path = "src/persistence/db/progress.db"

class ProgressHandler:
    def __init__(self) -> None:
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
        
    def getProgress(self):
        conn = sqlite3.connect(progress_path)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM chord_progressions")
        result = cursor.fetchall()
        conn.close()
        return result