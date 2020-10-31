import datetime
import pickle
import random as rd
from functools import partial
from tkinter import *
import tkinter.messagebox as tmsg
import pyttsx3
import speech_recognition as sr
from PIL import ImageTk, Image
import mysql.connector
import smtplib


engine = pyttsx3.init('sapi5')

#--------------------------------------------------global var we used
chktrns=0


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate', 150)

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.7
        r.adjust_for_ambient_noise(source,duration=0.4)
        r.energy_threshold=280
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        speak(query)
        return query
    except sr.RequestError as e:
        speak("Say that again please...")
        return "None"
    except sr.UnknownValueError:
        speak("unknown error occured.")
        return "None"


def help(command):
    global query
    if 'how to withdraw' in command:
        speak("To withdraw the cash using globe..excess you must have an account here...Do you have an account")
        reply=takeCommand()
        if('yes'in reply):
            speak('please go to the home page...then enter your credentials, press continue button provided there to fill the form for withdrawl')
            speak('...thanks')
        else:
            speak('please create an account by moving to home page so as to withdraw any amount ')
    elif"send account information"in command:
        speak("your registered email...please")
        email=takeCommand()
        speak('ok sending you in a minute..wait!!')
    elif"red star" in command:
        speak('if you encounter red astrisk in login menu it implies you entered invalid entry...please retry')
    elif"banks under collaboration" in command:
        speak(" we collaborate with...Axis Bank...Central Bank Of India...I C I C I Prudential Bank...HDFC bank")
    else:
        speak("Sorry,..i cant help you with this...kindly contact ...24..7 Globe excess helpline..on...8...3...1...8...6...4...1...8...7...2 ...if you were not able to catch,....no problem.. kindly refer to the message after session overs ...thanks")
        tmsg.showinfo("*HELPLINE*", "Contact 8318641872 for help")
assist=''
def assistant():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am globe excess assistant Sir! I will be guiding you how to use our globe excess app... Please select anyone of the category mentioned below with which i can help you")
    command=takeCommand()
    print(command)
    help(command)

def open_window_3():
    global root
    chktrns.destroy()
    fb = Tk()
    fb.geometry("1250x800")
    fb.title("first page")
    fb.maxsize(1250, 800)
    fb.minsize(1250, 800)
    fb.config(bg="#042148")

    def displaystar():
        f = open("feedback.txt", "a")
        ufb = str(rate.get())
        f.write(ufb + " ")
        f.close()
        f = open("feedback.txt", "r")
        ufb = f.read()
        f.close()
        ty = Label(fbcvs, text="• ● THANK YOU ● •", font=("arial black", 26, "bold"), bg="#042148", fg="white",
                   justify=CENTER, padx=20)
        speak("thank you.. we assure safer transactions and stronger relations")
        ty.place(x=300, y=220)
        if (rate.get() == 1):
            tmsg.showinfo("1 STAR", "SORRY FOR THE INCONVINIENCE WE APOLOGISE")
        elif (rate.get() == 2):
            tmsg.showinfo("2 STAR", "WE WILL TRY TO IMPROVE ON OUR SHORTCOMINGS")
        elif (rate.get() == 3):
            tmsg.showinfo("3 STAR", "WE ARE HAPPY FOR OUR SATISFACTORY PERFORMANCE")
        elif (rate.get() == 4):
            tmsg.showinfo("4 STAR", "WE HOPE TO CONTINUE SUCH GOOD SERVICE")
        elif (rate.get() == 5):
            tmsg.showinfo("5 STAR", "ITS REALLY OVER WHELMING FOR US ")
        fb.destroy()

    rate = IntVar()
    fbtcvs = Canvas(fb, width=1150, height=350, bg="#042148", highlightthickness=0)
    fbtcvs.place(x=50, y=0)

    l1 = fbtcvs.create_line(10, 60, 370, 60, width=4, fill="#05a9ea")
    l2 = fbtcvs.create_line(40, 80, 370, 80, width=4, fill="white")
    l3 = fbtcvs.create_line(70, 100, 370, 100, width=4, fill="#05a9ea")

    log1 = ImageTk.PhotoImage(Image.open("top1.jpg"))
    fbtcvs.create_image(400, 5, anchor='nw', image=log1)
    intr = Label(fbtcvs, text="• ● YOUR FEEDBACK MATTERS ● •", font=("arial black", 40, "bold"), bg="#042148",
                 fg="white", justify=CENTER, padx=20)
    intr.place(x=55, y=165)

    l4 = fbtcvs.create_line(780, 60, 1140, 60, width=4, fill="#05a9ea")
    l5 = fbtcvs.create_line(780, 80, 1110, 80, width=4, fill="white")
    l6 = fbtcvs.create_line(780, 100, 1090, 100, width=4, fill="#05a9ea")

    fbcvs = Canvas(fb, width=1010, height=445, bg="grey", highlightthickness=0)
    fbcvs.place(x=120, y=265)
    rtbus = Label(fbcvs, text="                                                               ",
                  font=("arial black", 33), bg="teal", fg="white", bd="2", justify=CENTER, padx=26, pady=10)
    rtbus.place(x=5, y=5)
    rtus = Label(fbcvs, text="                  RATE  YOUR  SATISFACTION                ", font=("arial black", 26),
                 bg="black", fg="white", justify=CENTER, padx=17, pady=10)
    rtus.place(x=5, y=10)
    logo = ImageTk.PhotoImage(Image.open("coin.png"))
    fbcvs.create_image(5, 5, anchor='nw', image=logo)
    bgrect = fbcvs.create_rectangle(840, 210, 985, 425, fill="#042148")

    r1 = Radiobutton(fbcvs, text=" 1 ★ ", value=1, variable=rate, width=8, bg="grey", fg="#042148", font=(8), padx=5,
                     activebackground="#042148", activeforeground="white")
    r1.place(x=850, y=220)
    r2 = Radiobutton(fbcvs, text=" 2 ★ ", value=2, variable=rate, width=8, bg="grey", fg="#042148", font=(8), padx=5,
                     activebackground="#042148", activeforeground="white")
    r2.place(x=850, y=260)
    r3 = Radiobutton(fbcvs, text=" 3 ★ ", value=3, variable=rate, width=8, bg="grey", fg="#042148", font=(8), padx=5,
                     activebackground="#042148", activeforeground="white")
    r3.place(x=850, y=300)
    r4 = Radiobutton(fbcvs, text=" 4 ★ ", value=4, variable=rate, width=8, bg="grey", fg="#042148", font=(8), padx=5,
                     activebackground="#042148", activeforeground="white")
    r4.place(x=850, y=340)
    r5 = Radiobutton(fbcvs, text=" 5 ★ ", value=5, variable=rate, width=8, bg="grey", fg="#042148", font=(8), padx=5,
                     activebackground="#042148", activeforeground="white")
    r5.place(x=850, y=380)

    rat = Button(fb, text="SUBMIT 🙂", font=("Franklin Gothic Demi", 16), bg="#05a9ea", fg="White", padx=2, bd=4,
                 command=displaystar)
    rat.place(x=1005, y=730)
    fb.mainloop()


def open_window_2(g):
    global chktrns
    global root
    root.destroy()
    chktrns = Tk()
    # WINDOW- SETUP ===========================================================================================
    chktrns.title("Transaction Window")
    chktrns.geometry("1250x800")
    chktrns.maxsize(1250, 800)
    chktrns.minsize(1250, 800)
    canvas = Canvas(chktrns, height=800, width=1250, highlightthickness=0)
    canvas.place(x=0, y=0)
    imageBG = ImageTk.PhotoImage(Image.open("nb.jpg"))
    canvas.create_image(0, 0, anchor='nw', image=imageBG)

    # variables===========================================================================================================
    acc = StringVar()
    ifcd = StringVar()
    bank = StringVar()
    notr = StringVar()
    global gbxd
    fs=""
    # functions =================================================================================================
    def convnotr():
        val = notr.get().split(" ")
        # print(val[1])
        if val[1] == "2":
            return 2
        elif val[1] == "4":
            return 4
        elif val[1] == "6":
            return 6
        elif val[1] == "8":
            return 8

    def username():
        global fs
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="11901811",
            database="mydatabase"
        )
        mycs = mydb.cursor()
        r = (gbxd.get(),)
        sql = ("SELECT firstname,lastname FROM PROJECT WHERE GBX_ID=%s")
        mycs.execute(sql, r)
        distxt = mycs.fetchone()
        fs = "\"" + distxt[0] + "  " + distxt[1] + "\""
        return (fs)
    def valid1():
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="11901811",
            database="mydatabase"
        )
        mycs = mydb.cursor()
        sql = ("SELECT * FROM BANK WHERE acc_no=%s AND GBX_ID=%s")
        val = (acc.get(), gbxd.get())
        mycs.execute(sql, val)
        result = mycs.fetchall()
        print(result)
        how_many_tranix = convnotr()
        if len(result) != 0:
            f = open(result[0][2], "rb")
            bankdet = pickle.load(f)
            trandet = bankdet[acc.get()]
            if how_many_tranix == 2:
                tr1 = Label(cs03, text=trandet[7]["T8"][0] + "    " + trandet[7]["T8"][1] + "             " +
                                       trandet[7]["T8"][2] + "          " + trandet[7]["T8"][3] + "          " +
                                       trandet[7]["T8"][4], bg="#042148", fg="white",
                            font=("arial black ", 9, "bold")).place(x=20, y=110)
                tr2 = Label(cs03, text=trandet[6]["T7"][0] + "    " + trandet[6]["T7"][1] + "             " +
                                       trandet[6]["T7"][2] + "          " + trandet[6]["T7"][3] + "          " +
                                       trandet[6]["T7"][4], bg="#042148", fg="white",
                            font=("arial black ", 9, "bold")).place(x=20, y=140)
            elif how_many_tranix == 4:
                tr1 = Label(cs03, text=trandet[7]["T8"][0] + "    " + trandet[7]["T8"][1] + "             " +
                                       trandet[7]["T8"][2] + "          " + trandet[7]["T8"][3] + "          " +
                                       trandet[7]["T8"][4], bg="#042148", fg="white",
                            font=("arial black ", 9, "bold")).place(x=20, y=110)
                tr2 = Label(cs03, text=trandet[6]["T7"][0] + "    " + trandet[6]["T7"][1] + "             " +
                                       trandet[6]["T7"][2] + "          " + trandet[6]["T7"][3] + "          " +
                                       trandet[6]["T7"][4], bg="#042148", fg="white",
                            font=("arial black ", 9, "bold")).place(x=20, y=140)
                tr3 = Label(cs03, text=trandet[5]["T6"][0] + "    " + trandet[5]["T6"][1] + "             " +
                                       trandet[5]["T6"][2] + "            " + trandet[5]["T6"][3] + "          " +
                                       trandet[5]["T6"][4], bg="#042148", fg="white",
                            font=("arial black ", 9, "bold")).place(x=20, y=170)
                tr4 = Label(cs03, text=trandet[4]["T5"][0] + "    " + trandet[4]["T5"][1] + "             " +
                                       trandet[4]["T5"][2] + "            " + trandet[4]["T5"][3] + "          " +
                                       trandet[4]["T5"][4], bg="#042148", fg="white",
                            font=("arial black ", 9, "bold")).place(x=20, y=200)
            elif how_many_tranix == 6:
                tr1 = Label(cs03, text=trandet[7]["T8"][0] + "    " + trandet[7]["T8"][1] + "             " +
                                       trandet[7]["T8"][2] + "          " + trandet[7]["T8"][3] + "          " +
                                       trandet[7]["T8"][4], bg="#042148", fg="white",
                            font=("arial black ", 9, "bold")).place(x=20, y=110)
                tr2 = Label(cs03, text=trandet[6]["T7"][0] + "    " + trandet[6]["T7"][1] + "             " +
                                       trandet[6]["T7"][2] + "          " + trandet[6]["T7"][3] + "          " +
                                       trandet[6]["T7"][4], bg="#042148", fg="white",
                            font=("arial black ", 9, "bold")).place(x=20, y=140)
                tr3 = Label(cs03, text=trandet[5]["T6"][0] + "    " + trandet[5]["T6"][1] + "             " +
                                       trandet[5]["T6"][2] + "          " + trandet[5]["T6"][3] + "          " +
                                       trandet[5]["T6"][4], bg="#042148", fg="white",
                            font=("arial black ", 9, "bold")).place(x=20, y=170)
                tr4 = Label(cs03, text=trandet[4]["T5"][0] + "    " + trandet[4]["T5"][1] + "             " +
                                       trandet[4]["T5"][2] + "          " + trandet[4]["T5"][3] + "          " +
                                       trandet[4]["T5"][4], bg="#042148", fg="white",
                            font=("arial black ", 9, "bold")).place(x=20, y=200)
                tr5 = Label(cs03, text=trandet[3]["T4"][0] + "    " + trandet[3]["T4"][1] + "             " +
                                       trandet[3]["T4"][2] + "          " + trandet[3]["T4"][3] + "          " +
                                       trandet[3]["T4"][4], bg="#042148", fg="white",
                            font=("arial black ", 9, "bold")).place(x=20, y=230)
                tr6 = Label(cs03, text=trandet[2]["T3"][0] + "    " + trandet[2]["T3"][1] + "             " +
                                       trandet[2]["T3"][2] + "          " + trandet[2]["T3"][3] + "          " +
                                       trandet[2]["T3"][4], bg="#042148", fg="white",
                            font=("arial black ", 9, "bold")).place(x=20, y=260)
            elif how_many_tranix == 8:
                tr1 = Label(cs03, text=trandet[7]["T8"][0] + "    " + trandet[7]["T8"][1] + "             " +
                                       trandet[7]["T8"][2] + "          " + trandet[7]["T8"][3] + "          " +
                                       trandet[7]["T8"][4], bg="#042148", fg="white",
                            font=("arial black ", 9, "bold")).place(x=20, y=110)
                tr2 = Label(cs03, text=trandet[6]["T7"][0] + "    " + trandet[6]["T7"][1] + "             " +
                                       trandet[6]["T7"][2] + "          " + trandet[6]["T7"][3] + "          " +
                                       trandet[6]["T7"][4], bg="#042148", fg="white",
                            font=("arial black ", 9, "bold")).place(x=20, y=140)
                tr3 = Label(cs03, text=trandet[5]["T6"][0] + "    " + trandet[5]["T6"][1] + "             " +
                                       trandet[5]["T6"][2] + "          " + trandet[5]["T6"][3] + "          " +
                                       trandet[5]["T6"][4], bg="#042148", fg="white",
                            font=("arial black ", 9, "bold")).place(x=20, y=170)
                tr4 = Label(cs03, text=trandet[4]["T5"][0] + "    " + trandet[4]["T5"][1] + "             " +
                                       trandet[4]["T5"][2] + "          " + trandet[4]["T5"][3] + "          " +
                                       trandet[4]["T5"][4], bg="#042148", fg="white",
                            font=("arial black ", 9, "bold")).place(x=20, y=200)
                tr5 = Label(cs03, text=trandet[3]["T4"][0] + "    " + trandet[3]["T4"][1] + "             " +
                                       trandet[3]["T4"][2] + "          " + trandet[3]["T4"][3] + "          " +
                                       trandet[3]["T4"][4], bg="#042148", fg="white",
                            font=("arial black ", 9, "bold")).place(x=20, y=230)
                tr6 = Label(cs03, text=trandet[2]["T3"][0] + "    " + trandet[2]["T3"][1] + "             " +
                                       trandet[2]["T3"][2] + "          " + trandet[2]["T3"][3] + "          " +
                                       trandet[2]["T3"][4], bg="#042148", fg="white",
                            font=("arial black ", 9, "bold")).place(x=20, y=260)
                tr7 = Label(cs03, text=trandet[1]["T2"][0] + "    " + trandet[1]["T2"][1] + "             " +
                                       trandet[1]["T2"][2] + "          " + trandet[1]["T2"][3] + "          " +
                                       trandet[1]["T2"][4], bg="#042148", fg="white",
                            font=("arial black ", 9, "bold")).place(x=20, y=290)
                tr8 = Label(cs03, text=trandet[0]["T1"][0] + "    " + trandet[0]["T1"][1] + "             " +
                                       trandet[0]["T1"][2] + "          " + trandet[0]["T1"][3] + "          " +
                                       trandet[0]["T1"][4], bg="#042148", fg="white",
                            font=("arial black ", 9, "bold")).place(x=20, y=320)
        else:
             tmsg.showerror("PAIR MISMATCH","INCORRECT ACCOUNT NUMBER ")

    # LEFT MOST PANE ----------------------------------------------------------------------------------------------
    cs01 = Canvas(chktrns, width=360, height=800, bd='5', bg="#042148", highlightthickness=0.5)
    cs01.place(x=0, y=0)
    logo = ImageTk.PhotoImage(Image.open("top1.jpg"))
    cs01.create_image(10, 10, anchor='nw', image=logo)

    cs = Canvas(chktrns, width=360, height=800, bd='5', bg="#042148")
    cs.place(x=0, y=0)

    logo = ImageTk.PhotoImage(Image.open("top1.jpg"))
    cs.create_image(10, 10, anchor='nw', image=logo)
    lbhd = Label(cs, text="WELCOME", font=("arial black", 20, "bold", "underline"), bg="#042148", fg="white",justify=CENTER)
    lbhd.place(x=110, y=195)
    lab = Label(cs, text=username(), font=("arial black", 20, "bold"), bg="#042148", fg="white", justify=CENTER)
    lab.place(x=80, y=250)

    sblb = Label(text="\"Our Proud Partners\"", font=("Bradley Hand ITC", 22, "bold"), fg="white", bg="#042148",padx=10)
    sblb.place(x=25, y=400)

    image1 = ImageTk.PhotoImage(Image.open("axcp.png"))
    cs.create_image(25, 450, anchor='nw', image=image1)

    image2 = ImageTk.PhotoImage(Image.open("oip.jpg"))
    cs.create_image(200, 450, anchor='nw', image=image2)

    image3 = ImageTk.PhotoImage(Image.open("cbi.png"))
    cs.create_image(25, 620, anchor='nw', image=image3)

    image4 = ImageTk.PhotoImage(Image.open("H3.png"))
    cs.create_image(200, 619, anchor='nw', image=image4)

    # Right Panel =========================================================================c
    cs02 = Canvas(chktrns, width=860, height=55, bd='5', bg="#042148", highlightthickness=0)
    cs02.place(x=380, y=5)
    heading01 = Label(cs02, text="• ● FETCH YOUR TRANSACTION DETAILS ● •", font=("Franklin Gothic Demi", 26, "bold"),bg="#042148", fg="#fff").place(x=70, y=12)

    # enter details FORM ===================================================================

    cs04 = Canvas(chktrns, width=400, height=420, bd='5', bg="#042148", highlightthickness=0, relief="ridge")
    cs04.place(x=400, y=90)
    heading02 = Label(cs04, text="• ENTER DETAILS •", font=("Franklin Gothic Demi", 19, "bold"), bg="#042148",fg="#fff").place(x=90, y=25)
    Line = cs04.create_line(117, 70, 300, 70, fill="#05a9ea", width=4)

    GID = Label(cs04, text="GLOBE-XS ID              "+g, font=("Franklin Gothic Demi", 15, "bold"), bg="#042148", fg="#fff").place(x=30, y=110)
    ACN = Label(cs04, text="ACCOUNT NO", font=("Franklin Gothic Demi", 15, "bold"), bg="#042148", fg="#fff").place(x=30,y=160)
    txt_ACN = Entry(cs04, font=("times new roman", 15), bg="#042148", fg="white", bd=4, textvariable=acc).place(x=210,y=160,width=170)
    TRS = Label(cs04, text="TRANSACTIONS", font=("Franklin Gothic Demi", 15, "bold"), bg="#042148", fg="#fff").place(x=30, y=210)
    txt_TRS = Spinbox(cs04, font=("times new roman", 15), bd=3, values=('Last 2', 'Last 4', 'Last 6', 'Last 8'),state="readonly", textvariable=notr).place(x=210, y=210, width=170)
    BK = Label(cs04, text="BANK", font=("Franklin Gothic Demi", 15, "bold"), bg="#042148", fg="#fff").place(x=30, y=260)
    txt_BK = Spinbox(cs04, font=("times new roman", 15), bd=3,values=('AXIS BANK', 'ICICI BANK', 'HDFC BANK', 'CENTRAL BANK'), state="readonly",textvariable=bank).place(x=210, y=260, width=170)

    # display area ======================================================================

    cs03 = Canvas(chktrns, width=400, height=420, bd='5', bg="#042148", highlightthickness=0, relief="ridge")
    cs03.place(x=820, y=90)
    heading03 = Label(cs03, text="• YOUR TRANSACTIONS •", font=("Franklin Gothic Demi", 19, "bold"), bg="#042148",fg="#fff").place(x=50, y=25)
    Line = cs03.create_line(80, 70, 330, 70, fill="#05a9ea", width=4)
    trHEAD = Label(cs03, text="DATE                  AMOUNT    MODE    TIME         PLACE", bg="#042148", fg="white",font=("arial black ", 10, "bold")).place(x=25, y=80)

    # Button 1  =========================================================================

    classButton = Button(chktrns, text="SHOW TRANSACTIONS", bg="#05a9ea", fg="White", cursor="hand2",font=("Franklin Gothic Demi", 15, "bold"), bd=3, command=valid1)
    classButton.place(x=440, y=550, width=330, height=40)

    FBKButton = Button(chktrns, text="FEEDBACK 🙂", bg="#05a9ea", fg="White", cursor="hand2",font=("Franklin Gothic Demi", 15, "bold"), bd=3,command=open_window_3)
    FBKButton.place(x=440, y=650, width=200, height=40)

    # BUTTON --------------------------------------------------------------------------------------------
    classButton = Button(chktrns, text="DONE   ✅", bg="#05a9ea", fg="White", cursor="hand2",font=("Franklin Gothic Demi", 15, "bold"), bd=3,command=open_window_3)
    classButton.place(x=970, y=550, width=130, height=40)

    chktrns.mainloop()

    #  BASE   WINDOW
#___________________________________________________________________________________________window charecterstics

root=Tk()
root.geometry("1250x800")
root.title("first page")
root.maxsize(1250,800)
root.minsize(1250,800)
result=list()
#-------------------------------------------------------------------------------------------MY GUI VARIABLES
uname=StringVar()
gbxd=StringVar()
pss=StringVar()
fgbxd=StringVar()
np=StringVar()
eOTP=StringVar()
sentotp=StringVar()
#--------------------------------------------------------------------------------------------MESSAGE BOX FOR EYE BUTTON
def visible():
    vp=pss.get()
    tmsg.showinfo("* PIN *",vp)


#--------------------------------------------------------------------------------------------VALIDATION WHEN YOU LOGIN
def validate1():
    u=uname.get()
    g=gbxd.get()
    p=pss.get()
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="11901811",
        database="mydatabase"
    )

    lg = (g,)
    mycs=mydb.cursor()
    sql=("SELECT * FROM PROJECT WHERE GBX_ID=%s")
    mycs.execute(sql,lg)
    result =mycs.fetchall()
    if len(result)!=0:
        err1.config(text="")
        if u==result[0][5]:
            err1.config(text="")
            err2.config(text="")
            if p==result[0][6]:
                err3.config(text="")
                del result[:]
                open_window_2(g)
            else:
                err3.config(text="*")
        else:
            if p == result[0][6]:
                err3.config(text="")
            else:
                err3.config(text="*")
            err2.config(text="*")
    else:
        err2.config(text="")
        err3.config(text="")
        err1.config(text="*")
#----------------------------------------------------------------------------------FUNCTION INVOLVED IN CHANGING PASWORD(finish())
def finish():
    if (sentotp.get() == eOTP.get()):
        n = fgbxd.get()
        p = np.get()
        qtuple=(p,n)
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="11901811",
            database="mydatabase"
        )
        mycs = mydb.cursor()
        sql = ("UPDATE project SET password=%s WHERE GBX_ID=%s")
        mycs.execute(sql, qtuple)
        mydb.commit()
        frame1bg.config(height=340)
        frame1.config(height=330)
        cvline.config(width=0, height=0)
        tmsg.showinfo("*SUCCESS*", "Your Password Was Sucessfully Reset!!")
    else:
        err5.config(text="*")
#-------------------------------------------------------------------------------------FUNCTION INVOLVED IN CHANGING PASWORD(sendotp())
def sendotp(towhom):
    f = open("otp.txt", "rb")
    l = pickle.load(f)
    sotp=l[rd.randint(0, 49)]
    f.close()

    sentotp.set(sotp)

    f = open("passwordofemail.txt", "rb")
    epss = pickle.load(f)
    f.close()

    content = "This is your GLOBE-XS OTP.Please confirm by entering this OTP that you were trying to reset the password through our app."
    MSG="Your One Time Password   "+sotp+"   (ALL RIGHTS RESERVED TO GLOBE-XS)  Regards Technical Team GLOBE-XS (India)"
    message="subject:{}\n\n{}".format(content,MSG)
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login("studybuddy162@gmail.com",epss[0])
    server.sendmail("studybuddy@162gmail.com",towhom,message)
    server.quit()

    reset = Button(frame1, text="RESET", font=("Franklin Gothic Demi", 12, "bold"), bg="#05a9ea", fg="White", padx=2,pady=0, bd=4, command=finish, width=12)
    reset.place(x=460, y=381)
#--------------------------------------------------------------------------------------------------FUNCTION INVOLVED IN CHANGING PASWORD(VALIDATE 2)
def validate2():
    global err4
    n=fgbxd.get()
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="11901811",
        database="mydatabase"
    )
    mycs = mydb.cursor()
    tn=(n,)
    sql = ("SELECT * FROM project WHERE GBX_ID=%s")
    mycs.execute(sql,tn)
    result=mycs.fetchall()
    if len(result)!=0:
        sendotp(result[0][4])
    else:
        err4.config(text="*")

#--------------------------------------------------------------------------------------------------FUNCTION INVOLVED IN CHANGING PASWORD(changepass())
def changepass():
    global err4
    global cvline
    global err5
    frame1bg.config(height=440)
    frame1.config(height=430)
    cvline = Canvas(frame1, width=700, height=5,bg="grey",highlightthickness=0)
    cvline.place(x=0, y=313)
    err4=Label(frame1,text="",fg="red",font=("Franklin Gothic Demi",18,"bold"),bg="#042148")
    err4.place(x=12,y=336)
    fgid=Label(frame1,text="● GLOBE-XS ID",fg="white",font=("Franklin Gothic Demi",14),bg="#042148")
    fgid.place(x=30,y=336)
    efgid=Entry(frame1,font=("Times New Roman",14,"bold"),textvariable=fgbxd,bd=5,bg="#042148",fg="White",width=12)
    efgid.place(x=170,y=331)
    npass=Label(frame1,text="● NEW PASSWORD",fg="white",font=("Franklin Gothic Demi",14),bg="#042148")
    npass.place(x=320,y=336)
    enpass = Entry(frame1, font=("Times New Roman", 14,"bold"), textvariable=np, bd=5, bg="#042148", fg="White",width = 8)
    enpass.place(x=500, y=331)
    err5 = Label(frame1, text="", fg="red", font=("Franklin Gothic Demi", 18, "bold"), bg="#042148")
    err5.place(x=12, y=381)
    otp = Label(frame1, text="● OTP", fg="white", font=("Franklin Gothic Demi", 14), bg="#042148")
    otp.place(x=30, y=381)
    eotp = Entry(frame1, font=("Times New Roman", 14, "bold"), textvariable=eOTP, bd=5, bg="#042148", fg="White",width=8)
    eotp.place(x=170, y=381)
    os = Button(frame1, text="SEND", font=("Franklin Gothic Demi", 12, "bold"), bg="#05a9ea", fg="White", padx=2,pady=0, bd=4, command=validate2, width=5)
    os.place(x=300, y=381)

#--------------------------------------------------------------------------------------------------FUNCTION FOR GENERATING DYNAMIC TIPS
#def tipgen():
#    l = ["USE ADVANCED ANTI-MALWARE PROGRAM", "WATCH OUT FOR SECURITY VUNERABILITIES IN YOUR PC",
#         "USE CREDIT CARDS FOR ONLINE SHOPPING", "DO NOT USE PUBLIC COMPUTERS", "SET A STRONG AND COMPLEX PASSWORD",
#         "KEEP DISTANCE FROM UNAUTHORISED LINKS", "USE SECURE Wi-Fi CONNECTION"]
#    t = rd.randint(0, 6)
#    f = open("tips.txt", "rb")
#    tiphead = l[t]
#    tip = pickle.load(f)
#    tp=tip[tiphead]
#    ct=tiphead+":"+tp
#    return ct
#___________________________________________________________________________window designing
canvas = Canvas(root, width=1250, height=800)
canvas.place(x=0,y=0)
imageBG = ImageTk.PhotoImage(Image.open("nb.jpg"))
canvas.create_image(0, 0, anchor='nw', image=imageBG)

# -----------------------------------------------------------------------------------------------------LOGIN MENU
frame1bg=Frame(root,height=340,width=640,bg="grey")##0b45b4
frame1bg.place(x=450,y=30)
frame1=Frame(frame1bg,bg="#042148",height=330,width=630)
frame1.place(x=5,y=5)

lcs=Canvas(frame1,height=60,width=240,bg="#042148",bd=0,highlightthickness=0)
lcs.place(x=0,y=0)
ll1=lcs.create_line(20,30,240,30,width=4,fill="white")
ll2=lcs.create_line(50,50,240,50,width=4,fill="#05a9ea")

rcs=Canvas(frame1,height=60,width=240,bg="#042148",bd=0,highlightthickness=0)
rcs.place(x=380,y=0)
rl1=rcs.create_line(0,30,220,30,width=4,fill="white")
rl2=rcs.create_line(0,50,190,50,width=4,fill="#05a9ea")

LOG=Label(frame1,text="LOGIN",fg="white",font=("Franklin Gothic Demi",30,"bold"),bg="#042148")
LOG.place(x=250,y=10)

gbxid=Label(frame1,text="GLOBE-XS ID",fg="white",font=("Franklin Gothic Demi",18,"bold"),bg="#042148",justify=CENTER)
gbxid.place(x=80,y=80)
err1=Label(frame1,text="",fg="red",font=("Franklin Gothic Demi",18,"bold"),bg="#042148",justify=CENTER)
err1.place(x=260,y=81)
eun=Entry(frame1,font=("Times New Roman",18),textvariable=gbxd,bd=5,bg="#042148",fg="White")
eun.place(x=300,y=80)

un=Label(frame1,text="USER NAME",fg="white",font=("Franklin Gothic Demi",18,"bold"),bg="#042148",justify=CENTER)
un.place(x=80,y=135)
err2=Label(frame1,text="",fg="red",font=("Franklin Gothic Demi",18,"bold"),bg="#042148",justify=CENTER)
err2.place(x=260,y=136)
egbxid=Entry(frame1,font=("Times New Roman",18),textvariable=uname,bd=5,bg="#042148",fg="White")
egbxid.place(x=300,y=135)

pin=Label(frame1,text="PIN",fg="white",font=("Franklin Gothic Demi",18,"bold"),bg="#042148",justify=CENTER)
pin.place(x=80,y=190)
epin=Entry(frame1,font=("Times New Roman",18),show="*",textvariable=pss,bd=5,bg="#042148",fg="White",width=8,justify=CENTER)
epin.place(x=300,y=190)
err3=Label(frame1,text="",fg="red",font=("Franklin Gothic Demi",18,"bold"),bg="#042148",justify=CENTER)
err3.place(x=260,y=191)
pht=ImageTk.PhotoImage(file=r"myb.png")
eyebt=Button(frame1,image=pht,height=40,width=38,bg="#042148",bd=0,activebackground="#042148",command=visible)
eyebt.place(x=520,y=190)

login=Button(frame1,text="LOGIN",font=("Franklin Gothic Demi",14),bg="#05a9ea",fg="White",padx=2,bd=4,command=validate1)
login.place(x=190,y=250)
fpass=Button(frame1,text="FORGOT PASSWORD",font=("Franklin Gothic Demi",14),bg="#05a9ea",fg="White",padx=2,bd=4,command=changepass)
fpass.place(x=290,y=250)

#-------------------------------------------------------------------------------------------------------------------------new user sign up
nufrbg=Frame(root,height=200,width=640,bg="grey")##0b45b4
nufrbg.place(x=450,y=465)
nufr=Frame(nufrbg,height=190,width=630,bg="#042148")##0b45b4
nufr.place(x=5,y=5)
intcvs=Canvas(nufr,height=190,width=190,bg="red",highlightthickness=0)
intcvs.place(x=440,y=0)
nwus = ImageTk.PhotoImage(Image.open("userlo.jpg"))
intcvs.create_image(6,0, anchor='nw',image=nwus)
s=intcvs.create_line(3,0,3,190,width=6,fill="grey")
intrlb1=Label(nufr,text="Do Not Have An Account Yet",font=("cavolini",20,"italic","bold"),fg="white",bg="#042148",padx=10)
intrlb1.place(x=5,y=4)
intrlb2=Label(nufr,text="?",font=("cavolini",35,"bold"),fg="red",bg="#042148",padx=7,pady=0)
intrlb2.place(x=387,y=-5)
intrlb3=Label(nufr,text="Get A New One Just On A Click",font=("cavolini",14,"italic","bold"),fg="white",bg="#042148",padx=10)
intrlb3.place(x=50,y=40)
regnow=Button(nufr,text="REGISTER NOW >>",font=("Franklin Gothic Demi",12),bg="#05a9ea",fg="White",padx=2,pady=0,bd=4,command=open_window_3)
regnow.place(x=150,y=80)
intrlb3=Label(nufr,text="We Assure Safer Transactions And ",font=("Bradley Hand ITC",18,"bold"),fg="white",bg="#042148",padx=10)
intrlb3.place(x=18,y=130)
intrlb4=Label(nufr,text="Stronger Relations ",font=("Bradley Hand ITC",18,"bold"),fg="white",bg="#042148",padx=10,justify=CENTER)
intrlb4.place(x=100,y=155)
# ----------------------------------------------------------------------------------------------SIDE PANE
cs = Canvas(root, width=360, height=800,bd='5',bg="#042148")
cs.place(x=0, y=0)

logo = ImageTk.PhotoImage(Image.open("top1.jpg"))
cs.create_image(10,10, anchor='nw', image=logo)
lbhd=Label(cs,text="TIP OF THE DAY",font=("arial black",13,"bold","underline"),bg="#042148",fg="white",justify=CENTER)
lbhd.place(x=110,y=195)
#tod=Label(cs,text=tipgen(),font=("arial black",11),wraplength=310,bg="#042148",fg="white",justify=CENTER,pady=4,padx=10)
#tod.place(x=20,y=220)
sblb=Label(text="\"Our Proud Partners\"",font=("Bradley Hand ITC",22,"bold"),fg="white",bg="#042148",padx=10)
sblb.place(x=25,y=400)
image1 = ImageTk.PhotoImage(Image.open("axcp.png"))
cs.create_image(25,450, anchor='nw', image=image1)

image2 = ImageTk.PhotoImage(Image.open("oip.jpg"))
cs.create_image(200,450, anchor='nw', image=image2)

image3 = ImageTk.PhotoImage(Image.open("cbi.png"))
cs.create_image(25,620 , anchor='nw', image=image3)

image4 = ImageTk.PhotoImage(Image.open("H3.png"))
cs.create_image(200,619, anchor='nw', image=image4)

pht1=ImageTk.PhotoImage(file=r"userlo.jpg")
assist=Button(root,image=pht1,text=" ASSISTANCE  ",compound=RIGHT,height=43,width=170,font=("Franklin Gothic Demi",14),bg="white",fg="#05a9ea",bd=4,activebackground="#042148",command=assistant)
assist.place(x=910,y=700)

rt=Entry()
root.mainloop()
