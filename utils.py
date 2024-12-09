import hmac
import hashlib

SECRET_KEY = "secret_key"

def generate_token(username):
    return hmac.new(SECRET_KEY.encode(), username.encode(), hashlib.sha256).hexdigest()

def verify_token(token, username):
    return hmac.compare_digest(token, generate_token(username))
