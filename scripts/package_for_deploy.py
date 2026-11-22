import os
import zipfile

ROOT_DIR = r"C:\Users\PC\.gemini\antigravity-ide\scratch\computer-repairs-fast"
ZIP_OUT = r"C:\temp\computerrepairsfast-deploy.zip"

EXCLUDE_DIRS = {".git", ".system_generated", "__pycache__", ".vscode", ".idea"}
EXCLUDE_EXTS = {".py", ".pyc", ".log", ".tmp"}

if os.path.exists(ZIP_OUT):
    os.remove(ZIP_OUT)

count = 0
with zipfile.ZipFile(ZIP_OUT, "w", zipfile.ZIP_DEFLATED) as z:
    for root, dirs, files in os.walk(ROOT_DIR):
        dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS and not d.startswith(".")]
        for file in files:
            ext = os.path.splitext(file)[1].lower()
            if ext in EXCLUDE_EXTS and not file.endswith(".php"):
                continue
            if file.startswith("test_") or file.startswith("inspect_") or file.startswith("debug_"):
                continue
            abs_path = os.path.join(root, file)
            rel_path = os.path.relpath(abs_path, ROOT_DIR).replace("\\", "/")
            z.write(abs_path, rel_path)
            count += 1

size_mb = os.path.getsize(ZIP_OUT) / (1024 * 1024)
print(f"Packaged {count} files into {ZIP_OUT} ({size_mb:.2f} MB)")
