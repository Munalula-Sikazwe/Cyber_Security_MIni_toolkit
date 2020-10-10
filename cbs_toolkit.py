from tkinter import *

root = Tk()

def button1_importer(event):

        import GUI_Hash_CHECKSUM


def button2_importer(event):
    import GUI

def button3_importer(event):
        import PassGen

def exit(event):

    root.quit()


def checksum_verifier():

    chksum_frame = Frame(root)
    chksum_frame.pack()
    # chksum_label = Label(chksum_frame,text="Checksum-Verifier")
    # chksum_label.pack()
    button1 = Button(chksum_frame, text='checksum_verifier', fg='red')
    button1.pack()
    button1.bind('<Button-1>', button1_importer)


def steganography():

    stego_frame = Frame(root).pack()
    button2 = Button(stego_frame, text='steganograpy', fg='green')
    button2.pack()
    button2.bind('<Button-1>',button2_importer)
def password_generator():
    encryption_frame = Frame(root).pack()

    button3 = Button(encryption_frame, text='password_generator', fg='yellow')
    button3.pack()
    button3.bind('<Button-1>',button3_importer )






def quit():
    bottom_frame = Frame(root).pack()
    button4 = Button(bottom_frame,text = 'Exit',fg = 'red')
    button4.pack()
    button4.bind('<Button-1>',exit)

checksum_verifier()

steganography()

password_generator()

quit()

root.title('Munalula-Sikazwe CyberSecurity Toolkit')

root.mainloop()
