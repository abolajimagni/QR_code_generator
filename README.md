# QR_code_generator
# QR Code Generator

Welcome to the QR Code Generator project! This application allows users to generate QR codes from text input using a simple graphical user interface (GUI) built with Tkinter.

## Features

- Input text to generate a QR code.
- Save generated QR codes as PNG images.
- Display the generated QR code in the application.

## Requirements

Make sure you have Python installed on your machine. This project also requires the following libraries:

- tkinter (comes pre-installed with Python)
- qrcode
- Pillow (PIL)

You can install the required libraries using pip:

pip install qrcode[pil] Pillow

# Magnitudo QR Code Generator

## Overview

Magnitudo is a simple and intuitive QR Code Generator that allows users to convert text or URLs into QR codes. This application is built using Python's Tkinter library for the GUI and is designed for ease of use.

## Features

- *User-friendly interface*: The application has a clean and straightforward layout, making it easy for anyone to generate QR codes.
- *Customizable Output*: Users can input any text or URL and save the resulting QR code as an image file.
- *Cross-Platform*: It works on any system that supports Python and Tkinter.

## Requirements

To run the Magnitudo QR Code Generator, make sure you have:

- Python 3.x installed on your system.
- Tkinter library (usually pre-installed with Python).
- A QR code generation library such as `qrcode` (install via pip if not already installed):
  
bash
  pip install qrcode[pil]
  

## Installation

1. Clone the repository or download the code files.
2. Navigate to the project directory.
3. Run the application using:
   
bash
   python main.py
   

## Usage

1. Enter the text or URL you want to convert into a QR code in the `Text/Url` field.
2. Specify the file name in the `Save as` field.
3. Click the `Generate` button.
4. The generated QR code will be saved as an image file in your specified location.

### Example Code Snippet

The main functionality of the application can be seen in the following snippet:

python
import tkinter
from tkinter import messagebox, Label, Entry, Button, Frame
import qrcode

def gen():
    data = entry_1.get()
    filename = saved_e.get() + '.png'
    if not data or not filename:
        messagebox.showerror("Error", "Please provide both text/URL and a file name.")
        return
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    img.save(filename)
    messagebox.showinfo("Success", f"QR Code saved as {filename}")

# GUI Setup
root = tkinter.Tk()
root.title("Magnitudo QR Code Generator")
frame = Frame(root, width=285, height=280, bg='#F2F7EA')
frame_2 = tkinter.Frame(root, bg='#9DD3AF', width=414,height=150)

head = Label(root, text='Magnitudo QR code Generator', font=('arialblack', 24, 'bold'), fg='#9DD3AF', bg='#605F54').pack(side='top', pady=20)
label_1 = Label(frame_2, text='Text/Url', font=('arialblack', 13, 'bold'), bg='#C5E4CA', fg='black').place(x=30, y=10)
entry_1 = Entry(frame_2, border=1, width=35, font=('arial', 12))
saved = Label(frame_2, text='Save as', fg='black', bg='#C5E4CA', font=('arialblack', 13, 'bold')).place(x=30, y=48)
saved_e = Entry(frame_2, width=30, font=('arial', 12))
generate = Button(frame_2, text='Generate', bg='#48887B', fg='white', width=35, height=2, font=('arialblack', 13, 'bold'), command=gen).place(x=20, y=95)

frame_2.place(x=0, y=150)
saved_e.place(x=100, y=48)
entry_1.place(x=100, y=10)
frame.place(x=414, y=100)
root.mainloop()

## Contributing

Feel free to raise issues or submit feature requests. Contributions in the form of pull requests are welcomed!

## License

This project is licensed under the MIT License - see the LICENSE file for details.

This README provides a comprehensive overview of the Magnitudo QR code generator, detailing its features, installation steps, usage instructions, and how to contribute. Adjust any content as necessary for your specific project style and requirements
