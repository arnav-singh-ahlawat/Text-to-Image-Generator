import os
import sys
import tkinter as tk
from tkinter import messagebox
from torch import autocast
from diffusers import StableDiffusionPipeline

class TextToImageGenerator:
    def __init__(self, root):
        # Initialize the GUI window
        self.root = root
        self.root.title("Text to Image Generator")

        # Create GUI elements: Label for prompt, Entry for user input, Restart button, and Generate Image button
        self.prompt_label = tk.Label(self.root, text="Enter a prompt:")
        self.prompt_label.grid(row=0, column=0, padx=10, pady=5)

        self.prompt_entry = tk.Entry(self.root, width=50)
        self.prompt_entry.grid(row=0, column=1, padx=10, pady=5)

        self.restart_button = tk.Button(self.root, text="Restart", command=self.restart_program)
        self.restart_button.grid(row=1, column=0, padx=10, pady=5, sticky="ew")

        self.generate_button = tk.Button(self.root, text="Generate Image", command=self.generate_image)
        self.generate_button.grid(row=1, column=1, padx=10, pady=5, sticky="ew")

        # Configure column weights to allow resizing
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)

    def generate_image(self):
        # Get the prompt entered by the user
        prompt = self.prompt_entry.get()

        # Check if prompt is empty
        if not prompt:
            messagebox.showerror("Error", "Please enter a prompt.")
            return

        # Set up paths for model and save directory
        SDV5_MODEL_PATH = os.getenv('SDV5_MODEL_PATH')
        SAVE_PATH = os.path.join(os.environ['USERPROFILE'], 'Desktop', 'Generated Images')

        # Create the save directory if it doesn't exist
        if not os.path.exists(SAVE_PATH):
            os.mkdir(SAVE_PATH)

        # Function to ensure unique filenames
        def individualize(path):
            filename, extension = os.path.splitext(path)
            counter = 1

            while os.path.exists(path):
                path = filename + ' (' + str(counter) + ')' + extension
                counter += 1

            return path

        # Initialize and set up the image generation pipeline
        pipeline = (StableDiffusionPipeline.from_pretrained(SDV5_MODEL_PATH))
        pipeline = pipeline.to('cuda')

        # Generate image with the provided prompt
        with autocast('cuda'):
            image = pipeline(prompt).images[0]

        # Save the generated image with a unique filename
        image_path = individualize(os.path.join(SAVE_PATH, (prompt[:25] + '...') if len(prompt) > 25 else prompt) + '.png')
        image.save(image_path)

        # Show success message with the saved image path
        messagebox.showinfo("Success", f"Image generated successfully and saved at:\n{image_path}")

    def restart_program(self):
        # Restart the Python program
        python = sys.executable
        os.execl(python, python, *sys.argv)

def main():
    # Create the main GUI window
    root = tk.Tk()
    TextToImageGenerator(root)
    root.mainloop()

# Entry point of the program
if __name__ == "__main__":
    main()