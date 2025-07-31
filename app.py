from flask import Flask, request, redirect, url_for, render_template, send_file
from werkzeug.utils import secure_filename
import os
from io import BytesIO
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend

# Flask config
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.secret_key = b'ThisIsA16ByteKey'

# Make upload folder if not exists
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

# AES Key generation using password and salt
def get_aes_key(password, salt):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    return kdf.derive(password.encode())

# Encrypt file
def encrypt_file(file_data, password):
    salt = os.urandom(16)
    iv = os.urandom(16)
    key = get_aes_key(password, salt)
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(file_data) + encryptor.finalize()
    return salt + iv + ciphertext  # return full payload

# Decrypt file
def decrypt_file(encrypted_data, password):
    salt = encrypted_data[:16]
    iv = encrypted_data[16:32]
    ciphertext = encrypted_data[32:]
    key = get_aes_key(password, salt)
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    return decryptor.update(ciphertext) + decryptor.finalize()

# Upload Route
@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        enc_key = request.form['enc_key']
        key = enc_key.strip()

        file = request.files['file']
        filename = secure_filename(file.filename)
        file_data = file.read()

        encrypted = encrypt_file(file_data, key)

        with open(os.path.join(app.config['UPLOAD_FOLDER'], filename + '.enc'), 'wb') as f:
            f.write(encrypted)

        return redirect(url_for('success', filename=filename + '.enc'))
    return render_template('form.html')

# Success Page
@app.route('/success')
def success():
    filename = request.args.get('filename')
    return render_template('success.html', filename=filename)

# Decrypt Route
@app.route('/decrypt', methods=['POST'])
def decrypt_file_route():
    filename = request.form['filename']
    dec_key = request.form['dec_key']
    key = dec_key.strip()

    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    with open(file_path, 'rb') as f:
        encrypted_data = f.read()

    try:
        decrypted_data = decrypt_file(encrypted_data, key)
    except Exception as e:
        return f"❌ Decryption failed. Wrong key or corrupted file: {str(e)}"

    return send_file(BytesIO(decrypted_data), as_attachment=True, download_name=filename.replace('.enc', ''))

# Run App
if __name__ == '__main__':
    app.run(debug=True)
