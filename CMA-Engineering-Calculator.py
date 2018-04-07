#===========================================import modulus and packages=================================================
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

#===============================================Matplotlib Graph Setup==================================================
style.use("ggplot")

f = Figure(figsize=(4.5, 2), dpi=110, facecolor="green", edgecolor="grey", linewidth=3)
a = f.add_subplot(111)
f.suptitle("Bending Moment Graph")

def animate(i):
    pullData = open("sampleData.txt", "r").read()
    dataList = pullData.split('\n')
    xList = []
    yList = []
    for eachLine in dataList:
        if len(eachLine) > 1:
            x,y = eachLine.split(',')
            xList.append(int(x))
            yList.append(int(y))


    a.clear()
    a.plot(xList, yList)


#=============================================Main Class================================================================
class TrailApps(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        tk.Tk.iconbitmap(self, default= "comakersicon3.ico")
        tk.Tk.title(self, "CoMakers Engineering Calculator")
        tk.Tk.wm_geometry(self, "900x700+200+0")

        container.pack(side="top", fill="both", expand=True)
        container.rowconfigure(0, weight=1)
        container.columnconfigure(0, weight=1)

        self.frames = {}

        for F in ( Civil, Mechanical, Statics):                                     #Different Frames

            frame = F(container, self)

            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
            self.show_frame(Civil)

    def show_frame(self, cont):                                                   #Function that shows different frames
        frame = self.frames[cont]
        frame.tkraise()

#=====================================================Mechanical Frame==================================================
class Mechanical(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#111F11")

        varMPower = tk.DoubleVar()
        varMSpeed = tk.DoubleVar()                                                  #Variables for Mechanical System
        varNoOfLoad2 = tk.DoubleVar()
        varNoOfLoad1 = tk.DoubleVar()
        varTLen = tk.DoubleVar()
        varLen1 = tk.DoubleVar()
        varLen2 = tk.DoubleVar()
        varDia1 = tk.DoubleVar()
        varDia2 = tk.DoubleVar()
        varLoad1 = tk.DoubleVar()
        varLoad2 = tk.DoubleVar()
        varShear = tk.DoubleVar()
        varTorqueTran = tk.StringVar()
        varDiameter01 = tk.StringVar()
        varTorqueEquiv = tk.StringVar()
        varReactionA = tk.StringVar()
        varReactionB = tk.StringVar()
        varBMoment = tk.StringVar()
        varBMa = tk.StringVar()
        varBMb = tk.StringVar()

        def Shaft():
            W1 = varLoad1.get()
            P = varMPower.get()
            L = varTLen.get()
            L1 = varLen1.get()
            L2 = varLen2.get()
            N = varMSpeed.get()
            Sh = varShear.get()
            W2 = varLoad2.get()

            if varNoOfLoad1.get() == True:
                M = W1*L/4
                T = P*9.549/N
                Te = ((M**2)+ (T**2))**0.5
                D = ((Te*1000)/(0.196*Sh))**(1/3)

                t1 = "Transmitted Torque: " + str("%.1f"%T) + "N-m."
                t2 = " Equivalent Torque: " + str("%.1f"%Te) + "N-m."
                m = "Bending Moment: " + str("%.1f"%M) + "N-m."
                d = "Shaft Diameter: " + str("%.0f"%D) + "mm."
                varTorqueTran.set(t1)
                varTorqueEquiv.set(t2)
                varReactionA.set(m)
                varDiameter01.set(d)

            elif varNoOfLoad2.get() == True:

                RB  = ((W1*L1) + W2*(L-L2))/L
                RA = W1+W2-RB

                Mc = RA*L1
                Md = RB*L2
                if Mc > Md:
                    M = Mc
                else:
                    M = Md
                T = P * 9.549 / N
                Te = ((M ** 2) + (T ** 2)) ** 0.5
                T = P * 9.549 / N
                D = ((Te * 1000) / (0.196 * Sh)) ** (1 / 3)

                ra = 'Reaction at A: ' + str("%.1f"%RA) + "N."
                rb = 'Reaction at B: ' + str("%.1f" % RB) + "N."

                t1 = "Transmitted Torque: " + str("%.1f" % T) + "N-m."
                t2 = " Equivalent Torque: " + str("%.1f" % Te) + "N-m."
                m = "Bending Moment: " + str("%.1f" % M) + "N-m."
                d = "Shaft Diameter: " + str("%.0f" % D) + "mm."
                bma = "BM-Left = " + str("%.1f"%Mc) + "N-m."
                bmd = "BM-Right = " + str("%.1f" % Md) + "N-m."
                varTorqueTran.set(t1)
                varTorqueEquiv.set(t2)
                varReactionA.set(ra)
                varReactionB.set(rb)
                varDiameter01.set(d)
                varBMoment.set(m)
                varBMa.set(bma)
                varBMb.set(bmd)

            else:
                varDiameter01.set("Please, select a specific loading type to start. \nThere can be 1 or 2 loading type"
                                  "and loads can \neither be at the right or left or even centralized")
                varTorqueTran.set("")
                varTorqueEquiv.set("")
                varReactionA.set("")
                varBMoment.set("")
                varReactionB.set("")
                varBMa.set("")
                varBMb.set("")


        def ResetShaft():
            varTorqueTran.set("")
            varTorqueEquiv.set("")
            varReactionA.set("")
            varBMoment.set("")
            varReactionB.set("")
            varDiameter01.set("")
            varBMa.set("")
            varBMb.set("")
            varLoad1.set("0.0")
            varMPower.set("0.0")
            varTLen.set("0.0")
            varLen1.set("0.0")
            varLen2.set("0.0")
            varMSpeed.set("0.0")
            varShear.set("0.0")
            varLoad2.set("0.0")
            a.clear()

        def qExit():
            rely = messagebox.askyesno("Quit System", "Do You Want To Quit The System?")
            if rely is True:
                app.destroy()
            return

        root = tk.Frame(self, width=750, height=650, bg="#111F11")
        root.pack()

        top =  tk.Frame(root, width=865, height=20, bg="#111F11")
        top.grid(row=0, column=0, columnspan=2, sticky="w")

        btnTopHome = tk.Button(top, text= "Mechanical", font=("arial", 10, "bold"), width=15, relief="groove", bd=2, bg="#111F11",
                        fg="white", command=lambda : controller.show_frame(Mechanical))
        btnTopHome.grid(row=0, column=0, sticky="w", padx=1)
        btnTopConv = tk.Button(top, text="Electrical", font=("arial", 10, "bold"), width=15, relief="groove", bd=2, bg="#111F11",
                        fg="white", command=lambda : controller.show_frame(Statics))
        btnTopConv.grid(row=0, column=1, sticky="w", padx=1)

        btnExit = tk.Button(top, text="Quit", relief="groove", bg="#111F11",
                         fg="red", command= qExit)
        btnExit.grid(row=0, column=2, sticky="e", columnspan=4, padx=50)

        btnTopHome.config(state="disabled")

        frMainL = tk.LabelFrame(root, width=750*2/3, height=400, text="GRAPHICS", font=("arial", 10, "bold"), bd=2,
                             bg="#111F11", fg="white")
        frMainL.grid(row=1, column=0, sticky="nw", padx=10, pady= 10)
        frMainR = tk.Frame(root, width=750/ 3, height=650,  bd=2, bg="#111F11")
        frMainR.grid(row=1, column=1, rowspan=2, sticky="n", padx=10, pady= 10)
        frMainB = tk.LabelFrame(root, width=506, height=220, text="PARAMETER", font=("arial", 10, "bold"), bd=2,
                             bg="#111F11", fg="white")
        frMainB.grid(row=2, column=0, columnspan=2, sticky="nw", padx=10, pady= 10)

        canvMain = tk.Canvas(frMainL, width=490, height=367, relief="ridge", bd=4, bg="light green")
        canvMain.grid(row=0, column=0, padx=10, pady= 10)

        canvID1 = FigureCanvasTkAgg(f, canvMain)
        canvID1.get_tk_widget().pack(side="bottom", fill="both", expand=True)

        toolbar = NavigationToolbar2Tk(canvID1, canvMain)
        toolbar.update()
        toolbar.pack(side="top", fill="both", expand=True)

        canvMain2 = tk.Canvas(frMainL, width=490, height=100, relief="ridge", bd=4, bg="light green")
        canvMain2.grid(row=1, column=0, padx=10, pady=10)

        lblNumberOfLoads = tk.Label(frMainB, text="No Of Loads : ", font=("arial", 7, "bold"), bg="#111F11", fg="white")
        lblNumberOfLoads.grid(row=0, column=0, sticky="e")

        uNLoads = tk.Menubutton(frMainB, text= "Select Loading", font=("arial", 7, "bold"), bd=3, bg="#111F11",
                                fg="white", relief="groove")
        uNLoads.grid(row=0, column=1, sticky="e", padx=3)

        uNLoads.menu = tk.Menu(uNLoads, tearoff=0)
        uNLoads["menu"] = uNLoads.menu
        uNLoads.menu.add_checkbutton(label="1 Load", variable=varNoOfLoad1)
        uNLoads.menu.add_separator()
        uNLoads.menu.add_checkbutton(label="2 Loads", variable=varNoOfLoad2)
        uNLoads.menu.add_separator()
        uNLoads.grid()

        lblTLen = tk.Label(frMainB, text="Total Length(m) : ", font=("arial", 7, "bold"), bg="#111F11", fg="white")
        lblTLen.grid(row=0, column=2, sticky="e")
        entryTLen = tk.Entry(frMainB, width=10, bd=2, relief="ridge", highlightbackground="green",
                              highlightthickness=2, textvariable=varTLen)
        entryTLen.grid(row=0, column=3, sticky="w", padx=3, pady=3)

        lblLen1 = tk.Label(frMainB, text="Left Length(m) : ", font=("arial",7, "bold"), bg="#111F11", fg="white")
        lblLen1.grid(row=1, column=0, sticky="e")
        entryLen1 = tk.Entry(frMainB, width=10, bd=2, relief="ridge", highlightbackground="green",
                              highlightthickness=2, textvariable=varLen1)
        entryLen1.grid(row=1, column=1, sticky="w", padx=3, pady=3)

        lblLen2 = tk.Label(frMainB, text="Right Length(m) : ", font=("arial", 7, "bold"), bg="#111F11", fg="white")
        lblLen2.grid(row=1, column=2, sticky="e")
        entryLen2 = tk.Entry(frMainB, width=10, bd=2, relief="ridge", highlightbackground="green",
                              highlightthickness=2, textvariable=varLen2)
        entryLen2.grid(row=1, column=3, sticky="w", padx=3, pady=3)

        #lblDia1 = tk.Label(frMainB, text="L Load Dia(mm) : ", font=("arial", 7, "bold"), bg="#111F11", fg="white")
        #lblDia1.grid(row=2, column=0, sticky="e")
        #entryDia1 = tk.Entry(frMainB, width=10, bd=2, relief="ridge", highlightbackground="green",
                             #highlightthickness=2, textvariable=varDia1)
        #entryDia1.grid(row=2, column=1, sticky="w", padx=3, pady=3)

        #lblDia2 = tk.Label(frMainB, text="R Load Dia(mm) : ", font=("arial", 7, "bold"), bg="#111F11", fg="white")
        #lblDia2.grid(row=2, column=2, sticky="e")
        #entryDia2 = tk.Entry(frMainB, width=10, bd=2, relief="ridge", highlightbackground="green",
                             #highlightthickness=2, textvariable=varDia2)
        #entryDia2.grid(row=2, column=3, sticky="w", padx=3, pady=3)

        lblLoad1 = tk.Label(frMainB, text="L Load(N) : ", font=("arial", 7, "bold"), bg="#111F11", fg="white")
        lblLoad1.grid(row=0, column=4, sticky="e")
        entryLoad1 = tk.Entry(frMainB, width=10, bd=2, relief="ridge", highlightbackground="green",
                             highlightthickness=2, textvariable=varLoad1)
        entryLoad1.grid(row=0, column=5, sticky="w", padx=3, pady=3)

        lblLoad2 = tk.Label(frMainB, text="R Load(N) : ", font=("arial", 7, "bold"), bg="#111F11", fg="white")
        lblLoad2.grid(row=1, column=4, sticky="e")
        entryLoad2 = tk.Entry(frMainB, width=10, bd=2, relief="ridge", highlightbackground="green",
                             highlightthickness=2, textvariable=varLoad2)
        entryLoad2.grid(row=1, column=5, sticky="w", padx=3, pady=3)

        lblMPower = tk.Label(frMainB, text="Shaft Power(W) : ", font=("arial", 7, "bold"), bg="#111F11", fg="white")
        lblMPower.grid(row=3, column=0, sticky="e")
        entryMPower = tk.Entry(frMainB, width=10, bd=2, relief="ridge", highlightbackground="green",
                              highlightthickness=2, textvariable=varMPower)
        entryMPower.grid(row=3, column=1, sticky="w", padx=3, pady=3)

        lblMSpeed = tk.Label(frMainB, text="Speed of Shaft(r.p.m) : ", font=("arial", 7, "bold"), bg="#111F11", fg="white")
        lblMSpeed.grid(row=3, column=2, sticky="e")
        entryMSpeed = tk.Entry(frMainB, width=10, bd=2, relief="ridge", highlightbackground="green",
                              highlightthickness=2, textvariable=varMSpeed)
        entryMSpeed.grid(row=3, column=3, sticky="w", padx=3, pady=3)

        lblShearStress = tk.Label(frMainB, text="Shear Stress\n(N/mm2) : ", font=("arial", 7, "bold"), bg="#111F11",
                             fg="white", justify="right")
        lblShearStress.grid(row=4, column=0, sticky="e")
        entryShearStress = tk.Entry(frMainB, width=10, bd=2, relief="ridge", highlightbackground="green",
                               highlightthickness=2, textvariable=varShear)
        entryShearStress.grid(row=4, column=1, sticky="w", padx=3, pady=3)

#==================================================Shaft Results========================================================
        lblDiameter01 = tk.Label(canvMain2, textvariable=varDiameter01, font=("arail", 9, "bold"), bg="light green",
                                 justify ="left")
        lblDiameter01.grid(row=0, column=0, padx=7, pady=5, sticky="w")
        lblTorqueTran = tk.Label(canvMain2, textvariable=varTorqueTran, bg="light green", font=("arial", 9, "bold"))
        lblTorqueTran.grid(row=0, column=1, columnspan=2, padx=7, pady=5, sticky="w")
        lblTorqueEquiv = tk.Label(canvMain2, textvariable=varTorqueEquiv, font=("arial", 9, "bold"), bg="light green")
        lblTorqueEquiv.grid(row=1, column=1, padx=5, pady=7, sticky="w")
        frmShaft1 = tk.Frame(canvMain2, width=4, height=100, bg="light green")
        frmShaft1.grid(row=0, rowspan=2, column=3, padx=5, pady=5)
        lblReactionA = tk.Label(canvMain2, textvariable=varReactionA, font=("arial", 9, "bold"), bg="light green")
        lblReactionA.grid(row=1, column=0, padx=7, pady=5, sticky="w")
        frmShaft = tk.Frame(canvMain2, width=450, height=1, bg="light green")
        frmShaft.grid(row=2, column=0, columnspan = 3, padx=5, pady=5)
        lblReactionB = tk.Label(canvMain2, textvariable=varReactionB, font=("arial", 9, "bold"), bg="light green")
        lblReactionB.grid(row=2, column=0, padx=7, pady=5, sticky="w")
        lblBMoment = tk.Label(canvMain2, textvariable=varBMoment, font=("arial", 9, "bold"), bg="light green")
        lblBMoment.grid(row=2, column=1, padx=7, pady=5, sticky="w")
        lblBMa = tk.Label(canvMain2, textvariable=varBMa, font=("arial", 9, "bold"), bg="light green")
        lblBMa.grid(row=0, column=2, padx=7, pady=5, sticky="w")
        lblBMb = tk.Label(canvMain2, textvariable=varBMb, font=("arial", 9, "bold"), bg="light green")
        lblBMb.grid(row=1, column=2, padx=7, pady=5, sticky="w")

#=============================================Buttons==================================================================
        btnCalc = tk.Button(frMainB, text="CALCULATE", font=("arial", 10, "bold"), width=10, bd=2, relief="groove",
                           bg="GREEN", command=Shaft)
        btnCalc.grid(row=4, column=3, rowspan=2, columnspan=1, padx=5, pady=5)
        btnReset1 = tk.Button(frMainB, text="RESET", font=("arial", 10, "bold"), width=10, bd=2, relief="groove",
                         bg="GREEN", command = ResetShaft)
        btnReset1.grid(row=4, column=2, columnspan=1, rowspan=2, padx=5, pady=5)

#===========================================Power Converter============================================================
        varHP = tk.DoubleVar()
        varWT = tk.DoubleVar()
        varHP1 = tk.StringVar()
        varWT1 = tk.StringVar()
        varWTe = tk.StringVar()

        def ConvHPvsWT():
            HP = varHP.get()
            WT = varWT.get()


            if varHP.get() > 0 and varWT.get() ==0:
                WTm = HP*745.699872
                WTe = HP*746
                WTmetric = HP*735.49875

                wm = str("%.2f" % HP) + " Mechanical Hp is " + str("%.3f" % WTm) + "W"
                we = str("%.2f" % HP) + " Electrical Hp is " + str("%.3f" % WTe) + "W"
                wme = str("%.2f" % HP) + " Metric Hp is " + str("%.3f" % WTmetric) + "W"
                if HP < 1000000:
                    varHP1.set(wm)
                    varWT1.set(wme)
                    varWTe.set(we)
                else:
                    varHP1.set("You have run out of range! \nYou can only convert Power \nless than 1000000 Horse-power")
                    varWT1.set("")
                    varWTe.set("")

            elif varWT.get() > 0 and varHP.get()==0:
                HPm = WT/745.699872
                HPe = WT/746
                HPmetric = WT/735.49875

                hm =  str("%.2f"%WT) + " Mechanical Watt is " + str("%.3f"%HPm) + "Hp"
                he = str("%.2f" % WT) + " Electrical Watt is " + str("%.3f" % HPe) + "Hp"
                hme = str("%.2f" % WT) + " Metric Watt is " + str("%.3f" % HPmetric) + "Hp"
                if WT < 1000000000:
                    varHP1.set(hm)
                    varWT1.set(hme)
                    varWTe.set(he)
                else:
                    varHP1.set("You have run out of range! \nYou can only convert Power \nless than 1000000000 Watt")
                    varWT1.set("")
                    varWTe.set("")

            elif varWT.get() > 0 and varHP.get() > 0:
                varHP1.set("You need to covert one at a time!")
                varWT1.set("")
                varWTe.set("")

            else:
                varHP1.set("Please select a power to convert!")
                varWT1.set("")
                varWTe.set("")

        def ResetPowerConv():
            varHP1.set("")
            varWT1.set("")
            varWTe.set("")
            varHP.set("0.0")
            varWT.set("0.0")

        frmPower = tk.LabelFrame(frMainR, text="POWER", font=("arial", 10, "bold"), width=250, height=350, bd=2,
                              bg="#111F11", fg="white")
        frmPower.grid(row=0, column=0, padx=10, pady=10)
        frmTorque = tk.LabelFrame(frMainR, text="TORQUE", font=("arial", 10, "bold"), width=250, height=240, bd=2,
                               bg="#111F11", fg="white")
        frmTorque.grid(row=1, column=0, padx=10, pady=10)

        canvPower = tk.Canvas(frmPower, width=200, height=100, relief="ridge", bd=4, bg="light green")
        canvPower.grid(row=0, column=0, columnspan=2, padx=10, pady=20)

        lblPowerHP = tk.Label(frmPower, text=" Horse-Power", font=("arial", 8, "bold"), bg="#111F11", fg="white")
        lblPowerHP.grid(row=1, column=0, sticky="w", padx=10, pady=2)

        lblPowerWT = tk.Label(frmPower, text=" Watt\t", font=("arial", 8, "bold"), bg="#111F11", fg="white")
        lblPowerWT.grid(row=1, column=1, sticky="e", padx=10, pady=2)

        entryHP = tk.Entry(frmPower, width=15, bd=2, relief="ridge", highlightbackground="green", highlightthickness=2,
                           textvariable = varHP)
        entryHP.grid(row=2, column=0, sticky="w", padx=10, pady=5)
        entryWT = tk.Entry(frmPower, width=15, bd=2, relief="ridge", highlightbackground="green", highlightthickness=2,
                           textvariable = varWT)
        entryWT.grid(row=2, column=1, sticky="e", padx=10, pady=5)

        lblHP1 = tk.Label(canvPower, textvariable = varHP1, font=("arial", 8, "bold"), justify="left", bg="light green")
        lblHP1.grid(row=0, column=0, padx=7, pady=5, sticky="w")
        lblWT1 = tk.Label(canvPower, textvariable=varWT1, font=("arial", 8, "bold"), justify ="left", bg="light green")
        lblWT1.grid(row=1, column=0, sticky="w", padx=7, pady=5)

        lblWTFrm = tk.Label(canvPower, width=30, height=1, bg="light green")
        lblWTFrm.grid(row=2, column=0, sticky="e", padx=7, pady=5)
        lblWTFrmL = tk.Label(canvPower, width=1, height=5, bg="light green")
        lblWTFrmL.grid(row=0, column=1,rowspan=2, sticky="e", padx=5, pady=5)
        lblWTe = tk.Label(canvPower, textvariable=varWTe, font=("arial", 8, "bold"), justify="left", bg="light green")
        lblWTe.grid(row=2, column=0, sticky="w", padx=7, pady=5)

        btnConvPW = tk.Button(frmPower, text="CONVERT", font=("arial", 10, "bold"), width=15, bd=2, relief="groove",
                         bg="GREEN", command=ConvHPvsWT)
        btnConvPW.grid(row=3, column=0, rowspan=1, columnspan=1, padx=10, pady=5, sticky="w")
        btnResetPW = tk.Button(frmPower, text="RESET", font=("arial", 10, "bold"), width=8, bd=2, relief="groove",
                           bg="GREEN", command=ResetPowerConv)
        btnResetPW.grid(row=3, column=1, columnspan=1, rowspan=2, padx=10, pady=5, sticky="w")

#=============================================Torque Conversion=========================================================
        varPFF1 = tk.StringVar()
        varNM1 = tk. StringVar()
        varKFM1 = tk.StringVar()
        varPFI1 = tk.StringVar()
        varPFF = tk.DoubleVar()
        varNM = tk.DoubleVar()
        varKFM = tk.DoubleVar()
        varPFI = tk.DoubleVar()

        def TorqueConv():
            PFF = varPFF.get()
            PFI = varPFI.get()
            KFM = varKFM.get()
            NM = varNM.get()
            if PFF > 0 :
                Pfi = PFF/12
                Nm = PFF/1.3558
                Kfm = PFF/0.1383
                pfi = str("%.0f "%PFF) + "Pound-Force-Foot <==> "+ str("%.3f"%Pfi)+"Pound-inch"
                nm = str("%.0f "%PFF) + "Pound-Force-Foot <==> " + str("%.3f" % Nm) + "N-m"
                kfm = str("%.0f "%PFF) + "Pound-Force-Foot <==> " + str("%.3f" % Kfm) + "Kg-m"
                varPFI1.set(pfi)
                varNM1.set(nm)
                varKFM1.set(kfm)
                varPFF1.set("")
                varPFF.set("0.0")
                varNM.set("0.0")
                varKFM.set("0.0")
                varPFI.set("0.0")



            elif PFI > 0 :
                Pff = PFI/0.0833
                Nm = PFI/0.1130
                Kfm = PFI/0.0115
                pff = str("%.0f "%PFI) + "Pound-Force-Inch <==> "+ str("%.3f"%Pff)+"Pound-foot"
                nm = str("%.0f "%PFI) + "Pound-Force-Inch <==> " + str("%.3f" % Nm) + "N-m"
                kfm = str("%.0f "%PFI) + "Pound-Force-Inch <==> " + str("%.3f" % Kfm) + "Kg-m"
                varPFF1.set(pff)
                varNM1.set(nm)
                varKFM1.set(kfm)
                varPFI1.set("")
                varPFF.set("0.0")
                varNM.set("0.0")
                varKFM.set("0.0")
                varPFI.set("0.0")

            elif NM > 0 :
                Pfi = NM/12
                Pff = NM/1.3558
                Kfm = NM/0.1383
                pfi = str("%.0f "%NM) + "Newton-Meter <==> "+ str("%.3f"%Pfi)+"Pound-inch"
                pff = str("%.0f "%NM) + "Newton-Meter <==> " + str("%.3f" % Pff) + "Pound-foot"
                kfm = str("%.0f "%NM) + "Newton-Meter <==> " + str("%.3f" % Kfm) + "Kg-m"
                varPFI1.set(pfi)
                varPFF1.set(pff)
                varKFM1.set(kfm)
                varNM1.set("")
                varPFF.set("0.0")
                varNM.set("0.0")
                varKFM.set("0.0")
                varPFI.set("0.0")

            elif KFM > 0 :
                Pfi = KFM/86.7964
                Nm = KFM/9.8067
                Pff = KFM/7.233
                pfi = str("%.0f "%KFM) + "Kilogram-Force-Meter <==> "+ str("%.3f"%Pfi)+"Pound-inch"
                nm = str("%.0f "%KFM) + "Kilogram-Force-Meter <==> " + str("%.3f" % Nm) + "N-m"
                pff = str("%.0f "%KFM) + "Kilogram-Force-Meter <==> " + str("%.3f" % Pff) + "Pound-foot"
                varPFI1.set(pfi)
                varNM1.set(nm)
                varPFF1.set(pff)
                varKFM1.set("")
                varPFF.set("0.0")
                varNM.set("0.0")
                varKFM.set("0.0")
                varPFI.set("0.0")

            else:
                varNM1.set("Please select a unit to convert")
                varKFM1.set("")
                varPFI1.set("")
                varPFF1.set("")

        def ClearTorque():
            varKFM1.set("")
            varPFI1.set("")
            varPFF1.set("")
            varNM1.set("")
            varPFF.set("0.0")
            varNM.set("0.0")
            varKFM.set("0.0")
            varPFI.set("0.0")

        canvTorque = tk.Canvas(frmTorque, width=200, height=104, relief="ridge", bd=4, bg="light green")
        canvTorque.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        lblTorqueNM = tk.Label(frmTorque, text=" Newton-Meter", font=("arial", 8, "bold"), bg="#111F11", fg="white")
        lblTorqueNM.grid(row=1, column=0, sticky="w", padx=10, pady=2)

        lblTorqueKFM = tk.Label(frmTorque, text=" Kg-Force-Meter", font=("arial", 8, "bold"), bg="#111F11", fg="white")
        lblTorqueKFM.grid(row=1, column=1, sticky="w", padx=10, pady=2)

        entryNM = tk.Entry(frmTorque, width=15, bd=2, relief="ridge", highlightbackground="green", highlightthickness=2,
                           textvariable=varNM)
        entryNM.grid(row=2, column=0, sticky="w", padx=10, pady=5)
        entryKFM = tk.Entry(frmTorque, width=15, bd=2, relief="ridge", highlightbackground="green", highlightthickness=2,
                            textvariable=varKFM)
        entryKFM.grid(row=2, column=1, sticky="e", padx=10, pady=5)


        lblTorquePFF = tk.Label(frmTorque, text=" Pound-Force-Foot", font=("arial", 8, "bold"), bg="#111F11", fg="white")
        lblTorquePFF.grid(row=3, column=0, sticky="w", padx=10, pady=2)

        lblTorquePFI = tk.Label(frmTorque, text=" Pound-Force-In", font=("arial", 8, "bold"), bg="#111F11", fg="white")
        lblTorquePFI.grid(row=3, column=1, sticky="e", padx=10, pady=2)

        entryPFF = tk.Entry(frmTorque, width=15, bd=2, relief="ridge", highlightbackground="green", highlightthickness=2,
                            textvariable=varPFF)
        entryPFF.grid(row=4, column=0, sticky="w", padx=10, pady=5)
        entryPFI = tk.Entry(frmTorque, width=15, bd=2, relief="ridge", highlightbackground="green", highlightthickness=2,
                            textvariable=varPFI)
        entryPFI.grid(row=4, column=1, sticky="e", padx=10, pady=5)

        btnConvTQ = tk.Button(frmTorque, text="CONVERT", font=("arial", 9, "bold"), width=15, bd=2, relief="groove",
                           bg="GREEN", command = TorqueConv)
        btnConvTQ.grid(row=5, column=0, rowspan=1, columnspan=1, padx=10, pady=2, sticky="w")
        btnResetTQ = tk.Button(frmTorque, text="RESET", font=("arial", 9, "bold"), width=8, bd=2, relief="groove",
                            bg="GREEN", command = ClearTorque)
        btnResetTQ.grid(row=5, column=1, columnspan=1, rowspan=2, padx=10, pady=2, sticky="e")

        lblNM1 = tk.Label(canvTorque, textvariable=varNM1, font=("arial", 8, "bold"), bg="light green")
        lblNM1.grid(row=0, column=0, padx=7, pady=7, sticky="w")
        lblPFF1 = tk.Label(canvTorque, textvariable=varPFF1, font=("arial", 8, "bold"), bg="light green")
        lblPFF1.grid(row=1, column=0, padx=7, pady=5, sticky="w")
        lblPFI1 = tk.Label(canvTorque, textvariable=varPFI1, font=("arial", 8, "bold"), bg="light green")
        lblPFI1.grid(row=2, column=0, padx=7, pady=5, sticky="w")
        lblTorqueFrm = tk.Frame(canvTorque, width=250, height=1, bg="light green")
        lblTorqueFrm.grid(row=3, column=0, columnspan=2)
        lblKFM1 = tk.Label(canvTorque, textvariable=varKFM1, font=("arial", 8, "bold"), bg="light green")
        lblKFM1.grid(row=3, column=0, padx=7, pady=7, sticky="w")
        lblTorqueFrmL = tk.Frame(canvTorque, width=1, height=110, bg="light green")
        lblTorqueFrmL.grid(row=0, column=1, rowspan=4)

class Statics(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#111F11")
        var1 =tk.DoubleVar()
        var2 = tk.DoubleVar()
        var3 =tk.DoubleVar()
        var4 = tk.DoubleVar()
        var5 = tk.DoubleVar()
        var6 = tk.DoubleVar()
        var7 = tk.DoubleVar()
        var8 = tk.StringVar()
        var9 = tk.StringVar()
        var10 = tk.StringVar()
        var11 = tk.StringVar()
        var01 = tk.StringVar()
        var02 = tk.StringVar()
        var03 = tk.StringVar()
        var04 = tk.StringVar()
        var05 = tk.StringVar()
        varSnyc = tk.IntVar()
        varFreq = tk.IntVar()
        varPole = tk.IntVar()
        var0Snyc = tk.StringVar()
        var0Freq = tk.StringVar()
        var0Pole = tk.StringVar()
        varSelect = tk.StringVar()
        varEApp = tk.DoubleVar()
        varEHours = tk.DoubleVar()
        varCost = tk.StringVar()
        varSelect.set("Select")
        varECostpD1 = tk.StringVar()
        varECostpM1 = tk.StringVar()
        varECostpY1 = tk.StringVar()
        item0 = tk.IntVar()
        item1 = tk.IntVar()
        item2 = tk.IntVar()


        def qExit():
            exit1 = messagebox.askyesno("Quit System", "Do You Want To Quit The System?")
            if exit1 is True:
                app.destroy()
            return


        def PowerConsumption():
            V = var3.get()
            P = var5.get()
            R = var2.get()
            I =var4.get()
            if I>0 and R>0:
                if var9.get() == "Volts":
                    V1 = float(I*R)
                    v1 = ("%.6f" %(V1))
                    var02.set(v1)

                if var9.get() == "milli-Volts":
                    V2 = float((I*R) / 1000)
                    v2 = ( "%.3f"%(V2))
                    var02.set(v2)

                if var9.get() == "kilo-Volts":
                    V3 = float((I*R) * 1000)
                    v3 = str( "%.3f" % (V3))
                    var02.set(v3)

                if var9.get() == "mega-Volts":
                    V4 = float((I*R) * 1000000)
                    v4 = str( "%.3f" % (V4))
                    var02.set(v4)

                if var8.get() == "Ohms":
                    R1 = float(R)
                    r1 = str( "%.3f" % R1)
                    var01.set(r1)

                if var8.get() == "milli-Ohms":
                    R2 = float(R / 1000)
                    r2 = "", str( "%.3f" % R2), "Ω"
                    var01.set(r2)

                if var8.get() == "kilo-Ohms":
                    R3 = float(R * 1000)
                    r3 = "", str( "%.3f" % R3), "Ω"
                    var01.set(r3)

                if var8.get() == "mega-Ohms":
                    R4 = float(R * 1000000)
                    r4 = "", str( "%.3f" % R4), "Ω"
                    var01.set(r4)



                if var11.get() == "Watts":
                    P1 = float(R*I**2)
                    p1 = str( "%.3f" % P1), "W"
                    var04.set(p1)

                if var11.get() == "milli-Watts":
                    P2 = float((R*I**2) / 1000)
                    p2 = str( "%.3f" % P2), "W"
                    var04.set(p2)

                if var11.get() == "kilo-Watts":
                    P3 = float((R*I**2) * 1000)
                    p3 = str( "%.3f" % P3), "W"
                    var04.set(p3)

                if var11.get() == "mega-Watts":
                    P4 = float((R*I**2) * 1000000)
                    p4 = str( "%.3f" % P4), "W"
                    var04.set(p4)


                if var10.get() == "Amps":
                    I1 = float(I)
                    i1 = str( "%.3f" % I1), "A"
                    var03.set(i1)

                if var10.get() == "milli-Amps":
                    I2 = float(I / 1000)
                    i2 = str( "%.3f" % I2), "A"
                    var03.set(i2)

                if var10.get() == "kilo-Amps":
                    I3 = float(I * 1000)
                    i3 = str( "%.3f" % I3), "A"
                    var03.set(i3)

                if var10.get() == "mega-Amps":
                    I4 = float(I * 1000000)
                    i4 = str( "%.3f" % I4), "A"
                    var03.set(i4)

            elif V>0 and R>0:

                if var9.get() == "Volts":
                    V1 = float(V*1)
                    v5 = str( "%.3f" % (V1)), "V"
                    var02.set(v5)

                if var9.get() == "milli-Volts":
                    V2 = float(V / 1000)
                    v6 = str( "%.3f" % (V2)),"V"
                    var02.set(v6)

                if var9.get() == "kilo-Volts":
                    V3 = float(V * 1000)
                    v7 = str( "%.3f" % (V3)), "V"
                    var02.set(v7)

                if var9.get() == "mega-Volts":
                    V4 = float(V * 1000000)
                    v8 = str( "%.3f" % (V4)),"V"
                    var02.set(v8)

                if var8.get() == "Ohms":
                    R1 = float(R)
                    r5 = str( "%.3f" % R1), "Ω"
                    var01.set(r5)

                if var8.get() == "milli-Ohms":
                    R2 = float(R / 1000)
                    r6 = str( "%.3f" % R2), "Ω"
                    var01.set(r6)

                if var8.get() == "kilo-Ohms":
                    R3 = float(R * 1000)
                    r7 = str( "%.3f" % R3), "Ω"
                    var01.set(r7)

                if var8.get() == "mega-Ohms":
                    R4 = float(R * 1000000)
                    r8 = str( "%.3f" % R4), "Ω"
                    var01.set(r8)

                if var10.get() == "Amps":
                    I1 = float(V/R)
                    i5 = str( "%.3f" % I1), "A"
                    var03.set(i5)

                if var10.get() == "milli-Amps":
                    I2 = float((V/R) / 1000)
                    i6 = str( "%.3f" % I2), "A"
                    var03.set(i6)

                if var10.get() == "kilo-Amps":
                    I3 = float((V/R) * 1000)
                    i7 = str( "%.3f" % I3), "A"
                    var03.set(i7)

                if var10.get() == "mega-Amps":
                    I4 = float((V/R) * 1000000)
                    i8 = str( "%.3f" % I4), "A"
                    var03.set(i8)


                if var11.get() == "Watts":
                    P1 = float(V/R**2)
                    p5 = str( "%.3f" % P1), "W"
                    var04.set(p5)

                if var11.get() == "milli-Watts":
                    P2 = float((R*I**2) / 1000)
                    p6 = str( "%.3f" % P2), "W"
                    var04.set(p6)

                if var11.get() == "kilo-Watts":
                    P3 = float((V/R**2) * 1000)
                    p7 = str( "%.3f" % P3), "W"
                    var04.set(p7)

                if var11.get() == "mega-Watts":
                    P4 = float((V/R**2) * 1000000)
                    p8 = str( "%.3f" % P4), "W"
                    var04.set(p8)

            elif I>0 and V>0:

                if var9.get() == "Volts":
                    V1 = float(V)
                    v9 = str( "%.3f" % (V1)), "V"
                    var02.set(v9)

                if var9.get() == "milli-Volts":
                    V2 = float(V / 1000)
                    v10 = str( "%.3f" % (V2)),"V"
                    var02.set(v10)

                if var9.get() == "kilo-Volts":
                    V3 = float(V * 1000)
                    v11 = str( "%.3f" % (V3)), "V"
                    var02.set(v11)

                if var9.get() == "mega-Volts":
                    V4 = float(V * 1000000)
                    v12 = str( "%.3f" % (V4)), "V"
                    var02.set(v12)


                if var8.get() == "Ohms":
                    R1 = float(V/I)
                    r9 = str( "%.3f" % R1), "Ω"
                    var01.set(r9)

                if var8.get() == "milli-Ohms":
                    R2 = float((V/I) / 1000)
                    r10 = str( "%.3f" % R2), "Ω"
                    var01.set(r10)

                if var8.get() == "kilo-Ohms":
                    R3 = float((V/I) * 1000)
                    r11 =  str( "%.3f" % R3), "Ω"
                    var01.set(r11)

                if var8.get() == "mega-Ohms":
                    R4 = float((V/I) * 1000000)
                    r12 = str( "%.3f" % R4), "Ω"
                    var01.set(r12)


                if var11.get() == "Watts":
                    P1 = float(I*V)
                    p9 = str( "%.3f" % P1), "W"
                    var04.set(p9)

                if var11.get() == "milli-Watts":
                    P2 = float((I*V) / 1000)
                    p10 = str( "%.3f" % P2), "W"
                    var04.set(p10)

                if var11.get() == "kilo-Watts":
                    P3 = float((I*V) * 1000)
                    p11 = str("%.3f" % P3), "W"
                    var04.set(p11)

                if var11.get() == "mega-Watts":
                    P4 = float((I*V) * 1000000)
                    p12 = str( "%.3f" % P4), "W"
                    var04.set(p12)

            elif P>0 and I>0:

                if var9.get() == "Volts":
                    V1 = float(P/I)
                    v13 =  str( "%.3f" % V1), "V"
                    var02.set(v13)

                if var9.get() == "milli-Volts":
                    V2 = float((P/I) / 1000)
                    v14 = str( "%.3f" % (V2)),"V"
                    var02.set(v14)

                if var9.get() == "kilo-Volts":
                    V3 = float((P/I) * 1000)
                    v15 = "", str( "%.3f" % V3), "V"
                    var02.set(v15)

                if var9.get() == "mega-Volts":
                    V4 = float((P/I)* 1000000)
                    v16 =  str( "%.3f" % (V4)), "V"
                    var02.set(v16)


                if var8.get() == "Ohms":
                    R1 = float((P/I**2))
                    r13 =  str( "%.3f" % R1), "Ω"
                    var01.set(r13)

                if var8.get() == "milli-Ohms":
                    R2 = float((P/I**2) / 1000)
                    r14 = str( "%.3f" % R2), "Ω"
                    var01.set(r14)

                if var8.get() == "kilo-Ohms":
                    R3 = float((P/I**2) * 1000)
                    r15 = str( "%.3f" % R3), "Ω"
                    var01.set(r15)

                if var8.get() == "mega-Ohms":
                    R4 = float((P/I**2) * 1000000)
                    r16 = str( "%.3f" % R4), "Ω"
                    var01.set(r16)

                if var10.get() == "Amps":
                    I1 = float(I)
                    i9 = str( "%.3f" % I1), "A"
                    var03.set(i9)

                if var10.get() == "milli-Amps":
                    I2 = float(I / 1000)
                    i10 =  str( "%.3f" % I2), "A"
                    var03.set(i10)

                if var10.get() == "kilo-Amps":
                    I3 = float(I * 1000)
                    i11 = str( "%.3f" % I3), "A"
                    var03.set(i11)

                if var10.get() == "mega-Amps":
                    I4 = float(I * 1000000)
                    i12 = str( "%.3f" % I4), "A"
                    var03.set(i12)

                if var11.get() == "Watts":
                    P1 = float(P)
                    p13 = str( "%.3f" % P1), "W"
                    var04.set(p13)

                if var11.get() == "milli-Watts":
                    P2 = float(P / 1000)
                    p14 = str( "%.3f" % P2), "W"
                    var04.set(p14)

                if var11.get() == "kilo-Watts":
                    P3 = float(P * 1000)
                    p15 = str( "%.3f" % P3), "W"
                    var04.set(p15)

                if var11.get() == "mega-Watts":
                    P4 = float(P * 1000000)
                    p16 = str( "%.3f" % P4), "W"
                    var04.set(p16)

            elif P>0 and R>0:

                if var9.get() == "Volts":
                    V1 = float((P*R)**0.5)
                    v17 = str( "%.3f" % (V1)), "V"
                    var02.set(v17)

                if var9.get() == "milli-Volts":
                    V2 = float(((P*R)**0.5) / 1000)
                    v18 = str( "%.3f" % (V2)), "V"
                    var02.set(v18)

                if var9.get() == "kilo-Volts":
                    V3 = float(((P*R)**0.5) * 1000)
                    v19 = str( "%.3f" % (V3)), "V"
                    var02.set(v19)

                if var9.get() == "mega-Volts":
                    V4 = float(((P*R)**0.5) * 1000000)
                    v20 = str( "%.3f" % (V4)), "V"
                    var02.set(v20)

                if var10.get() == "Amps":
                    I1 = float((P/R)**0.5)
                    i16 = str( "%.3f" % I1), "A"
                    var03.set(i16)

                if var10.get() == "milli-Amps":
                    I2 = float(((P/R)**0.5) / 1000)
                    i13 = str( "%.3f" % I2), "A"
                    var03.set(i13)

                if var10.get() == "kilo-Amps":
                    I3 = float(((P/R)**0.5) * 1000)
                    i14 = str( "%.3f" % I3), "A"
                    var03.set(i14)

                if var10.get() == "mega-Amps":
                    I4 = float(((P/R)**0.5) * 1000000)
                    i15 = str( "%.3f" % I4), "A"
                    var03.set(i15)


                if var8.get() == "Ohms":
                    R1 = float(R)
                    r17 = str( "%.3f" % R1), "Ω"
                    var01.set(r17)

                if var8.get() == "milli-Ohms":
                    R2 = float(R / 1000)
                    r18 = str( "%.3f" % R2), "Ω"
                    var01.set(r18)

                if var8.get() == "kilo-Ohms":
                    R3 = float(R * 1000)
                    r19 = str( "%.3f" % R3), "Ω"
                    var01.set(r19)

                if var8.get() == "mega-Ohms":
                    R4 = float(R * 1000000)
                    r20 = str( "%.3f" % R4), "Ω"
                    var01.set(r20)

                if var11.get() == "Watts":
                    P1 = float(P)
                    p17 = str( "%.3f" % P1), "W"
                    var04.set(p17)

                if var11.get() == "milli-Watts":
                    P2 = float(P / 1000)
                    p18 = str( "%.3f" % P2), "W"
                    var04.set(p18)

                if var11.get() == "kilo-Watts":
                    P3 = float(P * 1000)
                    p19 = str( "%.3f" % P3), "W"
                    var04.set(p19)

                if var11.get() == "mega-Watts":
                    P4 = float(P * 1000000)
                    p20 = str( "%.3f" % P4), "W"
                    var04.set(p20)

            elif V>0 and P>0:

                if var9.get() == "Volts":
                    V1 = float(V)
                    v21 = str( "%.3f" % (V1)), "V"
                    var02.set(v21)

                if var9.get() == "milli-Volts":
                    V2 = float(V / 1000)
                    v22 = str( "%.3f" % (V2)), "V"
                    var02.set(v22)

                if var9.get() == "kilo-Volts":
                    V3 = float(V * 1000)
                    v23 = str( "%.3f" % (V3)),"V"
                    var02.set(v23)

                elif var9.get() == "mega-Volts":
                    V4 = float(V * 1000000)
                    v24 = str( "%.3f" % (V4)), "V"
                    var02.set(v24)

                if var10.get() == "Amps":
                    I1 = float(P/V)
                    i17 = str( "%.3f" % I1), "A"
                    var03.set(i17)

                if var10.get() == "milli-Amps":
                    I2 = float((P/V) / 1000)
                    i18 = str( "%.3f" % I2), "A"
                    var03.set(i18)

                if var10.get() == "kilo-Amps":
                    I3 = float((P/V) * 1000)
                    i19 = str( "%.3f" % I3), "A"
                    var03.set(i19)

                if var10.get() == "mega-Amps":
                    I4 = float((P/V) * 1000000)
                    i20 = str( "%.3f" % I4), "A"
                    var03.set(i20)

                if var8.get() == "Ohms":
                    R1 = float((V**2)/P)
                    r21 = str( "%.3f" % R1), "Ω"
                    var01.set(r21)

                if var8.get() == "milli-Ohms":
                    R2 = float(((V**2)/P) / 1000)
                    r22 = str( "%.3f" % R2), "Ω"
                    var01.set(r22)

                if var8.get() == "kilo-Ohms":
                    R3 = float(((V**2)/P) * 1000)
                    r23 =  str( "%.3f" % R3), "Ω"
                    var01.set(r23)

                if var8.get() == "mega-Ohms":
                    R4 = float(((V**2)/P)* 1000000)
                    r24 = str( "%.3f" % R4), "Ω"
                    var01.set(r24)

                if var11.get() == "Watts":
                    P1 = float(P)
                    p21 = str( "%.3f" % P1), "W"
                    var04.set(p21)

                if var11.get() == "milli-Watts":
                    P2 = float(P / 1000)
                    p22 =  str( "%.3f" % P2), "W"
                    var04.set(p22)

                if var11.get() == "kilo-Watts":
                    P3 = float(P * 1000)
                    p23 = str( "%.3f" % P3), "W"
                    var04.set(p23)

                if var11.get() == "mega-Watts":
                    P4 = float(P * 1000000)
                    p24 = str( "%.3f" % P4), "W"
                    var04.set(p24)

            else:
                var05.set(" At Least Two Parameters Are \n Required!")
            lblRes6.config(text="")

        def ClearOhms ():

            var01.set(""), var02.set(""), var03.set(""), var04.set(""), var05.set("")
            var2.set(0.0), var3.set(0.0), var4.set(0.0), var5.set(0.0), var8.set("Ohms"), var9.set("Volts"), \
            var10.set("Amps"), var11.set("Watts")
            lblRes6.config(text="Put Two Parameters To \nCalculate Others")




        def MotorSpeed():
            S = varSnyc.get()
            F = varFreq.get()
            P = varPole.get()

            if F>0 and P>0:
                S = 120 * F / P
                s = str("%.3f"%(S)), "r.p.m"
                var0Snyc.set(s)
            elif S>0 and P>0:
                F = S * P / 120
                f = str("%.3f" % (F)), "Hz"
                var0Freq.set(f)
            elif F>0 and S>0:
                P = 120 * F / S
                p = str("%.0f" % (P)), "poles"
                var0Pole.set(p)
            else:
                MotorDFrm.config(text="Please input to values first.   ")

        def ResetMotor():
            var0Freq.set("")
            var0Snyc.set("")
            var0Pole.set("")
            varSnyc.set("0")
            varFreq.set("0")
            varPole.set("0")
            MotorDFrm.config(text="Put two values find the other.")


        root1 = tk.Frame(self, width=865, height=650, bg="#111F11")
        root1.pack()

        top1 = tk.Frame(root1, width=865, height=20, bg="#111F11")
        top1.grid(row=0, column=0, columnspan=2, sticky="w")

        btnTopHome1 = tk.Button(top1, text="Mechanical", font=("arial", 10, "bold"), width=15, relief="groove", bd=2, bg="#111F11",
                        fg="white", command=lambda: controller.show_frame(Mechanical))
        btnTopHome1.grid(row=0, column=0,  padx=1, sticky="w")
        btnTopConv1 = tk.Button(top1, text="Electrical", font=("arial", 10, "bold"), width=15, relief="groove", bd=2, bg="#111F11",
                        fg="white", command=lambda: controller.show_frame(Statics))
        btnTopConv1.grid(row=0, column=1,  padx=1, sticky="w")

        btnExit = tk.Button(top1, text="Quit", relief="groove", bg="#111F11",
                        fg="red", command=qExit)
        btnExit.grid(row=0, column=2, sticky="e", columnspan=4, padx=50)

        btnTopConv1.config(state="disabled")

        frMainL1 = tk.LabelFrame(root1, width=750/3, height=400, text="MOTOR SPEED", font=("arial", 10, "bold"), bd=2,
                             bg="#111F11", fg="white")
        frMainL1.grid(row=1, column=0, sticky="nw", padx=10, pady=10)

        frMainL2 = tk.LabelFrame(root1, width=750/3, height=400, text="ELECTRICITY BILL CALCULATOR", font=("arial", 10, "bold"), bd=2,
                              bg="#111F11", fg="white")
        frMainL2.grid(row=1, column=1, sticky="nw", padx=10, pady=10)

        frMainR1 = tk.LabelFrame(root1, width=850/3, height=650, text="THEOREMS", font=("arial", 10, "bold"), bd=2,
                             bg="#111F11", fg="white")
        frMainR1.grid(row=1, column=2, rowspan=2, sticky="n", padx=10, pady=10)
        frMainB1 = tk.LabelFrame(root1, width=536, height=220, text="OHM'S LAW", font=("arial", 10, "bold"), bd=2,
                             bg="#111F11", fg="white")
        frMainB1.grid(row=2, column=0, columnspan=2, sticky="nw", padx=10, pady=10)

        canvMotor = tk.Canvas(frMainL1, width=700/3, height=120, bg="light green", relief="ridge")
        canvMotor.grid(row=0, column=0, columnspan=2, padx=10, pady=10)


        MotorS = tk.Label(canvMotor, text="Sychro Speed:", font=("arial", 10, "bold"), justify="right", bg="light green")
        MotorF = tk.Label(canvMotor, text="Supply Freq:", font=("arial", 10, "bold"), justify="right", bg="light green")
        MotorP = tk.Label(canvMotor, text="# of Poles:", font=("arial", 10, "bold"), justify="right", bg="light green")
        MotorDFrm = tk.Label(canvMotor, text="Put two values find the other.",
                          font=("arial", 7, "bold"), bg="light green", fg="red")

        MotorS.grid(row=0, column=0, padx=2, pady=2, sticky="e")
        MotorF.grid(row=1, column=0, padx=2, pady=2, sticky="e")
        MotorP.grid(row=2, column=0, padx=2, pady=2, sticky="e")
        MotorDFrm.grid(row=3, column=1, padx=1, pady=2, sticky="w")


        Motor0S = tk.Label(canvMotor,textvariable=var0Snyc, font=("arial", 10, "bold"), justify="left", bg="light green")
        Motor0F = tk.Label(canvMotor, textvariable=var0Freq, font=("arial", 10, "bold"), justify="left", bg="light green")
        Motor0P = tk.Label(canvMotor,textvariable=var0Pole, font=("arial", 10, "bold"), justify="left", bg="light green")

        Motor0S.grid(row=0, column=1, padx=6, pady=6, sticky="w")
        Motor0F.grid(row=1, column=1, padx=6, pady=5, sticky="w")
        Motor0P.grid(row=2, column=1, padx=6, pady=5, sticky="w")


        canvMotor.create_rectangle(105, 5, 230, 95)

        lblSnycSpeed = tk.Label(frMainL1, text="Synchronous \nSpeed(R.P.M)", font=("arial", 10, "bold"), justify="right", bg="#111F11",
                        fg="white")
        lblSnycSpeed.grid(row=1, column=0,  sticky="e", padx=10, pady=10)
        entrySnycSpeed = tk.Entry(frMainL1, width=15, bd=2, textvariable=varSnyc, relief="ridge", highlightbackground="green", highlightthickness=2)
        entrySnycSpeed.grid(row=1, column=1, sticky="e", padx=10, pady=5)

        lblSfreq = tk.Label(frMainL1, text="Supply \nFrequency (Hz)", font=("arial", 10, "bold"), justify="right", bg="#111F11",
                        fg="white")
        lblSfreq.grid(row=2, column=0,  sticky="e", padx=10, pady=10)
        entrySfreq = tk.Entry(frMainL1, width=15, bd=2, textvariable= varFreq, relief="ridge", highlightbackground="green", highlightthickness=2)
        entrySfreq.grid(row=2, column=1, sticky="e", padx=10, pady=5)


        lblNoPoles = tk.Label(frMainL1, text="Number of \nPoles", font=("arial", 10, "bold"), justify="right", bg="#111F11",
                        fg="white")
        lblNoPoles.grid(row=3, column=0,  sticky="e", padx=10, pady=10)
        entryNoPoles = tk.Entry(frMainL1, width=15, bd=2, textvariable= varPole, relief="ridge", highlightbackground="green",
                             highlightthickness=2)
        entryNoPoles.grid(row=3, column=1, sticky="e", padx=10, pady=5)

        btnCalcMotor = tk.Button(frMainL1, text="CALCULATE", font=("arial", 10, "bold"), width=15, bd=2, relief="groove",
                         bg="GREEN", command=MotorSpeed)
        btnCalcMotor.grid(row=4, column=0, rowspan=2, columnspan=1, padx=5, pady=15)
        btnResetMotor = tk.Button(frMainL1, text="RESET", font=("arial", 10, "bold"), width=10, bd=2, relief="groove",
                           bg="GREEN", command=ResetMotor)
        btnResetMotor.grid(row=4, column=1, columnspan=1, rowspan=2, padx=5, pady=15)

        def ElectricCost():
            P = varEApp.get()
            t = varEHours.get()
            C = varCost.get()
            App = varSelect.get()

            if item0.get() == True and C == "R1: ₦4.00":

                varEApp.set(1000)

                E = P * t/1000
                cd = (E * 4)
                cm = cd * 30
                cy = cm * 12
                e = "₦", str("%.2f" % cd), "k"
                e1 = "₦", str("%.2f" % cm), "k"
                e2 = "₦", str("%.2f" % cy), "k"
                varECostpD1.set(e)
                varECostpM1.set(e1)
                varECostpY1.set(e2)
            if item0.get() == True and C == "R2SP: ₦21.30":
                varEApp.set(1000)

                E = P * t/1000
                cd = E * 21.30
                cm = cd * 30
                cy = cm * 12
                e = "₦", str("%.2f" % cd), "k"
                e1 = "₦", str("%.2f" % cm), "k"
                e2 = "₦", str("%.2f" % cy), "k"
                varECostpD1.set(e)
                varECostpM1.set(e1)
                varECostpY1.set(e2)
            if item0.get() == True and C == "R2TP: ₦21.80":
                varEApp.set(1000)

                E = P * t/1000
                cd = E * 21.80
                cm = cd * 30
                cy = cm * 12
                e = "₦", str("%.2f" % cd), "k"
                e1 = "₦", str("%.2f" % cm), "k"
                e2 = "₦", str("%.2f" % cy), "k"
                varECostpD1.set(e)
                varECostpM1.set(e1)
                varECostpY1.set(e2)
            if item1.get() == True and  C == "R1: ₦4.00":
                varEApp.set(2000)

                E = P * t / 1000

                cd = E * 4
                cm = cd * 30
                cy = cm * 12
                e = "₦", str("%.2f" % cd), "k"
                e1 = "₦", str("%.2f" % cm), "k"
                e2 = "₦", str("%.2f" % cy), "k"
                varECostpD1.set(e)
                varECostpM1.set(e1)
                varECostpY1.set(e2)
            if item1.get() == True and C == "R2SP: ₦21.30":
                varEApp.set(2000)

                E = P * t / 1000
                cd = E * 21.30
                cm = cd * 30
                cy = cm * 12
                e = "₦", str("%.2f" % cd), "k"
                e1 = "₦", str("%.2f" % cm), "k"
                e2 = "₦", str("%.2f" % cy), "k"
                varECostpD1.set(e)
                varECostpM1.set(e1)
                varECostpY1.set(e2)
            if item1.get() == True and C == "R2TP: ₦21.80":
                varEApp.set(2000)

                E = P * t / 1000
                cd = E * 21.80
                cm = cd * 30
                cy = cm * 12
                e = "₦", str("%.2f" % cd), "k"
                e1 = "₦", str("%.2f" % cm), "k"
                e2 = "₦", str("%.2f" % cy), "k"
                varECostpD1.set(e)
                varECostpM1.set(e1)
                varECostpY1.set(e2)


        def ResetElectric ():
            varECostpD1.set("")
            varECostpM1.set("")
            varECostpY1.set("")

            varEApp.set("0.0")
            varSelect.set("Select")
            varEHours.set("0.0")
            varCost.set("")

        #==============================================Electric Cost============================================================
        canvElectric = tk.Canvas(frMainL2, width=650/3, height=100, bg="light green", relief="ridge")
        canvElectric.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        ECostpD = tk.Label(canvElectric, text="Cost/Day:", font=("arial", 10, "bold"), justify="right", bg="light green")
        ECostpM = tk.Label(canvElectric, text="Cost/Month:", font=("arial", 10, "bold"), justify="right", bg="light green")
        ECostpY = tk.Label(canvElectric, text="Cost/Year:", font=("arial", 10, "bold"), justify="right", bg="light green")
        ECostpD.grid(row=0, column=0, sticky="e", pady=6, padx=6)
        ECostpM.grid(row=1, column=0, sticky="e", pady=6, padx=6)
        ECostpY.grid(row=2, column=0, sticky="e", pady=6, padx=6)

        ECostpD1 = tk.Label(canvElectric, textvariable=varECostpD1, font=("arial", 10, "bold"), justify="right", bg="light green")
        ECostpM1 = tk.Label(canvElectric, textvariable=varECostpM1, font=("arial", 10, "bold"), justify="right", bg="light green")
        ECostpY1 = tk.Label(canvElectric, textvariable=varECostpY1, font=("arial", 10, "bold"), justify="right", bg="light green")
        ECostpD1.grid(row=0, column=1, sticky="w", pady=6, padx=6)
        ECostpM1.grid(row=1, column=1, sticky="w", pady=6, padx=6)
        ECostpY1.grid(row=2, column=1, sticky="w", pady=6, padx=6)

        ECostConst = tk.Frame(canvElectric, width=130)
        ECostConst.grid(row=3, column=1)

        canvElectric.create_rectangle(95, 5, 215, 100)

        lblEApp = tk.Label(frMainL2, text="Appliance:", font=("arial", 10, "bold"), justify="right",
                        bg="#111F11", fg="white")
        lblEApp.grid(row=1, column=0, sticky="e", padx=5, pady=5)

        lblEPowr = tk.Label(frMainL2, text="Power\nConsumped(W):", font=("arial", 10, "bold"), justify="right",
                        bg="#111F11", fg="white")
        lblEPowr.grid(row=2, column=0,  sticky="e", padx=5, pady=5)
        entryEApp = tk.Entry(frMainL2, width=10, bd=2, relief="ridge", highlightbackground="green", textvariable=varEApp,
                          highlightthickness=2)
        entryEApp.grid(row=2, column=1, sticky="e", padx=2, pady=5)

        lblEHours = tk.Label(frMainL2, text="Hours of Use\nPer Day (h/day):", font=("arial", 10, "bold"), justify="right",
                          bg="#111F11", fg="white")
        lblEHours.grid(row=3, column=0,  sticky="e", padx=5, pady=10)
        entryEHours = tk.Entry(frMainL2, width=10, bd=2, relief="ridge", highlightbackground="green",
                            textvariable=varEHours, highlightthickness=2)
        entryEHours.grid(row=3, column=1, sticky="e", padx=2, pady=5)


        lblECost = tk.Label(frMainL2, text="1 kWh Cost (₦):", font=("arial", 10, "bold"), justify="right", bg="#111F11",
                        fg="white")
        lblECost.grid(row=4, column=0,  sticky="e", padx=5, pady=10)

        cmbCost = ttk.Combobox(frMainL2, font=("arial", 9, "bold"), textvariable=varCost, width=14, state="randomly")
        cmbCost["value"] = ("R1: ₦4.00", "R2SP: ₦21.30")

        ''', "R2TP: ₦21.80", "R3: 36.49", "R4: ₦36.92", "C1SP: ₦27.20",
        "C1TP: ₦28.47", "C2: ₦37.74", "C3: ₦38.14", "D1: ₦28.68", "D2: ₦38.38", "D3: ₦38.85",

    "A1:26.82", "A2: ₦30.20", "A3: ₦30.36", "S1: ₦19.42"'''
        cmbCost.current(0)
        cmbCost.grid(row=4, column=1, sticky="w", padx=2, pady=5)


        '''menuSelect = Menubutton(frMainL2, text="Select", font=("arial", 8,"bold"), width=13, height=1,
                                indicatoron=True, bd=3, relief=GROOVE, bg="#111F11", fg="white", textvariable=varSelect)
        menu = Menu(menuSelect, tearoff=False)
        menuSelect.config(menu=menu)
        menuSelect.grid(row=1, column=1, sticky=W, padx=2, pady=5)
        self.choices = {}
        for choice in ("Electric Iron", "Luandary", "Electric Kettle", "Refridgretor",
                                  "Air Conditioner", "Dish Washer", "Electric Stove", "Lighting"):
            self.choices[choice] = IntVar(value=0)
            menu.add_checkbutton(label=choice, variable=self.choices[choice], onvalue=1, offvalue=0)
            menu.add_separator()'''

        mb = tk.Menubutton(frMainL2, text="Select", font=("arial", 8, "bold"),width=18, height=1, relief="groove", bd=3,
                        bg="#111F11", fg="white", textvariable=varSelect)
        mb.grid(row=1, column=1, sticky="w", padx=2, pady=5)
        mb.menu = tk.Menu(mb, tearoff=0)
        mb["menu"] = mb.menu

        mb.menu.add_checkbutton(label="Electric iron", variable=item0)
        mb.menu.add_separator()
        mb.menu.add_checkbutton(label="Luandary", variable=item1)
        mb.menu.add_separator()
        #mb.menu.add_checkbutton(label="Electric Kettle", variable=item2)
        #mb.menu.add_separator()
        mb.grid()

        #entryECost = Entry(frMainL2, width=10, bd=2, relief=RIDGE, highlightbackground="green", highlightthickness=2)
        #entryECost.grid(row=4, column=1, sticky=E, padx=10, pady=5)

        btnCalcElect = tk.Button(frMainL2, text="CALCULATE", font=("arial", 10, "bold"), width=12, bd=2, relief="groove",
                         bg="GREEN", command=ElectricCost)
        btnCalcElect.grid(row=5, column=0, rowspan=2, columnspan=1, padx=5, pady=15)
        btnResetElect = tk.Button(frMainL2, text="RESET", font=("arial", 10, "bold"), width=10, bd=2, relief="groove",
                           bg="GREEN", command =ResetElectric )
        btnResetElect.grid(row=5, column=1, columnspan=1, rowspan=2, padx=5, pady=15)

        canvTheorem = tk.Canvas(frMainR1, width=750/3, height=590, relief="ridge", bd=5,
                             bg="#111F11")
        canvTheorem.grid(row=0, column=0, padx=10, pady=10)

        canvTheorem.ImageIkej = tk.PhotoImage(file="ikeja3.png")

        canvTheorem.create_image(250/2, 140/2, image=canvTheorem.ImageIkej)
        canvTheorem.create_rectangle(9, 390, 254, 430, width=2, outline="white")
        canvTheorem.create_text(130, 305, text="Energy consumption calculation", font=("arial", 10, "bold"), fill="white")

        canvTheorem.create_text( 120, 340, text= """  
        The energy E in kilowatt-hours (kWh) per 
        day is equal to the power P in watts (W) 
        times number of usage hours per day t 
        divided by 1000 watts per kilowatt:""", justify= "center", fill="white")

        canvTheorem.create_text(130, 413, text="E(kWh/day) = P(W) x t(h/day) /1000(W/kW)", font=("times", 9, "bold"), fill="white")

        canvTheorem.create_text(120, 490, text="""
        The electricity cost per day in naira is 
        equal to the energy consumption E in kWh per 
        day times the energy \ncost of 1kWh 1 Naira/kWh.""", justify= "center", fill="white")
        canvTheorem.create_rectangle(9, 590, 254, 550, width=2, outline="white")
        canvTheorem.create_text(130, 450, text="Electricity cost calculation", font=("arial", 10, "bold"), fill="white")
        canvTheorem.create_text(130, 570, text="Cost(₦/day) = E(kWh/day) x Cost(Naira/kWh))",
                                font=("times", 8, "bold"), fill="white")


        lblResistance = tk.Label(frMainB1, text="Resistance (Ω):", font=("arial", 10, "bold"), justify="right",
                        bg="#111F11", fg="white")
        lblResistance.grid(row=0, column=0, sticky="e", padx=2, pady=10)

        entryResistance = tk.Entry(frMainB1, width=10, bd=2, relief="ridge", textvariable=var2,
                                highlightbackground="green", highlightthickness=2)
        entryResistance.grid(row=0, column=1, sticky="e", padx=10, pady=5)

        cmbResistance = ttk.Combobox(frMainB1, font=("arial", 9, "bold"), textvariable=var8, width=14, state="randomly")
        cmbResistance["value"] = ("Ohms", "milli-Ohms", "kilo-Ohms", "Mega-Ohms")
        cmbResistance.current(0)
        cmbResistance.grid(row=0, column=2, sticky="e", padx=2, pady=10)

        lblVoltage = tk.Label(frMainB1, text="Voltage (V):", font=("arial", 10, "bold"), justify="right",
                         bg="#111F11", fg="white")
        lblVoltage.grid(row=1, column=0, sticky="e", padx=5, pady=5)

        entryVoltage = tk.Entry(frMainB1, width=10, bd=2, relief="ridge", highlightbackground="green",
                                textvariable=var3, highlightthickness=2)
        entryVoltage.grid(row=1, column=1, sticky="e", padx=10, pady=5)

        cmbVoltage = ttk.Combobox(frMainB1, font=("arial", 9, "bold"), textvariable=var9, width=14, state="randomly")
        cmbVoltage["value"] = ("Volts", "milli-Volts", "kilo-Volts", "Mega-Volts")
        cmbVoltage.current(0)
        cmbVoltage.grid(row=1, column=2, sticky="w", padx=2, pady=10)


        lblCurrent = tk.Label(frMainB1, text="Current (A):", font=("arial", 10, "bold"), justify="right",
                         bg="#111F11", fg="white")
        lblCurrent.grid(row=2, column=0, sticky="e", padx=5, pady=5)

        entryCurrent = tk.Entry(frMainB1, width=10, bd=2, relief="ridge", highlightbackground="green",
                                textvariable=var4, highlightthickness=2)
        entryCurrent.grid(row=2, column=1, sticky="e", padx=10, pady=5)

        cmbCurrent = ttk.Combobox(frMainB1, font=("arial", 9, "bold"), textvariable=var10, width=14, state="randomly")
        cmbCurrent["value"] = ("Amps", "milli-Amps", "kilo-Amps", "Mega-Amps")
        cmbCurrent.current(0)
        cmbCurrent.grid(row=2, column=2, sticky="w", padx=2, pady=10)

        lblPower = tk.Label(frMainB1, text="Power (W):", font=("arial", 10, "bold"), justify="right",
                           bg="#111F11", fg="white")
        lblPower.grid(row=3, column=0, sticky="e", padx=5, pady=5)

        entryPower = tk.Entry(frMainB1, width=10, bd=2, relief="ridge", highlightbackground="green",
                             textvariable=var5, highlightthickness=2)
        entryPower.grid(row=3, column=1, sticky="e", padx=10, pady=5)

        cmbPower = ttk.Combobox(frMainB1, font=("arial", 9, "bold"), textvariable=var11, width=14, state="randomly")
        cmbPower["value"] = ("Watts", "milli-Watts",  "kilo-Watts", "Mega-Watts")
        cmbPower.current(0)
        cmbPower.grid(row=3, column=2, sticky="w", padx=2, pady=10)

        canvOhms = tk.Canvas(frMainB1, width=180, height=140, bd=4, relief="ridge", bg="light green")
        canvOhms.grid(row=0, column=3, rowspan=3, padx=10, pady=10)

        #canvOhms.create_text(90, 20, text="Input two known values to \ncalculate the rest", justify="center", fill="white")

        frmBtnOhms = tk.Frame(frMainB1, width=180, height=50,  bg="#111F11")
        frmBtnOhms.grid(row=3, column=3, rowspan=2)

        btnCalcOhms = tk.Button(frmBtnOhms, text="CALCULATE", width=10,  font=("arial", 10, "bold"), relief="groove",
                             bd=3, bg="green", command=PowerConsumption)
        btnCalcOhms.grid(row=0, column=0, padx=10)

        btnResetOhms = tk.Button(frmBtnOhms, text="RESET", width=6, font=("arial", 10, "bold"), relief="groove",
                              bd=3, bg="green", command=ClearOhms)
        btnResetOhms.grid(row=0, column=1, padx=10, sticky="e")


        lblRes1 = tk.Label(canvOhms, textvariable = var01, font=("arial", 10, "bold"), justify="right", bg="light green")
        lblRes1.grid(row=0, column=1, sticky="w", pady=5, padx=6)
        lblRes01 = tk.Label(canvOhms, text="Resistance:", font=("arial", 10, "bold"), justify="right", bg="light green")
        lblRes01.grid(row=0, column=0, sticky="w", pady=3, padx=6)
        lblRes2 = tk.Label(canvOhms, textvariable=var02, font=("arial", 10, "bold"), justify="right", bg="light green")
        lblRes2.grid(row=1, column=1, sticky="w", pady=6, padx=6)
        lblRes02 = tk.Label(canvOhms, text="Voltage:", font=("arial", 10, "bold"), justify="right", bg="light green")
        lblRes02.grid(row=1, column=0, sticky="w", pady=1, padx=6)
        lblRes3 = tk.Label(canvOhms, textvariable=var03, font=("arial", 10, "bold"), justify="right", bg="light green")
        lblRes3.grid(row=2, column=1, sticky="w", pady=1, padx=6)
        lblRes03 = tk.Label(canvOhms, text="Current:", font=("arial", 10, "bold"), justify="right", bg="light green")
        lblRes03.grid(row=2, column=0, sticky="w", pady=1, padx=6)
        lblRes4 = tk.Label(canvOhms, textvariable=var04, font=("arial", 10, "bold"), justify="right", bg="light green")
        lblRes4.grid(row=3, column=1, sticky="w", pady=1, padx=6)
        lblRes04 = tk.Label(canvOhms, text="Power :", font=("arial", 10, "bold"), justify="right", bg="light green")
        lblRes04.grid(row=3, column=0, sticky="w", pady=1, padx=6)
        lblRes5 = tk.Label(canvOhms, textvariable=var05, font=("arial", 8), justify="left", fg="red",bg="light green")
        lblRes5.grid(row=4, column=0,columnspan=2, sticky="w", pady=2, padx=6)
        lblRes5 = tk.Frame(canvOhms, width=177, height=1, bg="light green")
        lblRes5.grid(row=5, column=0, columnspan=2, sticky="w", pady=1, padx=4)
        lblRes6 = tk.Label(canvOhms, text=" Put Two Parameters To Calculate \nOthers", font=("arial", 8), justify="left", fg="red", bg="light green")
        lblRes6.grid(row=4, column=0, columnspan=2, sticky="w", pady=2, padx=6)

        '''canvOhms.create_text(90, 45, text="V(v) = I(A) x R(Ω)", font=("times", 10, "bold"), fill="white")
        canvOhms.create_text(90, 80, text="To calculate Power P, \nyou use any of these:", justify="center", fill="white")
        canvOhms.create_text(90, 117, text="P(W) = I(A) x R^2(Ω^2) \nor V(v)/R(Ω) \nor I^2(A^2)xV(v)",
                             justify= "center", font=("times", 9, "bold"), fill="white")

        canvOhms.create_rectangle(15, 37, 175, 57, outline="white", width=2)
        canvOhms.create_rectangle(15, 96, 175, 140, outline="white", width=2)'''

class Civil(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#111F11")
        root2 = tk.Frame(self, width=865, height=650, bg="#111F11")
        root2.pack()
        var8 = tk.StringVar()
        var9 = tk.StringVar()
        #var10 = StringVar()
        P = tk.StringVar()
        I = tk.DoubleVar()
        V = tk.DoubleVar()
        R = tk.DoubleVar()

        def quit():
            app.destroy()

        def qExit():
            rely = messagebox.askyesno("Quit System", "Do You Want To Quit The System?")
            if rely is True:
                app.destroy()
            return


        frmTop2 = tk.Frame(root2, width=865, height=150, bg="#111F11")
        frmTop2.grid(row=1, column=0)

        canvComakers = tk.Canvas(frmTop2, width= 800, height=250, bg="#111F11")
        canvComakers.pack(side="bottom", fill="both", expand=True, pady=50)

        canvComakers.comakersImage = tk.PhotoImage(file="comakers2.png")

        canvComakers.create_image(800/2, 250/2, image= canvComakers.comakersImage)


        frmMID2 = tk.LabelFrame(root2, text="Agreement:", font=("arial", 10, "bold"), width=865, height=50, bg="#111F11",
                             fg="white")
        frmMID2.grid(row=2, column=0, padx=120, pady=5, sticky="w")

        lblWelcome = tk.Label(frmMID2, text="""Welcome to CoMakers Engineering Calculator""", font=("arial", 20, "bold"),
                          bg="#111F11", fg="white")
        lblWelcome.grid(row=0, column=0, columnspan=2, padx=10, pady=5)


        lblAgreement = tk.Label(frmMID2, text="This is a tool to carry out the most tasking engineering assignments. "
                                           "\nThe morden day application developed by CoMakers Africa, is super useful for both education, "
                                           "\nprofessional and home purposes. This tool contains two sections of engineering assignments; "
                                           "\nthe Electrical Tools and Mechanical Tools. Meanwhile, the tool is regulated under a law. "
                                           "\nYou can visit www.comakersafrica.org/terms to read the privacy terms."
                                           "\nTo use, you must agree with the terms and condition of CoMakers Africa. "
                                           "\nTo continue, click on Agree, otherwise, click on Disagree to exit the tool",
                             font=("arial", 10, "bold"), bg="#111F11", fg="white", justify= "center")
        lblAgreement.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

        btnAgree = tk.Button(frmMID2, width=8,  text="Agree", font=("arial", 12, "bold"), relief="groove",
                          command=lambda : controller.show_frame(Mechanical))
        btnAgree.grid(row=2, column=0, padx=5, pady=10, sticky="w")

        btnDisagree = tk.Button(frmMID2, width=8, text="Disagree", font=("arial", 12, "bold"), relief="groove", command=quit)
        btnDisagree.grid(row=2, column=1, padx=5, pady=10, sticky="e")


app = TrailApps()
ani = animation.FuncAnimation(f, animate, interval=1000)
app.mainloop()






