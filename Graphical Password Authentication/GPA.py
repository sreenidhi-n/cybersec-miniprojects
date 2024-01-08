from random import shuffle, choice
from pathlib import Path
import tkinter as tk

image_folder = Path("C:/Users/Sreenidhi/Desktop/cybersec/Graphical Password Authentication/images")
image_paths = list(image_folder.glob("*.png"))
shuffle(image_paths)

shown_images = []
image_values = {}
selected_images = []

password = [0, 1, 2] # Key is the first 3 images

def get_unique_image_path():
    if not image_paths:
        return None  
    image_path = choice(image_paths)
    image_paths.remove(image_path)
    return str(image_path)

def create_grid():
    for widget in root.winfo_children():
        widget.destroy()
    for _ in range(3):
        for _ in range(3):
            image_path = get_unique_image_path()
            if image_path:
                images = tk.PhotoImage(file=image_path)
                image_value = len(shown_images)  
                image_values[image_path] = image_value
                button = tk.Button(root, image=images, command=lambda path=image_path: button_click(path))
                button.photoimage = images
                button.grid(row=len(shown_images) // 3, column=len(shown_images) % 3)
                shown_images.append(image_path)

def button_click(image_path):
    value = image_values.get(image_path)
    selected_images.append(value)
    if len(selected_images) == len(password):
        validate_password()

def create_popup(message):
    popup = tk.Toplevel(root)
    popup.config(bg='ghost white')
    popup.geometry('50x50')
    label = tk.Label(popup, text=message)
    label.pack()
    button = tk.Button(popup, text="OK", command=popup.destroy)
    button.pack()

def validate_password():
    if selected_images == password:
        create_popup("Hello, World!")
    else:
        create_popup("Breh")
    selected_images.clear()
    root.after(10000, create_grid)

def create():
    create_grid()

root = tk.Tk()
root.config(bg='ghost white')
root.geometry('620x620')
button = tk.Button(root, text="Create Grid", command=create)
button.pack()
create_grid()  
root.mainloop()