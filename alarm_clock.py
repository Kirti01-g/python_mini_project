import customtkinter as ctk
import time
from tkinter import messagebox
from playsound import playsound # You will need to pip install playsound

# Set the default appearance mode and color theme
ctk.set_appearance_mode("Dark") # Modes: "Dark", "Light", "System"
ctk.set_default_color_theme("blue") # Themes: "blue", "green", "dark-blue"

# --- Alarm Logic Function ---
def check_alarm():
    """Checks the current time against the alarm time input and shows a confirmation."""
    alarm_time_str = entry.get()
    
    if not alarm_time_str:
        messagebox.showwarning("Warning", "Please enter a time.")
        return

    # In the final version, the time check happens continuously in the background loop
    # For now, this confirms the UI is working
    messagebox.showinfo("Alarm Status", f"Alarm set for: {alarm_time_str}")

# --- Time Update Function ---
def update_time():
    """Updates the digital clock label every second."""
    current_time = time.strftime('%H:%M:%S %p')
    clock_label.configure(text=current_time)
    # Check if alarm matches current time here in a future update
    
    root.after(1000, update_time)

## Setup the main window (using ctk components now)
root = ctk.CTk()
root.title("Modern Python Alarm Clock")
root.geometry("400x240")

# --- 1. Time Display ---
# Use CTkLabel for better styling
clock_label = ctk.CTkLabel(root, font=('Helvetica', 40, 'bold'), text="Loading Time...")
clock_label.pack(pady=(20, 10)) # Top padding first, then bottom

# --- 2. Alarm Input & Button ---
instruction_label = ctk.CTkLabel(root, text="Enter alarm time (HH:MM:SS 24h format):")
instruction_label.pack(pady=5)

entry = ctk.CTkEntry(root, font=('Helvetica', 15), width=200)
entry.pack(pady=5)

# Use CTkButton for modern, rounded look
set_button = ctk.CTkButton(root, text="Set Alarm", command=check_alarm)
set_button.pack(pady=20)

# Start the continuous time update loop
update_time()

# Keep the window open
root.mainloop()