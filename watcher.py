import time
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from detector import analyze_log_line

LOG_FILE = "logs/sample_auth.log"


class LogHandler(FileSystemEventHandler):

    def __init__(self):
        # Start from the current end of the file
        if os.path.exists(LOG_FILE):
            self.last_position = os.path.getsize(LOG_FILE)
        else:
            self.last_position = 0

    def on_modified(self, event):

        if not event.src_path.endswith("sample_auth.log"):
            return

        try:
            with open(LOG_FILE, "r") as file:

                file.seek(self.last_position)

                new_lines = file.readlines()

                self.last_position = file.tell()

            for line in new_lines:

                result = analyze_log_line(line)

                if result:
                    print(f"[ALERT] {result}")

        except Exception as error:
            print(f"[ERROR] {error}")


def start_watcher():

    event_handler = LogHandler()

    observer = Observer()

    observer.schedule(
        event_handler,
        path="logs",
        recursive=False
    )

    observer.start()

    print("=" * 50)
    print("AI GUARD - HIDS LOG MONITOR")
    print("=" * 50)
    print("Status: RUNNING")
    print("Monitoring:", LOG_FILE)
    print("Press CTRL+C to stop")
    print("=" * 50)

    try:

        while True:
            time.sleep(1)

    except KeyboardInterrupt:

        print("\nStopping monitor...")

        observer.stop()

    observer.join()


if __name__ == "__main__":
    start_watcher()