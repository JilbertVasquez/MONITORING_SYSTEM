from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import pymysql
import os
import platform
import psutil
import cpuinfo
import wmi
import csv
from datetime import date
from datetime import datetime


class MS:
    def __init__(self,root):
        self.root=root
        self.root.title("Monitoring System")
        self.root.geometry("1366x700+0+0")
        
        self.root.resizable(False,False)
        self.container()


    def container(self):
        Frame_AI = Frame(self.root)
        Frame_AI.place(x = 0, y = 0, height = 1000, width = 1800)
        self.img = ImageTk.PhotoImage(file = "background.png")
        img = Label(self.root, image = self.img)
        img.place(x = -1000, y = -1000)
        
        
        student_frame = Frame(self.root, bg = "#AA336A")
        student_frame.place(x = 390, y = 130, height = 450, width = 600)
        
        MS_label = Label(student_frame,text="Monitoring System",font=("impact", 32, "bold"), fg = "white", bg = "#AA336A")
        MS_label.place(x = 120,y = 20)
        
        
        admin_button = Button(student_frame, text = "Admin",command=self.Admin, cursor="hand2", font = ("times new roman",12), fg = "white", bg="#00008B", bd = 0, width = 5, height = 1)
        admin_button.place(x = 40,y = 80)
        
        sr_code_label = Label(student_frame, text="SR-CODE: ", font = ("times new roman",12), fg = "white", bg = "#AA336A")
        sr_code_label.place(x = 80, y = 130)
        
        self.sr_code_entry = Entry(student_frame, font=("times new roman",12,"bold"),bg='lightgray')
        self.sr_code_entry.place(x=220,y=130,width=250,height=25)
        
        name_label = Label(student_frame, text="STUDENT NAME: ", font = ("times new roman",12), fg = "white", bg = "#AA336A")
        name_label.place(x = 80, y = 180)
        
        self.name_entry = Entry(student_frame, font=("times new roman",12,"bold"),bg='lightgray')
        self.name_entry.place(x=220,y=180,width=250,height=25)
        
        section_label = Label(student_frame, text="SECTION: ", font = ("times new roman",12), fg = "white", bg = "#AA336A")
        section_label.place(x = 80, y = 230)
        
        self.section_entry = Entry(student_frame, font=("times new roman",12,"bold"),bg='lightgray')
        self.section_entry.place(x=220,y=230,width=250,height=25)
        
        prof_label = Label(student_frame, text="PROFESSOR: ", font = ("times new roman",12), fg = "white", bg = "#AA336A")
        prof_label.place(x = 80, y = 280)
        
        self.prof_entry = Entry(student_frame, font=("times new roman",12,"bold"),bg='lightgray')
        self.prof_entry.place(x=220,y=280,width=250,height=25)
        
        
        login_button = Button(student_frame, text = "LOGIN", command = self.CheckBoxID, cursor = "hand2", font = ("times new roman",12), fg = "white", bg = "#00008B", bd = 0, width = 20, height = 1)
        login_button.place(x = 190, y = 350)
        
        
    def Admin(self):
        admin_frame = Frame(self.root, bg = "black")
        admin_frame.place(x = 390, y = 130, height = 450, width = 600)
        
        label1 = Label(admin_frame,text="Monitoring System",font=("impact", 32, "bold"), fg = "white", bg = "black")
        label1.place(x = 120,y = 20)
        
        student_button = Button(admin_frame, text = "Student",command=self.container, cursor="hand2", font = ("times new roman",12), fg = "white", bg="#00008B", bd = 0, width = 5, height = 1)
        student_button.place(x = 40,y = 80)
        
        
        username_label = Label(admin_frame, text="USERNAME: ", font = ("times new roman",12), fg = "white", bg = "black")
        username_label.place(x = 80, y = 180)
        
        self.username_entry = Entry(admin_frame, font=("times new roman",12,"bold"),bg='lightgray')
        self.username_entry.place(x=220,y=180,width=250,height=25)
        
        self.password_label = Label(admin_frame, text="PASSWORD: ", font = ("times new roman",12), fg = "white", bg = "black")
        self.password_label.place(x = 80, y = 230)
        
        self.password_entry = Entry(admin_frame, font=("times new roman",12,"bold"),bg='lightgray')
        self.password_entry.place(x=220,y=230,width=250,height=25)
        
        login_button = Button(admin_frame, text = "LOGIN", command=self.Login, cursor = "hand2", font = ("times new roman",12), fg = "white", bg = "#00008B", bd = 0, width = 20, height = 1)
        login_button.place(x = 190, y = 350)
        
        
    def Login(self):
        try:
            username1 = self.username_entry.get()
            password1 = self.password_entry.get()
            con = pymysql.connect(host="localhost",user="root",password="root", database="AdminDB")
            cur = con.cursor()
            cur.execute("select * from admins where username=%s" , username1)
            
            uname = cur.fetchone()
            
            cur2 = con.cursor()
            cur2.execute("select * from admins where password=%s", password1)
            
            pword = cur2.fetchone()
            
            if uname == None or pword == None:
                messagebox.showinfo("Error" , "No Admin with " + username1 + " username found.")
                
            else:
                messagebox.showinfo("Successful", "Login In Successful.")
                self.HardwareInfo()
                
        except Exception as es:
            messagebox.showerror("Error",f"Error due to:{str(es)}" ,parent=self.root)
        
        
    def HardwareInformation(self):
        self.node = platform.node()
        self.system = platform.system()
        self.release = platform.release()
        self.version = platform.version()
        self.memory = round((psutil.virtual_memory().total / 1024 / 1024 / 1024), 2)
        self.memory2 = round(self.memory+0.5)
        self.memory3 = "%.2f" % self.memory2
        self.memory4 = str(self.memory) + " GB (" + str(self.memory3) + " GB)"
        
        pc = wmi.WMI()
        os_info = pc.Win32_OperatingSystem()[0]
        self.caption = os_info.Caption
        self.osbit = os_info.OSArchitecture + " operating system"
        self.processor_name = pc.Win32_processor()[0].Name
        self.gpu = pc.Win32_VideoController()[0].Name
        
        
    def HardwareInfo(self):
        info_frame = Frame(self.root, bg = "black")
        info_frame.place(x = 25, y = 25, height = 650, width = 1310)
        
        self.img2 = ImageTk.PhotoImage(file = "background.png")
        img2 = Label(info_frame, image = self.img)
        img2.place(x = -1025, y = -1025)
        
        hardware_info_button = Button(info_frame, text = "Hardware Information", command=self, cursor = "hand2", font = ("times new roman",12), fg = "white", bg = "#00008B", bd = 0, width = 20, height = 1)
        hardware_info_button.place(x = 10, y = 5)
        
        hardware_devices = Button(info_frame, text = "Hardware Devices", command=self.HardwareDevices, cursor = "hand2", font = ("times new roman",12), fg = "white", bg = "#00008B", bd = 0, width = 20, height = 1)
        hardware_devices.place(x = 200, y = 5)
        
        hardware_info_frame = Frame(info_frame, bg = "black")
        hardware_info_frame.place(x = 0, y = 40, height = 600, width = 1310)
        
        self.img3 = ImageTk.PhotoImage(file = "background.png")
        img3 = Label(hardware_info_frame, image = self.img)
        img3.place(x = -1025, y = -1065)
        
        self.HardwareInformation()
        
        device_name = Label(hardware_info_frame, text = "DEVICE NAME: ", font = ("times new roman",12), fg = "white", bg = "black")
        device_name.place(x = 450, y = 210)
        
        device_name2 = Label(hardware_info_frame, text = self.node, font = ("times new roman",12), fg = "white", bg = "black")
        device_name2.place(x = 700, y = 210)
        
        system_label = Label(hardware_info_frame, text = "SYSTEM: ", font = ("times new roman",12), fg = "white", bg = "black")
        system_label.place(x = 450, y = 240)
        
        system_label2 = Label(hardware_info_frame, text = self.system, font = ("times new roman",12), fg = "white", bg = "black")
        system_label2.place(x = 700, y = 240)
        
        release_label = Label(hardware_info_frame, text = "SYSTEM RELEASE: ", font = ("times new roman",12), fg = "white", bg = "black")
        release_label.place(x = 450, y = 270)
        
        release_label2 = Label(hardware_info_frame, text = self.release, font = ("times new roman",12), fg = "white", bg = "black")
        release_label2.place(x = 700, y = 270)
        
        version_label = Label(hardware_info_frame, text = "SYSTEM RELEASE", font = ("times new roman",12), fg = "white", bg = "black")
        version_label.place(x = 450, y = 300)
        
        version_label2 = Label(hardware_info_frame, text = self.version, font = ("times new roman",12), fg = "white", bg = "black")
        version_label2.place(x = 700, y = 300)
        
        memory_label = Label(hardware_info_frame, text = "INSTALLED MEMORY: ", font = ("times new roman",12), fg = "white", bg = "black")
        memory_label.place(x = 450, y = 330)
        
        memory_label2 = Label(hardware_info_frame, text = self.memory4, font = ("times new roman",12), fg = "white", bg = "black")
        memory_label2.place(x = 700, y = 330)
        
        edition_label = Label(hardware_info_frame, text = "EDITION: ", font = ("times new roman",12), fg = "white", bg = "black")
        edition_label.place(x = 450, y = 360)
        
        edition_label2 = Label(hardware_info_frame, text = self.caption, font = ("times new roman",12), fg = "white", bg = "black")
        edition_label2.place(x = 700, y = 360)
        
        system_type_label = Label(hardware_info_frame, text = "SYSTEM TYPE: ", font = ("times new roman",12), fg = "white", bg = "black")
        system_type_label.place(x = 450, y = 390)
        
        system_type_label2 = Label(hardware_info_frame, text = self.osbit, font = ("times new roman",12), fg = "white", bg = "black")
        system_type_label2.place(x = 700, y = 390)
        
        processor_label = Label(hardware_info_frame, text = "PROCESSOR", font = ("times new roman",12), fg = "white", bg = "black")
        processor_label.place(x = 450, y = 420)
        
        processor_label2 = Label(hardware_info_frame, text = self.processor_name, font = ("times new roman",12), fg = "white", bg = "black")
        processor_label2.place(x = 700, y = 420)
        
        gpu_label = Label(hardware_info_frame, text = "GPU", font = ("times new roman",12), fg = "white", bg = "black")
        gpu_label.place(x = 450, y = 450)
        
        gpu_label2 = Label(hardware_info_frame, text = self.gpu, font = ("times new roman",12), fg = "white", bg = "black")
        gpu_label2.place(x = 700, y = 450)
        
        
    def HardwareDevices(self):
        info_frame = Frame(self.root, bg = "black")
        info_frame.place(x = 25, y = 25, height = 650, width = 1310)
        
        self.img4 = ImageTk.PhotoImage(file = "background.png")
        img4 = Label(info_frame, image = self.img)
        img4.place(x = -1025, y = -1025)
        
        hardware_info_button = Button(info_frame, text = "Hardware Information", command=self.HardwareInfo, cursor = "hand2", font = ("times new roman",12), fg = "white", bg = "#00008B", bd = 0, width = 20, height = 1)
        hardware_info_button.place(x = 10, y = 5)
        
        hardware_devices = Button(info_frame, text = "Hardware Devices", command=self, cursor = "hand2", font = ("times new roman",12), fg = "white", bg = "#00008B", bd = 0, width = 20, height = 1)
        hardware_devices.place(x = 200, y = 5)
        
        hardware_device_frame = Frame(info_frame, bg = "black")
        hardware_device_frame.place(x = 0, y = 40, height = 600, width = 1310)
        
        self.img5 = ImageTk.PhotoImage(file = "background.png")
        img5 = Label(hardware_device_frame, image = self.img)
        img5.place(x = -1025, y = -1065)
        
        
        monitor_label = Label(hardware_device_frame, text = "MONITOR ID: ", font = ("times new roman",12), fg = "white", bg = "black")
        monitor_label.place(x = 450, y = 240)
        
        self.monitor_entry = Entry(hardware_device_frame, font=("times new roman",12,"bold"),bg='lightgray')
        self.monitor_entry.place(x = 650, y = 240,width=250,height=25)
        
        keyboard_label = Label(hardware_device_frame, text = "KEYBOARD ID", font = ("times new roman",12), fg = "white", bg = "black")
        keyboard_label.place(x = 450, y = 300)
        
        self.keyboard_entry = Entry(hardware_device_frame, font=("times new roman",12,"bold"),bg='lightgray')
        self.keyboard_entry.place(x = 650, y = 300,width=250,height=25)
        
        mouse_label = Label(hardware_device_frame, text = "MOUSE ID: ", font = ("times new roman",12), fg = "white", bg = "black")
        mouse_label.place(x = 450, y = 360)
        
        self.mouse_entry = Entry(hardware_device_frame, font=("times new roman",12,"bold"),bg='lightgray')
        self.mouse_entry.place(x = 650, y = 360,width=250,height=25)
        
        
        device_manager = Button(hardware_device_frame, text = "DEVICE MANAGER", command = self.DeviceManager, cursor = "hand2", font = ("times new roman",12), fg = "white", bg = "#00008B", bd = 0, width = 20, height = 1)
        device_manager.place(x = 425, y = 500)
        
        save_id = Button(hardware_device_frame, text = "SAVE IDS", command = self.SaveID, cursor = "hand2", font = ("times new roman",12), fg = "white", bg = "#00008B", bd = 0, width = 20, height = 1)
        save_id.place(x = 725, y = 500)
        
    
    def SaveID(self):    
        try:
            monitor1 = self.monitor_entry.get()
            keyboard1 = self.keyboard_entry.get()
            mouse1 = self.mouse_entry.get()
            con = pymysql.connect(host="localhost",user="root",password="root", database="AdminDB")
            cur = con.cursor()
            cur.execute("select * from admins where username=%s" , monitor1)
            
            monitor2 = cur.fetchone()
            
            cur2 = con.cursor()
            cur2.execute("select * from admins where password=%s", keyboard1)
            
            keyboard2 = cur2.fetchone()
            
            cur3 = con.cursor()
            cur3.execute("select * from admins where password=%s", mouse1)
            
            mouse2 = cur3.fetchone()
            
            if monitor2 == None or keyboard2 == None or mouse2 == None:
                cur.execute("DROP TABLE ids")
                cur.execute("CREATE TABLE ids (id int not null auto_increment, monitor varchar(255), keyboard varchar(255), mouse varchar(255), primary key (id));")
                cur.execute("INSERT INTO ids(monitor, keyboard, mouse) VALUES (%s, %s, %s)", (monitor1, keyboard1, mouse1))
                con.commit()
                messagebox.showinfo("Successful", "IDs Save Successfully.")
                
            else:
                cur.execute("UPDATE ids SET monitor = %s, keyboard = %s, mouse = %s WHERE id = 1", (monitor1, keyboard1, mouse1))
                con.commit()
                messagebox.showinfo("Successful", "IDs Save Successfully.")
                
        except Exception as es:
            messagebox.showerror("Error",f"Error due to:{str(es)}" ,parent=self.root)
        
        
    def DeviceManager(self):
        os.system("devmgmt.msc")
        
        
    def CheckBoxID(self):
        self.sr_code = self.sr_code_entry.get()
        self.name = self.name_entry.get()
        self.section = self.section_entry.get()
        self.prof = self.prof_entry.get()
        
        today = date.today()
        date_today = today.strftime("%D")
        now = datetime.now()
        time_now = now.strftime("%H:%M")
        
        self.temp = []
        self.temp.append(self.sr_code)
        self.temp.append(self.name)
        self.temp.append(self.section)
        self.temp.append(self.prof)
        self.temp.append(date_today)
        self.temp.append(time_now)
        
        if self.sr_code == "" or self.name == "" or self.section == "" or self.prof == "":
            messagebox.showerror("Error","All Fields Are Required",parent=self.root)
        else:
            messagebox.showinfo("Successful","Please check if the computer have the following devices:",parent=self.root)
        
            admin_frame = Frame(self.root, bg = "#AA336A")
            admin_frame.place(x = 390, y = 130, height = 450, width = 600)
            
            label1 = Label(admin_frame,text="Monitoring System",font=("impact", 32, "bold"), fg = "white", bg = "#AA336A")
            label1.place(x = 120,y = 20)
            
            self.monitor_var = IntVar()
            self.keyboard_var = IntVar()
            self.mouse_var = IntVar()
            
            self.monitor_button = Checkbutton(admin_frame, text='',variable= self.monitor_var, onvalue=1, offvalue=0, bg = "#AA336A")
            self.monitor_button.place(x = 220, y = 180)
            
            monitor_label = Label(admin_frame, text="MONITOR ", font = ("times new roman",12), fg = "white", bg = "#AA336A")
            monitor_label.place(x = 280, y = 180)
            
            keyboard_button = Checkbutton(admin_frame, text='',variable= self.keyboard_var, onvalue=1, offvalue=0, bg = "#AA336A")
            keyboard_button.place(x = 220, y = 230)
            
            keyboard_label = Label(admin_frame, text="KEYBOARD ", font = ("times new roman",12), fg = "white", bg = "#AA336A")
            keyboard_label.place(x = 280, y = 230)
            
            self.mouse_button = Checkbutton(admin_frame, text='',variable= self.mouse_var, onvalue=1, offvalue=0, bg = "#AA336A")
            self.mouse_button.place(x = 220, y = 280)
            
            mouse_label = Label(admin_frame, text="MOUSE ", font = ("times new roman",12), fg = "white", bg = "#AA336A")
            mouse_label.place(x = 280, y = 280)
            
            login_button = Button(admin_frame, text = "SAVE", command=self.SaveStudentInfo, cursor = "hand2", font = ("times new roman",12), fg = "white", bg = "#00008B", bd = 0, width = 20, height = 1)
            login_button.place(x = 190, y = 350)
            
            
            try:
                con = pymysql.connect(host="localhost",user="root",password="root", database="AdminDB")
                cur = con.cursor()
                cur.execute("select monitor, keyboard, mouse from ids")
                
                self.hardware_ids = cur.fetchall()
                self.list_ids = list(self.hardware_ids)[0]
                self.id1 = self.list_ids[0]
                self.id2= self.list_ids[1]
                self.id3 = self.list_ids[2]
                
            except Exception as es:
                messagebox.showerror("Error",f"Error due to:{str(es)}" ,parent=self.root)
            
            
            self.temp2 = []
        
        
    def SaveStudentInfo(self):
        
        self.HardwareInformation()
        
        self.temp.append(self.node)
        self.temp.append(self.system)
        self.temp.append(self.release)
        self.temp.append(self.version)
        self.temp.append(self.memory)
        self.temp.append(self.memory3)
        self.temp.append(self.caption)
        self.temp.append(self.osbit)
        self.temp.append(self.processor_name)
        self.temp.append(self.gpu)
        
        if self.monitor_var.get() == 1:
                self.temp2.append(self.id1)
        else:
            self.temp2.append("None")
            
        if self.keyboard_var.get() == 1:
            self.temp2.append(self.id2)
        else:
            self.temp2.append("None")
            
        if self.mouse_var.get() == 1:
            self.temp2.append(self.id3)
        else:
            self.temp2.append("None")
        
        ids1, ids2, ids3 = self.temp2
        
        self.temp.append(ids1)
        self.temp.append(ids2)
        self.temp.append(ids3)
        
        file_dir = os.getcwd() + "\Monitoring_System_Data.csv"
        flag = os.path.exists(file_dir)
        
        if flag:
            file = open("Monitoring_System_Data.csv", "a", newline="")
            writer = csv.writer(file)
            writer.writerow(self.temp)
            file.close()
            messagebox.showinfo("Successful","Informations Saved. Thank you",parent=self.root)
            root.destroy()
        else:
            headers = ["SR-CODE", "Student Name", "Section", "Professor", "Date", "Time" , "Device Name", "System", "System Release", "System Version", "Installed Memory", "Installed Memory (RAM)", "Edition", "System Type", "Processor", "GPU", "Monitor ID", "Keyboard ID", "Mouse ID"]
            with open ("Monitoring_System_Data.csv", "w", newline="") as wrt:
                writer2 = csv.writer(wrt)
                writer2.writerow(headers)
                writer2.writerow(self.temp)
                messagebox.showinfo("Successful","Informations Saved. Thank you",parent=self.root)
                root.destroy()


root = Tk()
ob = MS(root)
root.mainloop()