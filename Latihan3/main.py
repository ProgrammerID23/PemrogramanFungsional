# Data list yang sama seperti kegiatan 1 modul 1
data_list = [3.1, 1, 0, 'Hello', 2.7, 'Python', 5.5, 7.3, 'world', 'AI',747,875,101]

# Fungsi untuk memisahkan nilai float, int, dan string
def filter_data(data):
    float_data = list(filter(lambda x: isinstance(x, float), data))
    int_data = list(filter(lambda x: isinstance(x, int), data))
    str_data = list(filter(lambda x: isinstance(x, str), data))
    return float_data, int_data, str_data

# Fungsi untuk memetakan nilai int menjadi ratusan, puluhan, dan satuan
def map_int_data(data):
    int_mapping = []
    for num in data:
        if isinstance(num, int):
            satuan = num % 10
            puluhan = (num // 10) % 10
            ratusan = num // 100
            int_mapping.append({'ratusan': ratusan, 'puluhan': puluhan, 'satuan': satuan})
    return int_mapping

# Memisahkan dan memetakan data
float_data, int_data, str_data = filter_data(data_list)
int_mapping = map_int_data(int_data)

# Menampilkan hasil sesuai format yang diinginkan
print("Data Float:")
print(float_data)

print("Data Int:")
for item in int_mapping:
    print(item)

print("Data String:")
print(str_data)