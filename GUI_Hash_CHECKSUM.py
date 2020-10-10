from tkinter import *
from tkinter import filedialog
import hashlib
import sys


root = Tk()

f1 = StringVar()
f2 = StringVar()
Sha256f1 = StringVar()
Sha256f2 = StringVar()
MD5f1 = StringVar()
MD5f2 = StringVar()
Sha1f1 = StringVar()
Sha1f2 = StringVar()


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

	#Check MD5
	if MD5f1.get() and MD5f2.get():
		if MD5f1.get() == MD5f2.get():
			print("MD5 match!")
			MD5Lbl.config(bg='green')
			root.update()
		else:
			print("MD5 does not match!")
			MD5Lbl.config(bg='red')
			root.update()
	else:
		MD5Lbl.config(bg='yellow')
		print("MD5 data unavalible!")
		root.update()

	#Check Sha1
	if Sha1f1.get() and Sha1f2.get():
		if Sha1f1.get() == Sha1f2.get():
			print("Sha1 match!")
			Sha1Lbl.config(bg='green')
			root.update()
		else:
			print("Sha1 does not match!")
			Sha1Lbl.config(bg='red')
			root.update()
	else:
		Sha1Lbl.config(bg='yellow')
		print("Sha1 data unavalible!")
		root.update()

	#Check Sha256
	if Sha256f1.get() and Sha256f2.get():
		if Sha256f1.get() == Sha256f2.get():
			print("Sha256 match!")
			Sha256Lbl.config(bg='green')
			root.update()
		else:
			print("Sha256 does not match!")
			Sha256Lbl.config(bg='red')
			root.update()
	else:
		Sha256Lbl.config(bg='yellow')
		print("Sha256 data unavalible!")
		root.update()				

def getFile(fName, MD5f, SHA1, Sha256f):
	
	root.filename = filedialog.askopenfilename( )
	if root.filename == "":
		return 0
	fName.set(root.filename)
	MD5f.set(str(hash_bytestr_iter(file_as_blockiter(open(fName.get(), 'rb')), hashlib.md5())))
	SHA1.set(str(hash_bytestr_iter(file_as_blockiter(open(fName.get(), 'rb')), hashlib.sha1())))
	Sha256f.set(str(hash_bytestr_iter(file_as_blockiter(open(fName.get(), 'rb')), hashlib.sha256())))


root.geometry('%dx%d+%d+%d' % (650, 400, 125, 125))
root.title("Munalula Sikazwe 17221351006 Final Project 	CHECKSUM VERIFIER")

#File one stuff

f1Lbl = Label(root, textvariable=f1, bg="grey", width=35, anchor=W, font=("Courier New", 14)).place(x=20, y=20)
f1.set("First file or enter a HASH below.")

f1HashLbl1 = Label(root, text="MD5 : ", width=10, anchor=W, font=("Courier New", 12)).place(x=20, y=50)
f1MD5 = Entry(root, textvariable=MD5f1, bg="gold", width=68, font=("Courier New", 8)).place(x=110, y=55)

f1HashLbl2 = Label(root, text="Sha1 : ", width=10, anchor=W, font=("Courier New", 12)).place(x=20, y=80)
f1Sha1 = Entry(root, textvariable=Sha1f1, bg="gold", width=68, font=("Courier New", 8)).place(x=110, y=85)

f1HashLbl3 = Label(root, text="Sha256 : ", width=10, anchor=W, font=("Courier New", 12)).place(x=20, y=110)
f1Sha256 = Entry(root, textvariable=Sha256f1, bg="gold", width=68, font=("Courier New", 8)).place(x=110, y=115)

f1Btn = Button(root, text="File 1", command=lambda: getFile(f1, MD5f1, Sha1f1, Sha256f1))
f1Btn.place(x=450, y=34, anchor="c")

#File two stuff

f2Lbl = Label(root, textvariable=f2, bg="grey", width=35, anchor=W, font=("Courier New", 14)).place(x=20, y=190)
f2.set("Second file or enter a HASH below.")

f2HashLbl1 = Label(root, text="MD5 : ", width=10, anchor=W, font=("Courier New", 12)).place(x=20, y=220)
f2MD5 = Entry(root, textvariable=MD5f2, bg="gold", width=68, font=("Courier New", 8)).place(x=110, y=225)

f2HashLbl2 = Label(root, text="Sha1 : ", width=10, anchor=W, font=("Courier New", 12)).place(x=20, y=250)
f2Sha1 = Entry(root, textvariable=Sha1f2, bg="gold", width=68, font=("Courier New", 8)).place(x=110, y=255)

f2HashLbl3 = Label(root, text="Sha256 : ", width=10, anchor=W, font=("Courier New", 12)).place(x=20, y=280)
f2Sha256 = Entry(root, textvariable=Sha256f2, bg="gold", width=68, font=("Courier New", 8)).place(x=110, y=285)

f2Btn = Button(root, text="File 2", command=lambda: getFile(f2, MD5f2, Sha1f2, Sha256f2))
f2Btn.place(x=450, y=204, anchor="c")


MD5Lbl = Label(root, text="MD5", width=10, bg="yellow", font=("Courier New", 12))
MD5Lbl.place(x=100, y=350)

Sha1Lbl = Label(root, text="Sha1", width=10, bg="yellow", font=("Courier New", 12))
Sha1Lbl.place(x=200, y=350)
Sha256Lbl = Label(root, text="Sha256", width=10, bg="yellow", font=("Courier New", 12))
Sha256Lbl.place(x=300, y=350)
CmpBtn = Button(root, text="Compare", anchor="c", command=lambda: CmpHashes())#MD5Lbl, Sha1Lbl, Sha256Lbl))
CmpBtn.place(x=460, y=354)

quit_button = Button(root,text='Exit', fg='red',)
quit_button.pack()
def quit_gui_button(event):
	root.quit()

quit_button.pack()
quit_button.bind('<Button-1>',quit_gui_button)
root.mainloop()

