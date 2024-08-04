import tkinter
window = tkinter.Tk()
l1 = tkinter.Label(window, text = "example text" , font = ("Arial" , 14))
l1.grid(row =0 ,column = 0 , sticky = tkinter.E)
window.mainloop()