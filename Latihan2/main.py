data = ["2minggu 3hari 5jam 33menit 5detik",
        "4minggu 3hari 8jam 40menit 10detik"]

data_integer = []

for item in data:
    integer_part = ""
    for char in item:
        if char.isnumeric():
            integer_part += char
        elif integer_part:
            data_integer.append(int(integer_part))
            integer_part = ""

# Mengatur data integer menjadi matriks (nested list)
num_rows = 2
num_columns = 5
matrix_data_integer = []

for i in range(num_rows):
    row = data_integer[i * num_columns:(i + 1) * num_columns]
    matrix_data_integer.append(row)

# Mencetak data dalam list dan matriks data integer dengan pemformatan yang lebih rapi
print("Data:")
for item in data:
    print(item)

print("\nData Integer:")
for row in matrix_data_integer:
    print(" ".join(map(str, row)))
