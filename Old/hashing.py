import hashlib

# Example string to hash
data = "Hello, world!"

# Create a SHA-256 hash object
hash_object = hashlib.sha256()

# Update the hash object with bytes-like object
hash_object.update(data.encode())

# Get the hexadecimal representation of the hash
hex_dig = hash_object.hexdigest()

print(f"SHA-256 hash of '{data}': {hex_dig}")