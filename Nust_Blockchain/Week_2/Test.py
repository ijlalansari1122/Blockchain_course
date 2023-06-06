import hashlib


File_name =('./Lab5.pdf')


with open(File_name, "rb") as file:
    file_data = file.read()


Size_BLOCK = len(file_data) // 8
blocks = [file_data[i:i+Size_BLOCK] for i in range(0, len(file_data), Size_BLOCK)]


hashes = [hashlib.sha256(block).hexdigest() for block in blocks]


values = hashes.copy()

while len(values) > 1:
    Data_array = []
    for i in range(0, len(values), 2):
        if i+1 < len(values):
            Total_HASH = values[i] + values[i+1]

            hashed_value= Total_HASH.encode()

            Data_array.append(hashlib.sha256(hashed_value).hexdigest())
        else:
            Data_array.append(values[i])
    values = Data_array


Main_MERKLE = values[0]
print("The RootMerkle is :", Main_MERKLE)
