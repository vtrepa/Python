from pathlib import Path
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes, serialization

# Testkaust, kus asub RSA demo fail
folder = Path("testkaust_demo")
message_file = folder / "test2.txt"

# Loeme faili sisu
message = message_file.read_bytes()

# Loome RSA võtmepaari
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)
public_key = private_key.public_key()

# Krüpteerime faili avaliku võtmega
encrypted = public_key.encrypt(
    message,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

# Salvestame krüpteeritud faili
enc_file = folder / "test2.txt.enc"
enc_file.write_bytes(encrypted)

# Dekrüpteerime faili privaatvõtmega
decrypted = private_key.decrypt(
    encrypted,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

# Salvestame dekrüpteeritud faili
dec_file = folder / "test2_decrypted.txt"
dec_file.write_bytes(decrypted)

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

(folder / "rsa_private_key.pem").write_bytes(private_pem)
(folder / "rsa_public_key.pem").write_bytes(public_pem)

# Kuvame tulemuse terminalis
print("RSA krüpteeritud fail:", enc_file.name)
print("RSA dekrüpteeritud fail:", dec_file.name)
print("RSA võtmed salvestatud.")
