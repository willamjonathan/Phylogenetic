import tkinter as tk
from PIL import Image, ImageTk
import subprocess
# from mainpage import run_mainpage

def open_next_page(event):
    # root.destroy()
    # run_mainpage()
    try:
       
        root.destroy()  # 
        subprocess.run(['python', 'mainpage.py'])
        
    except FileNotFoundError:
        print("Error: mainpage.py not found!")

root = tk.Tk()
root.title("Clickable Background Image")


background_image = Image.open("bg/bg1.png")
background_photo = ImageTk.PhotoImage(background_image)


screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width - background_image.width) // 2
y = (screen_height - background_image.height) // 2
root.geometry(f"{background_image.width}x{background_image.height}+{x}+{y}")


background_label = tk.Label(root, image=background_photo)
background_label.place(relwidth=1, relheight=1)


root.bind("<Button-1>", open_next_page)


root.mainloop()
