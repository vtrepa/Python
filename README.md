Ransomware Krüpteerimise Demod

See projekt sisaldab nelja Python skripti, mis näitavad lunavara tööpõhimõttega seotud krüpteerimisprotsesse kontrollitud õppekeskkonnas. Skriptid on tehtud AI kasutusega.

Skriptid
simulate.py – failide krüpteerimise simulatsioon kaustas testkaust
AESdemo.py – AES-GCM krüpteerimise demonstratsioon
RSAdemo.py – RSA krüpteerimise demonstratsioon
HYBRIDdemo.py – hübriidkrüpteerimise demonstratsioon (AES + RSA)
Eesmärk

Projekt on loodud õppetöö jaoks. Skriptid ei ole päris pahavara, vaid näitavad, kuidas failide krüpteerimine, võtmehaldus ja hübriidlahendused töötavad.

Nõuded
Python 3.x
Paketid:
cryptography

Paigaldamine:

pip install cryptography
Kaustastruktuur
project/
├─ testkaust/
│  └─ ...
├─ testkaust_demo/
│  ├─ test1.txt
│  ├─ test2.txt
│  └─ test3.txt
├─ simulate.py
├─ AESdemo.py
├─ RSAdemo.py
└─ HYBRIDdemo.py
Failide roll
simulate.py

Krüpteerib kaustas testkaust olevad failid ja loob nende kõrvale .enc failid. Skript loob ka lihtsa taastemärkuse.

AESdemo.py

Krüpteerib faili test1.txt AES-GCM algoritmiga ja salvestab nii krüpteeritud kui ka dekrüpteeritud versiooni.

RSAdemo.py

Krüpteerib faili test2.txt RSA avaliku võtmega, taastab selle privaatvõtmega ning salvestab ka võtmefailid.

HYBRIDdemo.py

Krüpteerib faili test3.txt AES-iga ning AES-võtme RSA-ga. See näitab hübriidkrüpteerimise loogikat.

Käivitamine

Käivita skriptid eraldi, näiteks:

python simulate.py
python AESdemo.py
python RSAdemo.py
python HYBRIDdemo.py
Märkus

Skriptid eeldavad, et testfailid on juba loodud ja asuvad vastavates kaustades. Kui failinimed või kaustad on teistsugused, tuleb skriptis vastavad teed üle kontrollida.

Autor

Nikita Petuhov
