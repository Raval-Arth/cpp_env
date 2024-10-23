import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import subprocess
import os

class Watcher:
    DIRECTORY_TO_WATCH = "."  # Directory to watch (current directory)

    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.DIRECTORY_TO_WATCH, recursive=False)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except KeyboardInterrupt:
            self.observer.stop()
        self.observer.join()

class Handler(FileSystemEventHandler):
    @staticmethod
    def on_modified(event):
        if event.src_path.endswith(".py"):  # Watch only .py files
            # Clear the screen
            os.system('cls' if os.name == 'nt' else 'clear')
            subprocess.run(["python", event.src_path])

if __name__ == '__main__':
    w = Watcher()
    w.run()
