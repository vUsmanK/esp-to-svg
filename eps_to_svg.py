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

def delete_pdf(pdf_path):
    try:
        os.remove(pdf_path)
        print(f"Deleted: {pdf_path}")
    except Exception as e:
        print(f"Error deleting {pdf_path}: {e}")

def main():
    folder = os.getcwd()  # Current folder
    eps_files = [f for f in os.listdir(folder) if f.lower().endswith('.eps')]

    if not eps_files:
        print("No .eps files found!")
        return

    for eps_file in eps_files:
        base = os.path.splitext(eps_file)[0]
        eps_path = os.path.join(folder, eps_file)
        pdf_path = os.path.join(folder, f"{base}.pdf")
        svg_path = os.path.join(folder, f"{base}.svg")

        if convert_eps_to_pdf(eps_path, pdf_path):
            if convert_pdf_to_svg(pdf_path, svg_path):
                delete_pdf(pdf_path)  # Delete the PDF once SVG is created

    root = tk.Tk()
    root.withdraw()  # Hide main window
    messagebox.showinfo("Conversion Complete", "All EPS files have been converted to SVG!")
    root.destroy()

if __name__ == "__main__":
    main()
