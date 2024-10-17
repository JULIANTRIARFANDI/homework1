def membeli_motor():
    print("Mulai")
    print("aerox = 26000")
    print("beat = 16000")
    print("r 15 = 27000")
    print("vario = 23000")
    
    anggaran = input("Tentukan anggaran untuk membeli motor: ")
    
    print("Cari merek motor... : " ,"aerox","beat" , "r 15" , "vario")
    merek_motor = input("Apakah merek motor yang Anda inginkan tersedia? (ya/tidak): ")
    
    if merek_motor == "ya":

        print("Tentukan tipe motor...")
        tipe_motor = input("Apakah tipe motor yang Anda inginkan tersedia? (ya/tidak): ")
        
        if tipe_motor == "ya":

            print("Cek spesifikasi motor...")
            spesifikasi = input("Apakah spesifikasi sesuai? (ya/tidak): ")
            
            if spesifikasi == "ya":
                print("Lakukan test ride...")
                puas_test_ride = input("Apakah Anda puas dengan test ride? (ya/tidak): ")
                print("puas_test_ride")
                if puas_test_ride == "ya":
                    print("Beli motor!")
                else:
                    print("Cari tipe motor lain.")
            else:
                print("Cari tipe motor lain.")
        else:
            print("Cari tipe motor lain.")
    else:
        print("Cari merek motor lain.")
    
    print("Selesai")

# Menjalankan fungsi membeli motor
membeli_motor()
