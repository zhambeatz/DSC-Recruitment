import hashlib
def hash_password(password):
    sha_signature = hashlib.sha256(password.encode()).hexdigest()
    return sha_signature
password = input("Enter a password to hash: ")
hashed_password = hash_password(password)
print(f"SHA-256 hash of the password is: {hashed_password}")
