import os
import subprocess
import time
import platform
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class CppFileHandler(FileSystemEventHandler):
    def __init__(self, root_folder):
        self.root_folder = root_folder
        self.build_folder = os.path.join(root_folder, 'build')  # Define the build folder

        # Create the build folder if it doesn't exist
        if not os.path.exists(self.build_folder):
            os.makedirs(self.build_folder)

    def on_modified(self, event):
        if event.src_path.endswith('.cpp'):
            print(f'{event.src_path} has been modified.')
            self.compile_and_run(event.src_path)

    def compile_and_run(self, cpp_file):
        # clear console
        os.system('cls')
        
        # Get the file name without the extension
        file_name = os.path.splitext(os.path.basename(cpp_file))[0]

        # Enclose the cpp_file path in quotes to handle spaces
        cpp_file_quoted = f'"{cpp_file}"'
        
        # Define the output executable path in the build folder
        output_executable = os.path.join(self.build_folder, file_name)

        # Compile the C++ file
        compile_command = f'g++ {cpp_file_quoted} -o "{output_executable}"'
        try:
            subprocess.run(compile_command, check=True, shell=True)
            print(f'\nCompiled {cpp_file} successfully.')

            # Determine the executable command based on the operating system
            if platform.system() == 'Windows':
                exec_command = f'"{output_executable}.exe"'
            else:
                exec_command = f'./{output_executable}'

            # Full path to input.txt in the root folder
            input_file_path = os.path.join(self.root_folder, 'input.txt')

            # Run the executable with input redirection from input.txt
            with open(input_file_path, 'r') as input_file:
                subprocess.run(exec_command, stdin=input_file, check=True, shell=True)
        except subprocess.CalledProcessError as e:
            print(f'Error compiling or running {cpp_file}: {e}')

if __name__ == "__main__":
    # Set the path to your project root folder
    project_folder = os.path.abspath('./')  # Use the absolute path of the current directory

    cpp_file_handler = CppFileHandler(root_folder=project_folder)
    observer = Observer()
    observer.schedule(cpp_file_handler, project_folder, recursive=True)

    print(f'Starting to monitor {project_folder} for changes in C++ files...')
    observer.start()
    try:
        while True:
            time.sleep(1)  # Keep the script running
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
