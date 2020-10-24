import hashlib
import random
import string
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
from GUI import Application

root = Tk()
quit_button = Button(root, text='Exit', fg='red')
quit_button.pack(side=BOTTOM)

<<<<<<< HEAD
img = ImageTk.PhotoImage(Image.open("E:\Cyber_Security_MIni_toolkit\DMI-St.-Eugene-University-logo-258x300.png"))
=======
img = ImageTk.PhotoImage(Image.open("DMI-St.-Eugene-University-logo-258x300.png"))
>>>>>>> 27ad982bdee10016eeb58139123d1c43e4431be7
panel = Label(root, image = img,)
panel.pack(side = "top")
f1 = StringVar()
f2 = StringVar()
Sha256f1 = StringVar()
Sha256f2 = StringVar()
MD5f1 = StringVar()
MD5f2 = StringVar()
Sha1f1 = StringVar()
Sha1f2 = StringVar()

checksum = Frame(root, width=1350, height=1000, relief='raise', bd=14)

checksum.pack(side=LEFT, expand=True,fill = None)
password_gen = Frame(root, width=100, height=100, relief='raise', bd=14)
password_gen.pack(side=RIGHT, expand=True,fill= 'y')
stego = Frame(root, width=1350, height=1000, relief='raise', bd=14)
stego.pack(side=RIGHT,expand=True, fill= 'y')
app = Application(stego)

ckslbl = Label(checksum, text='CHECKSUM VERIFER').pack(side=TOP)
stegolbl = Label(stego,text='STEGANOGRAPHY MINI-TOOLKIT').pack(side=TOP)
password_genlbl = Label(password_gen,text="SECURE PASSWORD GENERATOR").pack(side=TOP)

def hash_bytestr_iter(bytesiter, hasher, ashexstr=True):
    for block in bytesiter:
        hasher.update(block)
    return (hasher.hexdigest() if ashexstr else hasher.digest())


def file_as_blockiter(afile, blocksize=65536):
    with afile:
        block = afile.read(blocksize)
        while len(block) > 0:
            yield block
            block = afile.read(blocksize)


def CmpHashes():
    # Check MD5
    if MD5f1.get() and MD5f2.get():
        if MD5f1.get() == MD5f2.get():
            print("MD5 match!")
            MD5Lbl.config(bg='green')
            checksum.update()
        else:
            print("MD5 does not match!")
            MD5Lbl.config(bg='red')
            checksum.update()
    else:
        MD5Lbl.config(bg='yellow')
        print("MD5 data unavalible!")
        checksum.update()

    # Check Sha1
    if Sha1f1.get() and Sha1f2.get():
        if Sha1f1.get() == Sha1f2.get():
            print("Sha1 match!")
            Sha1Lbl.config(bg='green')
            checksum.update()
        else:
            print("Sha1 does not match!")
            Sha1Lbl.config(bg='red')
            checksum.update()
    else:
        Sha1Lbl.config(bg='yellow')
        print("Sha1 data unavalible!")
        checksum.update()

    # Check Sha256
    if Sha256f1.get() and Sha256f2.get():
        if Sha256f1.get() == Sha256f2.get():
            print("Sha256 match!")
            Sha256Lbl.config(bg='green')
            checksum.update()
        else:
            print("Sha256 does not match!")
            Sha256Lbl.config(bg='red')
            checksum.update()
    else:
        Sha256Lbl.config(bg='yellow')
        print("Sha256 data unavalible!")
        checksum.update()


def getFile(fName, MD5f, SHA1, Sha256f):
    checksum.filename = filedialog.askopenfilename()
    if checksum.filename == "":
        return 0
    fName.set(checksum.filename)
    MD5f.set(str(hash_bytestr_iter(file_as_blockiter(open(fName.get(), 'rb')), hashlib.md5())))
    SHA1.set(str(hash_bytestr_iter(file_as_blockiter(open(fName.get(), 'rb')), hashlib.sha1())))
    Sha256f.set(str(hash_bytestr_iter(file_as_blockiter(open(fName.get(), 'rb')), hashlib.sha256())))


# File one stuff

f1Lbl = Label(checksum, textvariable=f1, bg="grey", width=35, anchor=W, font=("Courier New", 14)).pack()
f1.set("First file or enter a HASH below.")

f1HashLbl1 = Label(checksum, text="MD5 : ", width=10, anchor=W, font=("Courier New", 12)).pack()
f1MD5 = Entry(checksum, textvariable=MD5f1, bg="gold", width=68, font=("Courier New", 8)).pack()

f1HashLbl2 = Label(checksum, text="Sha1 : ", width=10, anchor=W, font=("Courier New", 12)).pack()
f1Sha1 = Entry(checksum, textvariable=Sha1f1, bg="gold", width=68, font=("Courier New", 8)).pack()

f1HashLbl3 = Label(checksum, text="Sha256 : ", width=10, anchor=W, font=("Courier New", 12)).pack()
f1Sha256 = Entry(checksum, textvariable=Sha256f1, bg="gold", width=68, font=("Courier New", 8)).pack()

f1Btn = Button(checksum, text="File 1", command=lambda: getFile(f1, MD5f1, Sha1f1, Sha256f1))
f1Btn.pack()

# File two stuff

f2Lbl = Label(checksum, textvariable=f2, bg="grey", width=35, anchor=W, font=("Courier New", 14)).pack()
f2.set("Second file or enter a HASH below.")

f2HashLbl1 = Label(checksum, text="MD5 : ", width=10, anchor=W, font=("Courier New", 12)).pack()
f2MD5 = Entry(checksum, textvariable=MD5f2, bg="gold", width=68, font=("Courier New", 8)).pack()

f2HashLbl2 = Label(checksum, text="Sha1 : ", width=10, anchor=W, font=("Courier New", 12)).pack()
f2Sha1 = Entry(checksum, textvariable=Sha1f2, bg="gold", width=68, font=("Courier New", 8)).pack()

f2HashLbl3 = Label(checksum, text="Sha256 : ", width=10, anchor=W, font=("Courier New", 12)).pack()
f2Sha256 = Entry(checksum, textvariable=Sha256f2, bg="gold", width=68, font=("Courier New", 8)).pack()

f2Btn = Button(checksum, text="File 2", command=lambda: getFile(f2, MD5f2, Sha1f2, Sha256f2))
f2Btn.pack()

MD5Lbl = Label(checksum, text="MD5", width=10, bg="yellow", font=("Courier New", 12))
MD5Lbl.pack()

Sha1Lbl = Label(checksum, text="Sha1", width=10, bg="yellow", font=("Courier New", 12))
Sha1Lbl.pack()
Sha256Lbl = Label(checksum, text="Sha256", width=10, bg="yellow", font=("Courier New", 12))
Sha256Lbl.pack()
CmpBtn = Button(checksum, text="Compare", anchor="c", command=lambda: CmpHashes())  # MD5Lbl, Sha1Lbl, Sha256Lbl))
CmpBtn.pack()

# quit_button = Button(root,text='Exit', fg='red',)
# quit_button.pack()
# def quit_gui_button(event):
# 	checksum.quit()
#
# quit_button.pack()
# quit_button.bind('<Button-1>',quit_gui_button)
#
# root = Tk()
# checksum.geometry("400x280")
# checksum.title("Password Generator")
# checksum.attributes("-fullscreen", 1)
# checksum.resizable(width=tr, height=FALSE)

# intro text
title = StringVar()
label = Label(password_gen, textvariable=title, anchor=N, pady=10).pack()
title.set("Password strength:")


# choice part


def sel():
    selection = choice.get()


choice = IntVar()
R1 = Radiobutton(password_gen, text="BASIC", variable=choice, value=1, command=sel).pack(anchor=CENTER)
R2 = Radiobutton(password_gen, text="MEDIUM", variable=choice, value=2, command=sel).pack(anchor=CENTER)
R3 = Radiobutton(password_gen, text="EXTRA", variable=choice, value=3, command=sel).pack(anchor=CENTER)
labelchoice = Label(password_gen)
labelchoice.pack()

# pass lenght information
lenlabel = StringVar()
lenlabel.set("Password length:")
lentitle = Label(password_gen, textvariable=lenlabel).pack()

# pass lenght number
val = IntVar()
spinlenght = Spinbox(password_gen, from_=8, to_=24, textvariable=val, width=13).pack()


# passprint


def callback():
    lsum.config(text=passgen())


# clickable button
passgenButton = Button(password_gen, text="Generate Password", relief=RIDGE, bd=5, height=2, command=callback, pady=3)
passgenButton.pack()
password = str(callback)

# password result message
lsum = Label(password_gen, text="")
lsum.pack(side=BOTTOM)

# function
lownum = string.ascii_uppercase + string.ascii_lowercase + string.digits
lowupp = string.ascii_uppercase + string.ascii_lowercase
symbols = """`~!@#$%^&*()_-+={}[]\|:;"'<>,.?/"""
everything = lowupp + lownum + symbols


def passgen():
    if choice.get() == 1:
        return "".join(random.sample(lowupp, val.get()))
    elif choice.get() == 2:
        return "".join(random.sample(lownum, val.get()))
    elif choice.get() == 3:
        return "".join(random.sample(everything, val.get()))


def quit_pass_gen(event):
    root.quit()



quit_button.bind('<Button-1>', quit_pass_gen)
# root.geometry('%dx%d+%d+%d' % (750, 750, 750, 750))
root.title("Munalula Sikazwe 17221351006 Final Project 	CYBERSECURITY MINI-TOOLKIT")
# root.attributes('-fullscreen',True)
# root.minsize("800x480")

root.mainloop()
