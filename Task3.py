import hashlib

# Dictionary to store username: hashed_password
users = {}

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register(username, password):
    if username in users:
        print("User already exists!")
    else:
        users[username] = hash_password(password)
        print(f"Created new user: {username}")

def login(username, password):
    hashed = hash_password(password)
    if username in users and users[username] == hashed:
        print("Login Successful")
    else:
        print("Login Failed")

# Example usage:
register("john", "mypassword")   # Output: Created new user: john
login("john", "mypassword")      # Output: Login Successful
login("john", "wrongpassword")   # Output: Login Failed
register("john", "anotherpass")  # Output: User already exists!
