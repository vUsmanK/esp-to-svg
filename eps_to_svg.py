import os
import subprocess
import time

# Paths to GhostScript and Inkscape executables
GS_PATH = r"C:\Program Files\gs\gs10.05.0\bin\gswin64c.exe"
INKSCAPE_PATH = r"C:\Program Files\Inkscape\bin\inkscape.com"

def log(action, source, target=""):
    source_name = os.path.basename(source)
    target_name = os.path.basename(target) if target else ""
    print(f"[{action}] {source_name} ➡️ {target_name}" if target else f"[{action}] {source_name} ✅")

def convert_eps_to_pdf(eps_file, pdf_file):
    try:
        cmd = [
            GS_PATH,
            "-dBATCH", "-dNOPAUSE", "-dSAFER",
            "-sDEVICE=pdfwrite",
            f"-sOutputFile={pdf_file}",
            eps_file
        ]
        subprocess.run(cmd, check=True)
        log("EPS ➡️ PDF", eps_file, pdf_file)
        return True
    except subprocess.CalledProcessError:
        log("❌ EPS2PDF Failed", eps_file)
        return False

def convert_pdf_to_svg(pdf_file, svg_file):
    try:
        cmd = [
            INKSCAPE_PATH,
            pdf_file,
            "--export-type=svg",
            f"--export-filename={svg_file}"
        ]
        subprocess.run(cmd, check=True)
        log("PDF ➡️ SVG", pdf_file, svg_file)
        return True
    except subprocess.CalledProcessError:
        log("❌ PDF2SVG Failed", pdf_file)
        return False

def delete_files(*files):
    for file in files:
        if os.path.exists(file):
            os.remove(file)
            log("Delete", file)

def process_folder(folder, processed_folders):
    folder = os.path.abspath(folder)
    if folder in processed_folders:
        return False

    processed_folders.add(folder)
    eps_files = [f for f in os.listdir(folder) if f.lower().endswith('.eps')]

    if not eps_files:
        return False

    for eps_file in eps_files:
        base = os.path.splitext(eps_file)[0]
        eps_path = os.path.join(folder, eps_file)
        pdf_path = os.path.join(folder, f"{base}.pdf")
        svg_path = os.path.join(folder, f"{base}.svg")

        if convert_eps_to_pdf(eps_path, pdf_path):
            convert_pdf_to_svg(pdf_path, svg_path)
            delete_files(pdf_path)
        else:
            log("❌ Skipped EPS", eps_path)

        delete_files(eps_path)

    return True

def scan_and_convert(base_folder):
    processed_folders = set()
    while True:
        found_new = False

        for root, dirs, files in os.walk(base_folder):
            if process_folder(root, processed_folders):
                found_new = True

        if not found_new:
            print("\n🎉 No more EPS files found. Conversion complete.")
            break

if __name__ == "__main__":
    base_folder = os.path.dirname(os.path.abspath(__file__))
    print(f"🔍 Starting conversion in: {base_folder}\n")
    scan_and_convert(base_folder)
    time.sleep(2)  # Give you time to read the success message if in .exe
