import tkinter as tk
from tkinter import * 

import PyPDF2 

import pyttsx3

import docx

from tkinter import filedialog

# Creating Main GUI

root = Tk()
root.geometry('500x400')
root.title('Text to speech')



Label(root, text="Text to speech",font="Arial 20",  bg='Red').pack()

m=tk.IntVar()
f=tk.IntVar()


# Browse function

def browse():
    global text_content
    text_content= ""
    file = filedialog.askopenfilename(title="Select a file",filetypes=[("PDF Files","*.pdf"),("Word File","*.docx"),("All Files","*.")])


    if file.endswith('.pdf'):
        try:
            pdf_reader = PyPDF2.PdfReader(open(file,'rb'))
            for page in pdf_reader.pages:
                text_content +=page.extract_text()  

        except Exception as e:
            print(f"Error while reading PDF {e}")

    
    elif file.endswith('.docs'):
        try:
            doc = docx.Document(file)
            for para in doc.paragraphs:
                text_content += para.text
            
        except Exception as e:
            print(f"Error while reading word file {e}")
        

    pathlabel.config(text=file)


def save():
    global speacker
    if not text_content:
        Label (root,text="No text content found. Pleasse select a vild file ").pack()
        return
    


# Initializing the text to speach engine 

    speacker = pyttsx3.init()
    voices = speacker.getProperty('voices')


    if m.get() == 0:
        speacker.setProperty('voice',voices[0].id) #Male voice

    elif f.get() ==1:
        speacker.setProperty('voice',voices[1].id) #Female voice

    #Converting text into speach and saving audio file 

    speacker.say(text_content)
    speacker.runAndWait()
    speacker.save_to_file(text_content,'audio.mp3')
    speacker.runAndWait()

    Label(root,text="Your audio file is saved").pack()


    #Creating GUI

pathlabel=Label(root)
pathlabel.pack()

Button(root,text="Browse your file",command=browse).pack()
Button(root,text="Create and save audio file ",command=save).pack()

Checkbutton(root, text="Male voice ",onvalue=0,offvalue=10,variable=m).pack()
Checkbutton(root,text="Female voice ",onvalue=1,offvalue=10,variable=f).pack()

root.mainloop()






