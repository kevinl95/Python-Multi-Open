import os
import tkinter
from tkinter import filedialog, Listbox


def add_files(root, box):
    files = filedialog.askopenfilenames(parent=root, title='Choose your files')
    # Check that the user didn't cancel this action
    if len(files) > 0:
        # Clear box
        box.delete(0, tkinter.END)
        # Add files to the file list
        for item in files:
            box.insert(tkinter.END, item)


def open_files(files):
    # Retrieve the list of files from our variable
    file_list = files.get()
    # Loop through and open these files in their default Windows program
    for f in file_list:
        os.startfile(f)


def main():
    root = tkinter.Tk()
    files = tkinter.Variable()
    listbox = Listbox(root, listvariable=files)
    listbox.pack()
    file_button = tkinter.Button(
        root, text="Select Files", command=lambda: add_files(root, listbox))
    file_button.pack()
    run_button = tkinter.Button(
        root, text="Open All Files", command=lambda: open_files(files))
    run_button.pack()
    root.mainloop()


if __name__ == "__main__":
    main()
