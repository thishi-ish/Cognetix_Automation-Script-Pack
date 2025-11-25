import os

def rename_files(folder, pattern, start_num=1):
    if not os.path.exists(folder):
        print("Folder not found.")
        return

    files = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]
    files.sort()
    num = start_num
    for f in files:
        ext = os.path.splitext(f)[1]
        new_name = f"{pattern}_{num}{ext}"
        os.rename(os.path.join(folder, f), os.path.join(folder, new_name))
        print(f"{f} -> {new_name}")
        num += 1
    print("✔ Renaming done.")

def main():
    print("===== BATCH FILE RENAMER =====")
    folder = input("Folder path: ").strip()
    pattern = input("New name pattern (e.g., holiday): ").strip()
    start = input("Start number (default 1): ").strip()
    try:
        start_num = int(start) if start else 1
    except ValueError:
        start_num = 1
    rename_files(folder, pattern, start_num)

if __name__ == "__main__":
    main()
