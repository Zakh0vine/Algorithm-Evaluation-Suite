import itertools
import numpy as np
import time
import matplotlib.pyplot as plt

# Fungsi untuk menghasilkan matriks jarak acak
def generate_distance_matrix(n):
    # Membuat matriks jarak acak
    matrix = np.random.randint(1, 10, size=(n, n))
    np.fill_diagonal(matrix, 0)  # Jarak ke diri sendiri adalah 0
    return matrix
# Algoritma Backtracking
def backtracking_tsp(distance_matrix):
    n = len(distance_matrix)
    visited = [False] * n
    best_distance = float('inf')
    best_path = []

    def dfs(current_city, count, current_distance, path):
        nonlocal best_distance, best_path

        # Jika semua kota sudah dikunjungi dan kembali ke kota asal
        if count == n and distance_matrix[current_city][0] > 0:
            total_distance = current_distance + distance_matrix[current_city][0]
            if total_distance < best_distance:
                best_distance = total_distance
                best_path = path + [0]
            return

        # Jelajahi semua kota yang belum dikunjungi
        for next_city in range(n):
            if not visited[next_city] and distance_matrix[current_city][next_city] > 0:
                visited[next_city] = True
                dfs(next_city, count + 1, current_distance + distance_matrix[current_city][next_city], path + [next_city])
                visited[next_city] = False

    visited[0] = True  # Mulai dari kota pertama
    dfs(0, 1, 0, [0])

    return best_path, best_distance

# Algoritma Dynamic Programming (Held-Karp)
def dp_tsp(distance_matrix):
    n = len(distance_matrix)
    # Mask state, starting point
    memo = [[None] * n for _ in range(1 << n)]

    def tsp(mask, pos):
        # Jika semua kota telah dikunjungi, kembali ke kota awal
        if mask == (1 << n) - 1:
            return distance_matrix[pos][0] if distance_matrix[pos][0] > 0 else float('inf')

        if memo[mask][pos] is not None:
            return memo[mask][pos]

        ans = float('inf')
        for city in range(n):
            if mask & (1 << city) == 0 and distance_matrix[pos][city] > 0:
                ans = min(
                    ans,
                    distance_matrix[pos][city] + tsp(mask | (1 << city), city)
                )
        memo[mask][pos] = ans
        return ans

    # Rekonstruksi jalur
    def reconstruct_path():
        path = []
        mask = 1
        pos = 0
        while mask != (1 << n) - 1:
            path.append(pos)
            next_city = None
            for city in range(n):
                if mask & (1 << city) == 0 and distance_matrix[pos][city] > 0:
                    if tsp(mask | (1 << city), city) + distance_matrix[pos][city] == memo[mask][pos]:
                        next_city = city
                        break
            pos = next_city
            mask |= (1 << pos)
        path.append(pos)
        path.append(0)  # Kembali ke kota asal
        return path

    total_distance = tsp(1, 0)
    path = reconstruct_path()
    return path, total_distance

# Uji coba untuk berbagai ukuran input
def run_tests():
    sizes = [3, 6, 9, 11, 12]  # Ukuran input yang akan diuji
    backtracking_times = []  # Store Backtracking times
    dp_times = []  # Store Dynamic Programming times

    for n in sizes:
        print(f"\nTesting with {n} cities...")

        # Generate random distance matrix
        distance_matrix = generate_distance_matrix(n)

        # Uji algoritma Backtracking
        print("\nRunning Backtracking TSP...")
        start_time = time.time()
        backtracking_path, backtracking_distance = backtracking_tsp(distance_matrix)
        backtracking_time = time.time() - start_time
        backtracking_times.append(backtracking_time)  # Store time
        print(f"Backtracking Path: {backtracking_path}, Distance: {backtracking_distance}, Time: {backtracking_time:.6f} seconds")

        # Uji algoritma Dynamic Programming
        print("\nRunning Dynamic Programming TSP...")
        start_time = time.time()
        dp_path, dp_distance = dp_tsp(distance_matrix)
        dp_time = time.time() - start_time
        dp_times.append(dp_time)  # Store time
        print(f"DP Path: {dp_path}, Distance: {dp_distance}, Time: {dp_time:.6f} seconds")

    # Grafik hasil
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, backtracking_times, label="Backtracking", marker='o')
    plt.plot(sizes, dp_times, label="Dynamic Programming", marker='s')
    plt.xlabel("Number of Cities")
    plt.ylabel("Execution Time (seconds)")
    plt.title("Execution Time vs. Number of Cities")
    plt.legend()
    plt.grid(True)
    plt.show()

# Jalankan uji coba
run_tests()
