from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
class category:
    def __init__(self, root):
        pass
        self.root = root
        self.root.geometry("1200x600+220+150")
        self.root.title("Dairy Management System")
        self.root.config(bg="white")
        self.root.focus_force()

        self.var_cat_id=StringVar()
        self.var_name=StringVar()

        lbl_title=Label(self.root,text="Manage Product Category",font=("goudy old style",30),bg="#184a45",fg="white",bd=3,relief=RIDGE).pack(side=TOP,fill=X,padx=10,pady=5)
        lbl_name=Label(self.root,text="Enter Category Name:",font=("goudy old style",24),bg="white",bd=3,relief=RIDGE).place(x=50,y=100)
        txt_name=Entry(self.root,textvariable=self.var_name,font=("goudy old style",24),bg="lightyellow",bd=3,relief=RIDGE).place(x=350,y=100,width=300)
        lbl_id = Label(self.root, text="Enter Category ID     :", font=("goudy old style", 24), bg="white", bd=3,relief=RIDGE).place(x=50, y=170)
        txt_id = Entry(self.root, textvariable=self.var_cat_id, font=("goudy old style", 24), bg="lightyellow", bd=3,relief=RIDGE).place(x=350, y=170, width=300)

        btn_add=Button(self.root,text="ADD",command=self.add,font=("goudy old style",24),bg="#4caf50",fg="white",cursor="hand2",bd=3,relief=RIDGE).place(x=50,y=300,width=300,height=50)
        btn_delete=Button(self.root,text="DELETE",command=self.delete,font=("goudy old style",24),bg="red",fg="white",cursor="hand2",bd=3,relief=RIDGE).place(x=50,y=370,width=300,height=50)
        btn_update=Button(self.root,text="UPDATE",command=self.update,font=("goudy old style",24),bg="orange",fg="white",cursor="hand2",bd=3,relief=RIDGE).place(x=350,y=300,width=300,height=50)
        btn_update=Button(self.root,text="CLEAR",command=self.clear,font=("goudy old style",24),bg="light blue",fg="white",cursor="hand2",bd=3,relief=RIDGE).place(x=350,y=370,width=300,height=50)

        emp_frame = Frame(self.root, bd=3, relief=RIDGE)
        emp_frame.place(x=700, y=100, width=455, height=400)

        scrolly = Scrollbar(emp_frame, orient=VERTICAL)
        scrollx = Scrollbar(emp_frame, orient=HORIZONTAL)
        self.CategoryTable = ttk.Treeview(emp_frame, columns=("catid", "catname"),yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.CategoryTable.xview)
        scrolly.config(command=self.CategoryTable.yview)
        self.CategoryTable.heading("catid", text="ID")
        self.CategoryTable.heading("catname", text="Category Name")


        self.CategoryTable["show"] = "headings"
        # self.CategoryTable.pack(fill=BOTH,expand=1)

        self.CategoryTable.column("catid", width=90)
        self.CategoryTable.column("catname", width=100)


        self.CategoryTable.pack(fill=BOTH, expand=1)
        self.CategoryTable.bind("<ButtonRelease-1>", self.get_data)
        self.show()


    def add(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_name.get() == "" or self.var_name == "":
                messagebox.showerror("Error", "Category Details Required", parent=self.root)
            else:
                cur.execute("Select * from category where catid =?", (self.var_cat_id.get(),))
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror("Error", "Category id already exists,try different", parent=self.root)
                else:
                    cur.execute("Insert into category (catid,catname) values(?,?)", (
                        self.var_cat_id.get(),
                        self.var_name.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Success", "Category Added Successfully!", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def show(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            cur.execute("select * from category")
            rows=cur.fetchall()
            self.CategoryTable.delete(*self.CategoryTable.get_children())
            for row in rows:
                self.CategoryTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)
    def get_data(self,ev):
        f=self.CategoryTable.focus()
        content=(self.CategoryTable.item(f))
        row=content['values']
        self.var_cat_id.set(row[0]),
        self.var_name.set(row[1]),

    def update(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_name=="":
                messagebox.showerror("Error","Category Details Required",parent=self.root)
            else:
                cur.execute("Select * from category where catid =?",(self.var_cat_id.get(),))
                row = cur.fetchone()
                if row ==None:
                    messagebox.showerror("Error","Invalid Category ID.\nCategory ID cannot be changed.",parent=self.root)
                else:
                    cur.execute("Update category set catname=? where catid=?",(
                        self.var_name.get(),
                        self.var_cat_id.get(),

                    ))
                    con.commit()
                    messagebox.showinfo("Success","Category Updated Successfully!",parent=self.root)
                    self.clear()
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    def delete(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_name=="":
                messagebox.showerror("Error","Category Details Required",parent=self.root)
            else:
                cur.execute("Select * from category where catid =?",(self.var_cat_id.get(),))
                row = cur.fetchone()
                if row ==None:
                    messagebox.showerror("Error","Invalid Category ID",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete?")
                    if op ==True:
                        cur.execute("delete from category where catid=?",(self.var_cat_id.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Category Deleted Successfully!",parent=self.root)
                        self.clear()
                        self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    def clear(self):
        self.var_cat_id.set(""),
        self.var_name.set(""),
        self.show()
if __name__=="__main__":
    root = Tk()
    obj = category(root)
    root.mainloop()