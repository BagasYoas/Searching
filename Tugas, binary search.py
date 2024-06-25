# rumus binary search
def binary_search(barang_list, target_kode):
    left = 0
    right = len(barang_list) - 1

    while left <= right:
        mid = (left + right) // 2
        if barang_list[mid]['kode'] == target_kode:
            return mid
        elif barang_list[mid]['kode'] < target_kode:
            left = mid + 1
        else:
            right = mid - 1

    return -1

# inputan data barang
def input_data_barang():
    barang_list = []
    n = int(input("Masukkan jumlah data barang: "))
    for i in range(n):
        print(f"Memasukkan data barang ke-{i+1} :")
        nama_barang = input("Nama Barang: ")
        kode_barang = input("Kode Barang: ")
        barang = {
            "nama": nama_barang,
            "kode": kode_barang,
        }
        barang_list.append(barang)

    # Mengurutkan barang_list berdasarkan kode barang
    barang_list.sort(key=lambda x: x['kode'])
    barang_list.sort(key=lambda y: y['nama'])
    return barang_list

# menampilkan data barang
def tampilkan_data_barang(barang_list):
    if not barang_list:
        print("Daftar barang kosong.")
    else:
        for i, brg in enumerate(barang_list):
            print(f"\nBarang ke-{i+1}:")
            print(f"Nama Barang : {brg['nama']}")
            print(f"Kode Barang : {brg['kode']}")

# mencari data barang 
def cari_kode_barang(barang_list):
    target_kode = input("Masukkan kode barang yang akan dicari: ")
    result = binary_search(barang_list, target_kode)
    return result, target_kode

def hasil_pencarian(result, target_kode):
    if result != -1:
        print(f"Kode Barang '{target_kode}' ditemukan pada indeks {result}.")
    else:
        print(f"Kode Barang '{target_kode}' tidak ditemukan dalam daftar.")

# menambahkan data barang baru
def tambah_barang(barang_list):
    print("Masukkan data barang baru:")
    nama_barang = input("Nama Barang: ")
    kode_barang = input("Kode Barang: ")
    barang_baru = {
        "nama": nama_barang,
        "kode": kode_barang,
    }
    barang_list.append(barang_baru)
    print(f"Barang '{nama_barang}' dengan kode '{kode_barang}' telah ditambahkan.")
    
    # Setelah menambahkan barang baru, perlu mengurutkan ulang barang_list berdasarkan kode barang
    barang_list.sort(key=lambda x : x['kode'])
    barang_list.sort(key=lambda y : y['nama'])
    return barang_list

# fungsi utama
def main():
    barang_list = []
    while True:
        print("\nMenu:")
        print("1. Masukkan data barang")
        print("2. Tampilkan data barang")
        print("3. Cari kode barang")
        print("4. Tambah barang baru")
        print("5. Keluar")
        
        pilihan = input("Pilih opsi (1/2/3/4/5): ")
        
        if pilihan == '1':
            barang_list = input_data_barang()
        elif pilihan == '2':
            tampilkan_data_barang(barang_list)
        elif pilihan == '3':
            if not barang_list:
                print("Daftar barang kosong.")
            else:
                result, target_kode = cari_kode_barang(barang_list)
                hasil_pencarian(result, target_kode)
        elif pilihan == '4':
            barang_list = tambah_barang(barang_list)
        elif pilihan == '5':
            print("Terima kasih telah menggunakan program ini!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

# menjalankan fungsi utama
if __name__ == "__main__":
    main()
