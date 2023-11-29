import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import ImageTk, Image

import numpy
#load the trained model to classify sign
from keras.models import load_model
model = load_model('traffic_classifier.h5')

#dictionary to label all traffic signs class.
classes = { 1: 'Limite di velocità (20 km/h)',
            2: 'Limite di velocità (30 km/h)',
            3: 'Limite di velocità (50 km/h)',
            4: 'Limite di velocità (60 km/h)',
            5: 'Limite di velocità (70 km/h)',
            6: 'Limite di velocità (80 km/h)',
            7: 'Fine del limite di velocità (80 km/h)',
            8: 'Limite di velocità (100 km/h)',
            9: 'Limite di velocità (120 km/h)',
           10: 'Vietato sorpassare',
           11: 'Vietato sorpassare veicoli oltre 3.5 tonnellate',
           12: 'Diritto di precedenza all’incrocio',
           13: 'Strada prioritaria',
           14: 'Cedere il passo',
           15: 'Stop',
           16: 'Vietato l’accesso ai veicoli',
           17: 'Vietato l’accesso a veicoli oltre 3.5 tonnellate',
           18: 'Divieto di accesso',
           19: 'Cautela generale',
           20: 'Curva pericolosa a sinistra',
           21: 'Curva pericolosa a destra',
           22: 'Doppia curva',
           23: 'Strada sconnessa',
           24: 'Strada scivolosa',
           25: 'Carreggiata che si restringe a destra',
           26: 'Lavori in corso',
           27: 'Semafori',
           28: 'Pedoni',
           29: 'Attraversamento bambini',
           30: 'Attraversamento ciclisti',
           31: 'Attenzione ghiaccio/neve',
           32: 'Attraversamento animali selvatici',
           33: 'Fine limite di velocità e sorpasso',
           34: 'Svolta a destra',
           35: 'Svolta a sinistra',
           36: 'Solo diritto',
           37: 'Diritto o svolta a destra',
           38: 'Diritto o svolta a sinistra',
           39: 'Tenere la destra',
           40: 'Tenere la sinistra',
           41: 'Rotatoria obbligatoria',
           42: 'Fine divieto di sorpasso',
           43: 'Fine divieto di sorpasso veicoli oltre 3.5 tonnellate' }

                 
#initialise GUI
top=tk.Tk()
top.geometry('800x600')
top.title('Traffic sign classification')
top.configure(background='#CDCDCD')

label=Label(top,background='#CDCDCD', font=('arial',15,'bold'))
sign_image = Label(top)

def classify(file_path):
    
    image = Image.open(file_path)
    image = image.resize((30,30))
    image = numpy.expand_dims(image, axis=0)
    image = numpy.array(image)
    print(image.shape)
    pred = model.predict(image)
    pred_class = numpy.argmax(pred, axis=1)
    sign = classes[pred_class[0] + 1]
    print(sign)
    label.configure(foreground='#011638', text=sign)
 
   

def show_classify_button(file_path):
    classify_b=Button(top,text="Classifica immagine",command=lambda: classify(file_path),padx=10,pady=5)
    classify_b.configure(background='#364156', foreground='white',font=('arial',10,'bold'))
    classify_b.place(relx=0.79,rely=0.46)

def upload_image():
    try:
        file_path=filedialog.askopenfilename()
        uploaded=Image.open(file_path)
        uploaded.thumbnail(((top.winfo_width()/2.25),(top.winfo_height()/2.25)))
        im=ImageTk.PhotoImage(uploaded)
        
        sign_image.configure(image=im)
        sign_image.image=im
        label.configure(text='')
        show_classify_button(file_path)
    except:
        pass

upload=Button(top,text="Carica Immagine",command=upload_image,padx=10,pady=5)
upload.configure(background='#364156', foreground='white',font=('arial',10,'bold'))

upload.pack(side=BOTTOM,pady=50)
sign_image.pack(side=BOTTOM,expand=True)
label.pack(side=BOTTOM,expand=True)
heading = Label(top, text="Scopri il significato di un cartello stradale",pady=20, font=('arial',20,'bold'))
heading.configure(background='#CDCDCD',foreground='#364156')
heading.pack()
top.mainloop()
