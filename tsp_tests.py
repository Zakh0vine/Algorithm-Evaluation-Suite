import itertools
import numpy as np
import time

# Fungsi untuk menghasilkan matriks jarak acak
def generate_distance_matrix(n):
    # Membuat matriks jarak acak
    matrix = np.random.randint(1, 10, size=(n, n))
    np.fill_diagonal(matrix, 0)  # Jarak ke diri sendiri adalah 0
    return matrix

# Algoritma Greedy
def greedy_tsp(distance_matrix):
    n = len(distance_matrix)
    visited = [False] * n
    path = []
    total_distance = 0

    # Mulai dari kota pertama
    current_city = 0
    visited[current_city] = True
    path.append(current_city)

    for _ in range(n - 1):
        next_city = None
        min_distance = float('inf')

        for j in range(n):
            if not visited[j] and distance_matrix[current_city][j] < min_distance:
                min_distance = distance_matrix[current_city][j]
                next_city = j

        visited[next_city] = True
        path.append(next_city)
        total_distance += min_distance
        current_city = next_city

    # Kembali ke kota asal
    total_distance += distance_matrix[current_city][0]
    path.append(0)  # Kembali ke kota asal
    return path, total_distance

# Algoritma Brute Force
def brute_force_tsp(distance_matrix):
    n = len(distance_matrix)
    cities_indices = list(range(n))
    min_path = None
    min_distance = float('inf')

    for perm in itertools.permutations(cities_indices):
        current_distance = 0

        # Hitung jarak untuk rute ini
        for i in range(n):
            current_distance += distance_matrix[perm[i]][perm[(i + 1) % n]]

        if current_distance < min_distance:
            min_distance = current_distance
            min_path = perm

    # Mengubah indeks kembali ke nama kota
    min_path = list(min_path) + [min_path[0]]  # Kembali ke kota asal
    return min_path, min_distance

# Uji coba untuk berbagai ukuran input
def run_tests():
    sizes = [5, 10, 15, 20]  # Ukuran input yang akan diuji
    for n in sizes:
        print(f"\nTesting with {n} cities...")
        # Generate random distance matrix
        distance_matrix = generate_distance_matrix(n)

        # Uji algoritma Greedy
        print("Running Greedy TSP...")
        start_time = time.time()
        greedy_path, greedy_distance = greedy_tsp(distance_matrix)
        greedy_time = time.time() - start_time
        print(f"Greedy Path: {greedy_path}, Distance: {greedy_distance}, Time: {greedy_time:.6f} seconds")

        # Uji algoritma Brute Force
        print("\nRunning Brute Force TSP...")
        start_time = time.time()
        brute_force_path, brute_force_distance = brute_force_tsp(distance_matrix)
        brute_force_time = time.time() - start_time
        print(f"Brute Force Path: {brute_force_path}, Distance: {brute_force_distance}, Time: {brute_force_time:.6f} seconds")

# Jalankan uji coba
run_tests()
