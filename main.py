import tkinter as tk
from tkinter import PhotoImage
from PIL import Image, ImageTk
import subprocess

def run_hand_tracking():
    # Get path to the Python interpreter
    import sys
    python_path = sys.executable
    # Run the hand tracking script using the Python interpreter
    subprocess.run([python_path, "test.py"])


def open_learn_window():
    # Create a new window for learning
    learn_window = tk.Toplevel(root)
    learn_window.title("Learn")
    learn_window.geometry("400x350")
    learn_window.configure(bg="lightgray")  # Set background color

    def open_picture(letter):
        # Example image path using f-string
        image_window = tk.Toplevel(root)
        image_window.title("Image")
        #image_window.configure(bg="gray")

        img_path = f"{letter}.png"

        # Open the image using PIL
        img = Image.open(img_path)

        img = img.resize((300, 400))

        img_tk = ImageTk.PhotoImage(img)

        # Display the image in a label
        img_label = tk.Label(image_window, image=img_tk)
        img_label.image = img_tk
        img_label.pack(pady=10)

    # Create buttons labeled with the first five alphabets
    alphabet_buttons = []
    for i in range(5):
        letter = chr(65 + i)
        alphabet_buttons.append(tk.Button(learn_window, text=letter, padx=10, pady=5, bg="white", fg="black", font=("Arial", 12, "bold"), command=lambda letter=letter: open_picture(letter)))
        alphabet_buttons[i].pack(pady=5)

    # Create a back button to return to the main homepage
    back_button = tk.Button(learn_window, text="Back", command=learn_window.destroy, padx=10, pady=5, bg="gray", fg="white", font=("Arial", 12, "bold"))
    back_button.pack(pady=5)
def hand_track():
    import sys
    python_path = sys.executable
    subprocess.run([python_path, "dataCollection.py"])

def exit_program():
    root.destroy()

# Create the main application window
root = tk.Tk()
root.title("SignWise")

# Set window size to 400x400 pixels
root.geometry("400x400")

# Set background image
background_image = PhotoImage(file="ss.png")
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

# Create a frame to contain the buttons and center it
button_frame = tk.Frame(root)
button_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Create a button to run the hand tracking script
hand_tracking_button = tk.Button(
    button_frame,
    text="Run Hand Tracking",
    command=run_hand_tracking,
    bg="blue",
    fg="white",
    font=("Arial", 12, "bold"),
    padx=10,
    pady=5
)
hand_tracking_button.pack(pady=10)

# Create three more buttons
button2 = tk.Button(
    button_frame,
    text="Make Dataset",
    command=hand_track,
    bg="green",
    fg="white",
    font=("Arial", 12, "bold"),
    padx=10,
    pady=5
)
button2.pack(pady=10)

button3 = tk.Button(
    button_frame,
    text="Learn",
    command=open_learn_window,  # Call the function to open the learning window
    bg="red",
    fg="white",
    font=("Arial", 12, "bold"),
    padx=10,
    pady=5
)
button3.pack(pady=10)

button4 = tk.Button(
    button_frame,
    text="Exit",
    command=exit_program,
    bg="orange",
    fg="white",
    font=("Arial", 12, "bold"),
    padx=10,
    pady=5
)
button4.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
