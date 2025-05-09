data = list(map(int,input("Masukkan sembarang angka anda: ").split()))

n = len(data)
for i in range(n):
    for j in range(0, n - i - 1):
        if data[j] < data[j + 1]:
            data[j], data[j + 1] = data[j + 1], data[j]  # tukar posisi


# Binary Search
def binary_search(data, target):
    low = 0
    high = len(data) - 1

    while low <= high:
        mid = (low + high) // 2
        if data[mid] == target:
            return mid
        elif data[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
            
    return -1

target = 3

pilihan = int(input("Apa yang ingin kamu cari? 1 untuk sort dan kalau bukan 2: "))
if pilihan == 1:
    hasil = binary_search(data, target)
    if hasil != -1:
        print(f"Data ditemukan di index ke-{hasil}")
    else:
        print("Data tidak ditemukan")
else:
    print("Data setelah diurutkan:", data)


