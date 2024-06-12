# Text-to-Image Generation with Stable Diffusion

## Overview:

This project implements a state-of-the-art text-to-image generation system using Stable Diffusion, a powerful generative model framework. The system takes natural language descriptions as input and generates corresponding high-quality images. This repository contains the codebase and resources necessary to replicate and extend the functionality of the system.

## Features:

**Text-to-Image Generation:** Convert textual descriptions into realistic images.

**User-friendly interface:** A minimalistic Python Tkinter window containing a text field to enter your image prompt.

**Stable Diffusion Model:** Utilizes the Stable Diffusion framework for image generation, ensuring stability and high-quality results.

## Potential Applications:

Generate creative visuals for concept art, illustrations, or design projects.

Create mockups or prototypes based on textual descriptions.

Explore artistic ideas and concepts through text-driven image generation.

## Getting Started:

**Prerequisites:** Ensure you have Python (version 3.9 recommended) and the required libraries installed (torch, transformers and diffusers) You can install them using the following commands:

"pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu117"

"pip install --upgrade diffusers[torch]"

"pip install transformers"

**Model Installation:** To install the Stable Diffusion model, open Command Prompt in the location in which the model is to be installed and run the following commands:

"git lfs install"

"git clone https://huggingface.co/runwayml/stable-diffusion-v1-5"

**Set the Model Path:** Open Command Prompt in your project folder and type "setx SDV5_MODEL_PATH _**Model Location**_".

For eg: -
PS C:\Users\WindowsUser\PycharmProjects\txt2ImgGen> setx SDV5_MODEL_PATH C:\Users\WindowsUser\stable-diffusion-v1-5

## Usage:

Simply run python *app.py* file and begin generating images using the prompt in the text field.

## Future Enhancements:

Integration with additional features (e.g., style selection, image editing tools).

Experimentation with different text-to-image prompts and generation parameters.

Exploration of advanced functionalities like image inpainting or style transfer (if applicable).
