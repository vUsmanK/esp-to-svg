import os
import sys
import subprocess

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
            log("Deleted", file)

def find_eps_files(base_folder):
    eps_files = []
    for root, dirs, files in os.walk(base_folder):
        print(f"📂 Checking: {root}")
        for file in files:
            if file.lower().endswith('.eps') and not file.endswith('.eps.done'):
                eps_files.append(os.path.join(root, file))
    return eps_files

def convert_all_eps(base_folder):
    while True:
        eps_files = find_eps_files(base_folder)

        if not eps_files:
            print("\n✅ No more EPS files found. Conversion fully complete.")
            break

        for eps_path in eps_files:
            base = os.path.splitext(eps_path)[0]
            pdf_path = base + ".pdf"
            svg_path = base + ".svg"

            if convert_eps_to_pdf(eps_path, pdf_path):
                if convert_pdf_to_svg(pdf_path, svg_path):
                    delete_files(pdf_path)  # Remove the temporary PDF
                    processed_eps = eps_path + ".done"
                    os.rename(eps_path, processed_eps)  # Rename EPS to mark as processed
                    log("Marked as processed", processed_eps)

if __name__ == "__main__":
    if getattr(sys, 'frozen', False):
        start_folder = os.path.dirname(sys.executable)
    else:
        start_folder = os.path.dirname(os.path.abspath(__file__))

    print(f"🔍 Searching for EPS files inside:\n{start_folder}\n")
    convert_all_eps(start_folder)

    input("\n🎉 Conversion complete! Press Enter to exit...")
