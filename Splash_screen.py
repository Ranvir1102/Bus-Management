from tkinter import *
root=Tk()
h,w=root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))
bus=PhotoImage(file='.\\Bus_for_project.png')
Label(root,image=bus).pack()
Label(root,text='Online Bus Booking System',font='Times 40 bold',bg='light blue',fg='red').pack()
Label(root,text='\n\n\n').pack()
Label(root,text='Name:Vishal Kumar',font='Times 20 bold',fg='blue').pack()
Label(root,text='\n').pack()
Label(root,text='Er:211B352',font='Times 20 bold',fg='blue').pack()
Label(root,text='\n').pack()
Label(root,text='Mobile:7007934854',font='Times 20 bold',fg='blue').pack()
Label(root,text='\n\n\n').pack()
Label(root,text='Submitted To:Dr.Mahesh Kumar',font='Times 30 bold',bg='light blue',fg='red').pack()
Label(root,text='Project Based Learning',font='Times 15 bold',fg='red').pack()
def close(e=1):
    root.destroy()
    import Home_screen
root.after(5000,close)
root.mainloop()
