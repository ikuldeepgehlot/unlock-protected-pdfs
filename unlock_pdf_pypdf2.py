#!/usr/bin/env python3
"""
Unlock a password-protected PDF (in the same folder as this script).

Steps:
1. Set PDF_FILENAME and PASSWORD variables below.
2. Run: python unlock_pdf.py
3. The unlocked file will be saved as <original>_unlocked.pdf
"""

import os
import pikepdf

# -------- EDIT THESE VALUES --------
PDF_FILENAME = "input.pdf"      # Example: "report.pdf"
PASSWORD = "name"  # Enter your PDF password
# -----------------------------------

def unlock_pdf(pdf_filename, password):
    input_path = os.path.join(os.getcwd(), pdf_filename)
    if not os.path.exists(input_path):
        print(f"❌ File not found: {input_path}")
        return

    base_name, ext = os.path.splitext(pdf_filename)
    output_path = os.path.join(os.getcwd(), f"{base_name}_unlocked{ext}")

    try:
        with pikepdf.open(input_path, password=password) as pdf:
            pdf.save(output_path)
        print(f"✅ Unlocked PDF saved as: {output_path}")
    except pikepdf.PasswordError:
        print("❌ Incorrect password or unable to decrypt this PDF.")
    except Exception as e:
        print(f"❌ Error unlocking PDF: {e}")

if __name__ == "__main__":
    unlock_pdf(PDF_FILENAME, PASSWORD)
