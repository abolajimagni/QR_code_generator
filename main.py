
import tkinter 
from tkinter import *
import qrcode 
from PIL import Image, ImageTk
from tkinter import messagebox


root= Tk()
root.geometry('700x400')
root.title('Qrcode Generator')
root.config(bg='#9DD3AF')
root.resizable(False,False)

def gen():
    qr= qrcode.QRCode(version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_H,
                box_size=10, border=4)
    qr.add_data(entry_1.get())
    qr.make(fit=True)
    img=qr.make_image(fill_color='black',back_color='white')
    file_n=saved_e.get()
    scan=img.save(f'{file_n}.png')
    my_img=ImageTk.PhotoImage(Image.open(f'{file_n}.png'))
    my_label= Label(frame,image=my_img)
    my_label.pack()


    messagebox.showinfo("Magnitudo Qr code Generator","QR Code saved successfully!")
      
    
 
frame=Frame(root, width=285, height=280,bg='#F2F7EA')
frame_2=tkinter.Frame(root,bg='#9DD3AF',width=414,height=150)
head= Label(root,text='Magnitudo QR code Generator', font=('arualblack',24,'bold'),fg='#9DD3AF', bg='#605F54').pack(side='top',pady=20)
label_1=Label (frame_2, text='Text/Url' ,font=('arialblack',13,'bold'),bg='#C5E4CA',fg='black').place(x=30, y=10)
entry_1=Entry(frame_2, border=1, width=35,)
entry_1=Entry(frame_2, border=1, width=35,font=('arial',12))

saved= Label(frame_2,text='Save as',fg='black',bg='#C5E4CA', font=('arialblack',13,'bold')).place(x=30, y=48)
saved_e= Entry(frame_2,width=30,font=('arial',12))

generate=Button(frame_2,text='Generate', bg='#48887B',fg='white',width=35,height=2,font=('arialblack',13,'bold') ,command= gen).place(x=20, y=95)


frame_2.place(x=0,y=150)
saved_e.place(x=100,y=48)
entry_1.place(x=100,y=10)
frame.place(x=414,y=100)
root.mainloop()