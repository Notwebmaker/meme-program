import tkinter as tk
import tkinter.messagebox

def show_win11error():
    tkinter.messagebox.showerror("Windows 11", "Task failed successfully.")
def showgenericerror():
    tkinter.messagebox.showerror("Error", "An error has occurred.")
def errorsgalore():
    for i in range(0, 100):
        tkinter.messagebox.showinfo("Notice", "buy now!")
def dontwannado():
    tkinter.messagebox.showerror("Notice", "Could not complete task because no.")


root = tk.Tk()
root.geometry("640x480")
root.title("meme program")

mainicon=tk .PhotoImage(file="assets/blank.png")
root.iconphoto(True, mainicon)
errorwin11button=tk.Button(root, text="task failed sucessfully windows 11", command=show_win11error)
errorwin11button.pack (padx=10, pady=10)
genericerrorbutton=tk.Button(root, text="generic error", command=showgenericerror)
genericerrorbutton.pack (padx=10, pady=10)
errorsgalorebutton=tk.Button(root, text="trying to get rid of that one popup be like(WARNING, PROCEED WITH CAUTION)", command=errorsgalore)
errorsgalorebutton.pack (padx=10, pady=10)
dontwannadobutton=tk.Button(root, text="could not complete task because no", command=dontwannado)
dontwannadobutton.pack (padx=10, pady=10)

root.mainloop()