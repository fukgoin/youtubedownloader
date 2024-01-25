from pytube import YouTube
import tkinter as tk
from tkinter import ttk, filedialog
import webbrowser

def openLink():
    webbrowser.open("https://feds.lol/cld40")

def download_video():
    url = urlField.get()
    download_path = filedialog.askdirectory()

    if not url or not download_path:
        status_label.config(text="Please provide a valid URL and download path.")
        return

    try:
        youtube = YouTube(url)
        video = youtube.streams.get_highest_resolution()
        video.download(download_path)
        status_label.config(text="Download complete!")
    except Exception as e:
        status_label.config(text=f"Error: {str(e)}")

# Starting GUI building
main = tk.Tk()
main.title("Cold's Social Media Downloader")

# Set the icon
main.iconbitmap('download.ico')
main.geometry("320x300")

# Create a frame for the main content
main_frame = ttk.Frame(main)
main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

# URL text field
label = ttk.Label(main_frame, text='Enter YouTube URL', font=("Oxygen", 15))
label.grid(row=0, column=0, columnspan=2, pady=10)

urlField = ttk.Entry(main_frame, font=("Oxygen", 18), justify=tk.CENTER)
urlField.grid(row=1, column=0, columnspan=2, pady=5)

# Download button
ttk.Button(main_frame, text="Download Video", style="TButton", command=download_video).grid(row=2, column=0, columnspan=2, pady=15)

# My Socials button
socials_button = ttk.Button(main_frame, text="My Socials", style="TButton", command=openLink)
socials_button.grid(row=3, column=1, pady=15, padx=(0, 10), sticky=tk.E+tk.S)  # Bottom right corner, slightly bigger

status_label = ttk.Label(main_frame, text="")
status_label.grid(row=4, column=0, columnspan=2, pady=10)

main.mainloop()