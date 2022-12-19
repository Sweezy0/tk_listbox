from tkinter import*
from tkinter import messagebox
pencere=Tk()
pencere.title("www.ornek.com")
pencere.geometry("500x500")
#grid form çizdirme
uygulama=Frame(pencere)
uygulama.grid()
Label=Listbox(uygulama)
Label.insert(1,"AUDİ")
Label.insert(2,"BMW")
Label.insert(3,"MERCEDES")
Label.insert(4,"PORSCHE")
Label.grid(padx=120,pady=20)
#formu çiz
pencere.mainloop()