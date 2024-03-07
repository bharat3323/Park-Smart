import tkinter as tk
from tkinter import messagebox, Frame, PhotoImage, Button, Entry
from tkinter import ttk
from PIL import Image, ImageTk
from tkcalendar import DateEntry
from google.cloud import firestore
import json
import customtkinter
from slot1 import SlotBookingApp

credential_path="assets\smartpark-5041b-firebase-adminsdk-fxldw-d4791e8efc.json"
with open(credential_path) as json_file:
    credential_info=json.load(json_file)
db=firestore.Client.from_service_account_info(credential_info)

class ParkingSystem(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Smart Parking System")
        self.geometry("1800x800")
        self.resizable(True, True)
        self.state('zoomed')

        self.create_login_screen()

    def create_login_screen(self):
        
        self.frame2 = Frame(self, width=1050, height=1000, bg='white')
        self.frame2.place(x=0, y=0)
        original_Image=Image.open('assets\parking1.png')
        resized_img=original_Image.resize((800,800))
        # self.img=ImageTk.PhotoImage(file=resized_img,width=800,height=2000)
        self.bg_img=ImageTk.PhotoImage(resized_img)
        self.lable1 = tk.Label(self.frame2, image=self.bg_img, bg='white')
        #self.lable1.img = self.img  # Keep a reference
        self.lable1.place(x=100, y=0)
        label2 = tk.Label(self.lable1, text="Welcome to ",font=('Arial Black', 30),bg='white',fg='black',justify='center')
        
        #label2["justify"]="center"
        label2.place(x=250, y=20)
        label3 = tk.Label(self.lable1, text="SmartPark",font=('Cooper Black', 30),bg='white',fg='#1260CC',justify='center')
        label3.place(x=270, y=80)
        #btn1 = Button(frame2, width=50, pady=7, text="About Us", bg='blue', fg='white', border=0, cursor='hand2',)
        #btn1.place(x=50, y=100)
        frame1 = Frame(self, width=500, height=1000, bg='#73A4FF')
        frame1.place(x=1050, y=0)
        
        #self.img2=PhotoImage(file="sm.png")
        #label3=Label(frame2,image=self.img2).place(x=800,y=60)
        self.logo_image = PhotoImage(file="assets\logo2.png")  # Cha
        self.logo_label = tk.Label(frame1, image=self.logo_image, bg='#73A4FF')
        self.logo_label.image = self.logo_image  # Keep a reference
        self.logo_label.place(x=150, y=0)
        
        heading = tk.Label(frame1, text="Login", fg='black', bg='#73A4FF', font=('Cooper Black', 23, 'bold'))
        heading.place(x=200, y=200)
        
       # label1 = Label(frame1, text="Username", font=('ariel', 11), bg='#73A4FF', fg='black')
        #label1.place(x=150, y=270)
        
        #label2 = Label(frame1, text="Password", font=('ariel', 11), bg='#73A4FF', fg='black')
        #label2.place(x=150, y=330)
        
        self.userentry = customtkinter.CTkEntry(frame1,placeholder_text="Enter Username",border_width=0, corner_radius=50,width=200,fg_color="white",text_color='black', bg_color="#73A4FF", font=('Microsoft YaHei UI Light', 11))
        self.userentry.place(x=150, y=290)
        
        self.passentry = customtkinter.CTkEntry(frame1,placeholder_text="Enter Password",border_width=0, corner_radius=50,width=200,fg_color="white",text_color='black',show='*', bg_color="#73A4FF", font=('Microsoft YaHei UI Light', 11))
        self.passentry.place(x=150, y=340)
        self.loginbtn=PhotoImage(file="assets\login.png")
        self.signinbtn=PhotoImage(file="assets\signin.png")
        btn1 = Button(frame1, image=self.loginbtn,border=0, cursor='hand2',bg='#73A4FF',activebackground='#73A4FF',command=self.login)
        btn1.place(x=150, y=400)
        
        btn2 = Button(frame1,width=30, pady=7 ,text="Forgot Password?", font=('ariel', 11), bg='#73A4FF',border=0, fg='blue',cursor='hand2',activebackground='#73A4FF')
        btn2.place(x=120, y=460)
        label4 = tk.Label(frame1, text="------------------   or   -----------------" ,bg='#73A4FF', fg='black')
        label4.place(x=150, y=490)
        btn3 = Button(frame1, image=self.signinbtn,border=0, cursor='hand2',bg='#73A4FF',activebackground='#73A4FF')
        btn3.place(x=150, y=520)
        
    

    def login(self):
        # Get username and password entered by the user
        username = self.userentry.get()
        password = self.passentry.get()
        user_profiles_ref=db.collection('user_profile')
        user_profile={
            'username':username,
            'password':password
        }
        new_user_ref=user_profiles_ref.add(user_profile)
        user_id=new_user_ref[1].id

        # Define a dictionary of predefined username-password pairs
        credentials = {
            "bharatbhandari036": "bharat123",
            "login": "123"
            # Add more username-password pairs as needed
        }

        # Check if the entered credentials match any of the predefined pairs
        if username in credentials and credentials[username] == password:
            messagebox.showinfo("Login Successful", "Welcome, " + username + "!")
            self.frame2.pack_forget()
            self.create_parking_app()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")

    def create_parking_app(self):
        self.parking_app_frame = Frame(self, width=1800, height=800)
        self.parking_app_frame.pack(fill='both', expand=True)
        self.parking_app_frame.place(x=0, y=0)

        self.bg_frame = Frame(self.parking_app_frame, width=1000, height=800)
        self.bg_frame.pack(fill='both', expand=True)
        self.bg_frame.place(x=-80, y=0)

        original_image = Image.open("assets/bharat.png")  # Adjusted file path
        resized_image = original_image.resize((900, 800))
        self.bg_image = ImageTk.PhotoImage(resized_image)

        self.background_label = tk.Label(self.bg_frame, image=self.bg_image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.info_frame = Frame(self.parking_app_frame, bg='#b5e2ff', width=700, height=800)
        self.info_frame.place(x=850, y=0)

        self.label1 = tk.Label(self.info_frame, text="Information page", width=20, height=1, bg='#b5e2ff',
                               font=('Helvetica', 35, 'italic'))
        self.label1.place(x=40, y=70)

        self.label2 = tk.Label(self.info_frame, text='Enter Vehicle Number:', font=('Arial', 20), bg='#b5e2ff',
                               fg='black')
        self.label2.place(x=20, y=190)

        self.label3 = tk.Label(self.info_frame, text='Enter Vehicle Model:', font=('Arial', 20), bg='#b5e2ff',
                               fg='black')
        self.label3.place(x=20, y=290)

        choices = ['Java', 'Python', 'C', 'C++', 'OS']
        self.label4 = tk.Label(self.info_frame, text='Select Batch:', font=('Arial', 20), bg='#b5e2ff', fg='black')
        self.label4.place(x=20, y=400)

        self.combo_box = ttk.Combobox(self.info_frame, values=choices, width=35, height=40)
        self.combo_box.place(x=300, y=400)

        self.label5 = tk.Label(self.info_frame, text='Select Date:', font=('Arial', 20), bg='#b5e2ff', fg='black')
        self.label5.place(x=20, y=500)

        self.label6 = tk.Label(self.info_frame, text='Select Time:', font=('Arial', 20), bg='#b5e2ff', fg='black')
        self.label6.place(x=20, y=600)

        self.entry1 = tk.Entry(self.info_frame, font=('Arial', 15))
        self.entry1.place(x=300, y=200)

        self.entry2 = tk.Entry(self.info_frame, font=('Arial', 15))
        self.entry2.place(x=300, y=295)

        self.entry4 = DateEntry(self.info_frame, width=12, background='darkblue', foreground='white', borderwidth=2,
                                year=2024, font=('Arial', 15))
        self.entry4.place(x=300, y=500)

        self.entry5 = tk.Entry(self.info_frame, font=('Arial', 15))
        self.entry5.place(x=300, y=600)

        self.button = Button(self.info_frame, text='Go to slot booking', bg='cyan3',
                             font=('Arial', 15, 'italic'), bd=5, command=self.go_to_slot_booking)
        self.button.place(x=100, y=700)
        self.button1 = Button(self.info_frame, text='Retrive data', bg='cyan3',
                             font=('Arial', 15, 'italic'), bd=5, command=self.data_retrive1)
        self.button1.place(x=400, y=700)
        

    def go_to_slot_booking(self):
        vehicalno=self.entry1.get()
        vehicalm=self.entry2.get()
        batch=self.combo_box.get()
        todayDate=self.entry4.get()
        time=self.entry5.get()
        user_vehicle_ref=db.collection('Vehicle Info')
        VehicleInfo={
            'vehicle no':vehicalno,
            'vehicle Model':vehicalm,
            'Batch':batch,
            'Date':todayDate,
            'Time':time
        }
        new_user_ref=user_vehicle_ref.add(VehicleInfo)
        user_id=new_user_ref[1].id
        self.parking_app_frame.pack_forget()
        self.create_slotbooking()
    def data_retrive1(self):
        self.parking_app_frame.pack_forget()
        self.data_retrive()
    def data_retrive(self):
        def retrieve_data():
            doc_ref = db.collection(u'Vehicle Info').document(u'QZH3am7oqj8rRyDOT0rp')
            
            doc = doc_ref.get()
            data = doc.to_dict()
            # ref = db.collection('Vehicle Info')
            # snapshot = ref.order_by_key().get()
            # print(snapshot)
            if data:
               # name_var.set(data.get('name', ''))
                vehicle_number_var.set(data.get('vehicle no', ''))
                vehicle_model_var.set(data.get('vehicle Model', ''))
                date_var.set(data.get('Date', ''))
                
                batch_var.set(data.get('Batch', ''))
        #self.parking_app_frame.pack_forget() 
          
        self.data = tk.Frame(self, width=1800, height=800)
        self.data.pack(fill='both', expand=True)
        self.data.place(x=0, y=0)
        # retriveframe=tk.Frame(data,width=800,height=1000)
        # retriveframe.place(x=1000,y=0)
        # original_Image=Image.open('assets\dr.png')
        # resized_img=original_Image.resize((800,800))
        # # self.img=ImageTk.PhotoImage(file=resized_img,width=800,height=2000)
        # self.bg_img=ImageTk.PhotoImage(resized_img)
        # self.lable1 = tk.Label(data, image=self.bg_img, bg='lightblue')
        # #self.lable1.img = self.img  # Keep a reference
        # self.lable1.place(x=100, y=0)
        # label2 = tk.Label(self.lable1, text="Welcome to ",font=('Arial Black', 30),bg='white',fg='black',justify='center')
        
        #label2["justify"]="center"
        # label2.place(x=250, y=20)

        # Variables to store retrieved data
        name_var = tk.StringVar()
        vehicle_number_var = tk.StringVar()
        vehicle_model_var = tk.StringVar()
        date_var = tk.StringVar()
        batch_var = tk.StringVar()

        # Labels
        #name_label = tk.Label(self.data, text="Name:")
        #name_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")

        self.vehicle_number_label = tk.Label(self.data, text="Vehicle Number:")
        self.vehicle_number_label.place(x=500,y=0)

        self.vehicle_model_label = tk.Label(self.data, text="Vehicle Model:")
        self.vehicle_model_label.place(x=500,y=20)

        self.date_label = tk.Label(self.data, text="Date:")
        self.date_label.place(x=500,y=40)

        self.batch_label = tk.Label(self.data, text="Batch:")
        self.batch_label.place(x=500,y=60)

        # Entry fields to display retrieved data
        #name_entry = tk.Entry(self.data, textvariable=name_var)
        #name_entry.grid(row=0, column=1, padx=5, pady=5)

        self.vehicle_number_entry = tk.Label(self.data, textvariable=vehicle_number_var)
        self.vehicle_number_entry.place(x=650,y=0)

        self.vehicle_model_entry = tk.Label(self.data, textvariable=vehicle_model_var)
        self.vehicle_model_entry.place(x=650,y=20)

        self.date_entry = tk.Label(self.data, textvariable=date_var)
        self.date_entry.place(x=650,y=40)

        self.batch_entry = tk.Label(self.data, textvariable=batch_var)
        self.batch_entry.place(x=650,y=60)

        # Button to retrieve data
        self.retrieve_button = tk.Button(self.data, text="Retrieve Data", command=retrieve_data)
        self.retrieve_button.place(x=500,y=100)
       
        self.back = tk.Button(self.data, text="home", command=self.home)
        self.back.place(x=700,y=100)
    def home(self):
        self.data.pack_forget()
        self.create_login_screen()

    def create_slotbooking(self):

        self.slotbooking_frame = Frame(self, width=1800, height=800,bg='#F0FFFF')
        self.slotbooking_frame.pack(fill='both', expand=True)
        self.slotbooking_frame.place(x=0, y=0)
        self.label = tk.Label(self.slotbooking_frame, text="Parking Area", font=("Arial", 50, "bold"), bg="#F0FFFF")
        self.label.place(x=120,y=40)

        homeButton = tk.Button(self.slotbooking_frame, text="Home",command=self.create_login_screen)
        homeButton.place(x=30,y=20)
        # Add buttons for parking slots
        for i in range(10):
            button = tk.Button(self.slotbooking_frame, text=f"P-no {i+1}", command=self.book_slot, width=15, height=10)
            button.pack()
            button.place(x=30+250*(i%3), y=150+230*(i//3))
        
        #2nd frame
        self.info_frame = Frame(self.slotbooking_frame, bg='#F0FFFF', width=700, height=800)
        self.info_frame.place(x=700, y=0)

        # self.label1 = tk.Label(self.info_frame, text="Information page", width=20, height=1, bg='#b5e2ff',
        #                     font=('Helvetica', 35, 'italic'))
        # self.label1.place(x=40, y=70)

        self.info_frame = Frame(self.slotbooking_frame, bg='#F0FFFF', width=700, height=800)
        self.info_frame.place(x=800, y=0)

        self.bg_frame = Frame(self.slotbooking_frame, width=700, height=800)
        self.bg_frame.pack(fill='both', expand=True)
        self.bg_frame.place(x=850, y=0)

        original_image = Image.open('assets\slotbg.png')
        resized_image = original_image.resize((700, 800))
        self.bg_image = ImageTk.PhotoImage(resized_image)

        self.background_label = tk.Label(self.bg_frame, image=self.bg_image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # self.info_frame = Frame(self, bg='#b5e2ff', width=700, height=800)
        # self.info_frame.place(x=900, y=0)

    def book_slot(self):
        messagebox.showinfo("Booking", "Slot booked successfully!")
        self.slotbooking_frame.pack_forget()
        self.create_login_screen()

    #     self.label = tk.Label(self, text="Parking Area", font=("Arial", 50, "bold"))
    #     self.label.pack(pady=20)

    #     # Add buttons for parking slots
    #     for i in range(10):
    #         button = tk.Button(self, text=f"parking NO {i+1}", command=self.book_slot, width=15, height=10,)
    #         button.pack()
    #         button.place(x=30+150*(i%3), y=150+230*(i//3))


        
if __name__ == "__main__":
    app = ParkingSystem()
    app.mainloop()
