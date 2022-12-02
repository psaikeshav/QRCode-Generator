import qrcode
from tkinter import *

# Tkinter Window Dimensions

cp = Tk()
cp.title('QR CODE GENERATOR (By Sai Keshav)')
cp.geometry('500x250')
cp.config(bg='#fef4f7')

# Function To Generate QR Code

def generate():
    img = qrcode.make(msg.get())
    type(img)
    img.save(f'{save_name.get()}.png')
    Label(cp, text='Image Saved Successfully !', bg='#fef4f7' , fg='black', font=('Times New Roman', 8)).pack()

# Function To Display QR Code
    
def show():
    img = qrcode.make(msg.get())
    type(img)
    img.show()

frame = Frame(cp, bg='#fef4f7')
frame.pack(expand=True)

# ENTER THE TEXT OR URL Text

Label(frame, text='Enter Your TEXT or URL : ', font=('Times New Roman', 16),
      bg='#fef4f7').grid(row=0, column=0, sticky='w')

msg = Entry(frame)

msg.grid(row=0, column=1)

# ENTER THE FILE NAME Text

Label(frame, text='Save QR Code as (File Name) : ', font=('Times New Roman', 16),
      bg='#fef4f7').grid(row=1, column=0, sticky='w')

save_name = Entry(frame)
save_name.grid(row=1, column=1)

# BUTTONS TO SHOW OR DISPLAY QRCODE

btn = Button(cp, text='Display QR code', bd='7', command=show, width=15)
btn.pack()
btn = Button(cp, text='Save QR code', command=generate, bd='7', width=15)
btn.pack()

cp.mainloop()