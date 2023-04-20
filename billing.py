from cProfile import label
from optparse import Values
import sqlite3
from textwrap import fill
from tkinter import *
from tkinter import ttk, messagebox
from tkinter import font
import time
import os
import tempfile


class BillClass:
    def __init__(self,root1):
        pass

        self.root = root1
        self.root.geometry("1500x1000+0+0")
        self.root.title("Dairy Management System")
        self.cart_list = []
        self.chk_print = 0

        self.icon_title = PhotoImage(file="image/menu_im.png")
        title = Label(self.root, text="Dairy Management System", image=self.icon_title, compound=LEFT,font=("times new roman", 40, "bold"), bg="#ADD8E6", anchor="w", padx=20).place(x=0, y=0,relwidth=1,height=70)
        self.lbl_clock = Label(self.root,text="Welcome to Dairy Management System\t\t Date: \t\t Time: ",font=("times new roman", 15,), bg="#ADD8E6")
        self.lbl_clock.place(x=0, y=70, relwidth=1, height=30)

        self.var_search = StringVar()
        ProductFrame1 = Frame(self.root, bd=4, relief=RIDGE, bg="white")
        ProductFrame1.place(x=6, y=110, width=450, height=665)

        pTitle = Label(ProductFrame1, text="All Products", font=("goudy old style", 20, "bold"), bg="#262626",fg="white").pack(side=TOP, fill=X)

        ProductFrame2 = Frame(ProductFrame1, bd=2, relief=RIDGE, bg="white")
        ProductFrame2.place(x=2, y=42, width=438, height=95)
        lbl_search = Label(ProductFrame2, text="Search Product | By Name", font=("times new roman", 15, "bold"),bg="white", fg="green").place(x=2, y=5)

        lbl_search1 = Label(ProductFrame2, text="Product Name", font=("times new roman", 15, "bold"), bg="white").place(x=2, y=45)
        txt_search = Entry(ProductFrame2, textvariable=self.var_search, font=("times new roman", 15),bg="lightyellow").place(x=128, y=47, width=150, height=22)
        btn_search = Button(ProductFrame2, text="Search", command=self.search, font=("goudy old style", 15),bg="#2196f3", fg="white", cursor="hand2").place(x=285, y=45, width=100, height=25)
        btn_show_all = Button(ProductFrame2, text="Show all", command=self.show, font=("goudy old style", 15),bg="#083531", fg="white", cursor="hand2").place(x=285, y=10, width=100, height=25)

        ProductFrame3 = Frame(ProductFrame1, bd=3, relief=RIDGE)
        ProductFrame3.place(x=2, y=140, width=438, height=480)

        scrolly = Scrollbar(ProductFrame3, orient=VERTICAL)
        scrollx = Scrollbar(ProductFrame3, orient=HORIZONTAL)

        self.Product_Table = ttk.Treeview(ProductFrame3, columns=("pid", "name", "price", "qty","status"),yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.Product_Table.xview)
        scrolly.config(command=self.Product_Table.yview)

        self.Product_Table.heading("pid", text="PID")
        self.Product_Table.heading("name", text="Name")
        self.Product_Table.heading("price", text="Price")
        self.Product_Table.heading("qty", text="QTY")
        self.Product_Table.heading("status", text="Status")
        self.Product_Table["show"] = "headings"
        self.Product_Table.column("pid", width=90)
        self.Product_Table.column("name", width=100)
        self.Product_Table.column("price", width=100)
        self.Product_Table.column("qty", width=100)
        self.Product_Table.column("status", width=90)
        self.Product_Table.pack(fill=BOTH, expand=1)
        self.Product_Table.bind("<ButtonRelease-1>", self.get_data)

        lbl_note = Label(ProductFrame1, text="NOTE:Enter 0 qty to remove product from the cart",font=("goudy old style", 10), anchor='w', bg="white", fg="red").pack(side=BOTTOM, fill=X)

        self.var_cname = StringVar()
        self.var_contact = StringVar()

        CustomerFrame = Frame(self.root, bd=4, relief=RIDGE, bg="white")
        CustomerFrame.place(x=460, y=110, width=530, height=95)
        cTitle = Label(CustomerFrame, text="Customer Details", font=("goudy old style", 15), bg="lightgray").pack(side=TOP, fill=X)
        lbl_name = Label(CustomerFrame, text="Name", font=("times new roman", 15), bg="white").place(x=5, y=45)
        txt_name = Entry(CustomerFrame, textvariable=self.var_cname, font=("times new roman", 13),bg="lightyellow").place(x=70, y=45, width=180)
        lbl_contact = Label(CustomerFrame, text="Contact No.", font=("times new roman", 15), bg="white").place(x=270,y=45)
        txt_contact = Entry(CustomerFrame, textvariable=self.var_contact, font=("times new roman", 13),bg="lightyellow").place(x=375, y=45, width=140)

        Cal_Cart_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="white")
        Cal_Cart_Frame.place(x=460, y=210, width=530, height=380)

        self.var_cal_input = StringVar()
        Cal_Frame = Frame(Cal_Cart_Frame, bd=4, relief=RIDGE, bg="white")
        Cal_Frame.place(x=5, y=10, width=268, height=340)
        self.txt_cal_input = Entry(Cal_Frame, textvariable=self.var_cal_input, font=('arial', 15, "bold"), width=22,bd=9, relief=GROOVE, state='readonly', justify=RIGHT)
        self.txt_cal_input.grid(row=0, columnspan=4)
        btn_7 = Button(Cal_Frame, text='7', font=('arial', 15, 'bold'), command=lambda: self.get_input(7), bd=5,width=4, pady=10, cursor='hand2').grid(row=1, column=0)
        btn_8 = Button(Cal_Frame, text='8', font=('arial', 15, 'bold'), command=lambda: self.get_input(8), bd=5,width=4, pady=10, cursor='hand2').grid(row=1, column=1)
        btn_9 = Button(Cal_Frame, text='9', font=('arial', 15, 'bold'), command=lambda: self.get_input(9), bd=5,width=4, pady=10, cursor='hand2').grid(row=1, column=2)
        btn_sum = Button(Cal_Frame, text='+', font=('arial', 15, 'bold'), command=lambda: self.get_input('+'), bd=5,width=4, pady=10, cursor='hand2').grid(row=1, column=3)

        btn_4 = Button(Cal_Frame, text='4', font=('arial', 15, 'bold'), command=lambda: self.get_input(4), bd=5,width=4, pady=10, cursor='hand2').grid(row=2, column=0)
        btn_5 = Button(Cal_Frame, text='5', font=('arial', 15, 'bold'), command=lambda: self.get_input(5), bd=5,width=4, pady=10, cursor='hand2').grid(row=2, column=1)
        btn_6 = Button(Cal_Frame, text='6', font=('arial', 15, 'bold'), command=lambda: self.get_input(6), bd=5,width=4, pady=10, cursor='hand2').grid(row=2, column=2)
        btn_subtract = Button(Cal_Frame, text='-', font=('arial', 15, 'bold'), command=lambda: self.get_input('-'),bd=5, width=4, pady=10, cursor='hand2').grid(row=2, column=3)

        btn_1 = Button(Cal_Frame, text='1', font=('arial', 15, 'bold'), command=lambda: self.get_input(1), bd=5,width=4, pady=12, cursor='hand2').grid(row=3, column=0)
        btn_2 = Button(Cal_Frame, text='2', font=('arial', 15, 'bold'), command=lambda: self.get_input(2), bd=5,width=4, pady=12, cursor='hand2').grid(row=3, column=1)
        btn_3 = Button(Cal_Frame, text='3', font=('arial', 15, 'bold'), command=lambda: self.get_input(3), bd=5,width=4, pady=12, cursor='hand2').grid(row=3, column=2)
        btn_mul = Button(Cal_Frame, text='*', font=('arial', 15, 'bold'), command=lambda: self.get_input('*'), bd=5,width=4, pady=12, cursor='hand2').grid(row=3, column=3)

        btn_0 = Button(Cal_Frame, text='0', font=('arial', 15, 'bold'), command=lambda: self.get_input(0), bd=5,width=4, pady=13, cursor='hand2').grid(row=4, column=0)
        btn_c = Button(Cal_Frame, text='c', font=('arial', 15, 'bold'), command=self.clear_cal, bd=5, width=4, pady=13,cursor='hand2').grid(row=4, column=1)
        btn_eq = Button(Cal_Frame, text='=', font=('arial', 15, 'bold'), command=self.perform_cal, bd=5, width=4,pady=13, cursor='hand2').grid(row=4, column=2)
        btn_div = Button(Cal_Frame, text='/', font=('arial', 15, 'bold'), command=lambda: self.get_input('/'), bd=5,width=4, pady=13, cursor='hand2').grid(row=4, column=3)

        Cart_Frame = Frame(Cal_Cart_Frame, bd=3, relief=RIDGE)
        Cart_Frame.place(x=280, y=8, width=245, height=342)
        self.CartTitle = Label(Cart_Frame, text="Cart \t Total Product: [0]", font=("goudy old style", 15),bg="lightgray")
        self.CartTitle.pack(side=TOP, fill=X)

        scrolly = Scrollbar(Cart_Frame, orient=VERTICAL)
        scrollx = Scrollbar(Cart_Frame, orient=HORIZONTAL)

        self.Cart_Table = ttk.Treeview(Cart_Frame, columns=("pid", "name", "price", "qty"),yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.Cart_Table.xview)
        scrolly.config(command=self.Cart_Table.yview)

        self.Cart_Table.heading("pid", text="PID")
        self.Cart_Table.heading("name", text="Name")
        self.Cart_Table.heading("price", text="Price")
        self.Cart_Table.heading("qty", text="QTY")
        #self.Cart_Table.heading("stock", text="Stock")
        self.Cart_Table["show"] = "headings"
        self.Cart_Table.column("pid", width=40)
        self.Cart_Table.column("name", width=90)
        self.Cart_Table.column("price", width=90)
        self.Cart_Table.column("qty", width=40)
        #self.Cart_Table.column("stock", width=40)
        self.Cart_Table.pack(fill=BOTH, expand=1)
        self.Cart_Table.bind("<ButtonRelease-1>", self.get_data_cart)

        self.var_pid = StringVar()
        self.var_name1 = StringVar()
        self.var_price = StringVar()
        self.var_qty = StringVar()
        self.var_stock = StringVar()
        self.bal=StringVar()
        Add_CartWidgetsFrame = Frame(self.root, bd=4, relief=RIDGE, bg="white")
        Add_CartWidgetsFrame.place(x=460, y=597, width=530, height=178)

        lbl_p_name = Label(Add_CartWidgetsFrame, text="Product Name", font=("times new roman", 15), bg="white").place(x=5, y=15)
        txt_p_name = Entry(Add_CartWidgetsFrame, textvariable=self.var_name1, font=("times new roman", 15),bg="lightyellow", state='readonly').place(x=5, y=45, width=190, height=22)

        lbl_p_price = Label(Add_CartWidgetsFrame, text="Price", font=("times new roman", 15), bg="white").place(x=230,y=15)
        txt_p_price = Entry(Add_CartWidgetsFrame, textvariable=self.var_price, font=("times new roman", 15),bg="lightyellow", state='readonly').place(x=230, y=45, width=100, height=22)

        lbl_p_qty = Label(Add_CartWidgetsFrame, text="Quantity", font=("times new roman", 15), bg="white").place(x=350,y=15)
        txt_p_qty = Entry(Add_CartWidgetsFrame, textvariable=self.var_qty, font=("times new roman", 15),bg="lightyellow").place(x=350, y=45, width=100, height=22)

        self.lbl_instock = Label(Add_CartWidgetsFrame, text="In Stock", font=("times new roman", 15), bg="white")
        self.lbl_instock.place(x=5, y=100)

        btn_clear_cart = Button(Add_CartWidgetsFrame, text="Clear", command=self.clear_cart,font=("times new roman", 15, "bold"), bg="lightgray", cursor="hand2").place(x=180, y=100,width=150,height=30)
        btn_add_cart = Button(Add_CartWidgetsFrame, text="Add|Update Cart", command=self.add_update_cart,font=("times new roman", 15, "bold"), bg="orange", cursor="hand2").place(x=340, y=100,width=180,height=30)

        billFrame = Frame(self.root, bd=2, relief=RIDGE, bg='white')
        billFrame.place(x=1000, y=110, width=400, height=480)
        BTitle = Label(billFrame, text="Customer Bill", font=("goudy old style", 20, "bold"), bg="#262626",fg="white").pack(side=TOP, fill=X)
        scrolly = Scrollbar(billFrame, orient=VERTICAL)
        scrolly.pack(side=RIGHT, fill=Y)
        self.txt_bill_area = Text(billFrame)
        self.txt_bill_area.pack(fill=BOTH, expand=1)
        scrolly.config(command=self.txt_bill_area.yview)

        billMenuFrame = Frame(self.root, bd=2, relief=RIDGE, bg='white')
        billMenuFrame.place(x=1000, y=600, width=400, height=175)

        self.lbl_amnt = Label(billMenuFrame, text='Bill amount\n[0]', font=("goudy old style", 15, "bold"),bg="#3f51b5", fg="white")
        self.lbl_amnt.place(x=2, y=10, width=125, height=70)

        self.lbl_disc = Label(billMenuFrame, text='Discount\n[5%]', font=("goudy old style", 15, "bold"), bg="#8bc34a",fg="white")
        self.lbl_disc.place(x=135, y=10, width=125, height=70)

        self.lbl_net_pay = Label(billMenuFrame, text='Net Pay\n[0]', font=("goudy old style", 15, "bold"), bg="#607d8b",fg="white")
        self.lbl_net_pay.place(x=268, y=10, width=125, height=70)

        btn_print = Button(billMenuFrame, text='Print', command=self.print_bill, font=("goudy old style", 15, "bold"),bg="lightgreen", fg="white", cursor='hand2')
        btn_print.place(x=2, y=90, width=125, height=70)

        btn_clear_all = Button(billMenuFrame, text='Clear ALL', command=self.clear_all,font=("goudy old style", 15, "bold"), bg="gray", fg="white", cursor='hand2')
        btn_clear_all.place(x=135, y=90, width=125, height=70)

        btn_generate = Button(billMenuFrame, text='Generate BILL', command=self.generate_bill,font=("goudy old style", 10, "bold"), bg="#009688", fg="white", cursor='hand2')
        btn_generate.place(x=268, y=90, width=125, height=70)
        self.var_pay=StringVar()
        #lbl_p_pay = Label(billMenuFrame, text="Amount Paid:", font=("times new roman", 24), bg="white").place(x=2, y=10)
        #txt_p_pay = Entry(billMenuFrame, textvariable=self.var_pay, font=("times new roman", 24),bg="lightyellow").place(x=190, y=10, width=200)

        self.show()

        # self.bill_top()
        self.update_date_time()

    def get_input(self, num):
        xnum = self.var_cal_input.get() + str(num)
        self.var_cal_input.set(xnum)

    def clear_cal(self):
        self.var_cal_input.set('')

    def perform_cal(self):
        result = self.var_cal_input.get()
        self.var_cal_input.set(eval(result))

    def show(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            cur.execute("select pid,name,price,qty,status from product where status='Active'")
            rows = cur.fetchall()
            self.Product_Table.delete(*self.Product_Table.get_children())
            for row in rows:
                self.Product_Table.insert('', END, values=row)
        except Exception as ex:
            messagebox.showerror("ERROR", f"error due to : {str(ex)}", parent=self.root)

    def search(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_search.get() == "":
                messagebox.showerror("Error", "Select Input Required!", parent=self.root)
            else:
                cur.execute(
                    "select pid,name,price,qty,status from product where name LIKE '%" + self.var_search.get() + "%'and status='Active'")
                rows = cur.fetchall()
                if len(rows) != 0:
                    self.Product_Table.delete(*self.Product_Table.get_children())
                    for row in rows:
                        self.Product_Table.insert('', END, values=row)
                else:
                    messagebox.showerror("Error", "No Record Found!", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def get_data(self, ev):
        f = self.Product_Table.focus()
        content = (self.Product_Table.item(f))
        row = content['values']
        self.var_pid.set(row[0])
        self.var_name1.set(row[1])
        self.var_price.set(row[2])
        self.lbl_instock.config(text=f"In Stock [{str(row[3])}]")
        self.var_qty.set('1')
        self.var_stock.set(row[3])

    def get_data_cart(self, ev):
        f = self.Cart_Table.focus()
        content = (self.Cart_Table.item(f))
        row = content['values']
        self.var_pid.set(row[0])
        self.var_name1.set(row[1])
        self.var_price.set(row[2])
        self.var_qty.set(row[3])
        self.lbl_instock.config(text=f"In Stock [{str(row[4])}]")
        self.var_stock.set(row[4])

    def add_update_cart(self):
        if self.var_pid.get() == '':
            messagebox.showerror('Error', "Please select a product", parent=self.root)
        elif self.var_qty.get() == '':
            messagebox.showerror('Error', "Quantity is required", parent=self.root)
        elif int(self.var_qty.get()) > int(self.var_stock.get()):
            messagebox.showerror('Error', "Invalid Quantity", parent=self.root)
        else:
            #price_cal=float(int(self.var_qty.get())*float(self.var_price.get()))
            price_cal = self.var_price.get()
            cart_data = [self.var_pid.get(), self.var_name1.get(), price_cal, self.var_qty.get(), self.var_stock.get() ]


            present = 'no'
            index_ = 0
            for row in self.cart_list:
                if self.var_pid.get() == row[0]:
                    present = 'yes'
                    break
                index_ += 1
            if present == 'yes':
                op = messagebox.askyesno('Confirmation',"Product already present\nDo you want to update|Remove from the Cart List",parent=self.root)
                if op == True:
                    if self.var_qty.get() == "0":
                        self.cart_list.pop(index_)
                    else:
                        # self.cart_list[index_][2]=price_cal
                        self.cart_list[index_][3] = self.var_qty.get()
            else:
                self.cart_list.append(cart_data)
            self.show_cart()
            self.bill_updates()

    def bill_updates(self):
        self.bill_amnt = 0
        self.net_pay = 0

        for row in self.cart_list:
            self.bill_amnt = self.bill_amnt + (float(row[2])*float(row[3]) )

        self.net_pay = (self.bill_amnt * 95) / 100

        self.lbl_amnt.config(text=f'Bill Amount\n[{str(self.bill_amnt)}]')
        self.lbl_net_pay.config(text=f'Net pay\n[{str(self.net_pay)}]')
        self.CartTitle.config(text=f"Cart \t Total Product: [{str(len(self.cart_list))}]")

    def show_cart(self):
        try:
            self.Cart_Table.delete(*self.Cart_Table.get_children())
            for row in self.cart_list:
                self.Cart_Table.insert('', END, values=row)
        except Exception as ex:
            messagebox.showerror("ERROR", f"error due to : {str(ex)}", parent=self.root)

    def generate_bill(self):
        if self.var_cname.get() == '' or self.var_contact.get() == '' :
            messagebox.showerror("error", f"Customer detail are required", parent=self.root)
            '''elif self.var_pay.get()=='':
                messagebox.showerror("error", f"Enter the Paid Amount", parent=self.root)'''
        elif len(self.cart_list) == 0:
            messagebox.showerror("error", f"Please Add products to the cart!!", parent=self.root)
        else:
            self.bill_top()
            self.bill_middle()
            self.bill_bottom()
            fp = open(f'bill/{str(self.invoice)}.txt', 'w')
            fp.write(self.txt_bill_area.get('1.0', END))
            fp.close()

            '''pay=int(self.var_pay.get())
            print(pay)'''

            messagebox.showinfo('Saved', "bill has been generated/saved", parent=self.root)
            self.chk_print = 1

    def bill_top(self):
        self.invoice = int(time.strftime("%H%M%S")) + int(time.strftime("%d%m%y"))
        bill_top_temp = f'''
\t\tXYZ-Milk
\t SIES GST
{str("=" * 46)}
 Customer name: {self.var_cname.get()}
 Ph No. :{self.var_contact.get()}
 Bill no. {str(self.invoice)}\t\t\tDate: {str(time.strftime("%d/%m/%y"))}
{str("=" * 46)}
 Product Name\t\t\tQty\tPrice
{str("=" * 46)}
        '''
        self.txt_bill_area.delete('1.0', END)
        self.txt_bill_area.insert('1.0', bill_top_temp)

    def bill_bottom(self):
        bill_bottom_temp = f'''
{str("=" * 46)}
 Bill Amount\t\t\t\tRs.{self.bill_amnt}
 Net pay\t\t\t\tRs.{self.net_pay}
{str("=" * 46)}\n
        '''
        self.txt_bill_area.insert(END, bill_bottom_temp)

    def bill_middle(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        status=''
        try:
            for row in self.cart_list:
                pid = row[0]
                name = row[1]
                qty = int(row[4]) - int(row[3])
                if int(row[3]) == int(row[3]):
                    status = 'Inactive'
                if int(row[3]) != int(row[4]):
                    status = 'Active'
                price = float(row[2]) * int(row[3])
                price = str(price)
                self.txt_bill_area.insert(END, "\n" + name + "\t\t\t" + row[3] + "\t Rs." + price)
                cur.execute('Update product set qty=?,status=? where pid=?', (
                    qty,
                    status,
                    pid
                ))
                con.commit()
            con.close()
            self.show()

        except Exception as ex:
            messagebox.showerror("error", f"ERROR due to : {str(ex)}", parent=self.root)

    def clear_cart(self):
        self.var_pid.set('')
        self.var_name1.set('')
        self.var_price.set('')
        self.lbl_instock.config(text=f"In Stock")
        self.var_qty.set('')
        self.var_stock.set('')

    def clear_all(self):
        del self.cart_list[:]
        self.var_cname.set('')
        self.var_contact.set('')
        self.txt_bill_area.delete('1.0', END)
        self.CartTitle.config(text=f"Cart \t Total Product: [0]")
        self.chk_print = 0
        self.clear_cart()
        self.show()
        self.show_cart()

    def update_date_time(self):
        time_ = time.strftime("%H:%M:%S")
        date_ = time.strftime("%d-%m-%y")
        self.lbl_clock.config(text=f"Welcome to Dairy Management System\t\t Date:{str(date_)}\t\t Time:{str(time_)}")
        self.lbl_clock.after(200, self.update_date_time)

    def print_bill(self):
        if self.chk_print == 1:
            new_file = tempfile.mktemp('.txt')
            open(new_file, 'w').write(self.txt_bill_area.get('1.0', END))
            os.startfile(new_file, 'print')
            messagebox.showinfo('Print', "please wait while printing", parent=self.root)
        else:
            messagebox.showerror('Print', "Please generate bill", parent=self.root)



if __name__ == "__main__":
    root = Tk()
    obj = BillClass(root)
    root.mainloop()