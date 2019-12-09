import os
import tkinter
from tkinter import filedialog, Listbox, messagebox


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
        try:
            os.startfile(f)
        except OSError:
            messagebox.showerror("Error", "Unable to open " + f +
                                 "! Do you have a default program set to open this type of file?")


def main():
    root = tkinter.Tk()
    root.title('Multi-Open')
    root.iconbitmap('icon.ico')
    root.minsize(300, 200)
    files = tkinter.Variable()
    listbox = Listbox(root, listvariable=files)
    listbox.pack(fill='x')
    file_button = tkinter.Button(
        root, text="Select Files", command=lambda: add_files(root, listbox))
    file_button.pack(fill='x')
    run_button = tkinter.Button(
        root, text="Open All Files", command=lambda: open_files(files))
    run_button.pack(fill='x')
    root.mainloop()


if __name__ == "__main__":
    main()
