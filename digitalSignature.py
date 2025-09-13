import subprocess

def generate_keys():
    subprocess.run(["openssl", "genpkey", "-algorithm", "RSA", "-out", "private_key.pem"])
    subprocess.run(["openssl", "rsa", "-pubout", "-in", "private_key.pem", "-out", "public_key.pem"])

def sign_file(file_path):
    subprocess.run(["openssl", "dgst", "-sha256", "-sign", "private_key.pem", "-out", "signature.bin", file_path])

def verify_signature(file_path):
    subprocess.run(["openssl", "dgst", "-sha256", "-verify", "public_key.pem", "-signature", "signature.bin", file_path])

if __name__ == "__main__":
    generate_keys()
    sign_file("sample.txt")
    verify_signature("sample.txt")
