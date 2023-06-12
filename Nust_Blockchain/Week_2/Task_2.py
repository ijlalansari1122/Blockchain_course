import hashlib

# Text_file = cr



filename = "Message.txt"
with open(filename, "w") as file:
 file.write("Hello this is ijlal ansari and iam enrolled in High Impact course");





with open(filename, "rb") as file:
    file_contents = file.read()
    initial_hash = hashlib.sha256(file_contents).hexdigest()

print("Initial Hash is :", initial_hash)

# Modify the content of the file



with open(filename, "w") as file:
    file.write("Hello this is ijlal ansari")

# modified hash



with open(filename, "rb") as file:
    file_contents = file.read()
    modified_hash = hashlib.sha256(file_contents).hexdigest()

print("Modified Hash is ", modified_hash)
