import hashlib
 
 
def hash_password(password, algorithm='sha1'):
   """Hashes the given password using the specified algorithm."""
   if algorithm not in hashlib.algorithms_available:
       raise ValueError("Unsupported hashing algorithm.")
   hash_func = getattr(hashlib, algorithm)
   return hash_func(password.encode()).hexdigest()
 
 
def crack_password_hash(hash_to_crack, password_list_file):
   """Attempts to crack the given hash using passwords from the provided list."""
   with open(password_list_file, 'r') as f:
       for line in f:
           password = line.strip()
           hashed_password = hash_password(password)
           if hash_to_crack == hashed_password:
               return password
   return None
 
 
def main():
   user_hash = input("Enter the hash you want to crack: ").strip().lower()
   password_list_file = 'password-list.txt'  # Update with your password list file
 
 
   cracked_password = crack_password_hash(user_hash, password_list_file)
   if cracked_password:
       print(f"Password successfully cracked: {cracked_password}")
   else:
       print("Failed to crack the password.")
 
 
if __name__ == '__main__':
   main()
