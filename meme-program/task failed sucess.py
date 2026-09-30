import tkinter as tk
import tkinter.messagebox

#partially assisted by ai(for boilerplate and repetitive code, i still did most of the work))

def showwin11error():
    tkinter.messagebox.showerror("Windows 11", "Task failed successfully.")
def showwin10error():
    tkinter.messagebox.showerror("Windows 10", "Task failed successfully.")
def showlinuxerror():
    tkinter.messagebox.showerror("Linux", "Task failed successfully.")
def showgenericerror():
    tkinter.messagebox.showerror("Error", "An error has occurred.")
def errorsgalore():
    for i in range(0, 64):
        tkinter.messagebox.showinfo("Notice", "buy now!")
def dontwannado():
    tkinter.messagebox.showerror("Error", "Could not complete task because no.")
message="wait how are you seeing this?"
def custommessage():
    global message
    message=custommessageinput.get() or "type somthing in the box below to change this message"
    tkinter.messagebox.showinfo("Notice", message)
root = tk.Tk()
root.geometry("640x480")
root.title("meme program")

mainicon=tk .PhotoImage(file="assets/blank.png")
root.iconphoto(True, mainicon)
errorwin11button=tk.Button(root, text="task failed sucessfully windows 11", command=showwin11error)
errorwin11button.pack (padx=10, pady=10)

errorwin10button=tk.Button(root, text="task failed sucessfully windows 10", command=showwin10error)
errorwin10button.pack (padx=10, pady=10)

errorlinuxbutton=tk.Button(root, text="task failed sucessfully linux", command=showlinuxerror)
errorlinuxbutton.pack (padx=10, pady=10)

genericerrorbutton=tk.Button(root, text="generic error", command=showgenericerror)
genericerrorbutton.pack (padx=10, pady=10)

errorsgalorebutton=tk.Button(root, text="trying to get rid of that one popup be like(WARNING, PROCEED WITH CAUTION)", command=errorsgalore)
errorsgalorebutton.pack (padx=10, pady=10)

dontwannadobutton=tk.Button(root, text="could not complete task because no", command=dontwannado)
dontwannadobutton.pack (padx=10, pady=10)

custommessagebutton=tk.Button(root, text="custom message", command=custommessage)
custommessagebutton.pack (padx=10, pady=0)

custommessageinput=tk.Entry(root)
custommessageinput.pack (padx=10, pady=0)


root.mainloop()