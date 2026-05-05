from pathlib import Path
import os
import base64
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes, serialization

# Testkaust, kus asub hübriiddemo fail
folder = Path("testkaust_demo")
sample = folder / "test3.txt"

# Loome RSA võtmepaari
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)
public_key = private_key.public_key()

# Salvestame RSA võtmed PEM-failidena
private_pem = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption()
)

public_pem = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

(folder / "hybrid_private_key.pem").write_bytes(private_pem)
(folder / "hybrid_public_key.pem").write_bytes(public_pem)

# Loeme testfaili sisu
data = sample.read_bytes()

# Genereerime AES võtme
aes_key = AESGCM.generate_key(bit_length=256)
aesgcm = AESGCM(aes_key)

# Nonce AES-GCM jaoks
nonce = os.urandom(12)

# Krüpteerime faili AES-iga
ciphertext = aesgcm.encrypt(nonce, data, None)

# Salvestame krüpteeritud faili
enc_file = folder / "test3.txt.enc"
enc_file.write_bytes(nonce + ciphertext)

# Krüpteerime AES võtme RSA avaliku võtmega
encrypted_aes_key = public_key.encrypt(
    aes_key,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

# Salvestame krüpteeritud AES võtme
key_file = folder / "test3_aes_key.enc"
key_file.write_bytes(encrypted_aes_key)

# Dekrüpteerime AES võtme RSA privaatvõtmega
decrypted_aes_key = private_key.decrypt(
    encrypted_aes_key,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

# Loeme krüpteeritud faili tagasi
loaded = enc_file.read_bytes()

# Dekrüpteerime faili AES võtmega
decrypted = AESGCM(decrypted_aes_key).decrypt(loaded[:12], loaded[12:], None)

# Salvestame dekrüpteeritud faili
dec_file = folder / "test3_decrypted.txt"
dec_file.write_bytes(decrypted)

# Kuvame tulemuse terminalis
print("Hübriid krüpteeritud fail:", enc_file.name)
print("Hübriid AES-võti:", key_file.name)
print("Hübriid dekrüpteeritud fail:", dec_file.name)
print("AES võti (Base64):", base64.b64encode(aes_key).decode())
