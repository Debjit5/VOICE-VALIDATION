from PIL import ImageTk
from tkinter import*
from tkinter import ttk,messagebox
import PIL.Image
import re
import mysql.connector
import pyttsx3



class Register:

    def __init__(self,root):
        self.root=root
        self.root.title('Register Page')
        self.root.geometry('1500x878+0+0')

        #text-to-speech
        self.engine=pyttsx3.init()
        self.voices=self.engine.getProperty('voices')
        self.engine.setProperty('voice',self.voices[1].id)

        #Variable
        self.name_var=StringVar()
        self.email_var=StringVar()
        self.contact_var=StringVar()
        self.gender_var=StringVar()
        self.country_var=StringVar()
        self.id_var=StringVar()
        self.id_no_var=StringVar()
        self.pass_var=StringVar()
        self.confirm_pass=StringVar()
        self.check_var=IntVar()



        #Background Image

        self.bg=ImageTk.PhotoImage(file='bg2.png')
        bg_lbl=Label(self.root,image=self.bg,bd=2,relief='raised')
        bg_lbl.place(x=5,y=10,relheight=1,relwidth=1)

        logo_img=PIL.Image.open('logo.jpg')
        logo_img=logo_img.resize((40,40),PIL.Image.Resampling.LANCZOS)
        self.photo_logo=ImageTk.PhotoImage(logo_img)

        #Title frame

        title_frm=Frame(self.root,bd=1,relief='ridge')
        title_frm.place(x=650,y=60,width=600,height=82)

        title_lbl=Label(title_frm,image=self.photo_logo,compound=LEFT,text='USER REGISTRATION FORM',font=('times new roman',26,'bold'),fg='darkblue')
        title_lbl.place(x=20,y=9)

        #info frame

        main_frame=Frame(self.root,bd=1,relief='ridge')
        main_frame.place(x=650,y=140,width=600,height=720)

        #Label & Entry

        #UserName 
        user_name=Label(main_frame,font=('times new roman',20,'bold'),text="UserName:")
        user_name.grid(row=0,column=0,padx=10,pady=10,sticky=W)

        user_entry=ttk.Entry(main_frame,textvariable=self.name_var,font=('times new roman',20,'bold'),width=20)
        user_entry.grid(row=0,column=1,padx=10,pady=10,sticky=W)
        
        #Validation

        validate_name=self.root.register(self.checkname)
        user_entry.config(validate='key',validatecommand=(validate_name,'%P'))

        #Email
        eml_lbl=Label(main_frame,font=('times new roman',20,'bold'),text="Email:")
        eml_lbl.grid(row=1,column=0,padx=10,pady=10,sticky=W)

        eml_entry=ttk.Entry(main_frame,textvariable=self.email_var,font=('times new roman',20,'bold'),width=20)
        eml_entry.grid(row=1,column=1,padx=10,pady=10,sticky=W)

        #Contact
        contact_lbl=Label(main_frame,font=('times new roman',20,'bold'),text="Contact No:")
        contact_lbl.grid(row=2,column=0,padx=10,pady=10,sticky=W)

        contact_entry=ttk.Entry(main_frame,textvariable=self.contact_var,font=('times new roman',20,'bold'),width=20)
        contact_entry.grid(row=2,column=1,padx=10,pady=10,sticky=W)

        #Validation

        validate_contact=self.root.register(self.checkcontact)
        contact_entry.config(validate='key',validatecommand=(validate_contact,'%P'))

        #Gender
        gender_lbl=Label(main_frame,font=('times new roman',20,'bold'),text="Gender:")
        gender_lbl.grid(row=3,column=0,padx=10,pady=10,sticky=W)

        gender_frame=Frame(main_frame)
        gender_frame.place(x=252,y=190,width=287,height=44)

        radio_male=Radiobutton(gender_frame,variable=self.gender_var,value='Male',text='Male',font=('times new roman',16,'bold'))
        radio_male.grid(row=0,column=0,padx=10,pady=0,sticky=W)
        self.gender_var.set('Male')

        radio_female=Radiobutton(gender_frame,variable=self.gender_var,value='Female',text='Female',font=('times new roman',16,'bold'))
        radio_female.grid(row=0,column=1,padx=10,pady=0,sticky=W)

        select_country=Label(main_frame,font=('times new roman',20,'bold'),text="Select Country:")
        select_country.grid(row=4,column=0,padx=10,pady=10,sticky=W)
         
        lst=['India','UK','Nepal','Afganistan','Pakistan']
        droplist=OptionMenu(main_frame,self.country_var,*lst)
        self.country_var.set('Select Your Country')
        droplist.config(width=30,height=2,bg='white',font=('times new roman',11,'bold'))
        droplist.grid(row=4,column=1,padx=10,pady=10,sticky=W)

        id_type=Label(main_frame,font=('times new roman',20,'bold'),text="Select ID Type:")
        id_type.grid(row=5,column=0,padx=10,pady=10,sticky=W)

        self.combo_id_type=ttk.Combobox(main_frame,textvariable=self.id_var,font=('times new roman',19,'bold'),justify='center',state='readonly',width=20)
        self.combo_id_type["values"]=("Select Your ID","Adhar Card","Passport","Driving Licence")
        self.combo_id_type.grid(row=5,column=1,padx=10,pady=10)
        self.combo_id_type.current(0)

        id_no=Label(main_frame,font=('times new roman',20,'bold'),text="ID Number:")
        id_no.grid(row=6,column=0,padx=10,pady=10,sticky=W)

        id_entry=ttk.Entry(main_frame,textvariable=self.id_no_var,font=('times new roman',20,'bold'),width=20)
        id_entry.grid(row=6,column=1,padx=10,pady=10,sticky=W)

        pass_lbl=Label(main_frame,font=('times new roman',20,'bold'),text="Enter Password:")
        pass_lbl.grid(row=7,column=0,padx=10,pady=10,sticky=W)

        pass_entry=ttk.Entry(main_frame,textvariable=self.pass_var,font=('times new roman',20,'bold'),width=20)
        pass_entry.grid(row=7,column=1,padx=10,pady=10,sticky=W)

        confi_pass=Label(main_frame,font=('times new roman',20,'bold'),text="Confirm Password:")
        confi_pass.grid(row=8,column=0,padx=10,pady=10,sticky=W)

        confi_entry=ttk.Entry(main_frame,textvariable=self.confirm_pass,font=('times new roman',20,'bold'),width=20)
        confi_entry.grid(row=8,column=1,padx=10,pady=10,sticky=W)

        chk_frame=Frame(main_frame)
        chk_frame.place(x=150,y=515,width=400,height=70)

        chk_btn=Checkbutton(chk_frame,variable=self.check_var,font=('times new roman',16,'bold'),text='Agree Our terms & Conditions',onvalue=1,offvalue=0)
        chk_btn.grid(row=0,column=0,padx=10,sticky=W)

        self.chk_lbl=Label(chk_frame,text='',font=('times new roman',14,'bold'),fg='red')
        self.chk_lbl.grid(row=1,column=0,padx=10,sticky=W)

        btn_frame=Frame(main_frame)
        btn_frame.place(x=30,y=595,width=550,height=70)

        save_data=Button(btn_frame,command=self.validations,font=('times new roman',20,'bold'),width=8,cursor='hand2',text='Save',bg='green',fg='white')
        save_data.grid(row=0,column=0,padx=1,sticky=W)

        verify_data=Button(btn_frame,command=self.verify_data,font=('times new roman',20,'bold'),width=8,cursor='hand2',text='Verify',bg='blue',fg='white')
        verify_data.grid(row=0,column=1,padx=63,sticky=W)

        clear_data=Button(btn_frame,command=self.clear_data,font=('times new roman',20,'bold'),width=8,cursor='hand2',text='Clear',bg='red',fg='white')
        clear_data.grid(row=0,column=2,padx=1,sticky=W)

    # callback Func
    def checkname(self,name):
        if name.isalnum():
            return True
        if name=='':
            return True
        else:
            messagebox.showerror('Invalid','Not Allowed'+name[-1])
            return False
        
    def checkcontact(self,contact):
        if contact.isdigit():
            return True
        if len(str(contact))==0:
            return True
        else:
            self.engine.say('Please Enter Valid Contact')
            self.engine.runAndWait()
            messagebox.showerror("invalid","Invalid Entry")
            return False
        
    def checkpassword(self,password):
        if len(password)<=21:
            if re.match("^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z](?=.*[^a-bA-B0-9]))",password):
                return True
            else:
                self.engine.say('Enter Valid Password(Example:Debu@123)')
                self.engine.runAndWait()
                messagebox.showinfo('invalid','Enter valid Password(Example:Deb@123)')
                return False
        else:
            messagebox.showerror('invalid','Length try to exceed')
            return False

    def checkmail(self,email):
        if len(email)>7:
            if re.match("^([a-zA-z0-9_\-\.]+)@([a-zA-z0-9_\-\.]+)\.([a-zA-Z]{2,5})$",email):
                return True
            else:
                self.engine.say('Invalid Email Enter Valid User Email(example:Debu@gamil.com)')
                self.engine.runAndWait()
                messagebox.showwarning('Alert','invalid email (abc@11gmail.com)')
                return False
        else:
            self.engine.say('Email length is too small')
            self.engine.runAndWait()
            messagebox.showinfo('invalid','Email length is too small')
    
    #Validations

    def validations(self):
        if self.name_var.get()=='':
            self.engine.say('Please Enter Your Name')
            self.engine.runAndWait()
            messagebox.showerror('Error','Please Enter your name',parent=self.root)
        
        elif self.email_var.get()=='':
            self.engine.say('Please Enter your Emailid')
            self.engine.runAndWait()
            messagebox.showerror('Error','Please Enter your Emailid',parent=self.root)

        elif self.contact_var.get()=='' or len(self.contact_var.get())!=10:
            self.engine.say('Please Enter your Valid Contact')
            self.engine.runAndWait()
            messagebox.showerror('Error','Please Enter your Valid Contact',parent=self.root)
        
        elif self.gender_var.get()=='':
            self.engine.say('Please Choose your Gender')
            self.engine.runAndWait()
            messagebox.showerror('Error','Please Choose your Gender',parent=self.root)
        
        elif self.country_var.get()=='' or self.country_var.get()=='Select your country':
            self.engine.say('Please Choose your Country')
            self.engine.runAndWait()
            messagebox.showerror('Error','Please Choose your Country',parent=self.root)
        
        elif self.id_var.get()=='Select Your ID':
            self.engine.say('Please Enter your ID')
            self.engine.runAndWait()
            messagebox.showerror('Error','Please Enter your ID',parent=self.root)
        
        elif self.id_no_var.get()=='':
            self.engine.say('Please enter your ID No')
            self.engine.runAndWait()
            messagebox.showerror('Error','Please enter your ID No',parent=self.root)
        
        elif len(self.id_no_var.get())!=14:
            self.engine.say('Please enter 14 Digit')
            self.engine.runAndWait()
            messagebox.showerror('Error','Please enter 14 Digit',parent=self.root)

        elif self.pass_var.get()=='':
            self.engine.say('Please Enter your Password')
            self.engine.runAndWait()
            messagebox.showerror('Error','Please Enter your Password',parent=self.root)

        elif self.confirm_pass.get()=='':
            self.engine.say('Please Confirm your Password')
            self.engine.runAndWait()
            messagebox.showerror('Error','Please Confirm your Password',parent=self.root)

        elif self.pass_var.get()!=self.confirm_pass.get():
            self.engine.say('Password & Confirm Password must be same')
            self.engine.runAndWait()
            messagebox.showerror('Error','Password & Confirm Password must be same',parent=self.root)

        elif self.email_var.get()!=None and self.pass_var.get()!=None:
            x=self.checkmail(self.email_var.get())
            y=self.checkpassword(self.pass_var.get())

        if (x==True) and (y==True):
            if self.check_var.get()==0:
                self.engine.say('Please Agree Our Terms')
                self.engine.runAndWait()
                self.chk_lbl.config(text='Please Agree Our Terms',fg='red')
            else:
                self.chk_lbl.config(text='Checked',fg='green')

                try:
                    conn=mysql.connector.connect(host='localhost',username='root',password='DebjitDatabase@4081002',database='voice_project')
                    my_cursur=conn.cursor()
                    my_cursur.execute('insert into register values(%s,%s,%s,%s,%s,%s,%s,%s)',(self.name_var.get(),self.email_var.get(),self.contact_var.get(),self.gender_var.get(),self.country_var.get(),self.id_var.get(),self.id_no_var.get(),self.pass_var.get()))
                    conn.commit()
                    conn.close()

                except Exception as es:
                    messagebox.showerror('Error',f'Due to:{str(es)}',parent=self.root)

                messagebox.showinfo('Successful',f'Your Registration Successfully Completed.\nYour Username:{self.name_var.get()} \n Password:{self.pass_var.get()}')
    
    def verify_data(self):
        data=f"Name:{self.name_var.get()}\nEmail:{self.email_var.get()}\nContact:{self.contact_var.get()}\nGender:{self.gender_var.get()}\nID Type:{self.id_var.get()}\nID No:{self.id_no_var.get()}\nCountry:{self.country_var.get()}\nPassword:{self.pass_var.get()}"
        messagebox.showinfo('Details',data)
    
    def clear_data(self):
        self.name_var.set('')
        self.email_var.set('')
        self.contact_var.set('')
        self.gender_var.set('Male')
        self.country_var.set('Select Your Country')
        self.id_var.set('Select Your ID')
        self.id_no_var.set('')
        self.pass_var.set('')
        self.confirm_pass.set('')
        self.check_var.set(0)

if __name__=='__main__':
    root=Tk()
    obj=Register(root)
    root.mainloop()