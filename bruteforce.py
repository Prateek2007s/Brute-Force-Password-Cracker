import hashlib
import itertools
import string

# Banner
print("""
===========================================
Brute Force Password Cracker
Made by AntifiedNull (Prateek)
===========================================
""")

def hash_password(password, algorithm):
    """Hashes the given password using the specified algorithm"""
    if algorithm == 'md5':
        return hashlib.md5(password.encode()).hexdigest()
    elif algorithm == 'sha1':
        return hashlib.sha1(password.encode()).hexdigest()
    elif algorithm == 'sha256':
        return hashlib.sha256(password.encode()).hexdigest()
    else:
        print(f"Unsupported hash algorithm: {algorithm}")
        return None

def brute_force_attack(target_hash, algorithm='sha256', max_length=4, charset=None):
    """Brute forces the password by generating all possible combinations and comparing hashes"""
    if charset is None:
        charset = string.ascii_lowercase + string.digits  # Default charset (a-z, 0-9)

    attempts = 0
    for length in range(1, max_length + 1):  # Try increasing lengths
        for password_tuple in itertools.product(charset, repeat=length):
            password = ''.join(password_tuple)
            attempts += 1
            hashed_password = hash_password(password, algorithm)
            print(f"Trying: {password} -> {hashed_password}")
            
            if hashed_password == target_hash:
                print(f"[+] Password found: {password}")
                print(f"[+] Attempts: {attempts}")
                return password
    print("[!] Password not found within the given length range.")
    return None

if __name__ == "__main__":
    print("Welcome to the Brute Force Password Cracker")
    
    # Example usage
    algorithm = input("Enter hash algorithm (md5, sha1, sha256): ").lower()
    target_password = input("Enter the target password (for testing): ")
    
    # Hash the target password to simulate the attack
    target_hash = hash_password(target_password, algorithm)
    print(f"Target hash: {target_hash}")
    
    max_length = int(input("Enter the maximum password length: "))
    
    print("\nStarting brute-force attack...")
    brute_force_attack(target_hash, algorithm, max_length)
