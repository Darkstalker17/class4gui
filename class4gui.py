from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename

root = Tk()
root.title("Codingal's Text editor")
root.geometry("600x500")
root.rowconfigure(0, minsize=800, weight=1)
root.columnconfigure(1, minsize=800, weight=1)

def open_file():
    file_path = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All files", "*.*")]
    )
    if not file_path:
        return
    txt_edit.delete(1.0, END)
    with open(file_path, "r") as input_file:
        text = input_file.read()
        txt_edit.insert(END, text)
        input_file.close()
    root.title(f"Codingal text editor - {file_path}")

def save_file():
    file_path = asksaveasfilename(
        filetypes=[("Text Files", "*.txt"), ("All files", "*.*")]
    )
    if not file_path:
        return
    with open(file_path, "w") as output_file:
        text = txt_edit.get(1.0, END)
        output_file.write(text)
    root.title(f"Codingal text editor - {file_path}")


txt_edit = Text(root)
fr_buttons = Frame(root, relief=RAISED, bd=2)
btn_open = Button(fr_buttons, text="Open", command=open_file)
btn_save = Button(fr_buttons, text="Save As...", command=save_file)

btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky="ew", padx=5)

fr_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")

root.mainloop()