# 🔐 Secure File Sharing System

## 📄 Project Overview

This project simulates a real-world solution where users can upload and download files securely using AES encryption. The goal is to protect files both at rest and during transit. It was developed using Python Flask (or optionally Node.js) and incorporates encryption best practices, a simple web interface, and secure key management.

This type of system is useful in environments like healthcare, legal, or corporate settings where sensitive data transfer must be protected.

---

## 🧠 Skills Gained

- Web development fundamentals (backend & frontend)
- AES encryption and secure file transfer
- Encryption key management and secure coding
- File handling best practices
- Git & GitHub version control

---

## 🛠️ Tools Used

- [Python Flask](https://flask.palletsprojects.com/en/latest/) / [Node.js + Express](https://expressjs.com/)
- [PyCryptodome](https://pycryptodome.readthedocs.io/en/latest/)
- [Node.js Crypto Module](https://nodejs.org/api/crypto.html)
- [HTML/CSS/JavaScript](https://developer.mozilla.org/en-US/docs/Web)
- [Postman](https://www.postman.com/downloads/)
- [curl](https://curl.se/)
- [Git](https://git-scm.com/) & [GitHub](https://github.com/)

---

## 🗂 Deliverables

- ✅ GitHub repository with commented code  
- 🎥 Walkthrough video demonstrating upload/download process and AES encryption  
- 🔐 Security overview document explaining encryption logic and key handling  

---

## 📌 Key Features Included 

- Secure file **upload and download functionality**
- **AES encryption** for all files at rest
- Basic **encryption key management** practices
- Clean, **user-friendly interface**
- Well-documented **code and system architecture**

---

## 📁 Folder Structure

```
SecureFileShare-Project/
├── README.md
├── Security_Overview.md
├── app/
│ ├── app.py
│ ├── templates/
│ └── uploads/
├── static/
│ ├── style.css
│ └── icons/
├── config/
│ ├── secret.key
│ └── requirements.txt
├── test/
│ └── sample_files/
└── screenshots/
    ├── file_upload_demo.png
    └── aes_encryption_flow.png
```
---

## 🔍 Sample Analysis Insights

- 🔐 **Encryption in Action**: Files are encrypted before storing using AES and only decrypted on download
- 📂 **Secure File Handling**: Uploads and downloads are validated and tracked
- 🧪 **API Security**: Tested endpoints using Postman and curl for verification
- 🗝️ **No Plaintext Keys**: Encryption keys are generated and stored securely
- 👤 **Simplicity for Users**: Interface designed for intuitive use

---

## 📸 Visuals

Found in the `screenshots/` folder:

- `upload_form_view.png` – Frontend upload form  
- `encrypted_file_saved.png` – Example AES-encrypted file result  
- `postman_api_test.png` – API testing validation  
- `architecture_flowchart.png` – Diagram of encryption process and architecture  

---

## ✅ Final Outcome

This project demonstrates my ability to:

- Build and secure full-stack applications  
- Implement AES encryption with key management  
- Write clean, well-documented, version-controlled code  
- Simulate real-world security-focused development  
