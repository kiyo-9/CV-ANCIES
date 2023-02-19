from tkinter import *
from PIL import Image, ImageTk
from tkinter.font import Font
from tkinter import messagebox
import tkinter as tk
import sqlite3

white = "#CBD8ED"
bgblue = "#4A78A9"
dblue = "#98C1D9"
cblue = "#213A5C"

main = Tk()
main.minsize(1100, 710)
main.maxsize(1100, 710)
main.title("CV-ANCIES")
main.iconbitmap('logo..ico')
main.config(bg="#4A78A9")


# button commands---------------------------------------------
def exit_all():
    main.destroy()


def home():
    main.destroy()
    import login

def show_cv():
    main.destroy()
    import cvtemp


# fonts-------------------------------------------------------
my_font0 = Font(
    family='Lucida sans',
    size=11,
    weight='bold',
    slant='roman',
    overstrike=0)

my_font = Font(
    family='Lucida sans',
    size=13,
    weight='bold',
    slant='roman',
    overstrike=0)

my_font1 = Font(
    family='Lucida sans',
    size=15,
    weight='bold',
    slant='roman',
    overstrike=0)
my_font2 = Font(
    family='Lucida sans',
    size=25,
    weight='bold',
    slant='roman',
    overstrike=0)
my_font3 = Font(
    family='Lucida sans',
    size=14,
    weight='bold',
    slant='roman',
    overstrike=0)

my_font4 = Font(
    family='Lucida sans',
    size=20,
    weight='bold',
    slant='roman',
    overstrike=0)


def about_p():
    abt = Frame(main, bg="black", borderwidth=2)
    abt.place(x=230, y=47)
    for_place = Label(abt, text="REGISTER", font=my_font, padx=655, pady=700, bg="#2B2828", fg="#2B2828")
    for_place.grid()
    my_font5 = Font(
        family='Lucida sans',
        size=60,
        weight='bold',
        slant='roman',
        overstrike=0)
    Label(abt, text="KASP", font=my_font5, bg="#2B2828", fg="#3D5A80").place(x=130, y=15)
    i1 = Image.open('abt.png')
    i2 = i1.resize((490, 525))
    i3 = ImageTk.PhotoImage(i2)
    i4 = Label(abt, image=i3, bg="#2B2828")
    i4.image = i3
    i4.place(x=10, y=105)
    img = Image.open('lg.png')
    img1 = img.resize((390, 310))
    logo = ImageTk.PhotoImage(img1)
    logo5 = Label(abt, image=logo, bg="#2B2828")
    logo5.image = logo
    logo5.place(x=480, y=20)


# logo--------------------------------------------------
img = Image.open('lg.png')
img1 = img.resize((220, 180))
logo = ImageTk.PhotoImage(img1)

img2 = Image.open('help.png')
img3 = img2.resize((30, 30))
help_ico = ImageTk.PhotoImage(img3)

img4 = Image.open('settings.png')
img5 = img4.resize((30, 30))
settings_ico = ImageTk.PhotoImage(img5)

# bar frame-------------------------------------------
bar = Frame(main, bg="white", borderwidth=1)
bar.grid(sticky=W)
random = Label(bar, text='hello', fg="black", bg="black", pady=380, padx=97).grid()

# inserting logo------------------------------------------
logo1 = Label(bar, image=logo, bg="black").place(y=25)

# buttons--------------------------------------------
home_btn = Button(bar, text="HOME", bg="#213A5C", fg="white", padx=80.4, font=my_font, pady=4,
                  command=lambda: indicate(home_indicate, home))
home_btn.place(y=240, x=0)

about_btn = Button(bar, text="ABOUT", bg=cblue, fg="white", padx=76, pady=4, font=my_font,
                   command=lambda: indicate(about_indicate, about_p))
about_btn.place(y=285, x=0)

cv_btn = Button(bar, text="CV FORM", bg=cblue, fg="white", padx=66.5, font=my_font, pady=4,
                command=lambda: indicate(cv_indicate, cv_page))
cv_btn.place(y=330, x=0)

vacancy_btn = Button(bar, text="VACANCY FORM", bg=cblue, fg="white", padx=38.5, font=my_font, pady=4, state=DISABLED)
vacancy_btn.place(y=375, x=0)

profile_btn = Button(bar, text="PROFILE", bg=cblue, fg="white", padx=69.3, font=my_font, pady=4, state=DISABLED,
                     command=lambda: indicate(profile_indicate))
profile_btn.place(y=420, x=0)

exit_btn = Button(bar, text="EXIT", bg=cblue, fg="white", padx=87, font=my_font, pady=4, command=exit_all)
exit_btn.place(y=465, x=0)

show_btn = Button(bar, text="SHOW CV", bg=cblue, fg="white", padx=64.4, font=my_font, pady=4, command=show_cv)
show_btn.place(y=510, x=0)

# top bar--------------------------------------------------
cvbar = Frame(main, bg="white", borderwidth=1)
cvbar.place(x=225, y=0)
spa = Label(cvbar, text="hello", bg="black", fg="black", padx=530, pady=10).grid()

help_btn = Button(main, image=help_ico, bg="white").place(x=1020, y=2)
settings_btn = Button(main, image=settings_ico, bg="white").place(x=1060, y=2)

# indicators------------------------------------------------
# indicate_buttons
home_indicate = tk.Label(bar, text=' ', bg="#fCA311")
home_indicate.place(x=0, y=240, width=5, height=37)

about_indicate = tk.Label(bar, text=' ', bg="#fCA311")
about_indicate.place(x=0, y=285, width=5, height=37)

cv_indicate = tk.Label(bar, text=' ', bg="#fCA311")
cv_indicate.place(x=0, y=330, width=5, height=37)

vacancy_indicate = tk.Label(bar, text=' ', bg="#fCA311")
vacancy_indicate.place(x=0, y=375, width=5, height=37)

profile_indicate = tk.Label(bar, text=' ', bg="#fCA311")
profile_indicate.place(x=0, y=420, width=5, height=37)

exit_indicate = tk.Label(bar, text=' ', bg="#fCA311")
exit_indicate.place(x=0, y=465, width=5, height=37)

show_indicate = tk.Label(bar, text=' ', bg="#fCA311")
show_indicate.place(x=0, y=510, width=5, height=37)
#create database_______
def cv_datab():
    try:
        log = sqlite3.connect('cv_detail.db')
        log1 = log.cursor()
        log1.execute("""CREATE TABLE cv_placement(
                
                User_ID PRIMARY KEY,
                f_name text,
                Field_of_job text,
                contact number,
                email1 varchar,
                address1 varchar,
                aboutMe text,
                extra_skill1 text,
                extra_skill2 text,
                yearsOf_expereience1 number,
                about_experience text,
                proficient_Language1 text,
                proficient_Language2 text,
                qualification1 varchar,
                qualification2 varchar,
                reference text,
                anything_else1 varchar
               )
           """)
        log.commit()
        log.close()

    except:
        pass


# hide_function-------
def hide_indicators(lb):
    home_indicate.config(bg="#fCA311")
    about_indicate.config(bg="#fCA311")
    cv_indicate.config(bg="#fCA311")
    vacancy_indicate.config(bg="#fCA311")
    profile_indicate.config(bg="#fCA311")
    exit_indicate.config(bg="#fCA311")


# indicate_function---------------
def indicate(lb, page):
    hide_indicators(lb)
    lb.config(bg='#91ffff')
    page()


def update():
        log = sqlite3.connect('cv_detail.db')
        log1 = log.cursor()
        log1.execute("""UPDATE cv_placement SET 
        f_name =:f_name ,
        Field_of_job=:Field_of_job,
        contact =:contact,
        email1 =:email1,
        address1 =:address1,
        aboutMe =:aboutMe,
        extra_skill1 =:extra_skill1,
        extra_skill2 =:extra_skill2,
        yearsOf_expereience1 =:yearsOf_expereience1,
        about_experience =:about_experience,
        proficient_Language1 =:proficient_Language1,
        proficient_Language2=:proficient_Language2,
        qualification1 =:qualification1,
        qualification2 =:qualification2,
        reference =:reference,
        anything_else1 =:anything_else1
        WHERE User_Id =:User_Id""",
        {
            'f_name': Fname_ent_next.get(),
            'Field_of_job': Field_of_job_ent_next.get(),
            'contact': contact_ent_next.get(),
            'email1': email1_ent_next.get(),
            'address1': address1_ent_next.get(),
            'aboutMe': aboutMe_ent_next.get(),
            'extra_skill1': extra_skill1_ent_next.get(),
            'extra_skill2': extra_skill2_ent_next.get(),
            'yearsOf_expereience1': yearsOf_expereience1_ent_next.get(),
            'about_experience': about_experience_ent_next.get(),
            'proficient_Language1': proficient_Language1_ent_next.get(),
            'proficient_Language2': proficient_Language2_ent_next.get(),
            'qualification1': qualification1_ent_next.get(),
            'qualification2': qualification2_ent_next.get(),
            'reference': reference_ent_next.get(),
            'anything_else1': anything_else1_ent_next.get(),
            'User_Id':oid
        })
        log.commit()
        log.close()
        # clear entries
        Fname_ent_next.delete(0, END)
        Field_of_job_ent_next.delete(0, END)
        contact_ent_next.delete(0, END)
        email1_ent_next.delete(0, END)
        address1_ent_next.delete(0, END)
        aboutMe_ent_next.delete(0, END)
        extra_skill1_ent_next.delete(0, END)
        extra_skill2_ent_next.delete(0, END)
        yearsOf_expereience1_ent_next.delete(0, END)
        about_experience_ent_next.delete(0, END)
        proficient_Language1_ent_next.delete(0, END)
        proficient_Language2_ent_next.delete(0, END)
        qualification1_ent_next.delete(0, END)
        qualification2_ent_next.delete(0, END)
        reference_ent_next.delete(0, END)
        anything_else1_ent_next.delete(0, END)
        next.destroy()


#fet_function----------------------------------------
def fet():
    global oid
    oid=id_entry.get()
    id_entry.delete(0,END)
    # Connect to the database
    conn = sqlite3.connect("cv_detail.db")
    c=conn.cursor()
    # Retrieve the CV information
    c.execute("SELECT * FROM cv_placement WHERE User_Id = ?", (oid,))
    global records
    records=c.fetchall()
    i=len(records)-1
    c.execute("SELECT User_Id FROM cv_placement")
    # compares value if it is empty-----------
    if oid=="" or oid=="Insert User_Id":
        messagebox.showerror("ERROR",'Please enter your User_Id')
        return
    # compares value if its filled-------
    elif(oid!=""):
        while i >= 0:
            if records[i][0]==oid:
                i=i-1
                print(records[i][0])
                global next
                next = Tk()
                next.minsize(1100, 710)
                next.maxsize(1100, 710)
                next.title("CV-ANCIES")
                next.iconbitmap('logo..ico')
                next.config(bg="#3D5A80")

                cv_ttl_next = tk.Label(next, text="CV ENTRIES", font=my_font4, fg="white", bg="#3D5A80")
                cv_ttl_next.place(x=20, y=40)
                cv_ttl2_next = tk.Label(next, text="Please enter the following data", font=my_font0, fg="white", bg="#3D5A80")
                cv_ttl2_next.place(x=20, y=85)


                global Fname_ent_next
                global Field_of_job_ent_next
                global contact_ent_next
                global email1_ent_next
                global address1_ent_next
                global aboutMe_ent_next
                global extra_skill1_ent_next
                global extra_skill2_ent_next
                global yearsOf_expereience1_ent_next
                global about_experience_ent_next
                global proficient_Language1_ent_next
                global proficient_Language2_ent_next
                global qualification1_ent_next
                global qualification2_ent_next
                global reference_ent_next
                global anything_else1_ent_next


                Fname_lbl_next = tk.Label(next, text="First Name", font=my_font0, fg="white", bg="#3D5A80")
                Fname_lbl_next.place(x=20, y=130)
                Fname_ent_next = Entry(next, font=my_font1, bg="white", fg="black")
                Fname_ent_next.place(x=20, y=160)

                Field_of_job_lbl_next = tk.Label(next, text="Field of Job", font=my_font0, fg="white", bg="#3D5A80")
                Field_of_job_lbl_next.place(x=20, y=220)
                Field_of_job_ent_next = Entry(next, font=my_font1, bg="white", fg="black")
                Field_of_job_ent_next.place(x=20, y=250)

                contact_lbl_next = tk.Label(next, text="Contact Number", font=my_font0, fg="white", bg="#3D5A80")
                contact_lbl_next.place(x=20, y=310)
                contact_ent_next = Entry(next, font=my_font1, bg="white", fg="black")
                contact_ent_next.place(x=20, y=340)

                email1_lbl_next = tk.Label(next, text="Email", font=my_font0, fg="white", bg="#3D5A80")
                email1_lbl_next.place(x=20, y=400)
                email1_ent_next = Entry(next, font=my_font1, bg="white", fg="black")
                email1_ent_next.place(x=20, y=430)

                address1_lbl_next = tk.Label(next, text="Address", font=my_font0, fg="white", bg="#3D5A80")
                address1_lbl_next.place(x=20, y=490)
                address1_ent_next = Entry(next, font=my_font1, bg="white", fg="black")
                address1_ent_next.place(x=20, y=520)

                aboutMe_lbl_next = tk.Label(next, text="About Me", font=my_font0, fg="white", bg="#3D5A80")
                aboutMe_lbl_next.place(x=20, y=580)
                aboutMe_ent_next = Entry(next, font=my_font1, bg="white", fg="black")
                aboutMe_ent_next.place(x=20, y=600)

                extra_skill1_lbl_next = tk.Label(next, text="Extra Skill 1", font=my_font0, fg="white", bg="#3D5A80")
                extra_skill1_lbl_next.place(x=305, y=130)
                extra_skill1_ent_next = Entry(next, font=my_font1, bg="white", fg="black")
                extra_skill1_ent_next.place(x=305, y=160)

                extra_skill2_lbl_next = tk.Label(next, text="Extra Skill 2", font=my_font0, fg="white", bg="#3D5A80")
                extra_skill2_lbl_next.place(x=305, y=220)
                extra_skill2_ent_next = Entry(next, font=my_font1, bg="white", fg="black")
                extra_skill2_ent_next.place(x=305, y=250)

                yearsOf_expereience1_lbl_next = tk.Label(next, text="Years of Expereience", font=my_font0, fg="white", bg="#3D5A80")
                yearsOf_expereience1_lbl_next.place(x=305, y=310)
                yearsOf_expereience1_ent_next = Entry(next, font=my_font1, bg="white", fg="black")
                yearsOf_expereience1_ent_next.place(x=305, y=340)

                about_experience_lbl_next = tk.Label(next, text="About the Experience", font=my_font0, fg="white", bg="#3D5A80")
                about_experience_lbl_next.place(x=305, y=400)
                about_experience_ent_next = Entry(next, font=my_font1, bg="white", fg="black")
                about_experience_ent_next.place(x=305, y=430)

                proficient_Language1_lbl_next = tk.Label(next, text="Proficient Language 1", font=my_font0, fg="white", bg="#3D5A80")
                proficient_Language1_lbl_next.place(x=305, y=490)
                proficient_Language1_ent_next = Entry(next, font=my_font1, bg="white", fg="black")
                proficient_Language1_ent_next.place(x=305, y=520)

                proficient_Language2_lbl_next = tk.Label(next, text="Proficient Language 2", font=my_font0, fg="white", bg="#3D5A80")
                proficient_Language2_lbl_next.place(x=305, y=580)
                proficient_Language2_ent_next = Entry(next, font=my_font1, bg="white", fg="black")
                proficient_Language2_ent_next.place(x=305, y=610)

                qualification1_lbl_next = tk.Label(next, text="Qualification 1", font=my_font0, fg="white", bg="#3D5A80")
                qualification1_lbl_next.place(x=590, y=130)
                qualification1_ent_next = Entry(next, font=my_font1, bg="white", fg="black")
                qualification1_ent_next.place(x=590, y=160)

                qualification2_lbl_next = tk.Label(next, text="Qualification 2", font=my_font0, fg="white", bg="#3D5A80")
                qualification2_lbl_next.place(x=590, y=220)
                qualification2_ent_next = Entry(next, font=my_font1, bg="white", fg="black")
                qualification2_ent_next.place(x=590, y=250)

                reference_lbl_next = tk.Label(next, text="Reference", font=my_font0, fg="white", bg="#3D5A80")
                reference_lbl_next.place(x=590, y=310)
                reference_ent_next = Entry(next, font=my_font1, bg="white", fg="black")
                reference_ent_next.place(x=590, y=340)

                anything_else1_lbl_next = tk.Label(next, text="Anything Else", font=my_font0, fg="white", bg="#3D5A80")
                anything_else1_lbl_next.place(x=590, y=400)
                anything_else1_ent_next = Entry(next, font=my_font1, bg="white", fg="black")
                anything_else1_ent_next.place(x=590, y=430)

                for n in records:
                    Fname_ent_next.insert(0,n[1])
                    Field_of_job_ent_next.insert(0,n[2])
                    contact_ent_next.insert(0,n[3])
                    email1_ent_next.insert(0,n[4])
                    address1_ent_next.insert(0,n[5])
                    aboutMe_ent_next.insert(0,n[6])
                    extra_skill1_ent_next.insert(0,n[7])
                    extra_skill2_ent_next.insert(0,n[8])
                    yearsOf_expereience1_ent_next.insert(0,n[9])
                    about_experience_ent_next.insert(0,n[10])
                    proficient_Language1_ent_next.insert(0,n[11])
                    proficient_Language2_ent_next.insert(0,n[12])
                    qualification1_ent_next.insert(0,n[13])
                    qualification2_ent_next.insert(0,n[14])
                    reference_ent_next.insert(0,n[15])
                    anything_else1_ent_next.insert(0,n[16])

                    save_btn=Button(next, text='Update', font=my_font2, bg="#213A5C", fg="white",padx=60 ,command=update)
                    save_btn.place(x=590,y=600)
                    break
            break
        else:
            messagebox.showerror("Error","Invalid User_Id")        
    conn.commit()
    conn.close()
        
        


# cv_form_frame------------------------------------
def cv_page():
    cv_frame = Frame(main, bg="#3D5A80", width=865, height=655)
    cv_frame.place(x=230, y=47)
    cv_ttl = tk.Label(cv_frame, text="CV ENTRIES", font=my_font4, fg="white", bg="#3D5A80")
    cv_ttl.place(x=20, y=40)
    cv_ttl2 = tk.Label(cv_frame, text="Please enter the following data (* Required)", font=my_font0, fg="white", bg="#3D5A80")
    cv_ttl2.place(x=20, y=85)

    Fname_lbl = tk.Label(cv_frame, text="Full Name *", font=my_font0, fg="white", bg="#3D5A80")
    Fname_lbl.place(x=20, y=130)
    Fname_ent = Entry(cv_frame, font=my_font1, bg="white", fg="black")
    Fname_ent.place(x=20, y=160)

    Field_of_job_lbl = tk.Label(cv_frame, text="Field of Job *", font=my_font0, fg="white", bg="#3D5A80")
    Field_of_job_lbl.place(x=20, y=220)
    Field_of_job_ent = Entry(cv_frame, font=my_font1, bg="white", fg="black")
    Field_of_job_ent.place(x=20, y=250)

    contact_lbl = tk.Label(cv_frame, text="Contact Number *", font=my_font0, fg="white", bg="#3D5A80")
    contact_lbl.place(x=20, y=310)
    contact_ent = Entry(cv_frame, font=my_font1, bg="white", fg="black")
    contact_ent.place(x=20, y=340)

    email1_lbl = tk.Label(cv_frame, text="Email *", font=my_font0, fg="white", bg="#3D5A80")
    email1_lbl.place(x=20, y=400)
    email1_ent = Entry(cv_frame, font=my_font1, bg="white", fg="black")
    email1_ent.place(x=20, y=430)

    address1_lbl = tk.Label(cv_frame, text="Address *", font=my_font0, fg="white", bg="#3D5A80")
    address1_lbl.place(x=20, y=490)
    address1_ent = Entry(cv_frame, font=my_font1, bg="white", fg="black")
    address1_ent.place(x=20, y=520)

    aboutMe_lbl = tk.Label(cv_frame, text="About Me *", font=my_font0, fg="white", bg="#3D5A80")
    aboutMe_lbl.place(x=20, y=580)
    aboutMe_ent = Entry(cv_frame, font=my_font1, bg="white", fg="black")
    aboutMe_ent.place(x=20, y=600)

    extra_skill1_lbl = tk.Label(cv_frame, text="Extra Skill 1 *", font=my_font0, fg="white", bg="#3D5A80")
    extra_skill1_lbl.place(x=305, y=130)
    extra_skill1_ent = Entry(cv_frame, font=my_font1, bg="white", fg="black")
    extra_skill1_ent.place(x=305, y=160)

    extra_skill2_lbl = tk.Label(cv_frame, text="Extra Skill 2", font=my_font0, fg="white", bg="#3D5A80")
    extra_skill2_lbl.place(x=305, y=220)
    extra_skill2_ent = Entry(cv_frame, font=my_font1, bg="white", fg="black")
    extra_skill2_ent.place(x=305, y=250)

    yearsOf_expereience1_lbl = tk.Label(cv_frame, text="Years of Experience *", font=my_font0, fg="white", bg="#3D5A80")
    yearsOf_expereience1_lbl.place(x=305, y=310)
    yearsOf_expereience1_ent = Entry(cv_frame, font=my_font1, bg="white", fg="black")
    yearsOf_expereience1_ent.place(x=305, y=340)

    about_experience_lbl = tk.Label(cv_frame, text="About the Experience", font=my_font0, fg="white", bg="#3D5A80")
    about_experience_lbl.place(x=305, y=400)
    about_experience_ent = Entry(cv_frame, font=my_font1, bg="white", fg="black")
    about_experience_ent.place(x=305, y=430)

    proficient_Language1_lbl = tk.Label(cv_frame, text="Proficient Language 1 *", font=my_font0, fg="white", bg="#3D5A80")
    proficient_Language1_lbl.place(x=305, y=490)
    proficient_Language1_ent = Entry(cv_frame, font=my_font1, bg="white", fg="black")
    proficient_Language1_ent.place(x=305, y=520)

    proficient_Language2_lbl = tk.Label(cv_frame, text="Proficient Language 2", font=my_font0, fg="white", bg="#3D5A80")
    proficient_Language2_lbl.place(x=305, y=580)
    proficient_Language2_ent = Entry(cv_frame, font=my_font1, bg="white", fg="black")
    proficient_Language2_ent.place(x=305, y=610)

    qualification1_lbl = tk.Label(cv_frame, text="Qualification 1 *", font=my_font0, fg="white", bg="#3D5A80")
    qualification1_lbl.place(x=590, y=130)
    qualification1_ent = Entry(cv_frame, font=my_font1, bg="white", fg="black")
    qualification1_ent.place(x=590, y=160)

    qualification2_lbl = tk.Label(cv_frame, text="Qualification 2 *", font=my_font0, fg="white", bg="#3D5A80")
    qualification2_lbl.place(x=590, y=220)
    qualification2_ent = Entry(cv_frame, font=my_font1, bg="white", fg="black")
    qualification2_ent.place(x=590, y=250)

    reference_lbl = tk.Label(cv_frame, text="Reference *", font=my_font0, fg="white", bg="#3D5A80")
    reference_lbl.place(x=590, y=310)
    reference_ent = Entry(cv_frame, font=my_font1, bg="white", fg="black")
    reference_ent.place(x=590, y=340)

    anything_else1_lbl = tk.Label(cv_frame, text="Anything Else", font=my_font0, fg="white", bg="#3D5A80")
    anything_else1_lbl.place(x=590, y=400)
    anything_else1_ent = Entry(cv_frame, font=my_font1, bg="white", fg="black")
    anything_else1_ent.place(x=590, y=430)


    # edit function----------------------------------
    def edit():
        def del1(event):
            a=id_entry.get()
            if a=='Insert User_Id':
                id_entry.delete(0,END)
        global id_entry
        id_entry=Entry(cv_frame,font=my_font,relief=GROOVE)
        id_entry.insert(0,'Insert User_Id')
        id_entry.place(x=520,y=20)
        id_entry.bind("<FocusIn>",del1)
        Esubmit_btn=Button(cv_frame,bg="#3D5A80",fg='white',text="Submit",command=fet)
        Esubmit_btn.place(x=660,y=20)

    
    

    # verification function-------------------------------------------------
    def verify():
        a = Fname_ent.get()
        b = Field_of_job_ent.get()
        c = contact_ent.get()
        d = email1_ent.get()
        e = address1_ent.get()
        f = aboutMe_ent.get()
        g = yearsOf_expereience1_ent.get()
        h = proficient_Language1_ent.get()
        i = qualification1_ent.get()
        j = qualification2_ent.get()
        k = reference_ent.get()
        l = extra_skill1_ent.get()

        if (a == "") or (b == "") or (c == "") or (
                d == "") or (e == "") or (f == "") or (g == "") or (h == "") or (i == "") or (j == "") or (k == "") or (l == ""):
            messagebox.showerror("Error", "One or More Fields Empty.")
        elif len(c)<10 or len(c)>10:
            messagebox.showerror("Error","Invalid Contact Number")
        elif '@' and '.com' not in d:
            messagebox.showerror("Error","Invalid Email")
        else:
            import random
            import string
            global rand
            rand = ''.join(random.choice(string.ascii_letters+ string.digits) for n in range(4))
            messagebox.showinfo('Your_ID',rand)
            cv_datab()
            submit()

    
    submit_btn1 = Button(cv_frame, text="SUBMIT", font=my_font4, bg="#213A5C", fg="white", command=verify)
    submit_btn1.place(x=620, y=570)
    edit_btn1 = Button(cv_frame, text="EDIT", font=my_font4, bg="#213A5C", fg="white", command=edit)
    edit_btn1.place(x=710, y=0)

    # Data insertion___________
    def submit():
        log = sqlite3.connect('cv_detail.db')

        # create cursor
        log1 = log.cursor()

        # insert into tables
        log1.execute(
            "INSERT INTO cv_placement VALUES(:User_ID,:f_name ,:Field_of_job,:contact,:email1,:address1,:aboutMe,:extra_skill1,:extra_skill2,:yearsOf_expereience1,:about_experience,:proficient_Language1,:proficient_Language2,:qualification1,:qualification2,:reference,:anything_else1)",
            {
                'User_ID': rand,
                'f_name': Fname_ent.get(),
                'Field_of_job': Field_of_job_ent.get(),
                'contact': contact_ent.get(),
                'email1': email1_ent.get(),
                'address1': address1_ent.get(),
                'aboutMe': aboutMe_ent.get(),
                'extra_skill1': extra_skill1_ent.get(),
                'extra_skill2': extra_skill2_ent.get(),
                'yearsOf_expereience1': yearsOf_expereience1_ent.get(),
                'about_experience': about_experience_ent.get(),
                 'proficient_Language1': proficient_Language1_ent.get(),
                'proficient_Language2': proficient_Language2_ent.get(),
                'qualification1': qualification1_ent.get(),
                'qualification2': qualification2_ent.get(),
                'reference': reference_ent.get(),
                'anything_else1': anything_else1_ent.get()
            })

        log.commit()
        log.close()

        # clear entries
        Fname_ent.delete(0, END)
        Field_of_job_ent.delete(0, END)
        contact_ent.delete(0, END)
        email1_ent.delete(0, END)
        address1_ent.delete(0, END)
        aboutMe_ent.delete(0, END)
        extra_skill1_ent.delete(0, END)
        extra_skill2_ent.delete(0, END)
        yearsOf_expereience1_ent.delete(0, END)
        about_experience_ent.delete(0, END)
        proficient_Language1_ent.delete(0, END)
        proficient_Language2_ent.delete(0, END)
        qualification1_ent.delete(0, END)
        qualification2_ent.delete(0, END)
        reference_ent.delete(0, END)
        anything_else1_ent.delete(0, END)

        
cv_page()

main.mainloop()
