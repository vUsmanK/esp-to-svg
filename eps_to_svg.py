import os
import subprocess
import tkinter as tk
from tkinter import messagebox

def convert_eps_to_pdf(eps_path, pdf_path):
    gs_path = r"C:\Program Files\gs\gs10.05.0\bin\gswin64c.exe"
    cmd = [
        gs_path,
        "-sDEVICE=pdfwrite",
        "-dNOPAUSE",
        "-dBATCH",
        f"-sOutputFile={pdf_path}",
        eps_path
    ]
    try:
        subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(f"Converted: {eps_path} ➡️ {pdf_path}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error converting {eps_path}: {e}")
        return False

def convert_pdf_to_svg(pdf_path, svg_path):
    inkscape_path = r"C:\Program Files\Inkscape\bin\inkscape.com"
    cmd = [
        inkscape_path,
        pdf_path,
        "--export-type=svg",
        f"--export-filename={svg_path}"
    ]
    try:
        subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(f"Converted: {pdf_path} ➡️ {svg_path}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error converting {pdf_path}: {e}")
        return False

def delete_files(file_path):
    try:
        os.remove(file_path)
        print(f"Deleted: {file_path}")
    except Exception as e:
        print(f"Error deleting {file_path}: {e}")

def process_folder(folder, processed_folders):
    # If the folder has been processed already, skip it
    if folder in processed_folders:
        return
    processed_folders.add(folder)

    eps_files = [f for f in os.listdir(folder) if f.lower().endswith('.eps')]

    if not eps_files:
        print(f"No .eps files found in {folder}")
        return

    for eps_file in eps_files:
        base = os.path.splitext(eps_file)[0]
        eps_path = os.path.join(folder, eps_file)
        pdf_path = os.path.join(folder, f"{base}.pdf")
        svg_path = os.path.join(folder, f"{base}.svg")

        if convert_eps_to_pdf(eps_path, pdf_path):
            if convert_pdf_to_svg(pdf_path, svg_path):
                delete_files(pdf_path)  # Delete the PDF once SVG is created
                delete_files(eps_path)  # Delete the EPS file after conversion

    # Recursively process subfolders
    for subfolder in os.listdir(folder):
        subfolder_path = os.path.join(folder, subfolder)
        if os.path.isdir(subfolder_path):
            process_folder(subfolder_path, processed_folders)

def main():
    folder = os.getcwd()  # Current folder
    processed_folders = set()  # Keep track of processed folders
    process_folder(folder, processed_folders)

    # Notify the user that the process is complete
    root = tk.Tk()
    root.withdraw()  # Hide main window
    messagebox.showinfo("Conversion Complete", "All EPS files have been converted to SVG!")
    root.destroy()

if __name__ == "__main__":
    main()
