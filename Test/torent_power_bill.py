amnt = 0.00 
def RGPC():
    print("-----Residential General Purpose------")
    print("*************************************")
    def RGP():
        global amnt
        unit = int(input("Enter Unit :- "))
        phase = int(input("Enter Phase 1 or Phase 3 :- "))
        while phase not in (1,3):
            phase = int(input("Please Enter Correct Phase 1 or Phase 3 :- "))
        if (unit<=50):
            amnt += 320 * unit
        elif (unit >50 & unit<=200):
            amnt += 16000
            amnt += (unit-50) * 390
        else:
            amnt += 74500
            amnt += (unit-200) * 490 
        amnt += 2500 if (phase == 1) else 6500
        return amnt
    def BPL():
        print("----Below Poverty Line----")
        global amnt
        amnt = 500
        unit = int(input("Enter Unit :- "))
        if (unit<=30):
            amnt += 150 * unit
        elif (unit >30 & unit<=50):
            amnt += 4500
            amnt += (unit-30) * 320
        elif (unit >50 & unit<=200):
            amnt += 10900
            amnt += (unit-50) * 390
        else:
            amnt += 69400
            amnt += (unit-200) * 490
        return amnt 
    sub = input("IS Customer Under BPL?? (yes/no): ").lower()
    return BPL() if (sub=="yes") else RGP()
def GLP():
    print("-----General Lighting Purpose------")
    print("*************************************")
    global amnt
    unit = int(input("Enter Unit :- "))
    phase = int(input("Enter Phase 1 or Phase 3 :- "))
    while phase not in (1,3):
        phase = int(input("Please Enter Correct Phase 1 or Phase 3 :- "))
    if (unit<=200):
        amnt += 410 * unit
    else:
        amnt = 82000
        amnt += 480 * (unit - 200)
    if (phase == 1):
        amnt += 3500
    else:
        amnt += 7000
    return amnt
def NON_RGP():
    print("--Low Tension Service for Commercial and Industrial Purpose--")
    print("*************************************")
    global amnt
    amnt = 450
    kw = int(input("Enter Kilowalt :- "))
    amnt += 700 if kw <= 5 else 900
    return amnt
def LTP():
    print("-----Agriculture Service------")
    print("*************************************")
    global amnt
    unit = int(input("Enter Unit :- "))
    amnt += 330 * unit
    bhp = 1.34 * unit *1000
    amnt=amnt if (amnt > bhp) else bhp   
    return amnt
def LTMD1():
    return "Your Category is LTMD1"
def LTMD2():
    return "Your Category is LTMD2"
def SL():
    print("-----Low Tension Tension Street Light Service------")
    print("*************************************")
    global amnt
    unit = int(input("Enter Unit :- "))
    amnt += 420 * unit
    return amnt
def LEV():
    print("----- LT- Electric Vehicle Charging Stations------")
    print("*************************************")
    global amnt
    unit = int(input("Enter Unit :- "))
    #Rs. 25/kw/day
    amnt += 410 * unit +2500
    return amnt
def TMP():
    print("-----Low Tension Temporary Supply------")
    print("*************************************")
    global amnt
    unit = int(input("Enter Unit :- "))
    #Rs. 25/kw/day
    amnt += 500 * unit +2500
    return amnt    
def HTMD1():    
    return "Your Category is HTMD1" 
def HTMD2():
    return "Your Category is HTMD2"
def HTMD3():
    return "Your Category is HTMD3"
def EV():
    print("-----Electical Vehicle Charging Stations------")
    print("*************************************")
    global amnt
    unit = int(input("Enter Unit :- "))
    amnt += 400 * unit
    return amnt
def HTMD():
    return "Your Category is HTMD"

if __name__ == "__main__":
    print("**************CATEGORY***************")
    print ("1-RGP\n2-GLP\n3-NON_RGP \n4-LTP \n5LTMD1 \n6-LTMD2 \n7-SL \n8-LEV \n9-TMP \n10-HTMD1 \n11-HTMD2 \n12-HTMD3 \n13-EV \n14-HTMD")
    print("*************************************")
    switcher = {
        1: RGPC,
        2: GLP,
        3: NON_RGP,
        4: LTP,
        5: LTMD1,
        6: LTMD2,
        7: SL,
        8: LEV,
        9: TMP,
        10: HTMD1,
        11: HTMD2,
        12: HTMD3,
        13: EV,
        14: HTMD
                    }
    def category(arg):
        func = switcher.get(arg)
        return func()
    choice = int(input("Enter Your Category :- "))
    while choice >14:
        choice = int(input("Invalid Choice PLease Enter Correct Category :- "))
    print("*************************************")
    print (category(choice))
    print("--------------------------------------")
    print(f"Final Amount To Be Paid: {amnt/100} Rs.")
    print("--------------------------------------")
