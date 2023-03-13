import os
from tkinter import filedialog
from traduction import convert

def main():
    directory = filedialog.askdirectory()
    directoryName = os.path.basename(os.path.normpath(directory))
    convert(directory,directoryName)

if __name__ == '__main__':
    main()