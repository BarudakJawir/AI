
<p align="center">
  <h1 align="center">CARA IDENTIFIKASI VULNERABILITY PADA MIKROTIK MENGGUNAKAN SHODAN DAN NMAP</h1>
</p>

### Pendahuluan
<h4>
Shodan adalah sebuah mesin pencari yang dirancang untuk mencari perangkat dan sistem komputer yang terhubung dengan world Wide Web. Shodan bekerja sama seperti google namun spesifik dalam memberi tahu informasi terkait informasi banner, http, SSH, FTP, dll. dalam ethical hacking, Shodan dapat membuka semua akses menuju vulnerability sehingga bisa di patch atau diperbaki kelemahan-kelemahan yang ditemukan. NMAP adalah sebuah tools open source yang dapat digunakan untuk memeriksa audit keamanan jaringan. Dengan menggabungkan fungsi antara shodan dan Nmap, kita dapat mengetahui Vulnerability suatu jaringan, berikut adalah caranya:
</h4>

### Langkah-langkah 
<h4>
Langkah pertama yang dilakukan adalah dengan mencari IP yang kemungkinan memiliki vulnerability menggunakan shodan, kali ini kita akan mencari server mikrotik yang terdapat di malaysia dengan menggunakan kata kunci mikrotik country:'my"
</h4>

<img width="750px" src="s1.png">

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
