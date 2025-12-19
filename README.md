🔓 PDF Unlock Automation Tool (Password-Based)  
📌 Business Problem

In many business scenarios, PDF files are password-protected for security reasons.
However, practical challenges often arise:
- You may need to share the PDF with someone
- You do not want to share the password
- Asking recipients to unlock PDFs themselves causes inconvenience
- Using third-party online PDF unlock websites poses:
  - Data privacy risks
  - Possibility of sensitive data misuse
  - Compliance and confidentiality concerns

Because of these risks, relying on online tools was not a safe or scalable solution.

🎯 Objective

To create a local, secure, and offline automation tool that:

- Unlocks password-protected PDFs using the correct password
- Generates a new unlocked PDF
- Eliminates dependency on third-party websites
- Ensures data privacy and confidentiality

🔐 Why This Project Was Created

This project was created to solve a real operational pain point:

- Sometimes you are required to share a PDF
- You don’t want to disclose the password
- You also don’t want to:
  - Ask the recipient to search for PDF unlock tools
  - Risk data leakage via online platforms

With this automation:
- You unlock the PDF once (locally)
- Share the unlocked version
- Keep the password confidential

🔧 Tools & Technologies Used
- Python
- pikepdf library
- os module
- Command-line execution
- ChatGPT-assisted development

🔄 Automation Workflow
1. Place the locked PDF in the same folder as the script
2. Provide:
  - PDF file name
  - Correct password
3. Run the Python script
4. Script unlocks the PDF locally
5. A new file is generated:
```
<original_filename>_unlocked.pdf
```
6. The unlocked PDF is ready to share

🧩 Key Automation Logic

- Uses pikepdf to safely open encrypted PDFs
- Validates:
  - File existence
  - Correct password
- Handles errors gracefully
- Ensures original PDF remains unchanged
- Creates a separate unlocked copy

⚠️ Challenges & Error Handling  

❌ Possible Issues
- Incorrect password
- File not found
- PDF decryption or read errors

✅ Handling Implemented
- Clear console messages for:
  - Missing files
  - Wrong passwords
  - Unexpected errors
- Prevents silent failures

📈 Business Impact
- Eliminated reliance on third-party PDF tools
- Improved data security and confidentiality
- Reduced manual effort and inconvenience
- Enabled faster document sharing
- Suitable for sensitive business documents

📂 Folder Structure
```
pdf-unlock-automation/
│
├── unlock_pdf.py
├── README.md
└── input.pdf
```
🧪 Python Automation Script
```
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
PASSWORD = "name"              # Enter your PDF password
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
```
📝 Notes

>Note:
This project was developed to ensure data privacy by avoiding third-party online PDF unlocking services.
It performs all operations locally, ensuring sensitive information is never uploaded externally.

>Disclaimer:
This script should be used only for PDFs you are authorized to unlock.

>Development Note:
This project was developed with the assistance of ChatGPT for ideation and debugging.
Final logic, testing, and business understanding were performed by me.

⭐ Why This Project Matters  

This automation demonstrates:
- Security-conscious thinking
- Practical problem-solving
- Responsible handling of sensitive data
- Real-world business automation usage