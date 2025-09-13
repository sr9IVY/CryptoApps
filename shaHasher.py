import hashlib

def hash_string(input_string):
    return hashlib.sha256(input_string.encode()).hexdigest()

def hash_file(file_path):
    sha256 = hashlib.sha256()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            sha256.update(chunk)
    return sha256.hexdigest()

if __name__ == "__main__":
    print("String hash:", hash_string("hello world"))
    print("File hash:", hash_file("sample.txt"))
