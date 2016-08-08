from tkinter import*

def donothing():
    print("nothing")

root=Tk()
menubar=Menu(root)
connectMenu=Menu(menubar,tearoff=0)
#command can be 'NONE' but not 'none'
connectMenu.add_command(label="CFR",command=NONE)
connectMenu.add_command(label="Arina",command=donothing)
connectMenu.add_command(label="GEMS",command=donothing)
menubar.add_cascade(label="Connection",menu=connectMenu)
root.config(menu=menubar)
root.mainloop()
