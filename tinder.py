import dbhelper
from tkinter import*
#from tkinter import filedialog as fd
from PIL import Image,ImageTk
from tkinter import messagebox
class tinder:
    def __init__(self):
        self._dbo=dbhelper.DBhelper()
        self.loginWindow()
     


    def loginWindow(self):
        self._root=Tk()
        self._root.configure(background="#FF5864")
        self._root.minsize(400,800)

        self._label1=Label(self._root,text="Tinder",bg="#FF5864",fg="#fff")
        self._label1.configure(font=("Comic Sans MS",25,"bold"))
        self._label1.pack(pady=(30,30))

        self._label2= Label(self._root, text="Email", bg="#FF5864", fg="#fff")
        self._label2.configure(font=("Comic Sans MS", 20, ))
        self._label2.pack(pady=(10, 5))

        self._emailInput=Entry(self._root)
        self._emailInput.pack(pady=(0,20),ipadx=30,ipady=7)

        self._label3 = Label(self._root, text="Password", bg="#FF5864", fg="#fff")
        self._label3.configure(font=("Comic Sans MS", 20,))
        self._label3.pack(pady=(10,10))

        self._passwordInput = Entry(self._root)
        self._passwordInput.pack(pady=(10, 20), ipadx=30, ipady=7)

        self._loginButton=Button(self._root,text="Login",bg="#fff",width=30,height=2,command=lambda:self.loginHandler(self._emailInput.get(),self._passwordInput.get()))
        self._loginButton.configure(font=("Comic Sans MS",12,))
        self._loginButton.pack()

        self._label4 = Label(self._root, text="Not a member ?", bg="#FF5864", fg="#fff")
        self._label4.configure(font=("Comic Sans MS", 16,))
        self._label4.pack(pady=(10, 5))

        self._regButton = Button(self._root, text="Click here", bg="#fff", width=10, height=1,
                                   command=lambda: self.regWindow())
        self._regButton.configure(font=("Comic Sans MS", 12,))
        self._regButton.pack()

        self._root.mainloop()

    def regWindow(self):
        self._root1=Tk()
        self._root1.configure(background="#FF5864")
        self._root1.minsize(400, 700)

        self._label5 = Label(self._root1, text="Name", bg="#FF5864", fg="#fff")
        self._label5.configure(font=("Comic Sans MS", 14,))
        self._label5.pack(pady=(5, 0))

        self._NameInput = Entry(self._root1)
        self._NameInput.pack(pady=(5,0), ipadx=25, ipady=7)

        self._label6 = Label(self._root1, text="Email", bg="#FF5864", fg="#fff")
        self._label6.configure(font=("Comic Sans MS", 14,))
        self._label6.pack(pady=(5, 0))


        self._EmailInput = Entry(self._root1)
        self._EmailInput.pack(pady=(5,0), ipadx=25, ipady=7)

        self._label7 = Label(self._root1, text="Password", bg="#FF5864", fg="#fff")
        self._label7.configure(font=("Comic Sans MS", 14,))
        self._label7.pack(pady=(5, 0))

        self._PasswordInput = Entry(self._root1)
        self._PasswordInput.pack(pady=(5, 0), ipadx=25, ipady=7)

        self._label8 = Label(self._root1, text="age", bg="#FF5864", fg="#fff")
        self._label8.configure(font=("Comic Sans MS", 14,))
        self._label8.pack(pady=(5,0))

        self._ageInput = Entry(self._root1)
        self._ageInput.pack(pady=(5,0), ipadx=25, ipady=7)

        self._label9 = Label(self._root1, text="Gender", bg="#FF5864", fg="#fff")
        self._label9.configure(font=("Comic Sans MS", 14,))
        self._label9.pack(pady=(5,0))

        self._genderInput = Entry(self._root1)
        self._genderInput.pack(pady=(5,0), ipadx=25, ipady=7)

        self._label10 = Label(self._root1, text="city", bg="#FF5864", fg="#fff")
        self._label10.configure(font=("Comic Sans MS", 14,))
        self._label10.pack(pady=(5,0))

        self._cityInput = Entry(self._root1)
        self._cityInput.pack(pady=(5, 0), ipadx=25, ipady=7)

        self._label11 = Label(self._root1, text="Bio", bg="#FF5864", fg="#fff")
        self._label11.configure(font=("Comic Sans MS", 14,))
        self._label11.pack(pady=(5,0))

        self._bioInput = Entry(self._root1)
        self._bioInput.pack(pady=(5, 0), ipadx=25, ipady=4)

        self._label14 = Label(self._root1, text="Profile Picture(Save the image in the project before entering)", bg="#FF5864", fg="#fff")
        self._label14.configure(font=("Comic Sans MS", 10,))
        self._label14.pack(pady=(5, 0))

        self._bgInput = Entry(self._root1)
        self._bgInput.pack(pady=(5, 0), ipadx=25, ipady=4)

        self._regButton = Button(self._root1, text="Register ", bg="#fff", width=30, height=2,
                                   command=lambda: self.regHandler(self._NameInput.get(),self._EmailInput.get(),self._PasswordInput.get(),self._ageInput.get(),self._genderInput.get(),self._cityInput.get() ,self._bioInput.get(),self._bgInput.get()))
        self._regButton.configure(font=("Comic Sans MS", 12,))
        self._regButton.pack(pady=(5,0))

        self._root1.mainloop()
    def loginHandler(self,email,password):

      response=self._dbo.search('email',email,'password',password,'usersactual')


      if len(response)==0:
          self.errorMessage("error", "incorrect")
      else:
            self.user_id=response[0][0]
            self.loadProfile(response)
    def loadProfile(self,response):
        self.mainWindow(response,1)

    def mainWindow(self,response,mode,num=0):
        self.headerMenu()
        self.loadMyprofile(response)





        if mode==2:
            frame = Frame(self._root)
            frame.pack()
            btn1 = Button(frame, text="Previous", fg="#fff", bg="#fd5068",command=lambda:self.othersProfile(num-1))
            btn1.pack(side=LEFT)
            btn2 = Button(frame, text="Propose", fg="#fff", bg="#fd5068",command=lambda:self.propose(response[0][0]))
            btn2.pack(side=LEFT)
            btn3 = Button(frame, text="Next", fg="#fff", bg="#fd5068",command=lambda:self.othersProfile(num+1))
            btn3.pack(side=LEFT)
    def loadMyprofile(self,response):
        self.clearWindow()
        self._label1 = Label(self._root, text="THE PROFILES", bg="#FF5864", fg="#fff")
        self._label1.configure(font=("Comic Sans MS", 20,))
        self._label1.pack(pady=(10, 5))
        background=response[0][5]
        try:
            load = Image.open(background)
            load = load.resize((200, 200), Image.ANTIALIAS)
            render = ImageTk.PhotoImage(load)

            img = Label(image=render)
            img.image = render
            img.pack()
        except:
            self.errorMessage("ERROR","Picture does not exsist in the directory,save it in the directory")

        name = response[0][1]

        self._label1 = Label(self._root, text="NAME:"+str.capitalize(name), bg="#FF5864", fg="#fff")
        self._label1.configure(font=("Comic Sans MS", 20,))
        self._label1.pack(pady=(10, 5))
        age = response[0][4]
        self._label2 = Label(self._root, text="AGE:"+str(age), bg="#FF5864", fg="#fff")
        self._label2.configure(font=("Comic Sans MS", 20,))
        self._label2.pack(pady=(10, 5))

        gender = response[0][6]
        self._label3 = Label(self._root, text="GENDER:"+str.capitalize(gender), bg="#FF5864", fg="#fff")
        self._label3.configure(font=("Comic Sans MS", 20,))
        self._label3.pack(pady=(10, 5))
        city = response[0][7]
        self._label4 = Label(self._root, text="CITY:"+str.capitalize(city), bg="#FF5864", fg="#fff")
        self._label4.configure(font=("Comic Sans MS", 20,))
        self._label4.pack(pady=(10, 5))
        bio=response[0][8]
        self._label6 = Label(self._root, text="BIO:"+str(bio), bg="#FF5864", fg="#fff")
        self._label6.configure(font=("Comic Sans MS", 20,))
        self._label6.pack(pady=(10, 5))


    def headerMenu(self):
        response=self._dbo.search2('user_id',self.user_id,'usersactual')
        menu = Menu(self._root)
        self._root.config(menu=menu)
        filemenu = Menu(menu)
        menu.add_cascade(label="Home", menu=filemenu)
        filemenu.add_command(label="My Profile",command=lambda:self.loadMyprofile(response))
        filemenu.add_command(label="Edit Profile",command=lambda:self.editProfile())
        filemenu.add_command(label="View Profile",command=lambda:self.othersProfile(0))
        filemenu.add_command(label="LogOut",command=lambda:self.newWindow())

        helpmenu = Menu(menu)
        menu.add_cascade(label="Proposals", menu=helpmenu)
        helpmenu.add_command(label="My Proposals",command=lambda:self.proposalssearch('juliet_id',self.user_id,1,"Received","Proposals/Proposals"))
        helpmenu.add_command(label="My Requests",command=lambda:self.proposalssearch('romeo_id',self.user_id,2,"Sent","Proposal/Proposals"))
        helpmenu.add_command(label="My Matches",command=lambda:self.matches())
    def newWindow(self):
        self._root.destroy()
        self.loginWindow()

    def clearWindow(self):
        for i in self._root.pack_slaves():
            i.destroy()


    def regHandler(self,name,email,password,age,gender,city,bio,bg):
        mydict={

          'name':name,
          'email':email,
          'password':password,
          'age':age,
          'bg':bg,
          'gender':gender,
          'city':city,
          'bio':bio
        }
        v=self._dbo.search('email',mydict['email'],'password',mydict['password'],'usersactual')

        if len(v)==0:
            flag=self._dbo.insert(mydict,'usersactual')
            if flag==0:
                self.errorMessage("error", "registration unsuccesfull")
            else:
                self.errorMessage("success", "registration successful")
        else:
         self.errorMessage("Failure","An account already exsists by this username and password,try for a different one")
    def othersProfile(self,num):
        send_data=[]
        data=self._dbo.searchone('user_id',self.user_id,'usersactual','NOT LIKE')

        if num<0:
            self.errorMessage("ERROR","No Profiles to show")
        elif num>len(data)-1:
            self.errorMessage("error","NO profiles to show")
        else:
            send_data.append(data[num])
            self.mainWindow(send_data,2,num)

    def propose(self,juliet_id):
        data=self._dbo.search('romeo_id',self.user_id,'juliet_id',juliet_id,'propose')

        if len(data)==0:
            mydict={

                'romeo_id':self.user_id,
                'juliet_id':juliet_id,
            }

            flag=self._dbo.insert2(mydict,'propose')

            if flag==1:
                self.errorMessage("SUCCESS","PROPOSAL SENT")
            else:
                self.errorMessage("FAILURE","GET A SURGERY")
        else:
             self.errorMessage("ERROR","CHILL DESPERATE HUMAN")
    def editProfile(self):
        self._root2 = Tk()
        self._root2.configure(background="#FF5864")
        self._root2.minsize(400, 1000)

        self._label5 = Label(self._root2, text="Enter new name", bg="#FF5864", fg="#fff")
        self._label5.configure(font=("Comic Sans MS", 14,))
        self._label5.pack(pady=(5, 0))

        self._NameInput = Entry(self._root2)
        self._NameInput.pack(pady=(5, 0), ipadx=10, ipady=4)

        self._label6 = Label(self._root2, text="Enter new email", bg="#FF5864", fg="#fff")
        self._label6.configure(font=("Comic Sans MS", 14,))
        self._label6.pack(pady=(5, 0))

        self._EmailInput = Entry(self._root2)
        self._EmailInput.pack(pady=(5, 0), ipadx=25, ipady=4)

        self._label7 = Label(self._root2, text="enter new Password", bg="#FF5864", fg="#fff")
        self._label7.configure(font=("Comic Sans MS", 14,))
        self._label7.pack(pady=(5, 0))

        self._PasswordInput = Entry(self._root2)
        self._PasswordInput.pack(pady=(5, 0), ipadx=25, ipady=7)

        self._label8 = Label(self._root2, text="enter new age", bg="#FF5864", fg="#fff")
        self._label8.configure(font=("Comic Sans MS", 14,))
        self._label8.pack(pady=(5, 0))

        self._ageInput = Entry(self._root2)
        self._ageInput.pack(pady=(5, 0), ipadx=25, ipady=4)

        self._label9 = Label(self._root2, text="enter new Gender", bg="#FF5864", fg="#fff")
        self._label9.configure(font=("Comic Sans MS", 14,))
        self._label9.pack(pady=(5, 0))

        self._genderInput = Entry(self._root2)
        self._genderInput.pack(pady=(5, 0), ipadx=25, ipady=4)

        self._label10 = Label(self._root2, text="enter new city", bg="#FF5864", fg="#fff")
        self._label10.configure(font=("Comic Sans MS", 14,))
        self._label10.pack(pady=(5, 0))

        self._cityInput = Entry(self._root2)
        self._cityInput.pack(pady=(5, 0), ipadx=25, ipady=4)

        self._label11 = Label(self._root2, text="enter new Bio", bg="#FF5864", fg="#fff")
        self._label11.configure(font=("Comic Sans MS", 14,))
        self._label11.pack(pady=(5, 0))

        self._bioInput = Entry(self._root2)
        self._bioInput.pack(pady=(5, 0), ipadx=25, ipady=4)

        self._label14 = Label(self._root2, text="Profile Picture", bg="#FF5864", fg="#fff")
        self._label14.configure(font=("Comic Sans MS", 14,))
        self._label14.pack(pady=(5, 0))

        self._bgInput = Entry(self._root2)
        self._bgInput.pack(pady=(5, 0), ipadx=25, ipady=4)

        self._editButton = Button(self._root2, text="Edit ", bg="#fff", width=30, height=2,command=lambda:self.editHandler(self._NameInput.get(),self._EmailInput.get(),self._PasswordInput.get(),self._ageInput.get(),self._genderInput.get(),self._cityInput.get(),self._bioInput.get(),self._bgInput.get()))

        self._editButton.configure(font=("Comic Sans MS", 14,))
        self._editButton.pack(pady=(15,0))

        self._root2.mainloop()

    def editHandler(self,name,email,password,age,gender,city,bio,bg):
        session=self.user_id

        flag=self._dbo.update(session,name,email,password,age,bg,gender,city,bio)
        if flag==0:
                self.errorMessage("error", "unsuccessful update")
        else:
                self.errorMessage("Success","update done")



    def proposalssearch(self,column,userid,num,name1,name):
        self._root3 = Tk()
        self._root3.configure(background="#FF5864")
        self._root3.minsize(400,600)
        send_data=[]
        data=self._dbo.search2(column,userid,'propose')
        send_data.append(data)

        p=send_data[0]
        myproposals = len(p)
        self._label1 = Label(self._root3, text="You have"+" "+ name1 +" "+ str(myproposals) +" "+ name, bg="#FF5864", fg="#fff")
        self._label1.configure(font=("Comic Sans MS", 14,))
        self._label1.pack(pady=(0, 5))

        self._label1 = Label(self._root3, text="They are:", bg="#FF5864", fg="#fff")
        self._label1.configure(font=("Comic Sans MS", 14,))
        self._label1.pack(pady=(0, 5))

        for i in range(myproposals):
            k=p[i][num]
            response=self._dbo.search2('user_id',k,'usersactual')

            name=response[0][1]
            self._label1 = Label(self._root3, text=str.capitalize(name), bg="#FF5864", fg="#fff",anchor=NE)
            self._label1.configure(font=("Comic Sans MS", 14,))
            self._label1.pack(pady=(0, 5))
    def matches(self):

        self._root3 = Tk()
        self._root3.configure(background="#FF5864")
        self._root3.minsize(400,600)
        send_data=[]
        data=self._dbo.search2('juliet_id',self.user_id,'propose')
        send_data.append(data)

        label12 = Label(self._root3, text="Your matches are", bg="#FF5864", fg="#fff")
        label12.configure(font=("Comic Sans MS", 14,))
        label12.pack(pady=(0, 5))

        for i in range(len(send_data[0])):
            response=send_data[0][i][2]

            send_data2=[]
            data2=self._dbo.search2('romeo_id',response,'propose')
            send_data2.append(data2)

            for j in range(len(send_data2[0])):
             if send_data2[0][j][2]==send_data[0][i][1]:
                    

                    response2 = self._dbo.search2('user_id',send_data2[0][j][2] , 'usersactual')
                    label12 = Label(self._root3, text=str.capitalize(response2[0][1]), bg="#FF5864", fg="#fff")
                    label12.configure(font=("Comic Sans MS", 14,))
                    label12.pack(pady=(10, 5))



    def errorMessage(self,title,message):
         messagebox.showerror(title,message)




obj1=tinder()




