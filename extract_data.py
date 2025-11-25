import re
import os

EMAIL_RE = re.compile(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+")
PHONE_RE = re.compile(r"\b(?:\+?\d{1,3}[-.\s]?)?(?:\d{10}|\d{3}[-.\s]\d{3}[-.\s]\d{4})\b")

def extract_from_file(path):
    if not os.path.exists(path):
        print("File not found.")
        return
    text = open(path, "r", errors="ignore").read()
    emails = set(re.findall(EMAIL_RE, text))
    phones = set(re.findall(PHONE_RE, text))
    print("Emails found:")
    for e in emails:
        print(" -", e)
    print("Phone numbers found:")
    for p in phones:
        print(" -", p)

def main():
    print("===== DATA EXTRACTION (Regex) =====")
    path = input("Enter text file path: ").strip()
    extract_from_file(path)

if __name__ == "__main__":
    main()
