import tkinter as tk
from PIL import Image, ImageTk
import subprocess

def open_next_page(event):
    try:
        # Execute the mainpage.py file
        root.destroy()  # Close the current window after opening the next page
        subprocess.run(['python', 'mainpage.py'])
        
    except FileNotFoundError:
        print("Error: mainpage.py not found!")

root = tk.Tk()
root.title("Clickable Background Image")

# Load the background image
background_image = Image.open("bg1.png")  # Replace with the actual path to your image
background_photo = ImageTk.PhotoImage(background_image)

# Set the window size and position
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width - background_image.width) // 2
y = (screen_height - background_image.height) // 2
root.geometry(f"{background_image.width}x{background_image.height}+{x}+{y}")

# Set the background image
background_label = tk.Label(root, image=background_photo)
background_label.place(relwidth=1, relheight=1)

# Bind the mouse click event to open the next page
root.bind("<Button-1>", open_next_page)

# Display the root window
root.mainloop()
