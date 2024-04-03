
<p align="center">
  <h1 align="center">IMPLEMENTASI ALGORITMA FUZZY PADA EVALUASI KELAYAKAN OUTLET MI AYAM</h1>
</p>

### Pendahuluan
<h4>
Fuzzy.py merupakan bentuk implementasi dari algoritma fuzzy untuk mengevaluasi tingkat kelayakan dari outlet mi ayam yang datanya telah termuat dalam file .xlsx yang akan dimuat kedalam code menggunakan library panda. Pada studi kasus kali ini saya menggunakan 3 variabel output yaitu kebersihan, rasa, dan harga dengan menggunakan output yaitu kelayakan outlet. Hasil evaluasi kemudian dicetak, bersama dengan nomor outlet, kebersihan, rasa, harga, dan tingkat kelayakan yang sesuai, seperti "Tidak layak", "Kurang layak", atau "layak". Dengan demikian, kode ini memberikan alat untuk menganalisis dan memahami tingkat kelayakan berdasarkan variabel kualitas kebersihan, rasa, dan harga.
</h4>

### Langkah-langkah 

### Pertama install module module dibawah:
## 1.Panda
<h4>
`import pandas as pd`: Library pandas digunakan untuk membaca data dari file Excel dan mengelola data dalam bentuk DataFrame.
untuk menginstall panda gunakan command
</h4>
'''
$pip install panda
'''
<img width="750px" src="s1.png">

## 2.Numpy
<h4>
`import numpy as np`: Library numpy digunakan untuk melakukan operasi numerik seperti membuat array dan melakukan operasi matematika.

<h4>
Cari IP server yang kemungkinan memiliki vulnerability sehingga dapat diakses, biasanya memiliki port 22 dan 23 yang terbuka
</h4>

<img width="750px" src="s2.png">

<h4>
Selain menggunakan shodan, kita juga dapat memastikan kembali port yang terbuka menggunakan nmap yang terdapat di Linux
</h4>

```
$nmap <ip address>
```

<img width="750px" src="s3.png">

<h4>
sekian cara mencari IP server yang memiliki vulnerability dengan menggunakan shodan dan nmap. dengan mengetahui celah yang ada pada IP tersebut, kita dapat melakukan proses yang lebih lanjut lagi agar mendapatkan akses IP tersebut.
</h4>
____________
