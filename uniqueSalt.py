import secrets
import time

# Generate a random 8-byte (64-bit) value
random_value = secrets.token_bytes(8)

# Get the current timestamp (time since epoch in seconds)
timestamp = int(time.time())

# Combine the random value and timestamp as the salt
salt = random_value + timestamp.to_bytes(8, 'big')

# Print salt
print(salt)
