class Pasien:
    def __init__(self, nama, nohp, alamat, penanggung):
        self.nama = nama
        self.nohp = nohp
        self.alamat = alamat
        self.penanggung = penanggung

class AntrianRS:
    def __init__(self):
        self.antrian = []

    def tambah_antrian(self):
        nama = input("Masukkan nama pasien: ")
        nohp = input("Masukkan nomor HP pasien: ")
        alamat = input("Masukkan alamat pasien: ")
        penanggung = input("Masukkan penanggung pasien (BPJS/UMUM): ")
        pasien = Pasien(nama, nohp, alamat, penanggung)
        self.antrian.append(pasien)
        print("Pasien", pasien.nama, "telah ditambahkan ke dalam antrian.")

    def panggil_antrian(self):
        if len(self.antrian) > 0:
            pasien = self.antrian.pop(0)
            print("Nomor antrian terpanggil: ", pasien.nama)
        else:
            print("Tidak ada antrian saat ini.")

    def tampilkan_antrian(self):
        if len(self.antrian) > 0:
            print("Daftar Antrian RS:")
            for i, pasien in enumerate(self.antrian):
                print("No.", i+1)
                print("Nama Pasien:", pasien.nama)
                print("Nomor HP Pasien:", pasien.nohp)
                print("Alamat Pasien:", pasien.alamat)
                print("Penanggung Pasien:", pasien.penanggung)
                print()
        else:
            print("Tidak ada antrian saat ini.")

def main():
    antrian_rs = AntrianRS()

    while True:
        print("Menu:")
        print("1. Tambah Antrian")
        print("2. Panggil Antrian")
        print("3. Tampilkan Antrian")
        print("0. Keluar")

        pilihan = input("Masukkan pilihan Anda: ")

        if pilihan == "1":
            antrian_rs.tambah_antrian()
        elif pilihan == "2":
            antrian_rs.panggil_antrian()
        elif pilihan == "3":
            antrian_rs.tampilkan_antrian()
        elif pilihan == "0":
            print("Terima kasih telah menggunakan program Antrian RS.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == '__main__':
    main()
