from tkinter import *
import csv

def call_back():
    a=[]
    a.append(text_fn.get())
    a.append(text_ln.get())
    a.append(text_fan.get())
    a.append(text_id.get())
    a.append(button_checked1.get())
    a.append(button_checked2.get())
    a.append(text_coll.get())
    a.append(text_colll.get())
    with open('DataBase.csv', 'a', newline='') as csvfile:
        fieldnames = ['First_name', 'Last_name','Reg No','Email','Male','Female','college','Department']
        spamwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
        spamwriter.writerow({'First_name':a[0],'Last_name':a[1],'Reg No':a[2],'Email':a[3],'Male':a[4],'Female':a[5],'college':a[6],'Department':a[7]})
    print("DONE...!!!")
roott = Tk()

roott.title("Student's Details Form")
Label(roott, text="First Name:").grid(row=0, column=0)
text_fn=StringVar()
Entry(roott, width=30, textvariable=text_fn).grid(row=0, column=1, columnspan=9)

Label(roott, text="Last Name:").grid(row=1, column=0)
text_ln=StringVar()
Entry(roott, width=30, textvariable=text_ln).grid(row=1, column=1, columnspan=9, padx=6, pady=6)

Label(roott, text="Redistered No:").grid(row=0, column=10)
text_fan=StringVar()
Entry(roott, width=30, textvariable=text_fan).grid(row=0, column=11)

Label(roott, text="Email Id:").grid(row=1, column=10)
text_id=StringVar()
Entry(roott, width=30, textvariable=text_id).grid(row=1, column=11,padx=2)

button_checked1=StringVar()
button_checked2=StringVar()
Checkbutton(roott, text="M", variable=button_checked1, onvalue="Y", offvalue="N").grid(row=2, column=2)
Checkbutton(roott, text="F", variable=button_checked2, onvalue="Y", offvalue="N").grid(row=3, column=2)

Label(roott, text="College:").grid(row=2,column=3,columnspan=7)
text_coll=StringVar()
spinbox1 = Spinbox(roott, value=("REC","RIT","PHARM"),state=NORMAL, textvariable=text_coll).grid(row=2, column=4,columnspan=8)

Label(roott, text="Department:").grid(row=3,column=3,columnspan=7)
text_colll=StringVar()
spinbox1 = Spinbox(roott, value=("CSE","ECE","EEE","MECH","CIVIL"),state=NORMAL, textvariable=text_colll).grid(row=3, column=4,columnspan=8)
Button(roott, text="Submit", command=call_back).grid(row=5, column=5, columnspan=6)

roott.mainloop()
