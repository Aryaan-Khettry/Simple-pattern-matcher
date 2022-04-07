import re,os
from tkinter import *
print(os.getcwd())
ipfile=input("Enter a file name")
fileopen=open(ipfile,'r')
readstr=fileopen.read()
EmRegex=re.findall(r'[\S,' ']+@[\S,' ']+',readstr)
PhRegex=re.findall(r'\d{3}-\d{3}-\d{4}|\d{10}',readstr,re.IGNORECASE)
ColRegRegex=re.findall(r'\d[a-z][a-z]\d\d[a-z][a-z]\d\d\d',readstr,re.IGNORECASE)
StreamRegex=re.findall(r'cse|ise|ece|mechanical',readstr,re.IGNORECASE)
EmRegex.sort()
PhRegex.sort()
ColRegRegex.sort()
StreamRegex.sort()
print("The file is sorted.\n Would you like to add more data? (y/n)")
yn=input()
if(yn=='n'):
    newfile=open('output.txt','w')
    newfile.write("Emails : " + str(EmRegex) + "\n")
    newfile.write("Phone numbers : " + str(PhRegex) + '\n')
    newfile.write("College registration numbers : " + str(ColRegRegex) + '\n')
    newfile.write("Streams within the file : " + str(StreamRegex) + '\n')
    newfile.close()
    print("The data within the file is :")
    x=open('output.txt','r')
    readx=x.read()
    print(readx)
    x.close()
elif(yn=='y'):
    def save_info():
        firstname_info = firstname.get()
        fname = [firstname_info]
        lastname_info = lastname.get()
        lname = [lastname_info]
        phone_info = phone.get()
        PhRegex.append(int(phone_info))
        email_info = email.get()
        EmRegex.append(email_info)
        college_info = college.get()
        col=[college_info]
        usn_info = usn.get()
        ColRegRegex.append(usn_info)
        course_info = course.get()
        StreamRegex.append(course_info)
        print(firstname_info,lastname_info,phone_info,email_info,college_info,usn_info,course_info)
        file = open("output.txt","w+")
        file.write("\n firstname: "+str(fname))
        file.write("\n lastname: "+str(lname))
        file.write("\n phone: "+str(PhRegex))
        file.write("\n email: "+str(EmRegex))
        file.write("\n college: "+str(col))
        file.write("\n usn: "+str(ColRegRegex))
        file.write("\n course :"+str(StreamRegex))
        file.close()
        print("User "+firstname_info+"registered successfully")
        print("The data within the file is :")
        x=open('output.txt','r')
        readx=x.read()
        print(readx)
    screen = Tk()
    screen.geometry("700x700")#set size of the window
    screen.title("Python form")#name of the screen
    heading = Label(text = "Student details form", bg = "grey", fg = "black",width = "500",height = "3") # heading foreground and background color is set
    heading.pack()#to make it in the centre of the screen
    firstname_text = Label(text = "Enter Student's first name ") #create label for firstname
    lastname_text = Label(text = "Enter Student's last form")#create label for lastname
    phone_text = Label(text = "Phone No")#create label for age
    email_text = Label(text = "Email Id")
    college_text = Label(text = "College Name")
    usn_text =  Label(text = "USN")
    course_text = Label(text = "Course name")
    firstname_text.place(x = 15, y = 70) #where the first name text label should be placed
    lastname_text.place(x = 15, y = 140) #where the last name text label should be placed
    phone_text.place(x = 15, y = 210) #where the age text label should be placed
    email_text.place(x=15 , y= 280)
    college_text.place(x=15 , y= 350)
    usn_text.place(x=15 , y= 420)
    course_text.place(x=15, y=490)
    firstname = StringVar() # firstName is stringVar (contains the text u put in the textbox)
    lastname = StringVar()  # lastName is stringVar (contains the text u put in the textbox)
    phone = IntVar() # firstName is IntVar (contains the text u put in the textbox)
    email = StringVar()
    college = StringVar()
    usn = StringVar()
    course = StringVar()
    firstname_entry = Entry(textvariable = firstname, width = "100")#TextBox which takes firstname .First name is stored in textvariable firstname
    lastname_entry = Entry(textvariable = lastname, width = "100") 
    phone_entry = Entry(textvariable = phone , width = "100")
    email_entry = Entry(textvariable = email , width = "100")
    college_entry = Entry(textvariable = college , width = "100")
    usn_entry = Entry(textvariable = usn , width = "100")
    course_entry = Entry(textvariable = course , width = "100")
    firstname_entry.place(x =15, y = 100)#Position the textbox
    lastname_entry.place(x =15, y = 170)
    phone_entry.place(x =15, y = 240)
    email_entry.place(x =15, y = 310)
    college_entry.place(x =15, y = 380)
    usn_entry.place(x =15, y = 450)
    course_entry.place(x =15, y = 520)
    register = Button(screen,text = "Register", width = "10",height = "2",command = save_info,bg = 'grey')#giving command as save_info
    register.place(x = 260,y = 590)
