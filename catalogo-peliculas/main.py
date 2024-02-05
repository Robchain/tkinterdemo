import tkinter as tk
from cliente.gui_app import Frame, barra_menus

def main():
    root = tk.Tk()
    root.title("Trabajo - Lomas")
    #root.iconbitmap("")
    root.resizable(1,1)
    barra_menus(root)

    app  = Frame(root = root)
   
    app.mainloop()

if __name__  == "__main__":
    main()




