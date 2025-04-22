# EPS to SVG Converter

This script automates the conversion of `.eps` files to `.svg` format using Ghostscript and Inkscape.  
It will scan all `.eps` files in the current folder and its subfolders, convert them to `.pdf` (using Ghostscript), then convert the `.pdf` to `.svg` (using Inkscape).  

Once a file is successfully converted, the `.pdf` file is deleted and the original `.eps` file is renamed by appending `(done)` to its name.

---

## Features
- Batch convert `.eps` files to `.svg`.
- Recursively processes subfolders.
- Deletes `.pdf` files after conversion.
- Renames `.eps` files to `filename(done).eps` after successful conversion.

---

## Prerequisites

1. **Ghostscript**  
   Download & install: [https://www.ghostscript.com/download/gsdnld.html](https://www.ghostscript.com/download/gsdnld.html)

2. **Inkscape**  
   Download & install: [https://inkscape.org/release/](https://inkscape.org/release/)

3. **Environment Variables**  
   Add Ghostscript and Inkscape `bin` paths to your system’s `PATH`.

---

## How to Use

1. Place `eps_to_svg.py` in your target folder.
2. Open Command Prompt or Terminal in that folder.
3. Run:

   ```bash
   python eps_to_svg.py
