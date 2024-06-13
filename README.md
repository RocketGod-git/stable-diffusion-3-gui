# Stable Diffusion 3 GUI

This repository contains a graphical user interface (GUI) application for generating images using the Stable Diffusion 3 model. The application is built with Python, using the `diffusers` library by Hugging Face and `tkinter` for the GUI.

## Features

- **Simple GUI**: Easy-to-use graphical interface for generating images.
- **Integrated Hugging Face Authentication**: Direct login to Hugging Face within the app for seamless use of the model.

## Prerequisites

Before you can run this application, you will need:

- Python
- GPU with CUDA installed
- An access token from Hugging Face (you will need to replace the `access_token` in the code with your own)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/RocketGod-git/stable-diffusion-3-gui.git
   ```
2. Navigate to the cloned directory and run the `sd3.bat` script to set up your environment and dependencies:
   ```bash
   cd stable-diffusion-3-gui
   sd3.bat
   ```
   This script will:
   - Check for a Python virtual environment in the current directory, creating one if it does not exist.
   - Activate the virtual environment.
   - Upgrade pip to the latest version.
   - Install and upgrade necessary Python packages including PyTorch, PIL, and Hugging Face libraries.
   - Install the `diffusers` library directly from the GitHub repository if not already installed.
   - Run the main application script.

## Usage

Upon launching, the application will prompt you to enter a text prompt and will display the generated image within the GUI.

## Contributing

Contributions are welcome! Please feel free to submit pull requests or create issues for bugs and feature requests.

## License

This project is open source and available under the [License](LICENSE).

## Disclaimer

This project is not affiliated with Stability AI or Hugging Face. It is a community-driven project.

![RocketGod](https://github.com/RocketGod-git/Flipper_Zero/assets/57732082/f5d67cfd-585d-4b23-905f-37151e3d6a7d)
