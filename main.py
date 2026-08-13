import tkinter as tk
from gui import show_welcome_screen
window = tk.Tk()
window.title("Smart Career Roadmap")
window.geometry("600x700")
window.configure(bg="#F5F7FB")
show_welcome_screen(window)

window.mainloop()