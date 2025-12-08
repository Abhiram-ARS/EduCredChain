from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64

class RSA_key:
    def genKeys():
        
        key = RSA.generate(2048)

        private_key = key.export_key()
        with open("key/private.pem", "wb") as f:
            f.write(private_key)

        public_key = key.publickey().export_key()
        with open("key/public.pem", "wb") as f:
            f.write(public_key)

        print("- Keys generated -")


class RSA_Funct:
    def rsa_encrypt(keyFile,pText):
    
        with open(keyFile, "rb") as f:
            public_key = RSA.import_key(f.read())

        cipher = PKCS1_OAEP.new(public_key)
        encrypted = cipher.encrypt(pText.encode())


        return base64.b64encode(encrypted).decode()


    def rsa_decrypt(keyFile,cText):
 
        with open("private.pem", "rb") as f:
            private_key = RSA.import_key(f.read())

        cipher = PKCS1_OAEP.new(private_key)
        ciphertext = base64.b64decode(cText)
        decrypted = cipher.decrypt(ciphertext)

        return decrypted.decode()


"""
a= RSA_Funct.rsa_encrypt("key/private.pem",'Secret')
b= RSA_Funct.rsa_decrypt("key/public.pem",a)
"""