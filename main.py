from tkinter import *
from tkinter import ttk
from db import Database
from tkinter import messagebox


db= Database('Employee.db')
root=Tk()
root.title('Employee Management System')
root.geometry('1024x768+0+0')
root.config(bg='#2c3e58')
root.state('zoomed')

name=StringVar()
age=StringVar()
doj=StringVar()
gender=StringVar()
email=StringVar()
address=StringVar()
contact=StringVar()



# entries Frame
entries_frame = Frame(root, bg='lightblue')
entries_frame.pack(side=TOP,fill=X)
title = Label(entries_frame,text='Employee Management Details',font=('Times New Roman',14,'bold'),bg='lightblue',fg='black',justify='center')
title.grid(row=0,columnspan=3,padx=10,pady=10,sticky='w')

lblName=Label(entries_frame,text='Name',font=('Times New Roman',14),bg='lightblue',fg='black')
lblName.grid(row=1,column=0,padx=10,pady=10,sticky='w')
txtName=Entry(entries_frame,textvariable=name,font=('Times New Roman',14),width=30)
txtName.grid(row=1,column=1,padx=10,pady=10,sticky='w')


lblAge=Label(entries_frame,text='Age',font=('Times New Roman',14),bg='lightblue',fg='black')
lblAge.grid(row=1,column=2,padx=10,pady=10,sticky='w')
txtAge=Entry(entries_frame,textvariable=age,font=('Times New Roman',14),width=30)
txtAge.grid(row=1,column=3,padx=10,pady=10,sticky='w')

lblDoj=Label(entries_frame,text='D.O.J',font=('Times New Roman',14),bg='lightblue',fg='black')
lblDoj.grid(row=2,column=0,padx=10,pady=10,sticky='w')
txtDoj=Entry(entries_frame,textvariable=doj,font=('Times New Roman',14),width=30)
txtDoj.grid(row=2,column=1,padx=10,pady=10,sticky='w')

lblGender=Label(entries_frame,text='Gender',font=('Times New Roman',14),bg='lightblue',fg='black')
lblGender.grid(row=2,column=2,padx=10,pady=10,sticky='w')
comboGender=ttk.Combobox(entries_frame,font=('Times New Roman',14),width=28, state='readonly')
comboGender['value']=('Male','Female')
comboGender.grid(row=2,column=3,padx=10,pady=10,sticky='w')

lblEmail=Label(entries_frame,text='Email',font=('Times New Roman',14),bg='lightblue',fg='black')
lblEmail.grid(row=3,column=0,padx=10,pady=10,sticky='w')
txtEmail=Entry(entries_frame,textvariable=email,font=('Times New Roman',14),width=30)
txtEmail.grid(row=3,column=1,padx=10,pady=10,sticky='w')

lblContact=Label(entries_frame,text='Contact',font=('Times New Roman',14),bg='lightblue',fg='black')
lblContact.grid(row=3,column=2,padx=10,pady=10,sticky='w')
txtContact=Entry(entries_frame,textvariable=contact,font=('Times New Roman',14),width=30)
txtContact.grid(row=3,column=3,padx=10,pady=10,sticky='w')

lblAddress=Label(entries_frame,text='Address',font=('Times New Roman',14),bg='lightblue',fg='black')
lblAddress.grid(row=4,column=0,padx=10,pady=10,sticky='w')
txtAddress=Text(entries_frame,font=('Times New Roman',14),height=6)
txtAddress.grid(row=5,columns=1,columnspan=4,padx=10,sticky='w')

def getData(event):
    selected_row=tv.focus()
    data=tv.item(selected_row)
    global row
    row = data['values']
    # print(row)
    name.set(row[1])
    age.set(row[2])
    doj.set(row[3])
    email.set(row[4])
    gender.set(row[5])
    contact.set(row[6])
    txtAddress.delete(1.0, END)
    txtAddress.insert(END, row[7])

def displayall():
    tv.delete(*tv.get_children())
    for row in db.fetch():
        tv.insert('',END,values=row)
def add_employee():
    if txtName.get()== '' or txtAge.get()== '' or txtDoj.get()== '' or txtEmail.get()== '' or txtContact.get()== '' or comboGender.get()== '' or txtAddress.get(1.0,END) == '':
        messagebox.showerror('Error in Input', 'Fill the all details')
        return
    db.insert(txtName.get(), txtAge.get(), txtDoj.get() ,txtEmail.get(),comboGender.get(), txtContact.get(), txtAddress.get(1.0,END))
    messagebox.showinfo('Success', 'Record inserted')
    clearall()
    displayall()

def update_employee():
    if txtName.get()== '' or txtAge.get()== '' or txtDoj.get()== '' or txtEmail.get()== '' or txtContact.get()== '' or comboGender.get()== '' or txtAddress.get(1.0,END) == '':
        messagebox.showerror('Error in Input', 'Fill the all details')
        return
    db.update(row[0], txtName.get(), txtAge.get(), txtDoj.get() ,txtEmail.get(),comboGender.get(), txtContact.get(), txtAddress.get(1.0,END))
    messagebox.showinfo('Success', 'Update successfully')
    clearall()
    displayall()

def delete_employee():
    db.remove(row[0])
    clearall()
    displayall()

def clearall():
    name.set('')
    age.set('')
    doj.set('')
    gender.set('')
    email.set('')
    txtAddress.delete(1.0,END)
    contact.set('')


btn_frame=Frame(entries_frame,bg='lightblue')
btn_frame.grid(row=6,column=0,columnspan=4,padx=10,pady=10,sticky='w')
btnAdd=Button(btn_frame,command=add_employee, text='Add Details',
              width=15,font=('Times New Roman',14,'bold'),bg='green',fg='white',bd=0).grid(row=0,column=0,padx=10)

btnEdit=Button(btn_frame,command=update_employee, text='Update Details',
               width=15,font=('Times New Roman',14,'bold'),bg='blue',fg='white',bd=0).grid(row=0,column=1,padx=10)

btnDelete=Button(btn_frame,command=delete_employee, text='Delete Details',
                 width=15,font=('Times New Roman',14,'bold'),bg='red',fg='white',bd=0).grid(row=0,column=2,padx=10)

btnClear=Button(btn_frame,command=clearall, text='Clear Details',
                 width=15,font=('Times New Roman',14,'bold'),bg='brown',fg='white',bd=0).grid(row=0,column=3,padx=10)


# Table frame
tree_frame= Frame(root,bg='white')
tree_frame.place(x=0,y=420,width=1330,height=410)
style=ttk.Style()
style.configure('mystyle.Treeview',font=('Times New Roman',14), rowheight=30)
style.configure('mystyle.Treeview.Heading',font=('Times New Roman',14))

tv=ttk.Treeview(tree_frame,columns=(1,2,3,4,5,6,7,8),style='mystyle.Treeview')
tv.heading('1', text='ID')
tv.column('1',width=5)
tv.heading('2', text='Name')
tv.heading('3', text='Age')
tv.column('3',width=8)
tv.heading('4', text='D.O.J')
tv.column('4',width=15)
tv.heading('5', text='Email')
tv.heading('6', text='Gender')
tv.column('6',width=10)
tv.heading('7', text='Contact')
tv.heading('8', text='Address')
tv['show']='headings'
tv.bind('<ButtonRelease-1>', getData)
tv.pack(fill=X)


displayall()
root.mainloop()