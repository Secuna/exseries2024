#!/usr/bin/python2
import random
import sqlite3

def generate_OTP():
    return str(random.randint(100000, 999999))

def create_database():
    conn = sqlite3.connect(':memory:')
    c = conn.cursor()
    c.execute('''CREATE TABLE users
                 (username TEXT, password TEXT)''')
    users = [
        ('alice', 'password123'),
        ('bob', 'securepass'),
        ('charlie', 'letmein')
    ]
    c.executemany('INSERT INTO users VALUES (?,?)', users)
    conn.commit()
    return conn

def login_2fa_verify(username, password):
    conn = create_database()
    c = conn.cursor()
    c.execute('SELECT * FROM users WHERE username=? AND password=?', (username, password))
    user = c.fetchone()
    conn.close()
    if user:
        generated_OTP = generate_OTP()
        input_otp = input("Provide OTP for user: ")
        if input_otp == generated_OTP:
            return True
    return False

# Sample usage
username = raw_input("Enter username: ")
password = raw_input("Enter password: ")

if login_2fa_verify(username, password):
    print("Login successful!")
else:
    print("Incorrect OTP or user not found. Login failed.")