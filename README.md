# Tugas Besar Strategi Algoritma: Traveling Salesman Problem (TSP)

## **Deskripsi Proyek**
Proyek ini merupakan implementasi dan analisis algoritma untuk menyelesaikan permasalahan Traveling Salesman Problem (TSP) menggunakan dua pendekatan berbeda:
1. **Algoritma Backtracking**
2. **Algoritma Dynamic Programming (Held-Karp)**

Proyek ini dirancang untuk membandingkan kinerja kedua algoritma dalam hal waktu eksekusi pada berbagai ukuran input (jumlah kota).

---

## **Anggota Kelompok**
1. Achmad Ata Irsyadudin (21102013)  
2. Aditya Setiawan (21102034)  
3. Andika Purnama Putra (21102141)  
4. Naufal Tsaqif Arkan (21102265)  
5. Landewank Fahreza Firdaus (21102120)

---

## **Fitur Program**
- Menghasilkan matriks jarak acak untuk merepresentasikan graf berbobot lengkap.
- Mengimplementasikan dua algoritma untuk menyelesaikan TSP:
  - **Backtracking** untuk pencarian solusi optimal secara eksplisit.
  - **Dynamic Programming (Held-Karp)** untuk pencarian solusi optimal dengan penyimpanan hasil perhitungan sebelumnya (memoization).
- Mengukur waktu eksekusi kedua algoritma untuk membandingkan performa.
- Menampilkan grafik hasil eksekusi untuk berbagai ukuran input.

---

## **Struktur Program**
- **`generate_distance_matrix(n)`**: Membuat matriks jarak acak berukuran `n x n`.
- **`backtracking_tsp(distance_matrix)`**: Mengimplementasikan algoritma Backtracking untuk TSP.
- **`dp_tsp(distance_matrix)`**: Mengimplementasikan algoritma Dynamic Programming (Held-Karp) untuk TSP.
- **`run_tests()`**: Menguji performa kedua algoritma pada berbagai ukuran input dan menampilkan hasilnya dalam bentuk grafik.

---

## **Instalasi dan Persyaratan**
### **1. Persyaratan Sistem**
- Python 3.x
- Paket tambahan:
  - numpy
  - matplotlib

### **2. Library yang digunakan**
```
numpy 
matplotlib
time
itertools
```

---

## **Cara Menjalankan Program**
1. Jalankan program dengan perintah berikut:
```
python tsp_tests.py
```
2. Program akan menghasilkan output berupa jalur optimal, jarak total, dan waktu eksekusi untuk setiap algoritma.
3. Program juga akan menampilkan grafik yang membandingkan waktu eksekusi kedua algoritma pada berbagai ukuran input.

---

## **Penjelasan Algoritma**
### **1. Algoritma Backtracking**
Algoritma ini mencoba semua kemungkinan jalur secara eksplisit dengan menggunakan rekursi dan backtracking. Pada setiap langkah, algoritma akan:
- Mengunjungi semua kota yang belum dikunjungi.
- Menghitung jarak total.
- Memeriksa apakah jalur yang diperoleh lebih optimal dibandingkan sebelumnya.
- Mengembalikan hasil berupa jalur optimal dan jarak total.

**Kompleksitas Waktu**: *O(n!)*

### **2. Algoritma Dynamic Programming (Held-Karp)**
Algoritma ini memanfaatkan metode *memoization* untuk menyimpan hasil perhitungan jarak yang sudah dihitung sebelumnya. Dengan menggunakan bitmasking, algoritma melacak kota yang sudah dikunjungi dan menghitung jarak optimal secara dinamis.

**Kompleksitas Waktu**: *O(n^2 * 2^n)*

---

## **Hasil Output**
```
Testing with 3 cities...

Running Backtracking TSP...
Backtracking Path: [0, 2, 1, 0], Distance: 12, Time: 0.000000 seconds

Running Dynamic Programming TSP...
DP Path: [0, 2, 1, 0], Distance: 12, Time: 0.000000 seconds

Testing with 6 cities...

Running Backtracking TSP...
Backtracking Path: [0, 3, 1, 5, 2, 4, 0], Distance: 16, Time: 0.000000 seconds

Running Dynamic Programming TSP...
DP Path: [0, 3, 1, 5, 2, 4, 0], Distance: 16, Time: 0.000000 seconds

Testing with 9 cities...

Running Backtracking TSP...
Backtracking Path: [0, 8, 7, 1, 5, 3, 2, 6, 4, 0], Distance: 23, Time: 0.098998 seconds

Running Dynamic Programming TSP...
DP Path: [0, 8, 7, 1, 5, 3, 2, 6, 4, 0], Distance: 23, Time: 0.005544 seconds

Testing with 11 cities...

Running Backtracking TSP...
Backtracking Path: [0, 2, 6, 3, 9, 7, 4, 8, 10, 5, 1, 0], Distance: 20, Time: 9.592755 seconds

Running Dynamic Programming TSP...
DP Path: [0, 2, 6, 3, 9, 7, 4, 8, 10, 5, 1, 0], Distance: 20, Time: 0.031126 seconds

Testing with 12 cities...

Running Backtracking TSP...
Backtracking Path: [0, 3, 11, 7, 8, 9, 6, 4, 1, 10, 2, 5, 0], Distance: 23, Time: 107.527479 seconds

Running Dynamic Programming TSP...
DP Path: [0, 3, 11, 7, 8, 9, 6, 4, 1, 10, 2, 5, 0], Distance: 23, Time: 0.111233 seconds
```

---

## **Analisis Hasil dan Grafik**
Program akan menampilkan grafik yang menunjukkan perbedaan waktu eksekusi antara algoritma Backtracking dan Dynamic Programming pada berbagai ukuran input.
- Algoritma Backtracking cenderung memiliki waktu eksekusi yang eksponensial karena kompleksitasnya *O(n!)*.
- Algoritma Dynamic Programming memiliki waktu eksekusi yang lebih baik untuk ukuran input yang besar, meskipun masih mengalami pertumbuhan eksponensial untuk jumlah kota yang sangat besar.

![Backtracking VS Dynamic Programming](https://github.com/user-attachments/assets/bd51d197-c9cf-4047-b168-3bfc84b6a476)

---
## **Perbandingan Kompleksitas Waktu**

![perbandingan](https://github.com/user-attachments/assets/50e45425-b08c-4e4c-9421-3de8f8afc415)

---

## **Mana yang Paling Minim Kompleksitasnya?**
**Dynamic Programming (Held-Karp)** memiliki kompleksitas yang lebih rendah dan waktu eksekusi yang lebih efisien dibandingkan dengan Backtracking. Oleh karena itu, jika menghadapi jumlah kota yang besar, **Dynamic Programming** adalah pilihan yang lebih baik dari segi waktu eksekusi.

Namun, jika hanya menangani sejumlah kota yang yang kecil dan ingin mencari solusi yang lebih intuitif atau sederhana, **Bactracking** mungkin cukup, meskipun lebih lambat dari **Dynamic Programming**.

---

## **Kesimpulan**
1. Untuk jumlah kota kecil (seperti `n=3`, `n=6`), perbedaan waktu eksekusi antara kedua algoritma mungkin tidak terlalu signifikan.
2. Untuk jumlah kota yang lebih besar (misalnya `n=20`, `n=25`), algoritma **Dynamic Programming** akan lebih unggul karena waktu eksekusinya jauh lebih rendah dibandingkan **Backtracking**. Dengan kata lain, **Dynamic Programming** lebih dapat menangani masalah dengan jumlah kota yang lebih banyak, sementara **Backtracking** akan menjadi sangat lambat dan tidak praktis untuk `n` yang besar
3. Algoritma Backtracking cocok untuk jumlah kota yang kecil, namun tidak efisien untuk input besar karena kompleksitasnya.
4. Algoritma Dynamic Programming (Held-Karp) lebih optimal untuk jumlah kota yang lebih besar karena memanfaatkan teknik *memoization*, meskipun masih memiliki batasan dalam skala yang sangat besar.
5. Program ini memberikan pemahaman tentang pendekatan brute force dan optimasi dalam menyelesaikan TSP.

---

## **Referensi**
- Held, M., & Karp, R. M. (1962). "A Dynamic Programming Approach to Sequencing Problems." Journal of the Society for Industrial and Applied Mathematics.
- https://numpy.org/
- https://matplotlib.org/

---

## **Lisensi**
Proyek ini dibuat untuk tujuan akademik dan edukasi. Semua kode dan dokumentasi dapat digunakan dengan menyertakan atribusi kepada pemilik asli.

