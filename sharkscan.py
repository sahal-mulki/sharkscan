import subprocess
from OuiLookup import OuiLookup
def dynamic(name, num, variable):

    globals()[name + num] = variable

    return name + num
def get_mac(mac):


    return OuiLookup().query(mac)
def main_ray():
    output = subprocess.getoutput("arp -a")

    good_lines = []

    cleaned_output = output.split("\n")

    thing = -1

    for x in cleaned_output[:]:

        if "Interface" in x:

            cleaned_output.remove(x)

        if "Type" in x:

            cleaned_output.remove(x)

    for x in cleaned_output[:]:

        if "Interface" in x:

            cleaned_output.remove(x)


    cleaned_output.pop(0)

    l_cleaned_output = cleaned_output

    thing = -1
    thingo = -1

    for x in cleaned_output[:]:

        if x == '':

            cleaned_output.remove('')


    for x in cleaned_output[:]:

        thing = thing + 1

        x_copy = x

        x_copy = x_copy.split("  ")

        for nirgth in range(10):

            try:
                x_copy.remove('')

            except:

                for nigrgrg in range(10):
                    try:
                        x_copy.remove(' ')

                    except:

                        break

                break

        nameofvar = dynamic("Device", str(thing), x_copy)



    for xax in range(thing):

        thingo_wingo = globals()["Device" + str(xax)]

        ilole = thingo_wingo[1].replace(" ", "")
        thingo90 = ilole.replace('-', '').upper()

        ress = str(thingo_wingo[0]) + str(", ") + str(get_mac(ilole)[0][thingo90]), str("," + thingo_wingo[2] + " IP")        
        good_lines.append(ress)

    return str(good_lines), thing



def when_start():

    
    window = Tk()
    window.geometry("1000x350")

    Text_to_change = StringVar()
    Text_to_change2 = StringVar()


    Text_to_change.set("""

    Scanning and Updating....""")
    Text_to_change2.set("")
    
    Font_tuple = ("Bahnschrift", 20, "bold")
  
    Title = Label(textvariable=Text_to_change2)
    Title.configure(font = Font_tuple)
    Title.pack()

    label = Label(
        textvariable=Text_to_change
        )

    label.pack()

    if var.get() == 1:
        print(var.get())
        OuiLookup().update()

    results, thing = main_ray()

    result = results.replace("(", "\n")
    result = result.replace(")", "")
    result = result.replace("[", "")
    result = result.replace("'", "")


    Text_to_change.set(result)
    Text_to_change2.set("""Hosts On Network:

                        """)
                
    window.mainloop()











from tkinter import *

window = Tk()
window.geometry("500x250")
label = Label(
    text="""SharkScan, The Network Scanner


    """,
)
label.pack()

global var
var = IntVar()

button = Button(
    text="Start Scanning",

    width=25,
    height=5,
    command=lambda:[window.destroy(), when_start()]
)

c = Checkbutton(window, text = "Update MAC lookup table before scanning (may take time)?", variable=var)
c.pack()

button.pack()

window.mainloop()
