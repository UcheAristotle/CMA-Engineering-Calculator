from tkinter import *
import time
from tkinter import messagebox

from tkinter import ttk,Tk, StringVar

#=================================================Root Window=======================================================
root = Tk()
root.geometry("950x600+0+0")
root.title("ATM")
root.config(bg="#728B8E")
icon = PhotoImage(file="icon7.gif")
root.call("wm",'iconphoto',root._w,icon)



#=================================================Variables============================================================
var2 = StringVar()
var1 = StringVar()
text_Input = DoubleVar()
var4 = IntVar()
text_Input.set("")
operator = ""
localtime = time.asctime(time.localtime(time.time()))
balance = DoubleVar()
result = DoubleVar()
exchange = StringVar()
currency = DoubleVar()
convert = DoubleVar()

#================================================Functions=============================================================

#=============================================Quit Function============================================================
def qExit():
    qExit = messagebox.askyesno("End Transaction!", "Are You Sure You Want To End The Transaction?")
    if qExit > 0:
        root.destroy()
        return
#=============================================Enter Function============================================================
def Enter():
    if var2.get() =="":
        var1.set("Oops! Please Enter Your Name to \nStart Transaction")

        btnA.config(state=NORMAL), btnB.config(state=NORMAL), btnC.config(state=NORMAL), btnD.config(state=NORMAL)
        btnE.config(state=NORMAL), btnF.config(state=NORMAL), btnG.config(state=NORMAL), btnH.config(state=NORMAL)
        btnI.config(state=NORMAL), btnJ.config(state=NORMAL), btnK.config(state=NORMAL), btnL.config(state=NORMAL)
        btnM.config(state=NORMAL), btnN.config(state=NORMAL), btnO.config(state=NORMAL), btnP.config(state=NORMAL)
        btnQ.config(state=NORMAL), btnR.config(state=NORMAL), btnS.config(state=NORMAL), btnT.config(state=NORMAL)
        btnU.config(state=NORMAL), btnV.config(state=NORMAL), btnX.config(state=NORMAL), btnY.config(state=NORMAL)
        btnZ.config(state=NORMAL), btnSpace.config(state=NORMAL), btnW.config(state=NORMAL)

    elif var2.get()== var2.get():
        var1.set("Welcome " + var2.get() + " \nPlease Click PROCEED to Continue")
        canvScreen.itemconfigure(canvas_text, text= "Dear "+var2.get() + ",\nThis Bank Takes 5% of All \nYour Transactions")
        var2.set("")
        instrucLabel.config(text="")
        var1.set("")
        instrucLabel.config(text="Are You OK With That? \nClick 'Proceed' to Continue Or 'Quit' to End \nTransaction")
        proceedLabel.config(text="PROCEED")
        entryScreen.config(state=DISABLED)
        btnScreen1.config(state=NORMAL)
        btnScreen2.config(state=DISABLED)
        #btnCLEAR.config(state=NORMAL)
        btnCANCEL.config(state=NORMAL)
        btnEnter.config(state=DISABLED)
        btnCLEAR.config(state=DISABLED)
        coverLabel.config(text="\t\t\t")
        var1.set("Do you know you can also \nconvert your currency using \nour conversion system?")
        label3.config(text="")

        btnA.config(state=DISABLED), btnB.config(state=DISABLED), btnC.config(state=DISABLED), btnD.config(state=DISABLED)
        btnE.config(state=DISABLED), btnF.config(state=DISABLED), btnG.config(state=DISABLED), btnH.config(state=DISABLED)
        btnI.config(state=DISABLED), btnJ.config(state=DISABLED), btnK.config(state=DISABLED), btnL.config(state=DISABLED)
        btnM.config(state=DISABLED), btnN.config(state=DISABLED), btnO.config(state=DISABLED), btnP.config(state=DISABLED)
        btnQ.config(state=DISABLED), btnR.config(state=DISABLED), btnS.config(state=DISABLED), btnT.config(state=DISABLED)
        btnU.config(state=DISABLED), btnV.config(state=DISABLED), btnX.config(state=DISABLED), btnY.config(state=DISABLED)
        btnZ.config(state=DISABLED), btnSpace.config(state=DISABLED), btnW.config(state=DISABLED), \
        btnPeriod.config(state=DISABLED), btnScreen3.config(state=DISABLED)
#=============================================Preceed Function============================================================
def Proceed():
    entryMoney.config(state=NORMAL)
    var1.set("")
    btnEnter.config(state=DISABLED)
    entryScreen.config(state=DISABLED)
    label1.config(text="Please Enter \nAmount Here")
    label4.config(image=iconPhoto1)
    canvScreen.itemconfigure(canvas_text,
                             text="Please Enter The Amount \nYou Want To Withdraw")
    label2.config(text="PROCEED")
    btnScreen2.config(state=NORMAL)
    btnScreen1.config(state=DISABLED)
    proceedLabel.config(text="")
    text_Input.set("")
    instrucLabel.config(text="")
    coverLabel.config(text="Our Min. Withdrawal Amount Is N500")
    #canvScreen.itemconfigure(canvas_text, text="")
    btnNum1.config(state=NORMAL), btnNum2.config(state=NORMAL), btnNum3.config(state=NORMAL), \
    btnNum4.config(state=NORMAL), btnNum0.config(state=NORMAL), btnNum8.config(state=NORMAL)
    btnNum5.config(state=NORMAL), btnNum6.config(state=NORMAL), btnNum7.config(state=NORMAL), \
    btnNum9.config(state=NORMAL), btnNumPoint.config(state=NORMAL), btnCLEAR.config(state=NORMAL)
    text_Input.set("")
    global operator
    operator = ("")


#================================================Withdrawal Function===================================================
def Balance():
    b = 1000000
    t = text_Input.get()
    result = b - t


    if text_Input.get() >= b:
        var1.set("Sorry. You Have Insufficient Balance. \nPlease Reduce The Amount")

    elif text_Input.get() < 500:
        var1.set("Sorry! You can Only Withdraw \nFrom N500 And Above \nIncrease And Try Again")

    elif text_Input.get() == "":
        var1.set("You Have Not Put Any Amount")

    else:
        var1.set("Please Do Take Your Cash....! \n\nYour Balance is N%.2f" % result)

    var2.set("")
    label1.config(text="")
    label2.config(text="")
    btnScreen2.config(state=DISABLED)
    canvScreen.itemconfigure(canvas_text, text="Thank You for Banking With Us. \nDo You Want to Perform \nAnother "
                                               "Transaction?")
    instrucLabel.config(text="\nClick 'Return' to Continue Or 'Quit' to End \nTransaction")
    text_Input.set("")
    entryMoney.config(state=DISABLED)
    coverLabel.config(text="\t\t\t")
    btnNum1.config(state=DISABLED), btnNum2.config(state=DISABLED), btnNum3.config(state=DISABLED), \
    btnNum4.config(state=DISABLED), btnNum0.config(state=DISABLED), btnNum8.config(state=DISABLED)
    btnNum5.config(state=DISABLED), btnNum6.config(state=DISABLED), btnNum7.config(state=DISABLED), \
    btnNum9.config(state=DISABLED), btnNumPoint.config(state=DISABLED)
    label3.config(text="RETURN")
    btnScreen3.config(state=NORMAL)
    label4.config(image="")
    var2.set("")
    global operator
    operator = ("")
#=============================================Cancel Function============================================================
def Cancel():
    var1.get()
    var2.set("")
    instrucLabel.config(text="")
    canvScreen.itemconfigure(canvas_text, text="Please Enter Your Name  \nto \nContinue")
    btnEnter.config(state=NORMAL)
    entryScreen.config(state=NORMAL)
    text_Input.set("")
    btnScreen1.config(state=DISABLED)
    label1.configure(text="")
    proceedLabel.config(text="")
    var1.set("Do you know you can also \nconvert your currency using \nour conversion system?")
    entryMoney.config(state=DISABLED)
    label2.config(text="")
    coverLabel.config(text="")

    if var2.get() =="":
        var1.set("Go Ahead..! \nThe Screen Has Been Clear")

    elif var2.get()== var2.get():
        var1.set("Welcome " + var2.get() + " \nPlease Click PROCEED to Continue")


    btnA.config(state=NORMAL), btnB.config(state=NORMAL), btnC.config(state=NORMAL), btnD.config(state=NORMAL)
    btnE.config(state=NORMAL), btnF.config(state=NORMAL), btnG.config(state=NORMAL), btnH.config(state=NORMAL)
    btnI.config(state=NORMAL), btnJ.config(state=NORMAL), btnK.config(state=NORMAL), btnL.config(state=NORMAL)
    btnM.config(state=NORMAL), btnN.config(state=NORMAL), btnO.config(state=NORMAL), btnP.config(state=NORMAL)
    btnQ.config(state=NORMAL), btnR.config(state=NORMAL), btnS.config(state=NORMAL), btnT.config(state=NORMAL)
    btnU.config(state=NORMAL), btnV.config(state=NORMAL), btnX.config(state=NORMAL), btnY.config(state=NORMAL)
    btnZ.config(state=NORMAL), btnSpace.config(state=NORMAL), btnW.config(state=NORMAL),btnPeriod.config(state=NORMAL)

    var2.set("")
    text_Input.set("")
    global operator
    operator = ("")


#=============================================Clear Function============================================================
def Clear():
    var2.set("")
    text_Input.set("")
    global operator
    operator = ("")
#=============================================Number Function===========================================================
def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)
#=============================================Return Function===========================================================
def Return():
    var1.get()
    instrucLabel.config(text="")
    canvScreen.itemconfigure(canvas_text, text="Please Enter Your Name  \nto \nContinue")
    btnEnter.config(state=NORMAL)
    entryScreen.config(state=NORMAL)
    btnScreen1.config(state=DISABLED)
    label1.configure(text="")
    proceedLabel.config(text="")
    entryMoney.config(state=DISABLED)
    label3.config(text="")
    label2.config(text="")
    btnScreen3.config(state=DISABLED)
    var2.set("")
    text_Input.set("")
    global operator
    operator = ("")
    btnCLEAR.config(state=NORMAL)
    coverLabel.config(text="")
    label3.config(text="")
    label4.config(image="")
    var1.set("Please We Will Like To Have \nYour Feedback: \nCall Us On 08069900222")

    btnA.config(state=NORMAL), btnB.config(state=NORMAL), btnC.config(state=NORMAL), btnD.config(state=NORMAL)
    btnE.config(state=NORMAL), btnF.config(state=NORMAL), btnG.config(state=NORMAL), btnH.config(state=NORMAL)
    btnI.config(state=NORMAL), btnJ.config(state=NORMAL), btnK.config(state=NORMAL), btnL.config(state=NORMAL)
    btnM.config(state=NORMAL), btnN.config(state=NORMAL), btnO.config(state=NORMAL), btnP.config(state=NORMAL)
    btnQ.config(state=NORMAL), btnR.config(state=NORMAL), btnS.config(state=NORMAL), btnT.config(state=NORMAL)
    btnU.config(state=NORMAL), btnV.config(state=NORMAL), btnX.config(state=NORMAL), btnY.config(state=NORMAL)
    btnZ.config(state=NORMAL), btnSpace.config(state=NORMAL), btnW.config(state=NORMAL), btnPeriod.config(state=NORMAL)

#============================Letters Function============================================================
def btnClick1(text):
    global operator
    operator = operator + str(text)
    var2.set(operator)

#======================================Top Level Frame Windows=============================================

def ConvertCurrency():
    if exchange.get() == "US Dollar":
        convert1 = float(convert.get()/360)
        convert2 = "USD", str("%.2f"%(convert1))
        currency.set(convert2)
    if exchange.get() == "Euro":
        convert1 = float(convert.get()/442.666)
        convert2 = "EUR", str("%.2f"%(convert1))
        currency.set(convert2)
    if exchange.get() == "Canada":
        convert1 = float(convert.get()/274.899)
        convert2 = "CAD", str("%.2f"%(convert1))
        currency.set(convert2)
    if exchange.get() == "Dutch":
        convert1 = float(convert.get()/201.963)
        convert2 = "ANG", str("%.2f"%(convert1))
        currency.set(convert2)
    if exchange.get() == "Pound":
        convert1 = float(convert.get()/502.072)
        convert2 = "GBP", str("%.2f"%(convert1))
        currency.set(convert2)
    if exchange.get() == "Krone":
        convert1 = float(convert.get()/46.69)
        convert2 = "DKK", str("%.2f"%(convert1))
        currency.set(convert2)

def btnClick2(number):
    global operator
    operator = operator + str(number)
    convert.set(operator)

def ConvClear():
    global operator
    operator = ""
    convert.set("0.0")
    currency.set("0.0")
    exchange.set("US Dollar")


top = Frame(root, width=950, bg="#728B8E", height=20)
top.pack(side=TOP)

topLabel = Label(top, font=("arial", 26,"bold"), bg="#50A8B0", text="\t\t\t\tBank of Youth for Technology Foundation"
                                                                    " ATM\t\t\t\t", bd=2, relief=GROOVE)
topLabel.pack(fill=X)


small_frame = Frame(top, width=950, bg="#728B8E", height=20)
small_frame.pack()

mainFrame_left = Frame(root, width=950*2/3, bg="#728B8E", height=550)
mainFrame_left.pack(side=LEFT, expand=True)

mainFrame_right = Frame(root, width=950/3, bg="#728B8E", height=550)
mainFrame_right.pack(side=RIGHT, expand=True)

screenFrame = LabelFrame(mainFrame_left, width=950*2/3, height=350, bg="#728B8E", font=("arial", 14, "bold"), text="ATM System")
screenFrame.pack(side=TOP, padx=30, pady=20, anchor=N)

propFrame = LabelFrame(mainFrame_right, width=950/3, height=350, bg="#728B8E", font=("arial", 14, "bold"),
                       text="Currency Converter")
propFrame.pack(padx=20, pady=20, anchor=N)

frame2 = Frame(propFrame, width=950/3, bg="#728B8E", height=200)
frame2.grid(row=1, column=0)

buttonFrameL = LabelFrame(mainFrame_left, width=950*2/3, height=200, bg="#728B8E", font=("arial", 14, "bold"),
                          text="Control Keys")
buttonFrameL.pack(side=BOTTOM, padx=30, pady=20, anchor=N)
#======================================================Screens==========================================================
convertLabelF = Label(frame2, text="\t  Convert To", font=("arial", 11, "normal"), bg="#728B8E")
convertLabelF.grid(row=0, column=0, sticky=W)

cmBox = ttk.Combobox(frame2, font=("arial", 8, "bold"), textvariable=exchange, width=8, state="randomly")
cmBox["value"] = ("US Dollar", "Canada", "Dutch", "Euro" , "Krone", "Pound")
cmBox.current(0)
cmBox.grid(row=0, column=0, sticky=W, padx=3, pady= 5)

convertLabelT = Label(frame2, text="\t  NGN: Convert From Naira  ", font=("arial", 11, "normal"), bg="#728B8E")
convertLabelT.grid(row=1, column=0, sticky=W)

entryConvert = Entry(frame2, font=("arial", 8, "bold"), textvariable=convert, width=11, bd=2, relief=RIDGE)
entryConvert.grid(row=1, column=0, sticky=W, padx=4, pady=3)

frameBtn =Frame(frame2, relief=FLAT , bg="#728B8E")
frameBtn.grid(row=3, column=0, sticky=W)

clearConvBtn = Button(frameBtn, text="CLEAR", font=("arial", 8, "bold"), width=13, bd=2, bg="#50A8B0",  relief=GROOVE,
                      command=ConvClear)
clearConvBtn.grid(row=4, column=0, columnspan=4, padx=1, pady=1, sticky=W)

convertButton = Button(frameBtn, text="CONVERT", font=("arial", 8, "bold"), bd=2, bg="#50A8B0",
                       command= ConvertCurrency, relief=GROOVE)
convertButton.grid(row=3, column=2,  padx=1, pady=2)

btnConv1 = Button(frameBtn, text="1", font=("arial", 8, "bold"), bd=2, width=3, bg="#50A8B0",relief=GROOVE,
                  command=lambda:btnClick2(1))
btnConv1.grid(row=0, column=0, padx=1, pady=2)
btnConv2 = Button(frameBtn, text="2", font=("arial", 8, "bold"), bd=2, width=3,bg="#50A8B0", relief=GROOVE,
                  command=lambda:btnClick2(2))
btnConv2.grid(row=0, column=1, padx=1, pady=2)
btnConv3 = Button(frameBtn, text="3", font=("arial", 8, "bold"), bd=2, width=3,bg="#50A8B0", relief=GROOVE,
                  command=lambda:btnClick2(3))
btnConv3.grid(row=0, column=2,padx=1, pady=2, sticky=W)
btnConv4 = Button(frameBtn, text="4", font=("arial", 8, "bold"), bd=2, width=3, bg="#50A8B0",relief=GROOVE,
                  command=lambda:btnClick2(4))
btnConv4.grid(row=1, column=0,padx=1, pady=2)
btnConv5 = Button(frameBtn, text="5", font=("arial", 8, "bold"), bd=2, width=3, bg="#50A8B0",relief=GROOVE,
                  command=lambda:btnClick2(5))
btnConv5.grid(row=1, column=1,padx=1, pady=2)

btnConv6 = Button(frameBtn, text="6", font=("arial", 8, "bold"), bd=2, width=3,bg="#50A8B0", relief= GROOVE,
                  command=lambda:btnClick2(6))
btnConv6.grid(row=1, column=2,padx=1, pady=2, sticky=W)
btnConv7 = Button(frameBtn, text="7", font=("arial", 8, "bold"), bd=2, width=3, bg="#50A8B0",relief=GROOVE,
                  command=lambda:btnClick2(7))
btnConv7.grid(row=2, column=0,padx=1, pady=2)
btnConv8 = Button(frameBtn, text="8", font=("arial", 8, "bold"), bd=2, width=3, bg="#50A8B0",relief=GROOVE,
                  command=lambda:btnClick2(8))
btnConv8.grid(row=2, column=1,padx=1, pady=2)
btnConv9 = Button(frameBtn, text="9", font=("arial", 8, "bold"), bd=2, width=3,bg="#50A8B0", relief=GROOVE,
                  command=lambda:btnClick2(9))
btnConv9.grid(row=2, column=2,padx=1, pady=2, sticky=W)
btnConv0 = Button(frameBtn, text="0", font=("arial", 8, "bold"), bd=2, width=3, bg="#50A8B0",relief=GROOVE,
                  command=lambda:btnClick2(0))
btnConv0.grid(row=3, column=0,padx=1, pady=2)
btnConvPoint = Button(frameBtn, text=".", font=("arial", 8, "bold"), bd=2, width=3,  bg="#50A8B0",relief=GROOVE,
                      command=lambda:btnClick2("."))
btnConvPoint.grid(row=3, column=1,padx=2, pady=2)

imageMoney = PhotoImage(file="moneyImage.png")

canv3 = Canvas(frameBtn, width= 150, height=70)
canv3.grid(row=0, column=3, rowspan=3)

canv3.create_image(77,37, image=imageMoney)

canv1 = Canvas(screenFrame, width=600, height=250, bg="#728B8E", relief=FLAT)
canv1.grid(row=0,  columnspan= 10, padx=30, pady=30)

canv2 = Canvas(propFrame,  height=170, bg="steel blue", width=280, bd=4, relief=RIDGE)
canv2.grid(row=0, column=0, padx=10, pady=30, sticky=W)

convFrame = Frame(propFrame, width=250, height=80, bg="light green", highlightthickness=2, highlightbackground="black", bd=3, relief=RIDGE)
convFrame.grid(row=0, column=0)

showCurrency = Label(propFrame, textvariable = currency, font=("arial", 12, "bold"), bg="light green")\
    .grid(row=0, column=0, sticky=W, padx=55)

iconPhoto3 = PhotoImage(file="image4.png", height=250)
canv2.create_image(100, 200, image=iconPhoto3)
iconPhoto4 = PhotoImage(file="imageYTF.png", height=250)
canv2.create_image(145, 130, image= iconPhoto4)


frameScreenL = Frame(canv1, bg="#728B8E", width=50, height=100)
frameScreenL.grid(row=1, column=0)

canvScreen = Canvas(canv1, width=400, height=200, bd=4, bg="steel blue", relief=RIDGE)
canvScreen.grid(row=1, column=1)

frameScreenR = Frame(canv1, width=50, bg="#728B8E", height=200)
frameScreenR.grid(row=1, column=2)

canvas_text = canvScreen.create_text(110, 20, text='', font="bold", anchor=NW, justify="center", fill="white")
test_string = "Welcome to Bank YTF...\nWe are Happy to Serve You"
delta = 50
delay=0
for i in range (len(test_string)+1):
    s = test_string[:i]
    update_text = lambda s=s: canvScreen.itemconfigure(canvas_text, text=s)
    canvScreen.after(delay, update_text)
    delay += delta

iconPhoto = PhotoImage(file="icon5.png")
iconPhoto1 = PhotoImage(file="icon6.png")
iconPhoto2 = PhotoImage(file="icon4.png")

#=============================================Buttons================================================================

#===========================================Number Buttons===========================================================
btnNum1 = Button(screenFrame, text="1", width=5, height=1, relief=GROOVE, bg="#50A8B0", command = lambda:btnClick(1))
btnNum1.grid(row=1, column=0, padx=1, pady=4)
btnNum2 = Button(screenFrame, text="2", width=5, height=1, relief=GROOVE, bg="#50A8B0", command = lambda:btnClick(2))
btnNum2.grid(row=1, column=1, padx=1, pady=4)
btnNum3 = Button(screenFrame, text="3", width=5, height=1, relief=GROOVE, bg="#50A8B0", command = lambda:btnClick(3))
btnNum3.grid(row=1, column=2, padx=1, pady=4)
btnNum4 = Button(screenFrame, text="4", width=5, height=1, relief=GROOVE, bg="#50A8B0", command = lambda:btnClick(4))
btnNum4.grid(row=1, column=3, padx=1, pady=4)
btnNum5 = Button(screenFrame, text="5", width=5, height=1, relief=GROOVE, bg="#50A8B0", command = lambda:btnClick(5))
btnNum5.grid(row=1, column=4, padx=1, pady=4)
btnNum6 = Button(screenFrame, text="6", width=5, height=1, relief=GROOVE, bg="#50A8B0", command = lambda:btnClick(6))
btnNum6.grid(row=1, column=5, padx=1, pady=4)
btnNum7 = Button(screenFrame, text="7", width=5, height=1, relief=GROOVE, bg="#50A8B0", command = lambda:btnClick(7))
btnNum7.grid(row=1, column=6, padx=1, pady=4)
btnNum8 = Button(screenFrame, text="8", width=5, height=1, relief=GROOVE, bg="#50A8B0", command = lambda:btnClick(8))
btnNum8.grid(row=1, column=7, padx=1, pady=4)
btnNum9 = Button(screenFrame, text="9", width=5, height=1, relief=GROOVE, bg="#50A8B0", command = lambda:btnClick(9))
btnNum9.grid(row=1, column=8, padx=1, pady=4)
btnNum0 = Button(screenFrame, text="0", width=5, height=1, relief=GROOVE, bg="#50A8B0", command = lambda:btnClick(0))
btnNum0.grid(row=1, column=9, padx=1, pady=4)
btnNumPoint = Button(screenFrame, text=".", width=5, height=1, relief=GROOVE, bg="#50A8B0", command = lambda:btnClick("."))
btnNumPoint.grid(row=1, column=10, padx=1, pady=4)

#===========================================Letter Buttons===========================================================

btnA = Button(frameScreenL, width=3, height=1, text="A" , bg="#50A8B0", font=("arial", 6, "bold"), command =lambda:
btnClick1("A") ,relief=GROOVE)
btnA.grid(row=0, column=0, padx=3, pady=1)
btnB = Button(frameScreenL, width=3, height=1, text="B" , bg="#50A8B0", font=("arial", 6, "bold"), command =lambda:
btnClick1("B") , relief=GROOVE)
btnB.grid(row=0, column=1, padx=3, pady=1)
btnC = Button(frameScreenL, width=3, height=1, text="C" , bg="#50A8B0", font=("arial", 6, "bold"),  command =lambda:
btnClick1("C") , relief=GROOVE)
btnC.grid(row=0, column=2, padx=3, pady=1)
btnD = Button(frameScreenL, width=3, height=1, text="D" , bg="#50A8B0", font=("arial", 6, "bold"), command =lambda:
btnClick1("D") , relief=GROOVE)
btnD.grid(row=1, column=0, padx=3, pady=1)
btnE = Button(frameScreenL, width=3, height=1, text="E" , bg="#50A8B0", font=("arial", 6, "bold"),command =lambda:
btnClick1("E") ,  relief=GROOVE)
btnE.grid(row=1, column=1, padx=3, pady=1)
btnF = Button(frameScreenL, width=3, height=1, text="F" , bg="#50A8B0", font=("arial", 6, "bold"),command =lambda:
btnClick1("F") ,  relief=GROOVE)
btnF.grid(row=1, column=2, padx=3, pady=1)
btnG = Button(frameScreenL, width=3, height=1, text="G" , bg="#50A8B0", font=("arial", 6, "bold"), command =lambda:
btnClick1("G") , relief=GROOVE)
btnG.grid(row=2, column=0, padx=3, pady=1)
btnH = Button(frameScreenL, width=3, height=1, text="H" , bg="#50A8B0", font=("arial", 6, "bold"),command =lambda:
btnClick1("H") , relief=GROOVE)
btnH.grid(row=2, column=1, padx=3, pady=1)
btnI = Button(frameScreenL, width=3, height=1, text="I" , bg="#50A8B0", font=("arial", 6, "bold"),command =lambda:
btnClick1("I") , relief=GROOVE)
btnI.grid(row=2, column=2, padx=3, pady=1)
btnJ = Button(frameScreenL, width=3, height=1, text="J" , bg="#50A8B0", font=("arial", 6, "bold"),command =lambda:
btnClick1("J") , relief=GROOVE)
btnJ.grid(row=3, column=0, padx=3, pady=1)
btnK = Button(frameScreenL, width=3, height=1, text="K" , bg="#50A8B0", font=("arial", 6, "bold"), command =lambda:
btnClick1("K") ,relief=GROOVE)
btnK.grid(row=3, column=1, padx=3, pady=1)
btnL = Button(frameScreenL, width=3, height=1, text="L" , bg="#50A8B0", font=("arial", 6, "bold"),command =lambda:
btnClick1("L") , relief=GROOVE)
btnL.grid(row=3, column=2, padx=3, pady=1)
btnM = Button(frameScreenL, width=3, height=1, text="M" , bg="#50A8B0", font=("arial", 6, "bold"),command =lambda:
btnClick1("M") , relief=GROOVE)
btnM.grid(row=4, column=0, padx=3, pady=1)
btnN = Button(frameScreenL, width=3, height=1, text="N" , bg="#50A8B0", font=("arial", 6, "bold"),command =lambda:
btnClick1("N") , relief=GROOVE)
btnN.grid(row=4, column=1, padx=3, pady=1)
btnO = Button(frameScreenL, width=3, height=1, text="O" , bg="#50A8B0", font=("arial", 6, "bold"),command =lambda:
btnClick1("O") , relief=GROOVE)
btnO.grid(row=4, column=2, padx=3, pady=1)
btnP = Button(frameScreenL, width=3, height=1, text="P" , bg="#50A8B0", font=("arial", 6, "bold"), command =lambda:
btnClick1("P") ,relief=GROOVE)
btnP.grid(row=5, column=0, padx=3, pady=1)
btnQ = Button(frameScreenL, width=3, height=1, text="Q" , bg="#50A8B0", font=("arial", 6, "bold"), command =lambda:
btnClick1("Q") ,relief=GROOVE)
btnQ.grid(row=5, column=1, padx=3, pady=1)
btnR = Button(frameScreenL, width=3, height=1, text="R" , bg="#50A8B0", font=("arial", 6, "bold"), command =lambda:
btnClick1("R") ,relief=GROOVE)
btnR.grid(row=5, column=2, padx=3, pady=1)
btnS = Button(frameScreenL, width=3, height=1, text="S" , bg="#50A8B0", font=("arial", 6, "bold"),command =lambda:
btnClick1("S") , relief=GROOVE)
btnS.grid(row=6, column=0, padx=3, pady=1)
btnT = Button(frameScreenL, width=3, height=1, text="T" , bg="#50A8B0", font=("arial", 6, "bold"),command =lambda:
btnClick1("T") , relief=GROOVE)
btnT.grid(row=6, column=1, padx=3, pady=1)
btnU = Button(frameScreenL, width=3, height=1, text="U" , bg="#50A8B0", font=("arial", 6, "bold"),command =lambda:
btnClick1("U") , relief=GROOVE)
btnU.grid(row=6, column=2, padx=3, pady=1)
btnV = Button(frameScreenL, width=3, height=1, text="V" , bg="#50A8B0", font=("arial", 6, "bold"),command =lambda:
btnClick1("V") , relief=GROOVE)
btnV.grid(row=7, column=0, padx=3, pady=1)
btnW = Button(frameScreenL, width=3, height=1, text="W" , bg="#50A8B0", font=("arial", 6, "bold"),command =lambda:
btnClick1("W") , relief=GROOVE)
btnW.grid(row=7, column=1, padx=3, pady=1)
btnX = Button(frameScreenL, width=3, height=1, text="X" , bg="#50A8B0", font=("arial", 6, "bold"),command =lambda:
btnClick1("X") , relief=GROOVE)
btnX.grid(row=7, column=2, padx=3, pady=1)
btnY = Button(frameScreenL, width=3, height=1, text="Y" , bg="#50A8B0", font=("arial", 6, "bold"),command =lambda:
btnClick1("Y") , relief=GROOVE)
btnY.grid(row=8, column=0, padx=3, pady=1)
btnZ = Button(frameScreenL, width=3, height=1, text="Z" , bg="#50A8B0", font=("arial", 6, "bold"),command =lambda:
btnClick1("Z") , relief=GROOVE)
btnZ.grid(row=8, column=1, padx=3, pady=1)
btnPeriod = Button(frameScreenL, width=3, height=1, text="." , bg="#50A8B0", font=("arial", 6, "bold"),command =lambda:
btnClick1(".") , relief=GROOVE)
btnPeriod.grid(row=8, column=2, padx=3, pady=1)
btnSpace = Button(frameScreenL, width=15, height=1, text="SPACE" , bg="#50A8B0", font=("arial", 6, "bold"),command
=lambda: btnClick1("  ") , relief=GROOVE)
btnSpace.grid(row=9, column =0, columnspan=4, padx=3, pady=1)
#===========================================Screen Buttons===========================================================

btnScreen1 = Button(frameScreenR, width=65, height=55, image=iconPhoto , bg="#50A8B0", font=("arial",10, "bold"),
                    command=Proceed,  justify=LEFT, anchor=W, relief=GROOVE)
btnScreen1.grid(row=0, column=0, padx=3, pady=3)
btnScreen2 = Button(frameScreenR, width=65, height=55, image=iconPhoto , bg="#50A8B0", font=("arial", 10, "bold"),
                    justify=LEFT, anchor=W, relief=GROOVE, command = Balance)
btnScreen2.grid(row=1, column=0, padx=3, pady=3)
btnScreen3 = Button(frameScreenR, width=65, height=55, image=iconPhoto , bg="#50A8B0", font=("arial", 10, "bold"),
                    justify=LEFT, anchor=W, relief=GROOVE, command=Return)
btnScreen3.grid(row=2, column=0, padx=3, pady=3)
#===========================================Bottom Buttons===========================================================

btnCANCEL = Button(buttonFrameL, font=("arial", 20, "bold"), bg="#50A8B0", text="RETURN", width=8, height=1, bd=4,
                   command=Cancel, relief=GROOVE)
btnCANCEL.grid(row=0, column=1, padx=9, pady=6)
btnCLEAR = Button(buttonFrameL, font=("arial", 20, "bold"), bg="#50A8B0", text="CLEAR", width=8, height=1, bd=4,
                  command=Clear, relief=GROOVE)
btnCLEAR.grid(row=0, column=2, padx=9, pady=6)
btnEnter = Button(buttonFrameL, font=("arial", 20, "bold"),  bg="#284P2G",  text="ENTER", width=8, height=1, bd=4,
                  command=Enter, relief=GROOVE)
btnEnter.grid(row=0, column=3, padx=9, pady=6)
btnQUIT = Button(buttonFrameL, font=("arial", 20, "bold"), bg="#50A8B0", fg="red", text="QUIT", width=8, height=1,
                 bd=4, command=qExit, relief=GROOVE)
btnQUIT.grid(row=0, column=4, padx=9, pady=6)
#===========================================Text and Number Entry Boxes================================================
entryScreen = Entry(canvScreen, width=20, font=("arial", 8, "bold"), bd=2, textvariable=var2, insertwidth=4,
                    justify=CENTER, relief=RIDGE, highlightthickness=1, highlightbackground="black",
                    bg="honeydew")
entryScreen.place(x=140, y=120)
entryMoney = Entry(canvScreen, textvariable = text_Input, bd=2, justify="center", relief=RIDGE,
                   highlightthickness=1, highlightbackground="black",bg="honeydew")
entryMoney.place(x=140, y=145)
#===========================================Labels===========================================================

instrucLabel = Label(canvScreen, text="Please Use The Keys At the Left To Enter \nYour Name Or Click In The Box To \nType With Keyboard; Click Enter"
                                      " to Continue!", font=("arial", 8, "bold"), fg="dark red", bg="steel blue")
instrucLabel.place(x=80, y=73)
welcLabel = Label(canvScreen, bg="steel blue", font=("arial", 10, "bold"), fg="green", justify="center", textvariable
= var1)
welcLabel.place(x=110, y=145)
proceedLabel = Label(canvScreen, text="", font=("arial", 10, "bold"), bg="steel blue", anchor="e")
proceedLabel.place(x=330, y=25)
label1 = Label(canvScreen, text="", bg="steel blue", justify ="left")
label1.place(x=15, y=140)
label2 = Label(canvScreen, text="", bg="steel blue", font=("arial", 10, "bold"), justify ="left")
label2.place(x=330, y=100)
label3 = Label(canvScreen, text="", bg="steel blue", font=("arial", 10, "bold"), justify ="left")
label3.place(x=330, y=165)
label4 = Label(canvScreen, text="", bg="steel blue", justify ="left")
label4.place(x=100, y=144)
lblDateOfOrder = Label(top, font=("arial", 12, "bold"),  width= 20, text=localtime, bd=2, bg="#728B8E",
                       fg="black", relief=GROOVE)
lblDateOfOrder.pack(side=LEFT, anchor=W)
var1.set("We are so happy to see you \ntoday and always")

coverLabel = Label(canvScreen, bg="steel blue", font=(6), fg="honeydew", text="")
coverLabel.place(x=80, y=120)

#================================================Buttons Disbaled at Launch============================================
btnScreen1.config(state=DISABLED)
btnScreen2.config(state=DISABLED)
btnScreen3.config(state=DISABLED)
btnCANCEL.config(state=DISABLED)
entryMoney.config(state=DISABLED)

btnNum1.config(state=DISABLED), btnNum2.config(state=DISABLED), btnNum3.config(state=DISABLED), \
btnNum4.config(state=DISABLED), btnNum0.config(state=DISABLED), btnNum8.config(state=DISABLED)
btnNum5.config(state=DISABLED), btnNum6.config(state=DISABLED), btnNum7.config(state=DISABLED), \
btnNum9.config(state=DISABLED), btnNumPoint.config(state=DISABLED)

#===========================================Window loop===========================================================
root.mainloop()