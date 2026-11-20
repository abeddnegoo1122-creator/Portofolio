#date and time.py latihan

import datetime as dt
now = dt.datetime.now()
print("Current date and time:", now)
print(f'Day: {now:%a}')

nama=str(input("masukkan nama anda: "))
print(f'hallo, {nama}! selamat datang di program hitung umur.')
print(f'kini tanggal dan waktu saat ini adalah: {now:%d-%m-%Y %H:%M:%S}')
print("\nmasukkan tanggal lahir anda")
tanggal = int(input("tanggal (1-31)\t: "))
bulan = int(input("bulan (1-12)\t: "))
tahun = int(input("tahun (misal 1990): "))

tanggal_lahir = dt.datetime(tahun, bulan, tanggal)
print(f"anda lahir pada hari:, {tanggal_lahir}")
print(f'anda lahir pada hari: {tanggal_lahir:%A}')

umur = now - tanggal_lahir
umur_tahun = umur.days // 365
print(f'anda berumur: {umur_tahun} tahun')
umur_bulan = (umur.days % 365) // 30
print(f'anda berumur: {umur_bulan} bulan')
umur_hari = (umur.days % 365) % 30
print(f'anda berumur: {umur_hari} hari')
if tanggal_lahir == now:
    print('selamat ulang tahun!')
else:
    print('selamat hari biasa untukmu kawan!')