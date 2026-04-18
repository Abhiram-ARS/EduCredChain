import sqlite3
import os
import base64
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes, serialization


class Sql_db:

    def __init__(self):

        db_path = "certificates.db"

        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()

        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS records(
                Certificate_No TEXT PRIMARY KEY,
                Name TEXT,
                Course_ID TEXT,
                Issue_Date TEXT,
                Grade TEXT,
                Hash TEXT
            )
            """
        )

        self.conn.commit()


    def rsa_encrypt(self, data):

        with open("D:\Mini_Project\code\Backend\key\public.pem", "rb") as f:
            public_key = serialization.load_pem_public_key(f.read())

        encrypted = public_key.encrypt(
            str(data).encode(),
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )

        return base64.b64encode(encrypted).decode()


    def rsa_decrypt(self, data):

        with open("D:\Mini_Project\code\Backend\key\private.pem", "rb") as f:
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


    def add_record(self, data):

        cert_no, name, course_id, issue_date, grade, hash_val = data

        name = self.rsa_encrypt(name)
        course_id = self.rsa_encrypt(course_id)
        grade = self.rsa_encrypt(grade)

        self.cursor.execute(
            """
            INSERT INTO records
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (cert_no, name, course_id, issue_date, grade, hash_val)
        )

        self.conn.commit()


    def select_record(self, cert):

        self.cursor.execute(
            "SELECT * FROM records WHERE Certificate_No=?",
            (cert,)
        )

        row = self.cursor.fetchone()

        if row:

            cert_no, name, course, issue_date, grade, hash_val = row

            name = self.rsa_decrypt(name)
            course = self.rsa_decrypt(course)
            grade = self.rsa_decrypt(grade)

            return (cert_no, name, course, issue_date, grade, hash_val)

        return None


    def view_records(self):

        self.cursor.execute("SELECT * FROM records")
        rows = self.cursor.fetchall()

        for r in rows:

            cert_no, name, course, issue_date, grade, hash_val = r

            name = self.rsa_decrypt(name)
            course = self.rsa_decrypt(course)
            grade = self.rsa_decrypt(grade)

            print("\n---------------------------")
            print("Certificate No:", cert_no)
            print("Name:", name)
            print("Course:", course)
            print("Issue Date:", issue_date)
            print("Grade:", grade)
            print("Hash:", hash_val)


    def update_record(self, cert, name, course, date, grade, hash_val):

        name = self.rsa_encrypt(name)
        course = self.rsa_encrypt(course)
        grade = self.rsa_encrypt(grade)

        self.cursor.execute(
            """
            UPDATE records
            SET Name=?, Course_ID=?, Issue_Date=?, Grade=?, Hash=?
            WHERE Certificate_No=?
            """,
            (name, course, date, grade, hash_val, cert)
        )

        self.conn.commit()


    def delete_record(self, cert):

        self.cursor.execute(
            "DELETE FROM records WHERE Certificate_No=?",
            (cert,)
        )

        self.conn.commit()


    def close(self):

        self.conn.close()


def menu():

    db = Sql_db()

    while True:

        print("\n====== Certificate Database Manager ======")
        print("1. View Records")
        print("2. Search Record")
        print("3. Add Record")
        print("4. Edit Record")
        print("5. Delete Record")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":

            db.view_records()


        elif choice == "2":

            cert = input("Certificate No: ")

            r = db.select_record(cert)

            if r:
                print("\nRecord Found")
                print("Certificate No:", r[0])
                print("Name:", r[1])
                print("Course:", r[2])
                print("Issue Date:", r[3])
                print("Grade:", r[4])
                print("Hash:", r[5])
            else:
                print("Record not found")


        elif choice == "3":

            cert = input("Certificate No: ")
            name = input("Name: ")
            course = input("Course ID: ")
            date = input("Issue Date: ")
            grade = input("Grade: ")
            hash_val = input("Hash: ")

            db.add_record((cert, name, course, date, grade, hash_val))

            print("Record Added")


        elif choice == "4":

            cert = input("Certificate No to edit: ")

            r = db.select_record(cert)

            if not r:
                print("Record not found")
                continue

            print("Leave blank to keep old value")

            name = input(f"Name ({r[1]}): ") or r[1]
            course = input(f"Course ({r[2]}): ") or r[2]
            date = input(f"Issue Date ({r[3]}): ") or r[3]
            grade = input(f"Grade ({r[4]}): ") or r[4]
            hash_val = input(f"Hash ({r[5]}): ") or r[5]

            db.update_record(cert, name, course, date, grade, hash_val)

            print("Record Updated")


        elif choice == "5":

            cert = input("Certificate No to delete: ")

            db.delete_record(cert)

            print("Record Deleted")


        elif choice == "6":

            db.close()
            break


        else:

            print("Invalid choice")


if __name__ == "__main__":

    menu()