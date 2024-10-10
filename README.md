# Image Resizer Application

This application allows you to resize image files in a selected folder to new dimensions. It supports various formats and offers both Turkish and English language options.

## Requirements

1. **Python 3.x**
2. **Pillow** (for image processing)
3. **tkinter** (for GUI creation; usually comes with Python)

### Installing Dependencies

You can install the necessary dependencies by using the `requirements.txt` file located in the project’s root directory:

```bash
pip install -r requirements.txt
```

Note: `tkinter` typically comes pre-installed with most Python distributions. However, manual installation may be required on some systems. See below for details.

## tkinter Installation

- **Windows**: `tkinter` is usually installed automatically with Python. If not, reinstall Python and ensure that "Tcl/Tk and IDLE" is selected during installation.
- **Linux (Ubuntu/Debian)**:
  ```bash
  sudo apt-get update
  sudo apt-get install python3-tk
  ```
- **macOS**: `tkinter` typically comes with the macOS version of Python. If necessary, you can reinstall it using Homebrew:
  ```bash
  brew install python-tk
  ```

## Running the Application

Navigate to the project directory and follow these steps to run the application:

1. **Running via a Batch File**:

   Create a `run_script.bat` file (or use the provided batch file). This will install the necessary dependencies and start the application. Here is an example of the file content:

   ```bat
   @echo off

   python script.py

   pause
   ```

   Replace `script.py` with the name of your Python file. You can run this batch file by double-clicking it.

2. **Running Directly with Python**:

   Open a terminal or command prompt and run the following command:

   ```bash
   python script.py
   ```

## Usage

1. **Select Input Folder**: Choose the folder containing the images you want to process.
2. **Enter New Width and Height**: Provide the new width and height values for resizing the images.
3. **Select Image Format**: Choose from all formats or a specific format. Supported formats include:
   - JPEG
   - PNG
   - JPG
   - GIF
   - BMP
   - TIFF
4. **Resize Images**: Click the "Resize Images" button to start the process.
5. When the process completes, resized images will be saved in a folder named `output_images`.

## Supported Languages

- **Turkish**
- **English**

You can select the language at the start. Use the language options to switch between languages.