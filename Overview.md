## Security Overview – Secure File Upload & Download Portal

1. AES Encryption (Custom Implementation) <br>
- All uploaded files are encrypted using AES encryption in CBC mode with PKCS7 padding for secure block alignment.<br>
- A random Initialization Vector (IV) is generated for each encryption session to ensure unique ciphertexts even for identical files.<br>
- Integrity is maintained by proper key handling and separating the IV from the ciphertext for later decryption.

---

2. Key Management
- The encryption key is manually provided by the user at runtime via a password field in the web interface.<br>
- Keys are validated before use to prevent incorrect decryption attempts.<br>
- In a production environment, keys should:<br>
a. Be stored securely in environment variables or a key vault.<br>
b. Never be hardcoded in the application.

---

3. File Upload Procedure<br>
- User uploads a file via the secure upload form.<br>
- The file is encrypted immediately on the server using the provided key and IV.<br>
- The encrypted version replaces the original file; plaintext files are never stored permanently.

---

4. File Download Procedure<br>
- User requests a file download from the download page.
- The system prompts for the correct decryption key.

- If the key matches:<br>
a. The file is decrypted in memory and sent to the user.<br>
b. The decrypted copy is deleted from memory immediately after sending.

- If the key is incorrect:<br>
a. The system returns an error message and no file is provided.

---

5. Decrypted File Handling<br>
- Decrypted data exists only during the active session.<br>
- No decrypted file is saved to the server’s filesystem.<br>
- This approach reduces the risk of sensitive data exposure in case of a breach.
