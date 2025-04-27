# SUML_03_Docker

## Wymagania
- Docker zainstalowany na komputerze

## Jak uruchomić aplikację
1. Sklonuj repozytorium:
   ```bash
   git clone https://github.com/RutkowskaKarolina/SUML_03_Docker
   cd SUML_03_Docker

2. Zbuduj obraz Docker:
   Aby zbudować obraz Docker, użyj poniższego polecenia:

   ```bash
   docker build -t yolov5s-model .

3. Uruchom aplikację:
   ```bash
   docker run -p 5000:5000 yolov5s-model


4. Otwórz aplikację w przeglądarce:

  ```bash
http://localhost:5000
