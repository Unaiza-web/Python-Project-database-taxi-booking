from tkinter import *
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox as ms
import sqlite3
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import messagebox, Toplevel
from tkinter import messagebox

class CabBookingSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Cab Booking System")
        self.root.geometry("1270x700")
        self.root.configure(bg="#FFEB3B")  # Yellow Background
        

        # Variables for login and booking
        self.username = tk.StringVar()
        self.password = tk.StringVar()
        self.pickup = tk.StringVar()
        self.destination = tk.StringVar()
        self.cab_type = tk.StringVar()
        self.total_cost = tk.StringVar()
        self.passenger_name = tk.StringVar()
        self.driver_name = tk.StringVar()
        self.driver_phone = tk.StringVar()
        self.driver_distance = tk.StringVar()
        self.cab_number = tk.StringVar()
        self.cab_color = tk.StringVar()

        
        # Start with the login screen
        self.create_db()
        self.show_login()


    def create_db(self):
        # Connect to SQLite database (it will create the database if it doesn't exist)
        conn = sqlite3.connect('cab_booking.db')
        c = conn.cursor()
        # Create table to store users if it doesn't exist
        c.execute('''CREATE TABLE IF NOT EXISTS users
                     (username TEXT PRIMARY KEY, password TEXT)''')
        conn.commit()
        conn.close()


    def show_login(self):
        # Login Window 
        login_frame = tk.Frame(self.root, bg="#FFEB3B")
        login_frame.pack(fill=BOTH, expand=True)


        # Add Image
        try:
            img = Image.open("88.jpg")
            img = img.resize((900,760))
            photo = ImageTk.PhotoImage(img)
            image_label = tk.Label(login_frame, image=photo, bg="#FFEB3B")
            image_label.image = photo  # Keep a reference to avoid garbage collection
            image_label.grid(row=0,column=0)


        except FileNotFoundError:
            image_label = tk.Label(login_frame,text="Image Not Found",font=("Arial", 14, "bold"),bg="#FFEB3B",fg="#000000")
            image_label.place(x=50, y=250)
        # Login Form
        form_frame = tk.Frame(login_frame, bg="#000000", relief="raised", bd=5)
        form_frame.grid(padx=25,row=0,column=1)

        tk.Label(form_frame,text="Login",font=("Broadway", 20, "bold"),bg="#000000",fg="#FFEB3B").pack(pady=20)

        tk.Label(form_frame,text="Username",font=("Berlin Sans FB Demi", 14),bg="#000000",fg="#FFEB3B").pack(pady=10)
        tk.Entry(form_frame, textvariable=self.username, font=("Arial", 14)).pack(pady=5)

        tk.Label(form_frame,text="Password",font=("Berlin Sans FB Demi", 14),bg="#000000",fg="#FFEB3B").pack(pady=10)
        tk.Entry(form_frame, textvariable=self.password, show="*", font=("Arial", 14)).pack(pady=5)

        tk.Button(form_frame,text="Login",command=self.validate_login,font=("Arial", 14, "bold"),bg="#FFEB3B",fg="#000000",activebackground="#FFF176").pack(pady=20)
        
        tk.Label(form_frame,text="Dont have an account? Create one.",font=("Arial", 14),bg="#000000",fg="#FFEB3B").pack(pady=5)

        tk.Button(form_frame,text="Create Account",command=self.show_signup,font=("Arial", 14, "bold"),bg="#FFEB3B",fg="#000000",activebackground="#FFF176").pack(pady=10)

    def validate_login(self):
        conn = sqlite3.connect('cab_booking.db')
        c = conn.cursor()
        c.execute("SELECT * FROM users WHERE username=? AND password=?", (self.username.get(), self.password.get()))
        user = c.fetchone()
        conn.close()

        if user:
            # Clear the screen for the passenger/driver choice
            for widget in self.root.winfo_children():
                widget.destroy()
            travel(root)
        else:
            messagebox.showerror("Login Failed", "Invalid username or password!")

    def show_signup(self):
        # Create Account Window
        signup_window = Toplevel(self.root)
        signup_window.title("Create Account")
        signup_window.geometry("400x400")
        signup_window.configure(bg="#FFEB3B")

        tk.Label(signup_window,text="Create Account",font=("Broadway", 20, "bold"),bg="#FFEB3B",fg="#000000").pack(pady=20)

        tk.Label(signup_window,text="Username",font=("Berlin Sans FB Demi", 14),bg="#FFEB3B",fg="#000000").pack(pady=10)
        new_username = tk.StringVar()
        tk.Entry(signup_window, textvariable=new_username, font=("Arial", 14)).pack(pady=5)

        tk.Label(signup_window,text="Password",font=("Berlin Sans FB Demi", 14),bg="#FFEB3B",fg="#000000").pack(pady=10)
        new_password = tk.StringVar()
        tk.Entry(signup_window, textvariable=new_password, show="*", font=("Arial", 14)).pack(pady=5)

        def save_new_account():
            if new_username.get() and new_password.get():
                conn = sqlite3.connect('cab_booking.db')
                c = conn.cursor()
                c.execute("INSERT INTO users (username, password) VALUES (?, ?)",
                          (new_username.get(), new_password.get()))
                conn.commit()
                conn.close()
                messagebox.showinfo("Account Created", "Account created successfully! Please login.")
                signup_window.destroy()
            else:
                messagebox.showwarning("Input Error", "Please fill in both fields.")

        tk.Button(signup_window,text="Create Account",command=save_new_account,font=("Arial", 14, "bold"),bg="#000000",fg="#FFEB3B",activebackground="#FFF176").pack(pady=20)
        
        application=travel(root)

        

class travel:
    
    def __init__(self,root):
        self.root = root
        self.root.title("Taxi Booking System")
        # self.root.geometry(geometry) 
        self.root.configure(background='black')

        DateofOrder=StringVar()
        DateofOrder.set(time.strftime(" %d / %m / %Y "))
        Receipt_Ref=StringVar()
        PaidTax=StringVar()
        SubTotal=StringVar()
        TotalCost=StringVar()

        var1=IntVar()
        var2=IntVar()
        var3=IntVar()
        var4=IntVar()
        carType=IntVar()
        
        varl1=StringVar()
        varl2=StringVar()
        varl3=StringVar()
        reset_counter=0


        Firstname=StringVar()
        Surname=StringVar()
        Address=StringVar()
        Postcode=StringVar()
        Mobile=StringVar()
        Telephone=StringVar()
        Email=StringVar()

        TaxiTax=StringVar()
        Km=StringVar()
        Travel_Ins=StringVar()
        Luggage=StringVar()
        Receipt=StringVar()


        Standard=StringVar()
        PrimeSedan=StringVar()
        PremiumSedan=StringVar()


        TaxiTax.set("0")
        Km.set("0")
        Travel_Ins.set("0")
        Luggage.set("0")


        Standard.set("0")
        PrimeSedan.set("0")
        PremiumSedan.set("0")



        def iExit():
            iExit= ms.askyesno("Prompt!","Do you want to exit?")
            if iExit > 0:
                root.destroy()
                return

        def Reset():
            TaxiTax.set("0")
            Km.set("0")
            Travel_Ins.set("0")
            Luggage.set("0")

            Standard.set("0")
            PrimeSedan.set("0")
            PremiumSedan.set("0")

            Firstname.set("")
            Surname.set("")
            Address.set("")
            Postcode.set("")
            Mobile.set("")
            Telephone.set("")
            Email.set("")

            PaidTax.set("")
            SubTotal.set("")
            TotalCost.set("")
            self.txtReceipt1.delete("1.0",END)
            self.txtReceipt2.delete("1.0",END)
            
            var1.set(0)
            var2.set(0)
            var3.set(0)
            var4.set(0)
            carType.set(0)
            varl1.set("0")
            varl2.set("0")
            varl3.set("0")

            self.cboPickup.current(0)
            self.cboDrop.current(0)
            self.cboPooling.current(0)

            self.txtTaxiTax.configure(state=DISABLED)
            self.txtKm.configure(state=DISABLED)
            self.txtTravel_Ins.configure(state=DISABLED)
            self.txtLuggage.configure(state=DISABLED)
        
            self.txtStandard.configure(state=DISABLED)
            self.txtPrimeSedan.configure(state=DISABLED)
            self.txtPremiumSedan.configure(state=DISABLED)
            self.reset_counter=1

        def Receiptt():
            if reset_counter is 0 and Firstname.get()!="" and Surname.get()!="" and Address.get()!="" and Postcode.get()!="" and Mobile.get()!="" and Telephone.get()!="" and Email.get()!="":
                self.txtReceipt1.delete("1.0",END)
                self.txtReceipt2.delete("1.0",END)
                x=random.randint(10853,500831)
                randomRef = str(x)
                Receipt_Ref.set(randomRef)

                self.txtReceipt1.insert(END,"Receipt Ref:\n")
                self.txtReceipt2.insert(END, Receipt_Ref.get() + "\n")
                self.txtReceipt1.insert(END,'Date:\n')
                self.txtReceipt2.insert(END, DateofOrder.get() + "\n")
                self.txtReceipt1.insert(END,'Taxi No:\n')
                self.txtReceipt2.insert(END, 'TR ' + Receipt_Ref.get() + " BW\n")
                self.txtReceipt1.insert(END,'Firstname:\n')
                self.txtReceipt2.insert(END, Firstname.get() + "\n")
                self.txtReceipt1.insert(END,'Surname:\n')
                self.txtReceipt2.insert(END, Surname.get() + "\n")
                self.txtReceipt1.insert(END,'Address:\n')
                self.txtReceipt2.insert(END, Address.get() + "\n")
                self.txtReceipt1.insert(END,'Postal Code:\n')
                self.txtReceipt2.insert(END, Postcode.get() + "\n")
                self.txtReceipt1.insert(END,'Telephone:\n')
                self.txtReceipt2.insert(END, Telephone.get() + "\n")
                self.txtReceipt1.insert(END,'Mobile:\n')
                self.txtReceipt2.insert(END, Mobile.get() + "\n")
                self.txtReceipt1.insert(END,'Email:\n')
                self.txtReceipt2.insert(END, Email.get() + "\n")
                self.txtReceipt1.insert(END,'From:\n')
                self.txtReceipt2.insert(END, varl1.get() + "\n")
                self.txtReceipt1.insert(END,'To:\n')
                self.txtReceipt2.insert(END, varl2.get() + "\n")
                self.txtReceipt1.insert(END,'Pooling:\n')
                self.txtReceipt2.insert(END, varl3.get() + "\n")
                self.txtReceipt1.insert(END,'Standard:\n')
                self.txtReceipt2.insert(END, Standard.get() + "\n")
                self.txtReceipt1.insert(END,'Prime Sedan:\n')
                self.txtReceipt2.insert(END, PrimeSedan.get() + "\n")
                self.txtReceipt1.insert(END,'Premium Sedan:\n')
                self.txtReceipt2.insert(END, PremiumSedan.get() + "\n")
                self.txtReceipt1.insert(END,'Paid:\n')
                self.txtReceipt2.insert(END, PaidTax.get() + "\n")
                self.txtReceipt1.insert(END,'SubTotal:\n')
                self.txtReceipt2.insert(END, str(SubTotal.get()) + "\n")
                self.txtReceipt1.insert(END,'Total Cost:\n')
                self.txtReceipt2.insert(END, str(TotalCost.get()))
                
            else:
                self.txtReceipt1.delete("1.0",END)
                self.txtReceipt2.delete("1.0",END)
                self.txtReceipt1.insert(END,"\nNo Input")
                

        def Taxi_Tax():
            global Item1
            if var1.get() == 1:
                self.txtTaxiTax.configure(state = NORMAL)
                Item1=float(50)
                TaxiTax.set("Rs " + str(Item1))
            elif var1.get() == 0:
                self.txtTaxiTax.configure(state=DISABLED)
                TaxiTax.set("0")
                Item1=0

        
        def Kilo():
            if var2.get() == 0:
                self.txtKm.configure(state=DISABLED)
                Km.set("0")
            elif var2.get() == 1 and varl1.get() != "" and varl2.get() != "":
                self.txtKm.configure(state=NORMAL)
                if varl1.get() == "Clifton":
                    switch ={"Gulshan": 10,"North Karachi": 8,"Jauhar":6,"Clifton": 0,"Malir":5,"Bahria Town":7,"DHA":8}
                    Km.set(switch[varl2.get()])
                elif varl1.get() == "Gulshan":
                    switch ={"Gulshan": 0,"North Karachi": 2,"Jauhar":5,"Clifton": 10,"Malir":5,"Bahria Town":9,"DHA":8}
                    Km.set(switch[varl2.get()])
                elif varl1.get() == "North Karachi":
                    switch ={"Gulshan": 2,"North Karachi":0,"Jauhar":3,"Clifton": 8,"Malir":5,"Bahria Town":7,"DHA":8}
                    Km.set(switch[varl2.get()])
                elif varl1.get() == "Jauhar":
                    switch ={"Gulshan": 5,"North Karachi": 3,"Jauhar":0,"Clifton": 6,"Malir":5,"Bahria Town":9,"DHA":8}
                    Km.set(switch[varl2.get()])   
                elif varl1.get() == "Malir":
                    switch ={"Gulshan": 5,"North Karachi": 3,"Jauhar":8,"Clifton": 6,"Malir":0,"Bahria Town":10,"DHA":8}
                    Km.set(switch[varl2.get()])  
                elif varl1.get() == "Bahria Town":
                    switch ={"Gulshan": 5,"North Karachi": 3,"Jauhar":7,"Clifton": 6,"Malir":5,"Bahria Town":0,"DHA":8}
                    Km.set(switch[varl2.get()]) 
                elif varl1.get() == "DHA":
                    switch ={"Gulshan": 5,"North Karachi": 3,"Jauhar":3,"Clifton": 6,"Malir":5,"Bahria Town":6,"DHA":0}
                    Km.set(switch[varl2.get()]) 
                

        
        def Travelling():
            global Item3
            if var3.get() == 1:
                self.txtTravel_Ins.configure(state = NORMAL)
                Item3=float(10)
                Travel_Ins.set("Rs " + str(Item3))
            elif var3.get() == 0:
                self.txtTravel_Ins.configure(state = DISABLED)
                Travel_Ins.set("0")
                Item3=0

        
        def Lug():
            global Item4
            if (var4.get()==1):
                self.txtLuggage.configure(state = NORMAL)
                Item4=float(30)
                Luggage.set("Rs "+ str(Item4))
            elif var4.get()== 0:
                self.txtLuggage.configure(state = DISABLED)
                Luggage.set("0")
                Item4=0

        
        def selectCar():
            global Item5
            if carType.get() == 1:
                self.txtPrimeSedan.configure(state = DISABLED)
                PrimeSedan.set("0") 
                self.txtPremiumSedan.configure(state = DISABLED)
                PremiumSedan.set("0")
                self.txtStandard.configure(state = NORMAL)
                Item5 = float(8)
                Standard.set("Rs "+ str(Item5))
            elif carType.get() == 2:
                self.txtStandard.configure(state =DISABLED)
                Standard.set("0")
                self.txtPremiumSedan.configure(state = DISABLED)
                PremiumSedan.set("0")
                self.txtPrimeSedan.configure(state = NORMAL)
                Item5 = float(10)
                PrimeSedan.set("Rs "+ str(Item5))
            else:
                self.txtStandard.configure(state =DISABLED)
                Standard.set("0")
                self.txtPrimeSedan.configure(state = DISABLED)
                PrimeSedan.set("0")
                self.txtPremiumSedan.configure(state = NORMAL)
                Item5 = float(15)
                PremiumSedan.set("Rs "+ str(Item5))
                
                    
        

        def Total_Paid():
            # Check if necessary inputs are provided
            if ((var1.get() == 1 and var2.get() == 1 and var3.get() == 1 or var4.get() == 1) and carType.get() != 0 and (varl1.get() != "" and varl2.get() != "")):
                
                # Retrieve km value and calculate base fare
                Item2 = Km.get()
                Cost_of_fare = (Item1 + (float(Item2) * Item5) + Item3 + Item4)
                
                # Apply tax calculation
                Tax = "Rs " + str('%.2f' % (Cost_of_fare * 0.09))
                ST = "Rs " + str('%.2f' % (Cost_of_fare))
                TT = "Rs " + str('%.2f' % (Cost_of_fare + (Cost_of_fare * 0.09)))
                
                # Set the calculated values to the labels
                PaidTax.set(Tax)
                SubTotal.set(ST)
                TotalCost.set(TT)
            else:
                # Show error if inputs are invalid
                w = ms.showwarning("Error !", "Invalid Input\nPlease try again !!!")



        

            

#  main frame

        MainFrame=Frame(self.root)
        MainFrame.pack(fill=BOTH,expand=True)
        
        
        Tops = Frame(MainFrame, bd=3, width=550,relief=RIDGE,bg="black",height=43)
        Tops.pack(side=TOP,fill=X)


        self.lblTitle=Label(Tops,font=('Bauhaus 93',40,'bold'),text=f"WELCOME To Our\nTaxi Booking System",bg="black",fg="#FFEB3B")
        self.lblTitle.grid(padx=376)


    #  customerframedetail
        CustomerDetailsFrame=LabelFrame(MainFrame, width=700,height=60,bd=3, pady=5, relief=RIDGE,bg="#FFEB3B")
        CustomerDetailsFrame.pack(side=BOTTOM,fill=BOTH,expand=True)

        FrameDetails=Frame(CustomerDetailsFrame, width=500,height=200,bd=3, relief=RIDGE,bg="beige")
        FrameDetails.pack(side=LEFT,fill=Y)

        CustomerName=LabelFrame(FrameDetails, width=200,height=100,bd=3, font=('Showcard Gothic',12,'bold'),text="Customer Detail", relief=RIDGE,fg="black",bg="#FFEB3B")
        CustomerName.grid(row=0,column=0,pady=0)

        TravelFrame = LabelFrame(FrameDetails,bd=3, width=200,height=250, font=('Showcard Gothic',12,'bold'),text="Booking Detail", relief=RIDGE,fg="black",bg="#FFEB3B")
        TravelFrame.grid(row=0,column=1,padx=4,pady=2)

        Book_Frame=LabelFrame(FrameDetails,width=300,height=150,bg="#FFEB3B",font=('Showcard Gothic',12,'bold'),text="Cars Detail", relief=RIDGE,fg="black",bd=5)
        Book_Frame.grid(row=1,pady=0,column=1,sticky="w",columnspan=2,padx=16)

        CostFrame = LabelFrame(FrameDetails,width=300,height=150,bd=5,bg="#FFEB3B",font=('Showcard Gothic',12,'bold'),text="Amount", relief=RIDGE,fg="black")
        CostFrame.grid(row=2,pady=0,column=1,sticky="w",columnspan=2,padx=16)
        



    #  receipt
        Receipt_BottonFrame=LabelFrame(CustomerDetailsFrame,bd=10, width=450,height=400, relief=RIDGE,bg="beige")
        Receipt_BottonFrame.pack(side=RIGHT,fill=BOTH,expand=True)

        ReceiptFrame=LabelFrame(Receipt_BottonFrame, width=350,height=300, font=('Showcard Gothic',12,'bold'),text="Receipt", relief=RIDGE,bg="#FFEB3B",fg="black")
        ReceiptFrame.grid(row=0,column=0)

        ButtonFrame=LabelFrame(Receipt_BottonFrame, width=350,height=100, relief=RIDGE)
        ButtonFrame.grid(row=1,column=0)



        

        # Insert image 1
        image = Image.open("taxi1.png")  # Replace with your image path
        photo = ImageTk.PhotoImage(image)
        # Create label for image
        imageLabel = Label(FrameDetails, image=photo, bg="#FFEB3B")
        imageLabel.grid(row=1, column=0, rowspan=2, padx=3, pady=3, sticky="n")


    #   CustomerName
        self.lblFirstname=Label(CustomerName,font=('arial',12,'bold'),text="Firstname",bd=5,fg="black",bg="#FFEB3B",width=10)
        self.lblFirstname.grid(row=0,column=0,sticky=W)
        self.txtFirstname=Entry(CustomerName,font=('arial',12,'bold'),textvariable=Firstname,bd=5,insertwidth=2,justify=RIGHT)
        self.txtFirstname.grid(row=0,column=1)


        self.lblSurname=Label(CustomerName,font=('arial',12,'bold'),text="Surname",bd=5,fg="black",bg="#FFEB3B",width=10)
        self.lblSurname.grid(row=1,column=0,sticky=W)
        self.txtSurname=Entry(CustomerName,font=('arial',12,'bold'),textvariable=Surname,bd=5,insertwidth=2,justify=RIGHT)
        self.txtSurname.grid(row=1,column=1,sticky=W)


        self.lblAddress=Label(CustomerName,font=('arial',12,'bold'),text="Address",bd=5,fg="black",bg="#FFEB3B",width=10)
        self.lblAddress.grid(row=2,column=0,sticky=W)
        self.txtAddress=Entry(CustomerName,font=('arial',12,'bold'),textvariable=Address,bd=5,insertwidth=2,justify=RIGHT)
        self.txtAddress.grid(row=2,column=1)


        self.lblPostcode=Label(CustomerName,font=('arial',12,'bold'),text="Postcode",bd=5,fg="black",bg="#FFEB3B",width=10)
        self.lblPostcode.grid(row=3,column=0,sticky=W)
        self.txtPostcode=Entry(CustomerName,font=('arial',12,'bold'),textvariable=Postcode,bd=5,insertwidth=2,justify=RIGHT)
        self.txtPostcode.grid(row=3,column=1)


        self.lblTelephone=Label(CustomerName,font=('arial',12,'bold'),text="Telephone",bd=5,fg="black",bg="#FFEB3B",width=10)
        self.lblTelephone.grid(row=4,column=0,sticky=W)
        self.txtTelephone=Entry(CustomerName,font=('arial',12,'bold'),textvariable=Telephone,bd=5,insertwidth=2,justify=RIGHT)
        self.txtTelephone.grid(row=4,column=1)

        self.lblMobile=Label(CustomerName,font=('arial',12,'bold'),text="Mobile",bd=5,fg="black",bg="#FFEB3B",width=10)
        self.lblMobile.grid(row=5,column=0,sticky=W)
        self.txtMobile=Entry(CustomerName,font=('arial',12,'bold'),textvariable=Mobile,bd=5,insertwidth=2,justify=RIGHT)
        self.txtMobile.grid(row=5,column=1)

        self.lblEmail=Label(CustomerName,font=('arial',12,'bold'),text="Email",bd=5,fg="black",bg="#FFEB3B",width=10)
        self.lblEmail.grid(row=6,column=0,sticky=W)
        self.txtEmail=Entry(CustomerName,font=('arial',12,'bold'),textvariable=Email,bd=5,insertwidth=3,justify=RIGHT)
        self.txtEmail.grid(row=6,column=1)


    #   Taxi Information
        self.lblPickup=Label(TravelFrame,font=('arial',12,'bold'),text="Pickup",bd=7,fg="black",bg="#FFEB3B")
        self.lblPickup.grid(row=0,column=0,sticky=W)

        self.cboPickup =ttk.Combobox(TravelFrame, textvariable = varl1 , state='readonly', font=('arial',12,'bold'), width=14)
        self.cboPickup['value']=('','Gulshan','North Karachi','Jauhar','Clifton','Malir',"Bahria Town","DHA")
        self.cboPickup.current(0)
        self.cboPickup.grid(row=0,column=1)


        self.lblDrop=Label(TravelFrame,font=('arial',12,'bold'),text="Drop",bd=7,fg="black",bg="#FFEB3B")
        self.lblDrop.grid(row=1,column=0,sticky=W)

        self.cboDrop =ttk.Combobox(TravelFrame, textvariable = varl2 , state='readonly', font=('arial',12,'bold'), width=14)
        self.cboDrop['value']=('','Gulshan','North Karachi','Jauhar','Clifton','Malir',"Bahria Town","DHA")
        self.cboDrop.current(0)
        self.cboDrop.grid(row=1,column=1)

        self.lblPooling=Label(TravelFrame,font=('arial',12,'bold'),text="Pooling",bd=7,fg="black",bg="#FFEB3B")
        self.lblPooling.grid(row=2,column=0,sticky=W)

        self.cboPooling =ttk.Combobox(TravelFrame, textvariable = varl3 , state='readonly', font=('arial',12,'bold'), width=14)
        self.cboPooling['value']=('','1','2','3','4')
        self.cboPooling.current(1)
        self.cboPooling.grid(row=2,column=1)

    #  Taxi Information

        self.chkTaxiTax=Checkbutton(TravelFrame,text="Taxi Tax(Base Charge) *",variable = var1, onvalue=1, offvalue=0,font=('arial',12,'bold'),fg="black",bg="#FFEB3B",command=Taxi_Tax).grid(row=3, column=0, sticky=W)
        self.txtTaxiTax=Label(TravelFrame,font=('arial',12,'bold'),textvariable=TaxiTax,bd=5,width=8,bg="white",state= DISABLED,justify=RIGHT,relief=SUNKEN)
        self.txtTaxiTax.grid(row=3,column=1,padx=1)


        self.chkKm=Checkbutton(TravelFrame,text="Distance(KMs) *",variable = var2, onvalue=1, offvalue=0,font=('arial',12,'bold'),fg="black",bg="#FFEB3B",command=Kilo).grid(row=4, column=0, sticky=W)
        self.txtKm=Label(TravelFrame,font=('arial',12,'bold'),textvariable=Km,bd=5,width=8,bg="white",state= DISABLED,justify=RIGHT,relief=SUNKEN,highlightthickness=0)
        self.txtKm.grid(row=4,column=1,padx=1)

        self.chkTravel_Ins=Checkbutton(TravelFrame,text="Travelling Insurance *",variable = var3, onvalue=1, offvalue=0,font=('arial',12,'bold'),fg="black",bg="#FFEB3B",command=Travelling).grid(row=5, column=0, sticky=W)
        self.txtTravel_Ins=Label(TravelFrame,font=('arial',12,'bold'),textvariable=Travel_Ins,bd=5,width=8,bg="white",state= DISABLED,justify=RIGHT,relief=SUNKEN)
        self.txtTravel_Ins.grid(row=5,column=1,padx=1)

    
        self.chkLuggage=Checkbutton(TravelFrame,text="Extra Luggage",variable = var4, onvalue=1, offvalue=0,font=('arial',12,'bold'),fg="black",bg="#FFEB3B",command=Lug).grid(row=6, column=0, sticky=W)
        self.txtLuggage=Label(TravelFrame,font=('arial',12,'bold'),textvariable=Luggage,bd=5,width=8,bg="white",state= DISABLED,justify=RIGHT,relief=SUNKEN)
        self.txtLuggage.grid(row=6,column=1,padx=1)
    
    #   payment information 

        self.lblPaidTax=Label(CostFrame,font=('arial',12,'bold'),text="Paid Tax\t\t",bd=5,fg="black",bg="#FFEB3B")
        self.lblPaidTax.grid(row=0,column=2,sticky=W)
        self.txtPaidTax = Label(CostFrame,font=('arial',12,'bold'),textvariable=PaidTax,bd=5, width=8,justify=RIGHT, bg="white",relief=SUNKEN)
        self.txtPaidTax.grid(row=0,column=3)
            

        
        self.lblSubTotal=Label(CostFrame,font=('arial',12,'bold'),text="Sub Total",bd=5,fg="black",bg="#FFEB3B")
        self.lblSubTotal.grid(row=1,column=2,sticky=W)
        self.txtSubTotal = Label(CostFrame,font=('arial',12,'bold'),textvariable=SubTotal,bd=5, width=8, justify=RIGHT,bg="white",relief=SUNKEN)
        self.txtSubTotal.grid(row=1,column=3)



        self.lblTotalCost=Label(CostFrame,font=('arial',12,'bold'),text="Total Cost",bd=5,fg="black",bg="#FFEB3B")
        self.lblTotalCost.grid(row=2,column=2,sticky=W)
        self.txtTotalCost = Label(CostFrame,font=('arial',12,'bold'),textvariable=TotalCost,bd=5, width=8, justify=RIGHT,relief=SUNKEN,bg="white")
        self.txtTotalCost.grid(row=2,column=3)

    #   taxiselect

        self.chkStandard=Radiobutton(Book_Frame,text="Standard",value=1,variable = carType,font=('arial',12,'bold'),fg="black",bg="#FFEB3B",command=selectCar).grid(row=0, column=0, sticky=W)
        self.txtStandard = Label(Book_Frame,font=('arial',12,'bold'),width =6,textvariable=Standard,bd=5, state= DISABLED, justify=RIGHT,bg="white",relief=SUNKEN)
        self.txtStandard.grid(row=0,column=1)
        

        self.chkPrimeSedand=Radiobutton(Book_Frame,text="PrimeSedan",value=2,variable = carType,font=('arial',12,'bold'),fg="black",bg="#FFEB3B",command=selectCar).grid(row=1, column=0, sticky=W)
        self.txtPrimeSedan= Label(Book_Frame,font=('arial',12,'bold'),width =6,textvariable=PrimeSedan,bd=5, state= DISABLED, justify=RIGHT,bg="white",relief=SUNKEN)
        self.txtPrimeSedan.grid(row=1,column=1)
            
    
        self.chkPremiumSedan = Radiobutton(Book_Frame,text="PremiumSedan",value=3,variable = carType,font=('arial',12,'bold'),fg="black",bg="#FFEB3B",command=selectCar).grid(row=2, column=0)
        self.txtPremiumSedan = Label(Book_Frame,font=('arial',12,'bold'),width =6,textvariable=PremiumSedan,bd=5, state= DISABLED, justify=RIGHT,bg="white",relief=SUNKEN)
        self.txtPremiumSedan.grid(row=2,column=1)

    
    
    #    Recipt 

        self.txtReceipt1 = Text(ReceiptFrame,width = 22, height = 21,font=('arial',8,'bold'),borderwidth=0,bg="white")
        self.txtReceipt1.grid(row=0,column=0,columnspan=2)
        self.txtReceipt2 = Text(ReceiptFrame,width = 22, height = 21,font=('arial',8,'bold'),borderwidth=0,bg="white")
        self.txtReceipt2.grid(row=0,column=2,columnspan=2)


        # insert image 2
        image2= Image.open("24.jpg")  # Replace with your image path
        photo2 = ImageTk.PhotoImage(image2)
        # Create label for image
        imageLabel2 = Label(Receipt_BottonFrame, image=photo2, bd=7, bg="#FFEB3B")
        imageLabel2.grid(row=0, column=1, rowspan=7, padx=1, pady=5, sticky="n")
        


        #  insert image 3
        image3= Image.open("taxi.jpg")  # Replace with your image path
        photo3 = ImageTk.PhotoImage(image3)
        # Create label for image
        imageLabel2 = Label(Receipt_BottonFrame, image=photo3, bd=7, bg="#FFEB3B")
        imageLabel2.grid(row=2, column=0, rowspan=7, padx=5, pady=10, sticky="n",columnspan=2)

    #  Button  
        
        self.btnTotal = Button(ButtonFrame,padx=18,bd=7,font=('arial',10,'bold'),width = 2,text='Total',bg="#FFEB3B",fg="black",command=Total_Paid).grid(row=0,column=0)
        self.btnReceipt = Button(ButtonFrame,padx=18,bd=7,font=('arial',10,'bold'),width = 2,text='Receipt',bg="#FFEB3B",fg="black",command=Receiptt).grid(row=0,column=1)
        self.btnReset = Button(ButtonFrame,padx=18,bd=7,font=('arial',10,'bold'),width = 2,text='Reset',bg="#FFEB3B",fg="black",command=Reset).grid(row=0,column=2)
        self.btnExit = Button(ButtonFrame,padx=18,bd=7,font=('arial',10,'bold'),width = 2,text='Exit',bg="#FFEB3B",fg="black", command=iExit).grid(row=0,column=3)
        

        self.photo = photo
        self.photo2=photo2
        self.photo3=photo3

        
if __name__=='__main__':
    root = Tk()

    #  Getting Screen Width   
    # w = root.winfo_screenwidth()
    # h = root.winfo_screenheight()
    # geometry="%dx%d+%d+%d"%(w,h,0,0)
    
    root.geometry("1370x720")
  
    root.title('Login Form')
    application = CabBookingSystem(root)
    root.mainloop()



