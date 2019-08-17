import tkinter 
import sqlite3 as sq
import sqlHelper as helper
def exitwind(root):
    root.destroy()



def getData(title,description):
    helper.saveData(text1=title,text2=description)




def addTask():
    master=tkinter.Tk()
    
    tkinter.Label(master, text='Title').grid(row=0)    
    tkinter.Label(master, text='TitleDescription').grid(row=1) 
    e1 = tkinter.Entry(master)  
    e2 = tkinter.Entry(master) 
    e1.insert(0,"s")
    e2.insert(0,"j")
    e1.grid(row=0, column=1) 
    e2.grid(row=1, column=1) 
    print("e1=="+e1.get())
    submit=tkinter.Button(master,height=1,width=10,text="commit",command=getData(e1.get(),e2.get()))
    submit.Pack()
    tkinter.mainloop()


addTask()
