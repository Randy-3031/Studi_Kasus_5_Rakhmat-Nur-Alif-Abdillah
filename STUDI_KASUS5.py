def hitung_biaya_parkir(jenis_kendaraan, durasi_parkir):
    if jenis_kendaraan.lower() == "mobil":
        biaya = 5000
    elif jenis_kendaraan.lower() == "motor":
        biaya = 3000
    else:
        return None

    return biaya * durasi_parkir

jenis = input("Masukkan jenis kendaraan (Mobil/Motor): ")
jam_masuk = int(input("Masukkan jam masuk (0-24): "))
jam_keluar = int(input("Masukkan jam keluar (0-24): "))

lama_parkir = jam_keluar - jam_masuk
total = hitung_biaya_parkir(jenis, lama_parkir)

print("=== Struk Parkir ===")
if total is None:
    print("Jenis kendaraan tidak sesuai!")
else:
    print(f"Jenis Kendaraan : {jenis}")
    print(f"Jam Masuk : {jam_masuk}.00")
    print(f" Jam Keluar : {jam_keluar}.00")
    print(f"Lama Parkir : {lama_parkir} jam")
    print(f"Total Biaya : Rp{total}")