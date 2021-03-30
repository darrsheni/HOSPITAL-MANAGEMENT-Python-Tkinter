from tkinter import *
import sqlite3 as s
from tkinter import messagebox
import matplotlib.pyplot as pl

from PIL import Image, ImageTk
root =Tk()
root.title("HOSPITAL")
index=6
billno=100
i=6
def create():
    con=s.connect('hospital.db')
    con.execute("create table  if not exists cat2(pid  int PRIMARY KEY, pname char(50),dname   varchar(50), age int, gender char(60),dop  date, ad  varchar(80))")
    print("table created")
    con.close()

create()
def check2():
    top=Toplevel()


    def insert():
        con=s.connect('hospital.db')
        a=int(e.get())
        pname=e1.get()
        dname=e2.get()
        age=int(e3.get())
        gender=e4.get()
        dop=e5.get()
        add=e6.get()
        
        data=con.execute("insert into cat2 values({},'{}','{}',{},'{}','{}','{}')".format(a,pname,dname,age,gender,dop,add))
        print("data insered")
        la5=Label(top,font=('aria',16,'bold'),text="data inserted",fg='blue',bd=10,anchor='w')
        la5.grid(row=10,column=2)


    
        con.commit()
        
    e=Entry(top,font=('arial',16,'bold'), bd=6, insertwidth=4, bg='powder blue', justify='right')#pid
    e1=Entry(top,font=('arial',16,'bold'), bd=6, insertwidth=4, bg='powder blue', justify='right')#pname
    e2=Entry(top,font=('arial',16,'bold'), bd=6, insertwidth=4, bg='powder blue', justify='right')#dname
    e3=Entry(top,font=('arial',16,'bold'), bd=6, insertwidth=4, bg='powder blue', justify='right')#age
    e4=Entry(top,font=('arial',16,'bold'), bd=6, insertwidth=4, bg='powder blue', justify='right')#gender
    e5=Entry(top,font=('arial',16,'bold'), bd=6, insertwidth=4, bg='powder blue', justify='right')#dop
    e6=Entry(top,font=('arial',16,'bold'), bd=6, insertwidth=4, bg='powder blue', justify='right')#add
    la=Label(top,font=('aria',16,'bold'),text="PATIENT ID",fg='blue',bd=10,anchor='w')
    la1=Label(top,font=('aria',16,'bold'),text="PATIENT NAME",fg='blue',bd=10,anchor='w')
    la2=Label(top,font=('aria',16,'bold'),text="DOCTOR NAME",fg='blue',bd=10,anchor='w')
    la3=Label(top,font=('aria',16,'bold'),text="AGE",fg='blue',bd=10,anchor='w')
    la4=Label(top,font=('aria',16,'bold'),text="GENDER",fg='blue',bd=10,anchor='w')
    la5=Label(top,font=('aria',16,'bold'),text="DATE OF APPOINTMENT",fg='blue',bd=10,anchor='w')
    la6=Label(top,font=('aria',16,'bold'),text="CITY",fg='blue',bd=10,anchor='w')
    la.grid(row=2,column=2)
    la1.grid(row=3,column=2)
    la2.grid(row=4,column=2)
    la3.grid(row=5,column=2)
    la4.grid(row=6,column=2)
    la5.grid(row=7,column=2)
    la6.grid(row=8,column=2)
    
    
    e.grid(row=2,column=5)
    e1.grid(row=3,column=5)
    e2.grid(row=4,column=5)
    e3.grid(row=5,column=5)
    e4.grid(row=6,column=5)
    e5.grid(row=7,column=5)
    e6.grid(row=8,column=5)
    b=Button(top,command=insert,padx=16, pady=16,bd=4, fg="black" , font=('arial', 10, 'bold'),text='submit', bg='powder blue')
    b.grid(row=9,column=5)
    

def delete():
        t=Toplevel()
        t.geometry=("700x900")
        con=s.connect('hospital.db')
        def de():
          a=int(en.get())
          data=con.execute("select count(*) from cat2 where pid={}".format(a))
          l=data.fetchall()
          print(l[0])
          if l[0][0]==0:
                          messagebox.showinfo("sorry","user does not exists")
          else:

            con.execute(('delete from cat2 where pid={}').format(a))
            print('deleted')
            messagebox.showinfo("deleted")
            con.commit()
        en=Entry(t,font=('arial',16,'bold'), bd=6, insertwidth=4, bg='powder blue', justify='right')
        en.grid(row=7,column=3)

        lab=Label(t,text="enter pid to be deleted",font=('arial',16,'bold'),fg='blue',bd=10,anchor='w')
        lab.grid(row=7,column=2)

        b=Button(t,text="done",command=de,padx=16,pady=16, bd=4, fg='black', font=('arial',10,'bold'),bg="powder blue")
        b.grid(row=10,column=3)
        

def update():
        tp=Toplevel()
        tp.geometry=("700x900")
        con=s.connect('hospital.db')
        x=StringVar()
        y=StringVar()
        z=StringVar()
        data=0
        q=Entry(tp,textvariable=x,font=('arial',16,'bold'), bd=6, insertwidth=4, bg='powder blue', justify='right')
        q1=Entry(tp,textvariable=y,font=('arial',16,'bold'), bd=6, insertwidth=4, bg='powder blue', justify='right')
        q2=Entry(tp,textvariable=z,font=('arial',16,'bold'), bd=6, insertwidth=4, bg='powder blue', justify='right')
        
        def godhelp():
                global data
                con=s.connect('hospital.db')
                n=(q.get())
                m=(q1.get())
                o=q2.get()
                #e from cat where srno={}, name ='{}',gender='{}',age={}").format(data,n,m,o)
                con.execute("update cat2  set pname='{}',ad='{} ',dop='{}'where pid={}".format(n,m,o,data))
                con.commit()
                
                print(data)
                messagebox.showinfo("record updated","record updated")
                print("finally done")
        def up():
            global data
            data=int(ent.get())
            row=con.execute(("select pname, ad,dop from cat2 where pid={}").format(data))
            l=row.fetchall()
            l1=Label(tp)
            if  len(l)==0:
                messagebox.showinfo("sorry","user does not exists")           
                
                l1.grid(row=4,column=4)
            else:

             
             q.grid(row=3,column=4)
             q1.grid(row=4,column=4)
             q2.grid(row=5,column=4)
             l6.grid(row=3,column=2)
             l2.grid(row=4,column=2)
             l3.grid(row=5,column=2)
             bbb1.grid(row=8,column=5) 
             for h in l:
                            print(h)
                            x.set(h[0])
                            y.set(h[1])
                            z.set(h[2])
             print("updated")
            
             
        bbb1=Button(tp,text="update",command=godhelp,padx=16,pady=16, bd=4, fg='black', font=('arial',10,'bold'),bg="powder blue")
        
       
                             
        l=Label(tp,text="PATIENT ID",font=('aria',16,'bold'),fg='blue',bd=10,anchor='w')
        l.grid(row=2,column=2)
        l6=Label(tp,text="PATIENT NAME ",font=('aria',16,'bold'),fg='blue',bd=10,anchor='w')
       
        l2=Label(tp,text="PATIENT ADDRESS ",font=('aria',16,'bold'),fg='blue',bd=10,anchor='w')
        
        l3=Label(tp,text="PATIENT DATE OF APPOINTMENT ",font=('aria',16,'bold'),fg='blue',bd=10,anchor='w')
      
        ent=Entry(tp,font=('arial',16,'bold'), bd=6, insertwidth=4, bg='powder blue', justify='right')
        ent.grid(row=2,column=4)
        bbb=Button(tp,text='search',command=up,padx=16,pady=16, bd=4, fg='black', font=('arial',10,'bold'), bg="powder blue")
        bbb.grid(row=8,column=3)
def report1():
    
    con=s.connect('hospital.db')
    data=con.execute("select count(*),dname from cat2 group by dname")
    l=[]
    l1=[]
    for row in data:
        l.append(row[0])
        l1.append(row[1])
    pl.pie(l,labels=l1,autopct="%2.2f%%")
    pl.title("NUMBER OF PATIENTS HANDLED BY EACH DOCTOR")
    pl.show()



def report2():
    
    con=s.connect('hospital.db')
    data=con.execute("select count(*),ad from cat2 group by ad")
    l=[]
    l1=[]
    for row in data:
        l.append(row[0])
        l1.append(row[1])
    pl.pie(l,labels=l1,autopct="%2.2f%%")
    pl.title("NUMBER OF PATIENTS HANDLED BY EACH CITY")
    pl.show()

def report3():
    
    con=s.connect('hospital.db')
    data=con.execute("select count(*),gender from cat2 group by gender")
    l=[]
    l1=[]
    for row in data:
        l.append(row[0])
        l1.append(row[1])
    pl.pie(l,labels=l1,autopct="%2.2f%%")
    pl.title("NUMBER OF PATIENTS ,EACH YEAR")
    pl.show()
   
        
    
def img():
   top=Toplevel()
   con=s.connect('hospital.db')
   image1 = Image.open("lines.jpeg")
   image1 = image1.resize((550, 550), Image.ANTIALIAS)
   test = ImageTk.PhotoImage(image1)

   label1 = Label(top,image=test,text="hello")
   label1.image = test
   b=Button(top,text="click")
   # Position image
   label1.grid(row=1,column=1)
   b.grid(row=2,column=2)

def report():
   global index
   top=Toplevel()
   con=s.connect('hospital.db')
   yy=Entry(top)
   yy1=Entry(top)
   q=StringVar()
   r=StringVar()
   def rep():
            
            
            global index
            top=Toplevel()
            x=int(yy.get())
            y=int(yy1.get())
            data=con.execute("select * from cat where age between {} and {}".format(x,y))
            l2=Label(top, text="id \t  name")
            l2.grid(row=2,column=9)
            for ans in data:
                
                l=Label(top,text=str(ans[0]))
                l.grid(row=index,column=8)
                l1=Label(top,text=str(ans[1]))
                l1.grid(row=index,column=10)
                print("hello")
                index+=1
                print(ans)
           
            con.commit()
            con.close()
            
   la6=Label(top,font=('aria',16,'bold'),text="age from",fg='blue',bd=10,anchor='w')
   la7=Label(top,font=('aria',16,'bold'),text="age to",fg='blue',bd=10,anchor='w')
   b4=Button(top,padx=16,pady=16, bd=4, fg='black', font=('arial',10,'bold'), text="submit",bg="powder blue",command=rep)
   b4.grid(row=4,column=4)
   yy.grid(row=2,column=3)
   yy1.grid(row=3,column=3)
   la6.grid(row=2,column=2)
   la7.grid(row=3,column=2)
                
                            
  
        
def check():
    if(e.get()=='g' and e1.get()=='h'):
        b1=Button(root,padx=16,pady=16, bd=4, fg='black', font=('arial',10,'bold'), text="New Patient",bg="powder blue",command=check2)
        b2=Button(root,padx=16,pady=16,bd=4, fg='black', font=('arial',10,'bold'),     text='Delete Patient', bg='powder blue',command=delete)
        b3=Button(root,padx=16,pady=16,bd=4, fg='black', font=('arial',10,'bold'),     text='Update Patient', bg='powder blue',command=update)
        b5=Button(root,padx=16,pady=16,bd=4, fg='black', font=('arial',10,'bold'),     text='Report', bg='powder blue',command=report1)
                
        b4=Button(root,padx=16,pady=16, bd=4, fg='black', font=('arial',10,'bold'), text="REPORT",bg="powder blue",command=intro)
        b4.grid(row=4,column=1) 

        

        l2.config(text=" ")

        b1.grid(row=3, column=0)
        b2.grid(row=3,column=2)
        b3.grid(row=3,column=1)
        b5.grid(row=4,column=1)
    else:
        l2.config(text='wrong username or password')


def intro():
    
   top=Toplevel() 
   
   con=s.connect('hospital.db')
   image1 = Image.open("C:\Users\darrsheni\Downloads\hospital.png")
   image1 = image1.resize((350, 350), Image.ANTIALIAS)
   test = ImageTk.PhotoImage(image1)

   label1 = Label(top,image=test,text="hello")
   label1.image = test
   b=Button(top,command=report1,padx=16,pady=16, bd=4, fg='black', font=('arial',10,'bold'), text="PATIENTS HANDLED BY EACH DOCTOR",bg="powder blue",)
   b1=Button(top,command=report2,padx=16,pady=16, bd=4, fg='black', font=('arial',10,'bold'), text="NUMBER OF PATIENTS IN EACH CITY",bg="powder blue")
   b2=Button(top,command=report3,padx=16,pady=16, bd=4, fg='black', font=('arial',10,'bold'), text="NUMBER OF PATIENTS GENDER WISE",bg="powder blue")
   # Position image
   label1.grid(row=1,column=1)
   b.grid(row=2,column=1)
   b1.grid(row=3,column=1)
   b2.grid(row=4,column=1)

l2=Label(root, font=('arial',16,'bold'),text=" ",fg='blue',bd=10,anchor='w')
l2.grid(row=3,column=1)
l=Label(root, font=('arial',16,'bold'),text='username', fg='blue',bd =10, anchor ='w').grid(row=0,column=0)
l1=Label(root, font=('arial',16,'bold'),text='password', fg='blue',bd =10, anchor ='w').grid(row=1,column=0)
e=Entry(root,font=('arial',16,'bold'), bd=6, insertwidth=4, bg='powder blue', justify='right')
e1=Entry(root,font=('arial',16,'bold'), bd=6, insertwidth=4, bg='powder blue', justify='right')
b= Button(root,padx=16, pady=16,bd=4, fg="black" , font=('arial', 10, 'bold'),text='submit', bg='powder blue', command=check)
                                
        
e.grid(row=0,column=1)
e1.grid(row=1,column=1)
b.grid(row=2,column=1)






root.mainloop()
