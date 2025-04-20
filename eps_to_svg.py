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
    eps_files = [f for f in os.listdir(folder) if f.lower().endswith('.eps')]

    if not eps_files:
        return False  # No EPS files found in this folder

    for eps_file in eps_files:
        base = os.path.splitext(eps_file)[0]
        eps_path = os.path.join(folder, eps_file)
        pdf_path = os.path.join(folder, f"{base}.pdf")
        svg_path = os.path.join(folder, f"{base}.svg")

        if convert_eps_to_pdf(eps_path, pdf_path):
            if convert_pdf_to_svg(pdf_path, svg_path):
                delete_files(pdf_path)  # Delete the PDF once SVG is created
                delete_files(eps_path)  # Delete the EPS file after conversion

    return True  # EPS files were found and converted

def check_and_convert(folder, processed_folders):
    while True:
        folders_to_check = [folder]

        # Loop through and check folders for EPS files
        while folders_to_check:
            current_folder = folders_to_check.pop()

            # If the folder has already been processed, skip it
            if current_folder in processed_folders:
                continue

            processed_folders.add(current_folder)

            # Process files in the current folder
            if process_folder(current_folder, processed_folders):
                print(f"Converted files in: {current_folder}")
            else:
                print(f"No .eps files found in {current_folder}")

            # Add subfolders to the list of folders to check
            for subfolder in os.listdir(current_folder):
                subfolder_path = os.path.join(current_folder, subfolder)
                if os.path.isdir(subfolder_path):
                    folders_to_check.append(subfolder_path)

        # If no EPS files are found, break the loop
        if not any(process_folder(folder, processed_folders) for folder in processed_folders):
            break

    # Notify the user that no more EPS files were found
    root = tk.Tk()
    root.withdraw()  # Hide main window
    messagebox.showinfo("Conversion Complete", "No more EPS files found. All available files have been converted!")
    root.destroy()

def main():
    folder = os.getcwd()  # Current folder
    processed_folders = set()  # Keep track of processed folders
    check_and_convert(folder, processed_folders)

if __name__ == "__main__":
    main()
