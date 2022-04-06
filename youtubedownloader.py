import tkinter as tk
from tkinter import *
from pytube import YouTube
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

root = tk.Tk()
urls = tk.StringVar()
downlod_path = tk.StringVar()
downlaod_text = StringVar()
#tilte and logo of the app
root.title('Youtube Video Downloader By Saurav')
youtube_logo = tk.PhotoImage(file="img/youtube.png")
root.iconphoto(False,youtube_logo)

#main canvas of the app
canvas = tk.Canvas(root, width=300,height=525)
canvas.grid(columnspan=4)

# background of the app
logo = Image.open('img/logo3.png')
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=1,row=0)

#labels
l3 = Label(root,text='Downloading...',font=('raleway', 10))
l4 = Label(root,text='Video is Downloaded',font=('raleway', 10))
l5 = tk.Label(root, text="SOMETHING WORNG, TRY AGAIN", font=("raleway", 5))

def createwidgets():
    #link entry
    link_entry = tk.Entry(root, textvariable=urls, width=40,)
    link_entry.place(relx=0.65, rely=0.6, anchor="center")
    #label text
    l1 = tk.Label(root,text="Enter Youtube Link :",bg="#FFFFFF",font=("raleway",15))
    l1.place(relx=0.2, rely=0.6, anchor="center")

    #instruction of the app
    instruction = tk.Label(root, text="paste the link of the youtube video here",font='raleway')
    instruction.grid(columnspan=3,column=0,row=1)

    #folder label
    folders_label = tk.Label(root,text='Browse folders:',bg="#FFFFFF",font=("raleway", 15))
    folders_label.place(relx=0.16, rely=0.7, anchor="center")

    folder_link = Entry(root,textvariable=downlod_path,width=30)
    folder_link.place(relx=0.52, rely=0.7, anchor="center")

    #browse button
    browse_text = tk.StringVar()
    browse_button = tk.Button(root,textvariable=browse_text,bg='#BBE3FA',command=browse,width=9,height=1,font='raleway')
    browse_text.set('Browse')
    browse_button.place(relx=0.85,rely=0.72,anchor="center")

    #download button
    download_btn = tk.Button(root, textvariable=downlaod_text,bg="#BBE3FA",command=downlaod,width=10,height=1,font="raleway")
    downlaod_text.set('Download')
    download_btn.place(relx=0.5,rely=0.78,anchor="center")

#browse function
def browse():
    downlod_dir = filedialog.askdirectory(initialdir='your directory path')
    downlod_path.set(downlod_dir)

# download function
def downlaod():
    try:
        url = urls.get()
        folder = downlod_path.get()
        get_video=YouTube(url)
        get_stream=get_video.streams.filter(progressive=True, file_extension="mp4")
        new_stream=get_stream.get_highest_resolution()
        new_stream.download(folder)
        while l4:
            messagebox.showinfo('',"Download Complete!")
            break  
    except:
         messagebox.showerror("Error","Something Went Wrong")

createwidgets()
root.mainloop()