import hashlib

class Hash:

    def sha256_hash_gen(text):

        sha256_hash = hashlib.sha256(text.encode()).hexdigest()

        print("\nSHA-256 Hash:")
        print(sha256_hash)

"""
Hash.sha256_hash_gen("String")
"""