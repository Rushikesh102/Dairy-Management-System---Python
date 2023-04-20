import time
from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import datetime as dt
from employee import *
from supplier import *
from category import *
from product import *
from sales import *
from report import *
from billing import *
from login import *
class MDS:
    def __init__(self, ):
        global root
        root = Tk()
        self.root = root
        self.root.geometry("1580x1000+0+0")
        self.root.title("Dairy Management System")
        self.icon_title = PhotoImage(file="image/logo1.png")
        title = Label(self.root, text="Dairy Management System", image=self.icon_title, compound=LEFT,font=("times new roman", 40, "bold"), bg="#ADD8E6", anchor="w", padx=20).place(x=0, y=0,relwidth=1,height=70)
        self.Updatedt()

        self.MenuLogo = Image.open("image/menu_im.png")
        self.MenuLogo = self.MenuLogo.resize((200, 200), Image.ANTIALIAS)
        self.MenuLogo=ImageTk.PhotoImage(self.MenuLogo)
        LeftMenu = Frame(self.root, bd=2, relief=RIDGE, bg="#379683")
        LeftMenu.place(x=0, y=102, width=200, height=638)

        lbl_menuLogo = Label(LeftMenu, image=self.MenuLogo)
        lbl_menuLogo.pack(side=TOP, fill=X)
        self.icon_side = PhotoImage(file="image/side.png")
        lbl_menu = Label(LeftMenu, text="Menu", font=("times new roman", 20) ,bg="#242582", fg="white").pack(side=TOP,fill=X)
        btn_emp = Button(LeftMenu, text="Employee",command=self.Emp, font=("times new roman", 20, "bold"),image= self.icon_side,compound=LEFT,padx=5,anchor="w", bg="white", bd=4,cursor="hand2").pack(side=TOP, fill=X)
        btn_sup = Button(LeftMenu, text="Supplier",command=self.Sup, font=("times new roman", 20, "bold"),image= self.icon_side,compound=LEFT,padx=5,anchor="w", bg="white", bd=4,cursor="hand2").pack(side=TOP, fill=X)
        btn_cat = Button(LeftMenu, text="Category",command=self.Cat, font=("times new roman", 20, "bold"),image= self.icon_side,compound=LEFT,padx=5,anchor="w", bg="white", bd=4,cursor="hand2").pack(side=TOP, fill=X)
        btn_prod = Button(LeftMenu, text="Products",command=self.Prod, font=("times new roman", 20, "bold"),image= self.icon_side,compound=LEFT,padx=5,anchor="w", bg="white", bd=4,cursor="hand2").pack(side=TOP, fill=X)
        btn_sal = Button(LeftMenu, text="Sales",command=self.Sales, font=("times new roman", 20, "bold"),image= self.icon_side,compound=LEFT,padx=5,anchor="w", bg="white", bd=4,cursor="hand2").pack(side=TOP, fill=X)
        btn_rep = Button(LeftMenu, text="Report",command=self.Rep, font=("times new roman", 20, "bold"),image= self.icon_side,compound=LEFT,padx=5,anchor="w", bg="white", bd=4,cursor="hand2").pack(side=TOP, fill=X)
        btn_exit = Button(LeftMenu, text="Exit", font=("times new roman", 20, "bold"),image= self.icon_side,compound=LEFT,padx=5,anchor="w", bg="white", bd=4,cursor="hand2",command= self.Exit).pack(side=TOP, fill=X)

        self.lbl_employee = Label(self.root, text="Total Employee\n[0]", bd=5, relief=RIDGE, bg="#33bbf9", fg="white",
                                  font=("goudy old style", 20, "bold"))
        self.lbl_employee.place(x=300, y=220, height=150, width=300)
        self.lbl_supplier = Label(self.root, text="Total Suppliers\n[0]", bd=5, relief=RIDGE, bg="#33bbf9", fg="white",
                                  font=("goudy old style", 20, "bold"))
        self.lbl_supplier.place(x=650, y=220, height=150, width=300)
        self.lbl_category = Label(self.root, text="Total Category\n[0]", bd=5, relief=RIDGE, bg="#33bbf9", fg="white",
                                  font=("goudy old style", 20, "bold"))
        self.lbl_category.place(x=1000, y=220, height=150, width=300)
        self.lbl_sales = Label(self.root, text="Total Sales\n[0]", bd=5, relief=RIDGE, bg="#33bbf9", fg="white",
                               font=("goudy old style", 20, "bold"))
        self.lbl_sales.place(x=300, y=400, height=150, width=300)
        self.lbl_product = Label(self.root, text="Total Product \n[0]", bd=5, relief=RIDGE, bg="#33bbf9", fg="white",
                                 font=("goudy old style", 20, "bold"))
        self.lbl_product.place(x=650, y=400, height=150, width=300)
        self.btn_sales = Button(self.root,command=self.SalesInv, text="View Invoice", bd=5, cursor='hand2',relief=RIDGE, bg="#33bbf9", fg="white",font=("goudy old style", 20, "bold"))
        self.btn_sales.place(x=1000, y=400, height=150, width=300)

        self.update_content()
    def Updatedt(self):
        self.t=time.strftime("%H:%M:%S")

        self.d=time.strftime("%d-%m-%Y")
        self.lbl_clock = Label(self.root,text="Welcome to Dairy Management System\t\t\t\t\t Date: "+ str(self.d)+ "\t\t\t\t\t Time: "+str(self.t),font=("times new roman", 15,), bg="#ADD8E6")
        self.lbl_clock.place(x=0, y=70, relwidth=1, height=30)
        self.lbl_clock.after(200,self.Updatedt)
    def SalesInv(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = salesClass(self.new_win)
    def Exit(self):
        result = messagebox.askquestion('Dairy Management System', 'Are you sure you want to exit?',icon="warning")
        if result == 'yes':
            self.root.destroy()
            exit()
    def Emp(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=employee(self.new_win)
    def Sup(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=supplier(self.new_win)
    def Cat(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=category(self.new_win)
    def Prod(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=product(self.new_win)
    def Sales(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=BillClass(self.new_win)
    def Rep(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=Report(self.new_win)
    def update_content(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            cur.execute("select * from employee")
            employee = cur.fetchall()
            self.lbl_employee.config(text=f'Total Employee\n[{str(len(employee))}]')

            cur.execute("select * from supplier")
            supplier = cur.fetchall()
            self.lbl_supplier.config(text=f'Total Suppliers\n[{str(len(supplier))}]')

            cur.execute("select * from category")
            category = cur.fetchall()
            self.lbl_category.config(text=f'Total Category\n[{str(len(category))}]')

            bill = len(os.listdir('bill'))
            self.lbl_sales.config(text=f'Total Sales [{str(bill)}]')

            cur.execute("select * from product")
            product = cur.fetchall()
            self.lbl_product.config(text=f'Total Product\n[{str(len(product))}]')


        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

if __name__=="__main__":
    #root = Tk()
    obj = MDS()
    root.mainloop()

