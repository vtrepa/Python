from pathlib import Path
import os
import base64
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

# Testkaust, kus asub AES demo fail
folder = Path("testkaust_demo")
sample = folder / "test1.txt"

# Loome AES-256 võtme
key = AESGCM.generate_key(bit_length=256)
aesgcm = AESGCM(key)

# 12-baidine nonce AES-GCM jaoks
nonce = os.urandom(12)

# Loeme failist andmed sisse
data = sample.read_bytes()

# Krüpteerime andmed
ciphertext = aesgcm.encrypt(nonce, data, None)

# Salvestame krüpteeritud faili
enc_file = folder / "test1.txt.enc"
enc_file.write_bytes(nonce + ciphertext)

# Loeme krüpteeritud faili tagasi
loaded = enc_file.read_bytes()

# Dekrüpteerime faili algkujule
decrypted = aesgcm.decrypt(loaded[:12], loaded[12:], None)

# Salvestame dekrüpteeritud faili
dec_file = folder / "test1_decrypted.txt"
dec_file.write_bytes(decrypted)

# Kuvame tulemuse terminalis
print("AES krüpteeritud fail:", enc_file.name)
print("AES dekrüpteeritud fail:", dec_file.name)
print("AES võti (Base64):", base64.b64encode(key).decode())
