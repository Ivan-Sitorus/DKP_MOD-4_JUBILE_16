#method harga kali banyak barang
class jual_beli:
    def harga_total(harga_satuan, jumlah_barang):
        return harga_satuan*jumlah_barang

    #fungsi tanpa kembalian berisi identitas kelompok 
def Identitas_kelompok():
    print("Kelompok 16")
    print("Shift 3")
    print("Jubile")
    print("Ivan")
    print("Raka")
    print("Louis")

  
#program main/untuk eksekusi
Identitas_kelompok()
objek=jual_beli
x="y"

  #perulangan berupa jumlah berapa kali transksi
while(x=="y"):

    #daftar barang
    print("1:Buku tulis")
    print("2:Pensil")
    print("3:Bolpoin")

    pilihan=int(input("masukan pilihan anda (1-3): "))
    jumlah_barang=int(input("Masukan jumlah barang yang akan dibeli: "))
    
    harga1=objek.harga_total(5000, jumlah_barang)
    harga2=objek.harga_total(2000, jumlah_barang)
    harga3=objek.harga_total(3000, jumlah_barang)
    harga_akhir=0

    if pilihan==1:
        print("Harga sementara : ", harga1)
        harga_akhir=harga_akhir+harga1
    elif pilihan==2:
        print("Harga sementara : ", harga2)
        harga_akhir=harga_akhir+harga2
    elif pilihan==3:
        print("Harga sementara : ", harga3)
        harga_akhir=harga_akhir+harga3
    else:
        print("input anda salah")

    x=input("Beli barang lain?(y=iya,selain itu dianggap tidak) ")  
  


print("Jumlah uang yang harus anda bayar: ", harga_akhir)
