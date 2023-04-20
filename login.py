from tkinter import *
from PIL import Image,ImageTk
from dashboard import *
from sales import *
from tkinter import ttk,messagebox
import sqlite3
class log:
    def __init__(self):
        global root
        root = Tk()
        self.root = root
        self.root.geometry("1200x600+160+100")
        self.root.title("Dairy Management System")
        #self.root.config(bg="white")
        self.root.focus_force()
        self.bg = PhotoImage(file="image/login_bg.png")
        self.bg_label = Label(self.root, image=self.bg)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.uid=StringVar()
        self.pword=StringVar()

        login_Frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        login_Frame.place(x=60, y=35, width=500, height=505)
        label = Label(login_Frame, text="LOGIN ", padx=10, pady=10, bg="white",bd=10,relief=RIDGE ,font=("goudy old style", 40)).place(x=20,y=20,width=455)
        lbl_uid=Label(login_Frame,text="User Mail ID:",font=("goudy old style",24),bg="white").place(x=30,y=180)
        lbl_pword=Label(login_Frame,text="Password:",font=("goudy old style",24),bg="white").place(x=30,y=270)
        txt_uid=Entry(login_Frame,textvariable=self.uid,font = ("goudy old style",24),bd=3,bg="light yellow").place(x=230,y=180,width=230)
        txt_pword=Entry(login_Frame,textvariable=self.pword,font = ("goudy old style",24),bd=3,bg="light yellow",show='*').place(x=230,y=270,width=230)
        btn_login=Button(login_Frame,text="Login",command=self.add,font=("goudy old style",24),bg="#4caf50",fg="white",cursor="hand2",bd=3,relief=RIDGE).place(x=100,y=375,width=300,height=50)
    def add(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()

        try:
            if self.uid.get()=="" or self.pword.get()=="":
                messagebox.showerror("Error","Info. Required",parent=self.root)
            else:
                rows = []
                r=[]
                cur.execute("Select * from employee where email =?",(self.uid.get(),))
                rows = cur.fetchall()
                print(rows)
                for row in rows:
                    r.append(row)
                #print(r)
                if len(rows) ==0:
                    messagebox.showerror("Error","User not registered",parent=self.root)
                else:
                    uname=row[2]
                    password=row[7]
                    type=row[8]
                    print(uname)
                    print(password)
                    print(type)
                    if(uname==str(self.uid.get()) and password==str(self.pword.get())):
                        if(type=="Admin"):
                            root.destroy()
                            MDS()
                            print("Admin Logged in")

                        else:
                            self.new_win = Toplevel(self.root)
                            self.new_obj = BillClass(self.new_win)
                            print("Employee logged in")
                    else:
                        messagebox.showerror("Login Error","Invalid Mail ID/ Password")
                        print("Invalid Details")
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

if __name__=="__main__":

    obj = log()
    root.mainloop()