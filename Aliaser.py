import wave
import numpy as np
import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox, ttk
from scipy.interpolate import interp1d
import sys
import os

def upsample_audio(data, upsample_factor):
    """Upsample audio data by a given factor using simple repeat."""
    return np.repeat(data, upsample_factor)

def linear_interpolate(data, upsample_factor):
    """Linearly interpolate audio data by a given factor."""
    x = np.arange(len(data))
    x_new = np.linspace(0, len(data) - 1, len(data) * upsample_factor)
    return np.interp(x_new, x, data)

def cubic_interpolate(data, upsample_factor):
    """Cubically interpolate audio data by a given factor."""
    x = np.arange(len(data))
    x_new = np.linspace(0, len(data) - 1, len(data) * upsample_factor)
    cubic_interp = interp1d(x, data, kind='cubic')
    return cubic_interp(x_new)

def downsample_wav(input_file, output_file, target_rate, interp_method="none", upsample_back=True):
    """Downsample a stereo wave file to an arbitrary rate and optionally upsample it."""
    with wave.open(input_file, 'rb') as wf:
        n_channels, sampwidth, framerate, n_frames, comptype, compname = wf.getparams()
        if n_channels != 2:
            raise ValueError("The input file is not a stereo wave file.")
        frames = wf.readframes(n_frames)
        audio_data = np.frombuffer(frames, dtype=np.int16)
        left_channel = audio_data[::2]
        right_channel = audio_data[1::2]
        downsample_factor = int(framerate / target_rate)
        left_downsampled = left_channel[::downsample_factor]
        right_downsampled = right_channel[::downsample_factor]

        if upsample_back:
            # Upsample the downsampled audio
            upsample_factor = downsample_factor
            if interp_method == "linear":
                left_upsampled = linear_interpolate(left_downsampled, upsample_factor)
                right_upsampled = linear_interpolate(right_downsampled, upsample_factor)
            elif interp_method == "cubic":
                left_upsampled = cubic_interpolate(left_downsampled, upsample_factor)
                right_upsampled = cubic_interpolate(right_downsampled, upsample_factor)
            else:
                left_upsampled = upsample_audio(left_downsampled, upsample_factor)
                right_upsampled = upsample_audio(right_downsampled, upsample_factor)

            output_data = np.column_stack((left_upsampled, right_upsampled)).ravel().astype(np.int16)
            output_rate = framerate
        else:
            output_data = np.column_stack((left_downsampled, right_downsampled)).ravel().astype(np.int16)
            output_rate = target_rate

        with wave.open(output_file, 'wb') as out_wf:
            out_wf.setparams((n_channels, sampwidth, output_rate, len(output_data) // 2, comptype, compname))
            out_wf.writeframes(output_data.tobytes())

if __name__ == "__main__":
    root = tk.Tk()
    # Check if the script is running as a standalone executable
    if hasattr(sys, "frozen"):
        # If it's an executable, use the executable's directory
        BASE_DIR = os.path.dirname(sys.executable)
    else:
        # If it's a script, use the script's directory
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    ICON_PATH = os.path.join(BASE_DIR, 'icon.ico')
    root.iconbitmap(ICON_PATH)
    root.withdraw()
    input_file_path = filedialog.askopenfilename(title="Select the input WAV file", filetypes=[("WAV files", "*.wav")])
    if not input_file_path:
        print("No input file selected. Exiting.")
        sys.exit()
    output_file_path = filedialog.asksaveasfilename(title="Save the output WAV file", defaultextension=".wav", filetypes=[("WAV files", "*.wav")])
    if not output_file_path:
        print("No output file selected. Exiting.")
        sys.exit()
    desired_rate = simpledialog.askinteger("Sample Rate", "Enter the desired sample rate:", initialvalue=18947)
    if not desired_rate:
        print("No sample rate provided. Exiting.")
        sys.exit()
    upsample_back = messagebox.askyesno("Upsample Back", "Do you want to upsample the audio back to its original rate?")
    
    if upsample_back:
        root.deiconify()  # Show the root window for the dropdown
        interp_label = tk.Label(root, text="Choose interpolation method:")
        interp_label.pack(pady=20)
        
        interp_methods = ["none", "linear", "cubic"]
        combo = ttk.Combobox(root, values=interp_methods)
        combo.set("none")  # default value
        combo.pack(pady=20)
        
        def on_ok():
            global interp_method
            interp_method = combo.get()
            root.quit()
        
        ok_button = tk.Button(root, text="OK", command=on_ok)
        ok_button.pack(pady=20)
        
        root.mainloop()
        root.destroy()
    else:
        interp_method = "none"
    
    downsample_wav(input_file_path, output_file_path, desired_rate, interp_method, upsample_back)