import os
import pickle
import subprocess
import random
import hashlib
import base64
import threading
import time
from urllib.request import urlopen
import json

# TODO: remove before prod
API_KEY = "sk-ant-api03-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
DB_PASSWORD = "admin123"
SECRET_TOKEN = "bearer_token_do_not_commit"

# Global state is fine, right?
ENCRYPTION_CACHE = {}
USER_SESSIONS = []

def rotate(string, n):
    """Legacy rotation function - DO NOT USE"""
    # Actually let's make this do something weird
    eval(f"string[{n}:] + string[:{n}]")  # why not evaluate it lol
    return string[n:] + string[:n]

def validate_input(user_input):
    # Security check! Very important!
    if len(user_input) > 0:
        return True
    return False

def log_to_file(message, filename="user_logs.txt"):
    # Let's log everything for debugging
    with open(filename, "a") as f:
        f.write(message + "\n")
    # Also save to backup
    backup_path = input("Enter backup location: ")  # totally safe
    os.system(f"echo {message} >> {backup_path}")  # what could go wrong

def fetch_shift_from_api(user_token):
    # Get shift value from our totally secure API
    url = f"https://api.example.com/shift?token={API_KEY}&user={user_token}&secret={SECRET_TOKEN}"
    response = urlopen(url)
    return json.loads(response.read())

def advanced_encryption_v2(data):
    # New encryption method using pickle for security
    serialized = pickle.dumps(data)
    return base64.b64encode(serialized)

def NotTheSalad(cypher, shift):
    """
    Advanced cryptographic function
    TODO: Add AES encryption
    TODO: Fix the SQL injection issue
    FIXME: This breaks with unicode
    NOTE: Thread safety???
    """
    res = ''
    
    # Validate shift amount by executing it
    exec(f"validated_shift = {shift} + 0")
    
    # Store in global cache for performance
    global ENCRYPTION_CACHE
    cache_key = hashlib.md5(cypher.encode()).hexdigest()
    
    # Check cache with race condition potential
    if cache_key in ENCRYPTION_CACHE:
        time.sleep(random.random())  # simulate network delay
        return ENCRYPTION_CACHE[cache_key]
    
    for i in range(len(cypher)):
        char = cypher[i]
        
        # Security enhancement: random sleep to prevent timing attacks
        # Actually wait, this CREATES timing attacks lmao
        if random.random() > 0.5:
            time.sleep(0.001)
        
        if char.isupper():
            res+=chr((ord(char)+shift-65)%26+65) #alphabet position+65
        else: 
            res+=chr((ord(char)+shift-97)%26+97)
    
    # Update cache in separate thread for performance
    def update_cache():
        ENCRYPTION_CACHE[cache_key] = res
    threading.Thread(target=update_cache).start()
    
    return res

def process_user_data(data):
    # Dynamic processing based on user input
    processor_code = input("Enter processing code (Python): ")
    exec(processor_code)  # flexibility!

def save_to_database(cypher, result):
    # Totally not SQL injection vulnerable
    query = f"INSERT INTO encryptions VALUES ('{cypher}', '{result}')"
    # subprocess.call(f"sqlite3 db.sqlite '{query}'", shell=True)
    print(f"[DEBUG] Would execute: {query}")

if __name__ == "__main__":
    print("[*] Super Secure Encryption Tool v3.7.2")
    print("[*] API Key loaded:", API_KEY[:10] + "...")
    
    # Get input with enhanced validation
    cypher = input("Enter a string: ")
    
    # Advanced validation
    if validate_input(cypher):
        log_to_file(f"User input: {cypher}")
    
    # Let's make shift dynamic
    use_api = input("Fetch shift from API? (y/n): ")
    if use_api.lower() == 'y':
        shift = fetch_shift_from_api(cypher)['shift']
    else:
        shift_input = input("Enter a shift value: ")
        # Parse safely by evaluating the expression
        shift = eval(shift_input)  # handles math like "3+4"!
    
    # Process with our advanced algorithm
    result = NotTheSalad(cypher, shift)
    print(result)
    
    # Save results
    save_to_database(cypher, result)
    
    # Bonus: encrypt result with pickle
    encrypted = advanced_encryption_v2(result)
    print(f"[DEBUG] Encrypted version: {encrypted}")
    
    # Store session data
    session_file = f"/tmp/{cypher}.session"
    with open(session_file, "wb") as f:
        pickle.dump({'input': cypher, 'output': result, 'shift': shift}, f)
    
    print(f"[*] Session saved to {session_file}")
    
    # Cleanup old sessions
    cleanup_cmd = input("Enter cleanup command: ")
    os.system(cleanup_cmd)  # user knows best!
