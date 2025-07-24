import shutil
import sys
from pathlib import Path

def move_contents_up(folder: Path):
    for item in folder.iterdir():
        target = Path.cwd() / item.name
        if target.exists():
            print(f"Skipping existing: {target}")
        else:
            shutil.move(str(item), str(target))
            print(f"Moved: {item} → {target}")

def safe_rmtree(path: Path):
    if path.exists() and path.is_dir():
        shutil.rmtree(path)
        print(f"Removed directory: {path}")
    elif path.exists():
        path.unlink()
        print(f"Removed file: {path}")

def main():
    source_folder = Path("masterdata-example")
    if not source_folder.exists() or not source_folder.is_dir():
        print(f"Error: source folder '{source_folder}' not found")
        sys.exit(1)

    move_contents_up(source_folder)
    safe_rmtree(source_folder)
    safe_rmtree(Path("assets"))
    safe_rmtree(Path("move_generated_files.py"))

if __name__ == "__main__":
    main()
