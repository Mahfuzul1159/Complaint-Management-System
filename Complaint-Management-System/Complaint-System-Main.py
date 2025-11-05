from tkinter import *
from tkinter.ttk import Button, Radiobutton, Style
from tkinter.messagebox import *
from PIL import Image, ImageTk
from complaintListing import ComplaintListing
from configdb import ConnectionDatabase



# --------------------------
#   HOMEPAGE FUNCTION
# --------------------------
def homePage():
    global homeroot
    homeroot = Tk()
    homeroot.geometry('1200x600')
    homeroot.title('Complaint Management System')
    homeroot.resizable(False, False)
    homeroot.configure(bg='#6FE7FF')

    #photo = PhotoImage(file='C:\\Users\\Rafi\\Desktop\\RAFI\\RAFI\\CSE_Journey\\Complaint-Management-System\\book.png')
    label = Label(homeroot, bg='#6FE7FF')
    label.pack()

    submitbtn = Button(homeroot, text='Submit', command=submitPage)
    submitbtn.place(x=550, y=200)

    viewbtn = Button(homeroot, text='View Complain', command=viewPage)
    viewbtn.place(x=542, y=230)

    homeroot.mainloop()


# --------------------------
#   SUBMIT PAGE
# --------------------------
def submitPage():
    homeroot.destroy()
    conn = ConnectionDatabase()
    root = Tk()
    root.geometry('1200x600')
    root.title('Complaint Management System - Submit Page')
    root.configure(bg='#6FE7FF')

    style = Style()
    style.theme_use('classic')
    for styles in ['TLabel', 'TButton', 'TRadioButton']:
        style.configure(styles, bg='blue')

    ButtonSubmit = Button(root, text='Submit Now')
    ButtonSubmit.grid(row=5, column=2)

    # labels
    first_name_label = Label(root, text="Firstname:")
    first_name_label.grid(row=0, column=0, padx=10, pady=10)

    last_name_label = Label(root, text="Lastname:")
    last_name_label.grid(row=1, column=0, padx=10, pady=10)

    address_label = Label(root, text="Address:")
    address_label.grid(row=2, column=0, padx=10, pady=10)

    gender_label = Label(root, text="Gender:")
    gender_label.grid(row=3, column=0, padx=10, pady=10)

    comment_label = Label(root, text="Comment:")
    comment_label.grid(row=4, column=0, padx=10, pady=10)

    # entries
    firstname = Entry(root, width=40, font=('Arial', 14, 'bold'))
    firstname.grid(row=0, column=1, columnspan=2)

    lastname = Entry(root, width=40, font=('Arial', 14, "bold"))
    lastname.grid(row=1, column=1, columnspan=2)

    address = Entry(root, width=40, font=('Arial', 14, "bold"))
    address.grid(row=2, column=1, columnspan=2)

    GenderGroup = StringVar()
    Radiobutton(root, text='Male', value='male', variable=GenderGroup).grid(row=3, column=1)
    Radiobutton(root, text='Female', value='female', variable=GenderGroup).grid(row=3, column=2)

    comment = Text(root, width=40, height=5, font=('Arial', 14))
    comment.grid(row=4, column=1, columnspan=2, padx=10, pady=10)

    def SaveData():
        message = conn.Add(firstname.get(), lastname.get(), address.get(), GenderGroup.get(), comment.get(1.0, 'end'))
        firstname.delete(0, 'end')
        lastname.delete(0, 'end')
        address.delete(0, 'end')
        comment.delete(1.0, 'end')
        showinfo(title='Add Information', message=message)

    ButtonSubmit.config(command=SaveData)

    # 🔙 BACK BUTTON
    def goBack():
        root.destroy()
        homePage()

    backBtn = Button(root, text='Back', command=goBack)
    backBtn.grid(row=6, column=0, pady=20)

    root.mainloop()


# --------------------------
#   VIEW PAGE
# --------------------------
def viewPage():
    homeroot.destroy()
    viewroot = Tk()
    viewroot.geometry('1200x600')
    viewroot.title('Complaint Management System - Admin Login')
    viewroot.configure(bg='#6FE7FF')

    ButtonList = Button(viewroot, text='View Complain')
    ButtonList.grid(row=5, column=1)

    def adminLogin(username, password):
        adminUsername = "u1"
        adminPassword = "123"

        if adminUsername == username and adminPassword == password:
            listrequest = ComplaintListing()
        else:
            showerror(title="Error!", message="Invalid Login")

    label = Label(viewroot, text="Username:")
    label.grid(row=7, column=0, padx=10, pady=10)
    username = Entry(viewroot, width=40, font=('Arial', 14))
    username.grid(row=7, column=1, columnspan=2)

    label = Label(viewroot, text="Password:")
    label.grid(row=8, column=0, padx=10, pady=10)
    password = Entry(viewroot, width=40, font=('Arial', 14), show="*")
    password.grid(row=8, column=1, columnspan=2)

    ButtonLogin = Button(viewroot, text="Login")
    ButtonLogin.grid(row=9, column=1)
    ButtonLogin.config(command=lambda: adminLogin(username.get(), password.get()))

    # 🔙 BACK BUTTON
    def goBack():
        viewroot.destroy()
        homePage()

    backBtn = Button(viewroot, text='Back', command=goBack)
    backBtn.grid(row=10, column=0, pady=20)

    viewroot.mainloop()


# --------------------------
#   START APP
# --------------------------
homePage()
from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *
from PIL import Image, ImageTk
from complaintListing import ComplaintListing
from configdb import ConnectionDatabase


# --------------------------
#   HOMEPAGE FUNCTION
# --------------------------
def homePage():
    global homeroot
    homeroot = Tk()
    homeroot.geometry('1200x600')
    homeroot.title('Complaint Management System')
    homeroot.resizable(False, False)
    homeroot.configure(bg='#6FE7FF')

    photo = PhotoImage(file='C:\\Users\\Rafi\\Desktop\\RAFI\\RAFI\\CSE_Journey\\Complaint-Management-System\\book.png')
    label = Label(homeroot, image=photo, bg='#6FE7FF')
    label.pack()

    submitbtn = Button(homeroot, text='Submit', command=submitPage)
    submitbtn.place(x=550, y=200)

    viewbtn = Button(homeroot, text='View Complain', command=viewPage)
    viewbtn.place(x=542, y=230)

    homeroot.mainloop()


# --------------------------
#   SUBMIT PAGE
# --------------------------
def submitPage():
    homeroot.destroy()
    conn = ConnectionDatabase()
    root = Tk()
    root.geometry('1200x600')
    root.title('Complaint Management System - Submit Page')
    root.configure(bg='#6FE7FF')

    style = Style()
    style.theme_use('classic')
    for styles in ['TLabel', 'TButton', 'TRadioButton']:
        style.configure(styles, bg='blue')

    ButtonSubmit = Button(root, text='Submit Now')
    ButtonSubmit.grid(row=5, column=2)

    # labels
    first_name_label = Label(root, text="Firstname:")
    first_name_label.grid(row=0, column=0, padx=10, pady=10)

    last_name_label = Label(root, text="Lastname:")
    last_name_label.grid(row=1, column=0, padx=10, pady=10)

    address_label = Label(root, text="Address:")
    address_label.grid(row=2, column=0, padx=10, pady=10)

    gender_label = Label(root, text="Gender:")
    gender_label.grid(row=3, column=0, padx=10, pady=10)

    comment_label = Label(root, text="Comment:")
    comment_label.grid(row=4, column=0, padx=10, pady=10)

    # entries
    firstname = Entry(root, width=40, font=('Arial', 14, 'bold'))
    firstname.grid(row=0, column=1, columnspan=2)

    lastname = Entry(root, width=40, font=('Arial', 14, "bold"))
    lastname.grid(row=1, column=1, columnspan=2)

    address = Entry(root, width=40, font=('Arial', 14, "bold"))
    address.grid(row=2, column=1, columnspan=2)

    GenderGroup = StringVar()
    Radiobutton(root, text='Male', value='male', variable=GenderGroup).grid(row=3, column=1)
    Radiobutton(root, text='Female', value='female', variable=GenderGroup).grid(row=3, column=2)

    comment = Text(root, width=40, height=5, font=('Arial', 14))
    comment.grid(row=4, column=1, columnspan=2, padx=10, pady=10)

    def SaveData():
        message = conn.Add(firstname.get(), lastname.get(), address.get(), GenderGroup.get(), comment.get(1.0, 'end'))
        firstname.delete(0, 'end')
        lastname.delete(0, 'end')
        address.delete(0, 'end')
        comment.delete(1.0, 'end')
        showinfo(title='Add Information', message=message)

    ButtonSubmit.config(command=SaveData)

    # 🔙 BACK BUTTON
    def goBack():
        root.destroy()
        homePage()

    backBtn = Button(root, text='Back', command=goBack)
    backBtn.grid(row=6, column=0, pady=20)

    root.mainloop()


# --------------------------
#   VIEW PAGE
# --------------------------
def viewPage():
    homeroot.destroy()
    viewroot = Tk()
    viewroot.geometry('1200x600')
    viewroot.title('Complaint Management System - Admin Login')
    viewroot.configure(bg='#6FE7FF')

    ButtonList = Button(viewroot, text='View Complain')
    ButtonList.grid(row=5, column=1)

    def adminLogin(username, password):
        adminUsername = "u1"
        adminPassword = "123"

        if adminUsername == username and adminPassword == password:
            listrequest = ComplaintListing()
        else:
            showerror(title="Error!", message="Invalid Login")

    label = Label(viewroot, text="Username:")
    label.grid(row=7, column=0, padx=10, pady=10)
    username = Entry(viewroot, width=40, font=('Arial', 14))
    username.grid(row=7, column=1, columnspan=2)

    label = Label(viewroot, text="Password:")
    label.grid(row=8, column=0, padx=10, pady=10)
    password = Entry(viewroot, width=40, font=('Arial', 14), show="*")
    password.grid(row=8, column=1, columnspan=2)

    ButtonLogin = Button(viewroot, text="Login")
    ButtonLogin.grid(row=9, column=1)
    ButtonLogin.config(command=lambda: adminLogin(username.get(), password.get()))

    # 🔙 BACK BUTTON
    def goBack():
        viewroot.destroy()
        homePage()

    backBtn = Button(viewroot, text='Back', command=goBack)
    backBtn.grid(row=10, column=0, pady=20)

    viewroot.mainloop()


# --------------------------
#   START APP
# --------------------------
homePage()
from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *
from PIL import Image, ImageTk
from complaintListing import ComplaintListing
from configdb import ConnectionDatabase


# --------------------------
#   HOMEPAGE FUNCTION
# --------------------------
def homePage():
    global homeroot
    homeroot = Tk()
    homeroot.geometry('1200x600')
    homeroot.title('Complaint Management System')
    homeroot.resizable(False, False)
    homeroot.configure(bg='#6FE7FF')

    photo = PhotoImage(file='C:\\Users\\Rafi\\Desktop\\RAFI\\RAFI\\CSE_Journey\\Complaint-Management-System\\book.png')
    label = Label(homeroot, image=photo, bg='#6FE7FF')
    label.pack()

    submitbtn = Button(homeroot, text='Submit', command=submitPage)
    submitbtn.place(x=550, y=200)

    viewbtn = Button(homeroot, text='View Complain', command=viewPage)
    viewbtn.place(x=542, y=230)

    homeroot.mainloop()


# --------------------------
#   SUBMIT PAGE
# --------------------------
def submitPage():
    homeroot.destroy()
    conn = ConnectionDatabase()
    root = Tk()
    root.geometry('1200x600')
    root.title('Complaint Management System - Submit Page')
    root.configure(bg='#6FE7FF')

    style = Style()
    style.theme_use('classic')
    for styles in ['TLabel', 'TButton', 'TRadioButton']:
        style.configure(styles, bg='blue')

    ButtonSubmit = Button(root, text='Submit Now')
    ButtonSubmit.grid(row=5, column=2)

    # labels
    first_name_label = Label(root, text="Firstname:")
    first_name_label.grid(row=0, column=0, padx=10, pady=10)

    last_name_label = Label(root, text="Lastname:")
    last_name_label.grid(row=1, column=0, padx=10, pady=10)

    address_label = Label(root, text="Address:")
    address_label.grid(row=2, column=0, padx=10, pady=10)

    gender_label = Label(root, text="Gender:")
    gender_label.grid(row=3, column=0, padx=10, pady=10)

    comment_label = Label(root, text="Comment:")
    comment_label.grid(row=4, column=0, padx=10, pady=10)

    # entries
    firstname = Entry(root, width=40, font=('Arial', 14, 'bold'))
    firstname.grid(row=0, column=1, columnspan=2)

    lastname = Entry(root, width=40, font=('Arial', 14, "bold"))
    lastname.grid(row=1, column=1, columnspan=2)

    address = Entry(root, width=40, font=('Arial', 14, "bold"))
    address.grid(row=2, column=1, columnspan=2)

    GenderGroup = StringVar()
    Radiobutton(root, text='Male', value='male', variable=GenderGroup).grid(row=3, column=1)
    Radiobutton(root, text='Female', value='female', variable=GenderGroup).grid(row=3, column=2)

    comment = Text(root, width=40, height=5, font=('Arial', 14))
    comment.grid(row=4, column=1, columnspan=2, padx=10, pady=10)

    def SaveData():
        message = conn.Add(firstname.get(), lastname.get(), address.get(), GenderGroup.get(), comment.get(1.0, 'end'))
        firstname.delete(0, 'end')
        lastname.delete(0, 'end')
        address.delete(0, 'end')
        comment.delete(1.0, 'end')
        showinfo(title='Add Information', message=message)

    ButtonSubmit.config(command=SaveData)

    # 🔙 BACK BUTTON
    def goBack():
        root.destroy()
        homePage()

    backBtn = Button(root, text='Back', command=goBack)
    backBtn.grid(row=6, column=0, pady=20)

    root.mainloop()


# --------------------------
#   VIEW PAGE
# --------------------------
def viewPage():
    homeroot.destroy()
    viewroot = Tk()
    viewroot.geometry('1200x600')
    viewroot.title('Complaint Management System - Admin Login')
    viewroot.configure(bg='#6FE7FF')

    ButtonList = Button(viewroot, text='View Complain')
    ButtonList.grid(row=5, column=1)

    def adminLogin(username, password):
        adminUsername = "u1"
        adminPassword = "123"

        if adminUsername == username and adminPassword == password:
            listrequest = ComplaintListing()
        else:
            showerror(title="Error!", message="Invalid Login")

    label = Label(viewroot, text="Username:")
    label.grid(row=7, column=0, padx=10, pady=10)
    username = Entry(viewroot, width=40, font=('Arial', 14))
    username.grid(row=7, column=1, columnspan=2)

    label = Label(viewroot, text="Password:")
    label.grid(row=8, column=0, padx=10, pady=10)
    password = Entry(viewroot, width=40, font=('Arial', 14), show="*")
    password.grid(row=8, column=1, columnspan=2)

    ButtonLogin = Button(viewroot, text="Login")
    ButtonLogin.grid(row=9, column=1)
    ButtonLogin.config(command=lambda: adminLogin(username.get(), password.get()))

    # 🔙 BACK BUTTON
    def goBack():
        viewroot.destroy()
        homePage()

    backBtn = Button(viewroot, text='Back', command=goBack)
    backBtn.grid(row=10, column=0, pady=20)

    viewroot.mainloop()


# --------------------------
#   START APP
# --------------------------
homePage()

