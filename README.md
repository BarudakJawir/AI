# AI_320220301006_P7
# Fuzzy Logic

Codingan Fuzzy.py adalah implementasi dari sistem logika fuzzy untuk mengevaluasi tingkat kepuasan pelanggan berdasarkan kualitas produk, pelayanan, dan harga. Pertama, kode memuat data pelanggan dari file Excel menggunakan library pandas. Variabel input fuzzy, yaitu kualitas, pelayanan, dan harga, ditentukan dengan menggunakan fungsi keanggotaan segitiga yang dihasilkan secara otomatis dengan tiga himpunan fuzzy untuk setiap variabel. Selanjutnya, variabel output fuzzy, kepuasan pelanggan, juga didefinisikan dengan fungsi keanggotaan segitiga yang sama. Setelah itu, aturan fuzzy ditentukan berdasarkan logika bisnis yang diinginkan. Misalnya, aturan dapat menyatakan bahwa jika kualitas produk, pelayanan, atau harga rendah, maka tingkat kepuasan pelanggan akan rendah. Sistem kontrol fuzzy dibangun dengan aturan-aturan ini. Kemudian, sistem kontrol ini digunakan untuk mengevaluasi tingkat kepuasan pelanggan untuk setiap pelanggan dalam data. Hasil evaluasi kemudian dicetak, bersama dengan nomor pelanggan, tingkat kepuasan, dan kategori kepuasan yang sesuai, seperti "Tidak Puas", "Kurang Puas", atau "Puas". Dengan demikian, kode ini memberikan alat untuk menganalisis dan memahami tingkat kepuasan pelanggan berdasarkan variabel kualitas produk, pelayanan, dan harga.

Codingan Fuzzy.pyadalah implementasi dari sistem logika fuzzy untuk mengevaluasi tingkat kepuasan pelanggan berdasarkan kualitas produk, pelayanan, dan harga. Pertama, kode memuat data pelanggan dari file Excel menggunakan library pandas. Variabel input fuzzy, yaitu kualitas, pelayanan, dan harga, ditentukan dengan menggunakan fungsi keanggotaan segitiga yang dihasilkan secara otomatis dengan tiga himpunan fuzzy untuk setiap variabel. Selanjutnya, variabel output fuzzy, kepuasan pelanggan, juga didefinisikan dengan fungsi keanggotaan segitiga yang sama. Setelah itu, aturan fuzzy ditentukan berdasarkan logika bisnis yang diinginkan. Misalnya, aturan dapat menyatakan bahwa jika kualitas produk, pelayanan, atau harga rendah, maka tingkat kepuasan pelanggan akan rendah. Sistem kontrol fuzzy dibangun dengan aturan-aturan ini. Kemudian, sistem kontrol ini digunakan untuk mengevaluasi tingkat kepuasan pelanggan untuk setiap pelanggan dalam data. Hasil evaluasi kemudian dicetak, bersama dengan nomor pelanggan, tingkat kepuasan, dan kategori kepuasan yang sesuai, seperti "Tidak Puas", "Kurang Puas", atau "Puas". Dengan demikian, kode ini memberikan alat untuk menganalisis dan memahami tingkat kepuasan pelanggan berdasarkan variabel kualitas produk, pelayanan, dan harga.

### Pastikan sudah menginstall semua library berikut:
1. Pandas
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


