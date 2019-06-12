from tkinter import *
from tkinter import ttk

import smtplib
from email.mime.text import MIMEText
import config

class mail:

    def __init__(self,root):
        self.root = root
        self.root.title('MAIL NOW')
        self.root.geometry('750x750')
        self.root.config(bg='steelblue4',padx=10,pady=20)

        getFrom = StringVar()
        getTo = StringVar()
        getCc = StringVar()
        getBcc = StringVar()
        getSubject = StringVar()
        getBodyText = StringVar()

        # CREATE MENUBAR
        menubar = Menu(root)
        root.config(menu=menubar)

        # get your port number for different service providers such as for yahoo
        server = smtplib.SMTP('smtp.gmail.com',587) # server url, port number ,587 for gmail
        server.starttls() # it convert insecure connection into tls or ssl
        EMAIL = config.EMAIL  # reading email and password from the config python file
        PASSWORD = config.PASSWORD

        # setting icon
        self.root.iconbitmap('mail.ico')

        def create_window(): # new window definition
            root = Tk()
            newwin = mail(root)
            root.mainloop()

            
        # CREATE SUBMENU
        submenu = Menu(menubar , tearoff=0)
        menubar.add_cascade(label='FILE',menu=submenu)
        submenu.add_command(label='New',command=create_window)
        submenu.add_command(label='Exit',command=root.destroy)
       
    

        # frames

        mainFrame = Frame(self.root , bg= 'steelblue3',height = 730, width = 950)
        mainFrame.pack(fill=BOTH, expand=True)
        
        topFrame = Frame(mainFrame,bg='ghost White',height=200,width=850) #Frame(root,relief= RAISED, borderwidth=1)
        topFrame.pack(padx=10,pady=10,fill=X, expand=True)

        bottomFrame = Frame(mainFrame,height=400,width=850) #Frame(root,relief= RAISED, borderwidth=1)
        bottomFrame.pack(padx=10,pady=10,fill= X, expand=True)

        subFrameTop = Frame(bottomFrame,bd=1,width=800,height=300,relief=RIDGE)
        subFrameTop.pack(side = TOP,fill=X,expand=True)
        
        subFrameBottom = Frame(bottomFrame,bd=1,width=800,height=50,relief=RIDGE,bg='steelblue2')
        subFrameBottom.pack(side =BOTTOM)

        # labels
        
        self.fromLabel = Label(topFrame, font = ('Arial',14,'bold'),text='FROM : ',padx=10,pady=5,bg='steelblue1',width=10)
        self.fromLabel.grid(row=0,column=0,sticky = W) # sticky in capital letters
        self.fromText = Entry(topFrame,width= 750,font = ('Arial',14,'bold'),textvariable = getFrom,bg = 'lightblue') # we cannot use padding here
        self.fromText.grid(row=0,column=1)

        self.fromText.insert(0,EMAIL)

        self.toLabel = Label(topFrame, font = ('Arial',14,'bold'),text='TO : ',padx =10,pady=5,bg='ghost White',width=10)
        self.toLabel.grid(row=1,column=0,sticky = W) # sticky in capital letters
        self.toText = Entry(topFrame,width=750,font = ('Arial',14,'bold'),textvariable = getTo ,bg = 'lightblue') # we cannot use padding here
        self.toText.grid(row=1,column=1)

        self.ccLabel = Label(topFrame, font = ('Arial',14,'bold'),text='CC : ',padx =10,pady=5,bg='steelblue1',width=10)
        self.ccLabel.grid(row=2,column=0,sticky = W) # sticky in capital letters
        self.ccText = Entry(topFrame,width=750,font = ('Arial',14,'bold'),textvariable = getCc,bg = 'lightblue') # we cannot use padding here
        self.ccText.grid(row=2,column=1)

        self.bccLabel = Label(topFrame, font = ('Arial',14,'bold'),text='BCC : ',padx =10,pady=5,bg='ghost White',width=10)
        self.bccLabel.grid(row=3,column=0,sticky = W) # sticky in capital letters
        self.bccText = Entry(topFrame,width=750,font = ('Arial',14,'bold'),textvariable = getBcc,bg = 'lightblue') # we cannot use padding here
        self.bccText.grid(row=3,column=1)

        self.subjectLabel = Label(topFrame, font = ('Arial',14,'bold'),text='SUBJECT : ',padx =10,pady=5,bg='steelblue1',width=10)
        self.subjectLabel.grid(row=4,column=0,sticky = W) # sticky in capital letters
        self.subjectText = Entry(topFrame,width=750,font = ('Arial',14,'bold'),textvariable = getSubject,bg = 'lightblue') # we cannot use padding here
        self.subjectText.grid(row=4,column=1)
        self.fromLabel = EMAIL

        # scroll for text in subFrameTOp

        scrollbar = Scrollbar(subFrameTop)
        scrollbar.pack(side = RIGHT,fill=Y)

        self.bodyText = Text(subFrameTop,height = 17, width = 300, bd =1, font =('arial',15,'bold'),yscrollcommand = scrollbar.set)
        self.bodyText.pack(fill=X , expand = True)

        scrollbar.config(command = self.bodyText.yview)        


        
        #buttons
        self.btnHome = Button(subFrameBottom , text = 'HOME' , font=('arial',12,'bold'),height = 1,width =11 ,bd =2,padx=5,pady=2)
        self.btnHome.grid(row=0,column =0)

        self.btnAttach = Button(subFrameBottom , text = 'ATTACH' , font=('arial',12,'bold'),height = 1,width =11 ,bd =2,padx=5)
        self.btnAttach.grid(row=0,column =1)
    

        self.btnDiscard = Button(subFrameBottom , text = 'DISCARD' , font=('arial',12,'bold'),height = 1,width =11 ,bd =2,padx=5)
        self.btnDiscard.grid(row=0,column =2)

        def sendData():
            server.login(EMAIL,PASSWORD)

            message = MIMEText(self.bodyText.get("1.0",END))

            message['FROM'] = self.fromText.get()
            message['TO'] = self.toText.get()
            message['subject']= self.subjectText.get()
            getFrom = self.fromText.get()
            getTO = self.toText.get()
            server.sendmail(getFrom,getTO,message.as_string())
            print('Mail sent')
            
        self.btnSend = Button(subFrameBottom , text = 'SEND' , font=('arial',12,'bold'),height = 1,width=18 ,bd =2,padx=5,command = sendData)
        self.btnSend.grid(row=0,column =3)

        
        
        self.btnExit = Button(subFrameBottom , text = 'EXIT' , font=('arial',12,'bold'),height = 1,width =11 ,bd =2,padx=5,command = root.destroy)
        self.btnExit.grid(row=0,column =4)


    
if __name__ == '__main__':
    root = Tk()
    application = mail(root)
    root.mainloop()
