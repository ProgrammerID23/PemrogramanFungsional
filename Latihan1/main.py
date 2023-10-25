def konversi(minggu=0, hari=0, jam=0, menit=0, detik=0):
    total_menit = ((minggu * 7 * 24 * 60) + (hari * 24 * 60) + (jam * 60) + menit + detik / 60)
    return total_menit

if __name__ == '__main__':
    data = ["2minggu 3hari 5jam 33menit 5detik",
            "4minggu 3hari 8jam 40menit 10detik"]  # Contoh input dengan minggu, hari, jam, menit, dan detik

    data_list = []  # List untuk data
    hasil_konversi_list = []  # List untuk hasil konversi

    for item in data:
        minggu = 0
        hari = 0
        jam = 0
        menit = 0
        detik = 0

        parts = item.split()
        for part in parts:
            if 'minggu' in part:
                minggu = int(part.replace('minggu', ''))
            elif 'hari' in part:
                hari = int(part.replace('hari', ''))
            elif 'jam' in part:
                jam = int(part.replace('jam', ''))
            elif 'menit' in part:
                menit = int(part.replace('menit', ''))
            elif 'detik' in part:
                detik = int(part.replace('detik', ''))

        konvert = konversi(minggu, hari, jam, menit, detik)

        data_list.append(item)
        hasil_konversi_list.append(konvert)

    print("Data:")
    print(data_list)

    print("Hasil Konversi:")
    formatted_results = ["{:.2f}".format(result) for result in hasil_konversi_list]
    print(formatted_results)
