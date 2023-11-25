import tkinter as tk
from packs.gui_interface import Frame

def main():
    root = tk.Tk()
    root.title("Vuelos")
    root.iconbitmap("")
    root.resizable(0,0)
    main = Frame(root = root)
    root.iconphoto(True, tk.PhotoImage(file='.\img\de-viaje.png'))
    root.mainloop()

if __name__ == "__main__":
    main()
