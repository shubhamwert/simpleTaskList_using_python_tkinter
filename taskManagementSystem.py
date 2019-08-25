import tkinter
import sqlite3 as sq
import sqlHelper as helper

def getData(e1,e2):
    title=e1.get()
    description=e2.get()
    if len(title)!=0 & len(description):
        helper.saveData(text1=""+title,text2=""+description)




def addTask():
    master=tkinter.Tk()
    
    tkinter.Label(master, text='Title').grid(row=0)    
    tkinter.Label(master, text='TitleDescription').grid(row=1) 
    e1 = tkinter.Entry(master)  
    e2 = tkinter.Entry(master) 
   
    e1.grid(row=0, column=1) 
    e2.grid(row=1, column=1) 
    print("e1=="+e1.get())
    submit=tkinter.Button(master,height=1,width=10,text="commit",command=lambda:getData(e1,e2))
    submit.grid(row=2,column=1)
    tkinter.mainloop()


def getTaskName():
    mastera=tkinter.Tk()
    
    
    scrollbar = tkinter.Scrollbar(mastera)
    scrollbar.pack( side = tkinter.RIGHT, fill = tkinter.Y )

    mylist = tkinter.Listbox(mastera, yscrollcommand = scrollbar.set )
    mylist.bind('<<ListboxSelect>>',lambda event:onClickEvent(mylist))
    p=helper.getData()
    for i in p:
            mylist.insert(tkinter.END,i[0])

    mylist.pack( side = tkinter.LEFT, fill = tkinter.BOTH )
    scrollbar.config( command = mylist.yview )

    mastera.mainloop()
def onClickEvent(mylist):
        selection=mylist.curselection()
        if len (selection)>0:
                print(selection[0])
                p=helper.getData()
                master=tkinter.Tk()
                viewText=tkinter.Text(master)
                print(p[selection[0]][1])
                viewText.insert(tkinter.END,p[selection[0]][1])
                viewText.grid(row=0,column=0)
                master.mainloop()

getTaskName() 
addTask()

