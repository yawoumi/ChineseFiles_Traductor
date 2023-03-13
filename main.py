import os
import pathlib
from tkinter import filedialog
from traduction import convert

def main():
    directory = filedialog.askdirectory(title="Hello there, select your folder")
    if directory == "":
        print("okay")
        print("No folder selected. Program exiting.")
        quit()
    else:
        directoryName = str(os.path.basename(os.path.normpath(directory)))
        convert(directory,directoryName)

if __name__ == '__main__':
    main()