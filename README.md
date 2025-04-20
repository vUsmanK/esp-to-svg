# EPS to SVG Converter

This script automates the conversion of `.eps` files to `.svg` format using Ghostscript and Inkscape. It processes all `.eps` files in the current directory and its subfolders, converts them to `.pdf` using Ghostscript, and then converts the `.pdf` files to `.svg` using Inkscape. The intermediate `.pdf` files and original `.eps` files are deleted after successful conversion.

## Features
- Batch conversion of `.eps` files to `.svg`.
- Processes `.eps` files in the current folder and all subfolders.
- Uses Ghostscript for `.eps` to `.pdf` conversion.
- Uses Inkscape for `.pdf` to `.svg` conversion.
- Deletes intermediate `.pdf` files and original `.eps` files to save space.

## Prerequisites
1. **Install Ghostscript**:
   - Download Ghostscript from [Ghostscript Downloads](https://www.ghostscript.com/download/gsdnld.html).
   - Install it and note the installation path (e.g., `C:\Program Files\gs\gs10.05.0\bin`).

2. **Install Inkscape**:
   - Download Inkscape from [Inkscape Downloads](https://inkscape.org/release/).
   - Install it and note the installation path (e.g., `C:\Program Files\Inkscape\bin`).

3. **Add Paths to Environment Variables**:
   - Add the Ghostscript and Inkscape installation paths to your system's `PATH` environment variable:
     1. Open the Start Menu and search for "Environment Variables".
     2. Click on "Edit the system environment variables".
     3. In the System Properties window, click "Environment Variables".
     4. Under "System variables", find the `Path` variable and click "Edit".
     5. Add the paths to Ghostscript and Inkscape (e.g., `C:\Program Files\gs\gs10.05.0\bin` and `C:\Program Files\Inkscape\bin`).
     6. Click "OK" to save.

## How to Use
1. Place the script (`eps_to_svg.py`) in the folder containing your `.eps` files.
2. Open a terminal or command prompt in the same folder.
3. Run the script:
   ```bash
   python eps_to_svg.py
   ```
4. The script will process all `.eps` files in the folder and its subfolders. Once the script completes, all `.eps` files will be converted to `.svg`.

## Turning the Script into an Executable
To make the script easier to run, you can convert it into a standalone `.exe` file using `pyinstaller`:
1. Install `pyinstaller`:
   ```bash
   pip install pyinstaller
   ```
2. Create the `.exe` file:
   ```bash
   pyinstaller --onefile eps_to_svg.py
   ```
3. The `.exe` file will be located in the `dist` folder. You can run it directly without needing Python installed.

### Using the Prebuilt `.exe` File
If your file paths match the ones provided in this README (e.g., Ghostscript and Inkscape paths), you can download the prebuilt `.exe` file from the `dist` folder. Simply place the `.exe` file in the folder containing your `.eps` files and run it. The script will process all `.eps` files in the folder and its subfolders.

## Description
This script is ideal for designers, developers, and anyone working with vector graphics who needs to convert `.eps` files to `.svg` format. It simplifies the process by automating the conversion steps, cleaning up intermediate files, and processing subfolders recursively.

## SEO Keywords
- EPS to SVG converter
- Batch EPS to SVG conversion
- Convert EPS to SVG using Python
- Ghostscript EPS to PDF
- Inkscape PDF to SVG
- Automate EPS to SVG conversion
- Python script for EPS to SVG
- EPS to SVG tool
- Convert EPS files to SVG format
- EPS to SVG batch processing
- Recursive EPS to SVG conversion
- EPS to SVG subfolder processing

## Troubleshooting
- **Error: Ghostscript or Inkscape not found**:
  Ensure their paths are correctly added to the `PATH` environment variable.
- **Permission Denied**:
  Run the script or `.exe` file with administrator privileges.
- **No `.eps` files found**:
  Ensure the `.eps` files are in the same directory or subfolders as the script.

## License
This project is open-source and available under the MIT License.
