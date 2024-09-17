import tkinter as tk
from tkinter import messagebox
import random
L = []

def findnum():
    # Calculate the result using the random number
    global randomnum
    result = randomnum / 2
    f = f"The final value after subtracted is {result}"
    messagebox.showinfo("Result", f)

# Create the main window
root = tk.Tk()
root.title("Guessing Game")
root.state('zoomed')
L = [i for i in range(2, 1001, 2)]
randomindex = random.randint(0, len(L) - 1)
randomnum = L[randomindex]

# Generate the random number
randomnum = random.randint(2, 1000)

# Create the welcome message
welcome_label = tk.Label(root, text="Welcome to the Guessing Game\nThink of any integer of your wish.")
welcome_label.pack(pady=10)

# Create the instructions with the random number included
instructions_text = f"1. Multiply your number by 2.\n2. Add the random number {randomnum}\n3. Divide the result by 2.\n4. Subtract the original number."
instructions_label = tk.Label(root, text=instructions_text)
instructions_label.pack(pady=5)

# Create the button to calculate the result
calculate_button = tk.Button(root, text="Calculate Result", command=findnum)
calculate_button.pack(pady=10)

# Start the main loop
root.mainloop()
