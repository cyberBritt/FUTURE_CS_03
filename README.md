# Secure File Upload Portal

## Project Overview

This task involved developing a secure file upload/download portal using Python Flask with AES encryption. The system allows users to upload files, encrypt them with a password, and securely download decrypted files using the correct key. The goal was to protect sensitive files from unauthorized access.


## Skills Gained
- Flask web application development
- AES encryption and decryption implementation
- Secure password handling with salt and initialization vector (IV)
- HTML/CSS/JavaScript UI creation
- File handling and server-side validation


## Tools Used
- Python (Flask, PyCryptodome) – Backend development and encryption
- HTML/CSS/JavaScript – Frontend and UI functionality
- OBS Studio/Canva - Screen record and video editing
- Kali Linux – Testing environment
- GitHub – Project host


## Deliverables
Secure File Upload Portal source code
Encryption/decryption demonstration video
Bash command logs
Screenshot documentation of encryption process


## Folder Structure
```
Secure-File-Portal/
│── README.md
│── Languages
│── -HTML
│ ├── upload.html
│ ├── download.html
│── -CSS
│ ├── style.css
│── -Javascript
│ ├── script.js
│── -Python
│ ├── app.py
│── Screenshots/
│ ├── 1_upload_form.png
│ ├── 2_upload_file.png
│ ├── 3_success_form.png
│ ├── 4_success_key.png
│ ├── 5_file_decrypted.png
│ ├── 6_incorrect_key.png
│ ├── 7_incorrect_result.png
│── Overview.md
│── Tools_Used.md
│── View_Demo.md
```

## Final Outcome

The portal successfully encrypts uploaded files using AES with a salt and initialization vector (IV) to ensure each encryption is unique. This prevents rainbow table attacks and guarantees confidentiality. All encryption, decryption, and user interaction occurs at Application Layer 7 of the OSI model.

---

Created by: B.Brinson
