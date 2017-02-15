import re
import ttk
from Tkinter import Tk, BOTH, Listbox, StringVar, END, Entry, Label



def is_not_int(x):
    try:
        x = int(x)
        return False
    except:
        return True

main = Tk()
main.title("Cpt Params")
main.geometry("+50+150")
frame1 = ttk.Frame(main, padding=(3, 3, 12, 12))
frame1.grid(column=0, row=0, sticky=('N', 'S', 'E', 'W'))

values = StringVar()
values.set("Voltage Calcium CalciumER")

lbl = Label(frame1, text="Options")
lbl.grid(column=0, row=0)

lstbox = Listbox(frame1, listvariable=values, selectmode='multiple', width=20, height=3)
lstbox.grid(column=1, row=0, columnspan=2)

lbl2 = Label(frame1, text="How Many Branchtype")
lbl2.grid(column=0, row=1)

txtbox = Entry(frame1)
txtbox.grid(column=1, row=1)

def initalwrite():
    global reslist
    reslist = list()
    selection = lstbox.curselection()
    for i in selection:
        ent = lstbox.get(i)
        reslist.append(ent)
    howmany = txtbox.get()
    if is_not_int(howmany):
        howmany = 0
    else:
        howmany = int(howmany)
    if (howmany > 7 or howmany < 0):
        howmany = 0
    cptfile = open("CptParams.par", 'w')
    cptfile.write("COMPARTMENT_VARIABLE_TARGETS %d \nBRANCHTYPE\n" % (howmany))
    idx = 0
    while idx < howmany:
        cptfile.write("%d %s\n" % (idx+1, re.sub('[\[\]\',]','',str(reslist))))
        idx += 1
    cptfile.close()
    frame1.quit()



btn = ttk.Button(frame1, text="Generate", command=initalwrite)
btn.grid(column=1, row=2)

main.mainloop()

second = Tk()
second.title("Chan Params")
second.geometry("+50+150")
frame2 = ttk.Frame(second, padding=(3, 3, 12, 12))
frame2.grid(column=0, row=0, sticky=('N', 'S', 'E', 'W'))



lbl1 = Label(frame2, text="Channel Name")
lbl1.grid(column=0, row=0)

txtbox1 = Entry(frame2)
txtbox1.grid(column=1, row=0)

lbl2 = Label(frame2, text="Input")
lbl2.grid(column=0, row=1)

lstbox1 = Listbox(frame2, selectmode='multiple', width=20, height=3, exportselection=0)
lstbox1.grid(column=1, row=1, columnspan=2)
for item in reslist:
        lstbox1.insert(END, item)


lbl4 = Label(frame2, text="Output")
lbl4.grid(column=0, row=2)

lstbox2 = Listbox(frame2, selectmode='multiple', width=20, height=3, exportselection=0)
lstbox2.grid(column=1, row=2, columnspan=2)
for item in reslist:
        lstbox2.insert(END, item)

lbl5 = Label(frame2, text="Channel Type")
lbl5.grid(column=0, row=3)

lstbox3 = Listbox(frame2, selectmode='multiple', width=20, height=7, exportselection=0)
lstbox3.grid(column=1, row=3, columnspan=2)
for num in range(1,8):
    lstbox3.insert(END, num)

def finalwrite():
    input1 = list()
    input2 = list()
    input3 = list()
    selection1 = lstbox1.curselection()
    for i in selection1:
        ent = lstbox1.get(i)
        input1.append(ent)
    selection2 = lstbox2.curselection()
    for i in selection2:
        ent = lstbox2.get(i)
        input2.append(ent)
    selection3 = lstbox3.curselection()
    for i in selection3:
        ent = lstbox3.get(i)
        input3.append(ent)
    chanfile = open('ChanParams.par', 'w')
    chanfile.write("CHANNEL_TARGETS %d\nBranchtype\n" % (len(input3)))
    for numstring in input3:
        chanfile.write("%s %s %s %s\n" % (numstring, txtbox1.get(), re.sub('[\']','',str(input1)),
                                          re.sub('[\']','',str(input2)),))
    chanfile.close()
    frame2.quit()

btn1 = ttk.Button(frame2, text="Add", command=finalwrite)
btn1.grid(column=1, row=4)


second.mainloop()