<p align="center">
  <h1 align="center">CARA IDENTIFIKASI VULNERABILITY PADA MIKROTIK MENGGUNAKAN SHODAN DAN NMAP</h1>
</p>

### Pendahuluan
<h4>
Fuzzy.py merupakan bentuk implementasi dari algoritma fuzzy untuk mengevaluasi tingkat kelayakan dari outlet mi ayam yang datanya telah termuat dalam file .xlsx yang akan dimuat kedalam code menggunakan library panda. Pada studi kasus kali ini saya menggunakan 3 variabel output yaitu kebersihan, rasa, dan harga dengan menggunakan output yaitu kelayakan outlet. Hasil evaluasi kemudian dicetak, bersama dengan nomor outlet, kebersihan, rasa, harga, dan tingkat kelayakan yang sesuai, seperti "Tidak layak", "Kurang layak", atau "layak". Dengan demikian, kode ini memberikan alat untuk menganalisis dan memahami tingkat kelayakan berdasarkan variabel kualitas kebersihan, rasa, dan harga.
</h4>

### Langkah-langkah 

### Pertama install module module dibawah:
## 1.Panda
`import pandas as pd`: Library pandas digunakan untuk membaca data dari file Excel dan mengelola data dalam bentuk DataFrame.
```
pip install pandas
```
2. Numpy
`import numpy as np`: Library numpy digunakan untuk melakukan operasi numerik seperti membuat array dan melakukan operasi matematika.
```
pip install numpy
```
3. Skfuzzy
`import skfuzzy as fuzz`: Library skfuzzy adalah pustaka untuk pemrosesan logika fuzzy dan `from skfuzzy import control as ctrl`: Ini mengimpor modul kontrol dari pustaka skfuzzy dengan alias ctrl.
```
pip install scikit-fuzzy
```
4. Sklearn
`from sklearn.model_selection import train_test_split`: Modul train_test_split digunakan untuk membagi data menjadi set pelatihan dan set pengujian.
```
pip install scikit-learn
```


