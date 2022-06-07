from tkinter import *
from tkinter import messagebox
root = Tk()
root.title('Konverter Biner')

biner =[]

def konverterBiner(angka):
    if angka > 512:
        messagebox.showinfo('Perhatian !', 'Maksimal 512 untuk decimal\nDirubah menjadi Binary Number ')
        return
    else: pass
    if angka//2 == 0:
        biner.append(angka%2)
    else:
     biner.append(angka%2)
     return konverterBiner(angka//2)

    new = [str(i) for i in biner]
    string = " "
    while len(new) > 0:
        a = new.pop()
        string += a
    masukan.delete(0, END)
    masukan.insert(END, string)
def konvert():
    if len(biner) >= 1:
        while len(biner) >= 1:
            a = biner.pop()
            sampah = []
            sampah.append(a)
            sampah.remove(a)
    else: pass
    a = var.get()
    b = int(masukan.get())
    if a == 1:
        konverterBiner(b)
    return

masukan = Entry(root, width=50)
masukan.grid(row=0, column=0)

var = IntVar()
bin = Radiobutton(root, text="Conver to Binary Number (max. 512)", variable=var, value=1)
bin.grid(row=1, column=0, sticky=W)

tombol = Button(root, text="Konvert", command=konvert, width=15, bg='black', fg='green').grid(row=4, column=0, pady=5)
root.mainloop()
