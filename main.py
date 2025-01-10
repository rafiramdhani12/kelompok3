from module.calculator import calculator
from module.currency import currency_conversion
from module.geometry import geometry
from module.clear import clear
from utils.interface import main_interface


def main():
    while True:
        try:
            clear()
            main_interface()
            try:
                option = int(input("Masukan opsi yang anda ingin lakukan, pilih opsi [1]/[2]/[3] [0] untuk keluar : ")) 
                match option:
                    case 1:
                        calculator()
                    case 2:
                        currency_conversion()
                    case 3:
                        geometry()
                    case 0:
                        exit()
                    case _:
                        print("opsi yg anda masukkan tidak valid / tidak ada")
            except ValueError:
             print("value terdeteksi selain angka masukan input bertipe angka")
            
            
            opsi_lanjut = input("kamu telah kembali ke halaman utama apakah kamu ingin melanjutkan ? [Y/N]").upper()
            if opsi_lanjut == "N":
                        break
        except KeyboardInterrupt:
            print("\nanda telah keluar paksa dari proggram")
            break

print("proggram sudah selesai")

if __name__ == ("__main__"):
    main()
  