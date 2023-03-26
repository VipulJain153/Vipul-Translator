from tkinter import *
from tkinter import ttk
import googletrans,gtts,playsound,os,shutil

os.mkdir("audio")
count =0

lst = list(googletrans.LANGUAGES.values())

LANGUAGES = {k:v for k,v in zip(tuple(googletrans.LANGUAGES.values()),tuple(googletrans.LANGUAGES.keys()))}

setter = False
myVal=None

translator = googletrans.Translator()
filePath = f"{os.getcwd()}/audio.mp3"

def check_input(event):
    global setter,myVal
    value = event.widget.get()

    if value == '':
        combo_box['values'] = lst
    else:
        data = []
        for item in lst:
            if value.lower() in item.lower():
                data.append(item)

        combo_box['values'] = data    
    for i in combo_box['values']:
        value = event.widget.get()
        if value == i:
            myVal = value
            setter=True

def translate():
    global setter,myVal
    if setter and myVal!=None:
        key = LANGUAGES.get(myVal)
        trans = translator.translate(textbox.get(1.0,END),dest=key)
        label.config(text=trans.text)
        return trans.text,key

def speak():
    global count
    if setter and myVal!=None:
        mytext,key = translate()
        mytextCon = gtts.gTTS(mytext,lang=key)
        mytextCon.save(f"audio/{count}.mp3")
        playsound.playsound(f"audio/{count}.mp3")
        count += 1
    

root = Tk()
root.geometry("1280x720")
root.minsize(1280,720)
root.maxsize(1919,1080)
root.title("Vipul Translator")
icon = PhotoImage(file="icon.png")
root.iconphoto(True, icon)
root.config(background="black")

# creating Combobox

combo_box = ttk.Combobox(root,background="#25CCF7",foreground="#EAB543")
combo_box['values'] = lst
combo_box.bind('<KeyRelease>', check_input)
combo_box.pack(fill=X)
textbox = Text(root,background="#3B3B98",foreground="white",font=("Monospace", 20),height=15)
textbox.pack(fill=X)
button = Button(root,background="#58B19F",foreground="#2C3A47",font=("Monospace", 15),text="Translate",command=translate,cursor="circle")
button.pack(anchor="nw",fill=X)
buttonAI = Button(root,background="#58B19F",foreground="#2C3A47",font=("Monospace", 15),text="Speak",command=speak,cursor="heart")
buttonAI.pack(anchor="ne",fill=X)
label = Label(root,background="#FD7272",foreground="white",font=("Monospace", 20, "bold", "italic"))
label.pack(fill=BOTH,side=BOTTOM)

root.mainloop()
shutil.rmtree("audio")