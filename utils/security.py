from werkzeug.security import generate_password_hash, check_password_hash

def hash_password(password: str) -> str:
    return generate_password_hash(password)
#recibe la contraseña recibida y la compara con su hasheo ya guardado
def verify_password(password_plain: str, password_hashed: str) -> bool:
    return check_password_hash(password_hashed, password_plain)