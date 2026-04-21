"""
Project Title : EduCredChain
Description   : Blockchain-Based Certificate Verification System

File Name     : SQL_ECC.py
Description   : Database module managing certificate storage with SQLite and RSA encryption/decryption for secure data handling

Author(s)     : ABHIRAM_S, AMARNATH MOHAN, MOHAMMED YASEEN

Last Modified : 18-04-2026
"""

import sqlite3
import os
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes, serialization
import base64


class Sql_db:
    def __init__(self, db_path=None):
        if db_path is None:
            db_path = os.path.join(os.path.dirname(__file__), "database/certificates.db")

        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()

        # Debug: show exact DB file being used
        self.cursor.execute("PRAGMA database_list;")
        print("DB in use:", self.cursor.fetchall())

        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS records(
                Certificate_No VARCHAR(11) PRIMARY KEY,
                Name VARCHAR(30),
                Course_ID VARCHAR(5),
                Issue_Date DATE,
                Grade INTEGER,
                Hash VARCHAR(32)
            )
            """
        )
        self.conn.commit()

    def add_record(self, data):
        """
        data = (Certificate_No, Name, Course_ID, Issue_Date, Grade, Hash)
        """
        cert_no, name, course_id, issue_date, grade, hash_val = data

        name_enc = self.rsa_encrypt(name)
        course_enc = self.rsa_encrypt(course_id)
        grade_enc = self.rsa_encrypt(grade)

        self.cursor.execute(
            """
            INSERT INTO records (Certificate_No, Name, Course_ID, Issue_Date, Grade, Hash)
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (cert_no, name_enc, course_enc, issue_date, grade_enc, hash_val)
        )
        self.conn.commit()


    def select_record(self, cert_no):
        self.cursor.execute(
            "SELECT * FROM records WHERE Certificate_No = ?",
            (cert_no,)  
        )
        row = self.cursor.fetchone()
        if row:
            cert_no, name, course_id, issue_date, grade, hash_val = row

            name = self.rsa_decrypt(name)
            course_id = self.rsa_decrypt(course_id)
            grade = self.rsa_decrypt(grade)

            return (cert_no, name, course_id, issue_date, grade, hash_val)  
        
        return None
    
    def view_records(self):
        self.cursor.execute("SELECT COUNT(*) FROM records")
        print("Row count:", self.cursor.fetchone()[0])

        self.cursor.execute("SELECT * FROM records")
        rows = self.cursor.fetchall()
        for i in rows:
             print(i)
        return rows
    
    def delete_record(self, cert_no):
        self.cursor.execute(
            "DELETE FROM records WHERE Certificate_No = ?",
            (str(cert_no),)
        )
        self.conn.commit()
        return self.cursor.rowcount > 0

    def close(self):
            self.conn.close()


    


    def rsa_encrypt(self,data):
        key_path = os.path.join(os.path.dirname(__file__), "key", "public.pem")
        with open(key_path, "rb") as f:
            public_key = serialization.load_pem_public_key(f.read())

        encrypted = public_key.encrypt(
            data.encode(),
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )

        return base64.b64encode(encrypted).decode()
    
    def rsa_decrypt(self,data):

        # Load private key from file
        key_path = os.path.join(os.path.dirname(__file__), "key", "private.pem")
        with open(key_path, "rb") as f:
            private_key = serialization.load_pem_private_key(
                f.read(),
                password=None
            )

        decrypted = private_key.decrypt(
            base64.b64decode(data),
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )

        return decrypted.decode()
