import sqlite3
from tkinter import *
from tkinter import messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np

class Report:
    def __init__(self, root):
        pass
        self.root = root
        self.root.geometry("1200x600+220+150")
        self.root.title("Dairy Management System")
        self.root.config(bg="white")
        self.root.focus_force()
        self.show()

    def show(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        self.lbl=[]
        self.val=[]
        try:
            cur.execute("select * from product")
            rows = cur.fetchall()
            print(rows)

            for row in rows:
                string=row[3]+" "+row[1]
                self.lbl.append(string)
                s=100-int(row[5])
                self.val.append(s)
            print(self.lbl)
            print(self.val)
            for x in range(0,len(self.val)):
                if self.val[x] == 0:
                    self.val[x] = 1
            y = np.array(self.val)
            label = np.array(self.lbl)
            '''plt.pie(y, labels=label)
            plt.show()'''
            fig = Figure()  # create a figure object
            ax = fig.add_subplot(111)  # add an Axes to the figure

            ax.pie(y, radius=1.2, labels=label, autopct='%0.2f%%', shadow=True, )

            chart1 = FigureCanvasTkAgg(fig, self.root)
            chart1.get_tk_widget().place(x=250,y=50)


        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)




if __name__=="__main__":
    root = Tk()
    obj = Report(root)
    root.mainloop()