import os
from tkinter import *
from tkinter import filedialog, messagebox
from tkinter import ttk
from PIL import Image
import threading

translations = {
    "tr": {
        "input_folder": "Giriş Klasörü:",
        "select": "Seç",
        "new_width": "Yeni Genişlik:",
        "new_height": "Yeni Yükseklik:",
        "image_format": "Resim Formatı:",
        "all_formats": "tüm formatlar",
        "jpeg": "jpeg",
        "png": "png",
        "jpg": "jpg",
        "gif": "gif",
        "bmp": "bmp",
        "tiff": "tiff",
        "start": "Resimleri Boyutlandır",
        "completed": "Resimler başarıyla yeniden boyutlandırıldı ve {output_folder} klasörüne kaydedildi!",
        "no_images": "Seçilen klasörde uygun resim dosyası bulunamadı!",
        "invalid_format": "Geçersiz format seçimi!",
        "invalid_dimensions": "Genişlik ve yükseklik pozitif tam sayılar olmalıdır!",
        "warning": "Uyarı",
        "info": "Tamamlandı",
    },
    "en": {
        "input_folder": "Input Folder:",
        "select": "Select",
        "new_width": "New Width:",
        "new_height": "New Height:",
        "image_format": "Image Format:",
        "all_formats": "all formats",
        "jpeg": "jpeg",
        "png": "png",
        "jpg": "jpg",
        "gif": "gif",
        "bmp": "bmp",
        "tiff": "tiff",
        "start": "Resize Images",
        "completed": "Images have been successfully resized and saved to {output_folder}!",
        "no_images": "No suitable image files found in the selected folder!",
        "invalid_format": "Invalid format selection!",
        "invalid_dimensions": "Width and height must be positive integers!",
        "warning": "Warning",
        "info": "Completed",
    },
}

selected_language = "tr"

def select_language(lang):
    global selected_language
    selected_language = lang
    update_labels()

def update_labels():
    input_folder_label.config(text=translations[selected_language]["input_folder"])
    input_folder_button.config(text=translations[selected_language]["select"])
    width_label.config(text=translations[selected_language]["new_width"])
    height_label.config(text=translations[selected_language]["new_height"])
    format_label.config(text=translations[selected_language]["image_format"])
    start_button.config(text=translations[selected_language]["start"])

    format_var.set(translations[selected_language]["all_formats"])
    format_dropdown['menu'].delete(0, 'end')
    
    for format_name in ["all_formats", "jpeg", "png", "jpg", "gif", "bmp", "tiff"]:
        format_dropdown['menu'].add_command(label=translations[selected_language][format_name], command=lambda value=format_name: format_var.set(value))

def select_input_folder():
    folder_selected = filedialog.askdirectory()
    input_folder_entry.delete(0, END)
    input_folder_entry.insert(0, folder_selected)

def resize_images():
    input_folder = input_folder_entry.get()
    output_folder = os.path.join(os.getcwd(), "output_images")
    new_width = width_entry.get()
    new_height = height_entry.get()

    if not (new_width.isdigit() and new_height.isdigit()):
        messagebox.showwarning(translations[selected_language]["warning"], translations[selected_language]["invalid_dimensions"])
        return
    
    new_width = int(new_width)
    new_height = int(new_height)
    new_size = (new_width, new_height)

    selected_format = format_var.get().lower()
    if selected_format == translations[selected_language]["all_formats"]:
        image_extensions = [".jpeg", ".png", ".jpg", ".gif", ".bmp", ".tiff"]
    elif selected_format == translations[selected_language]["jpeg"]:
        image_extensions = [".jpeg"]
    elif selected_format == translations[selected_language]["png"]:
        image_extensions = [".png"]
    elif selected_format == translations[selected_language]["jpg"]:
        image_extensions = [".jpg"]
    elif selected_format == translations[selected_language]["gif"]:
        image_extensions = [".gif"]
    elif selected_format == translations[selected_language]["bmp"]:
        image_extensions = [".bmp"]
    elif selected_format == translations[selected_language]["tiff"]:
        image_extensions = [".tiff"]
    else:
        messagebox.showwarning(translations[selected_language]["warning"], translations[selected_language]["invalid_format"])
        return

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    image_files = [f for f in os.listdir(input_folder) if any(f.endswith(ext) for ext in image_extensions)]
    total_images = len(image_files)

    if total_images == 0:
        messagebox.showwarning(translations[selected_language]["warning"], translations[selected_language]["no_images"])
        return

    progress_bar['maximum'] = total_images
    progress_bar['value'] = 0

    for i, filename in enumerate(image_files):
        img_path = os.path.join(input_folder, filename)
        img = Image.open(img_path)

        resized_img = img.resize(new_size)
        output_path = os.path.join(output_folder, filename)
        resized_img.save(output_path)

        progress_bar['value'] = i + 1
        root.update_idletasks()

    messagebox.showinfo(translations[selected_language]["info"], translations[selected_language]["completed"].format(output_folder=output_folder))

def start_resizing():
    threading.Thread(target=resize_images).start()

root = Tk()
root.title("Resim Boyutlandırıcı")

language_frame = Frame(root)
language_frame.grid(row=0, column=0, columnspan=3, padx=10, pady=5)

language_label = Label(language_frame, text="Dil Seçimi:")
language_label.pack(side=LEFT)

language_var = StringVar(value="tr")
language_tr = Radiobutton(language_frame, text="Türkçe", variable=language_var, value="tr", command=lambda: select_language("tr"))
language_en = Radiobutton(language_frame, text="English", variable=language_var, value="en", command=lambda: select_language("en"))
language_tr.pack(side=LEFT)
language_en.pack(side=LEFT)

input_folder_label = Label(root, text="")
input_folder_label.grid(row=1, column=0, padx=10, pady=5)
input_folder_entry = Entry(root, width=40)
input_folder_entry.grid(row=1, column=1, padx=10, pady=5)
input_folder_button = Button(root, text="", command=select_input_folder)
input_folder_button.grid(row=1, column=2, padx=10, pady=5)

width_label = Label(root, text="")
width_label.grid(row=2, column=0, padx=10, pady=5)
width_entry = Entry(root, width=10)
width_entry.grid(row=2, column=1, padx=10, pady=5, sticky="w")
width_entry.insert(0, "416")

height_label = Label(root, text="")
height_label.grid(row=3, column=0, padx=10, pady=5)
height_entry = Entry(root, width=10)
height_entry.grid(row=3, column=1, padx=10, pady=5, sticky="w")
height_entry.insert(0, "416")

format_label = Label(root, text="")
format_label.grid(row=4, column=0, padx=10, pady=5)
format_var = StringVar(value="tüm formatlar")
format_dropdown = OptionMenu(root, format_var, "tüm formatlar", "jpeg", "png", "jpg", "gif", "bmp", "tiff")
format_dropdown.grid(row=4, column=1, padx=10, pady=5, sticky="w")

progress_bar = ttk.Progressbar(root, orient=HORIZONTAL, length=300, mode='determinate')
progress_bar.grid(row=5, column=0, columnspan=3, padx=10, pady=10)

start_button = Button(root, text="", command=start_resizing)
start_button.grid(row=6, column=0, columnspan=3, padx=10, pady=10)

update_labels()
root.mainloop()
