import jwt
from functools import wraps
from flask import request, jsonify
from config import JWT_SECRET_KEY  # Importamos la clave secreta

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        #eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTc1MDYxNjI2OSwianRpIjoiMWRmYzVkZWMtYjI3MS00N2JlLWIwMzQtNDg1OTQ1MTNkYjg3IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6NSwibmJmIjoxNzUwNjE2MjY5LCJjc3JmIjoiMzJlNTAzOGItYzIwMC00NDUzLTg5NTctODViYTM1ZDYzOGQ2IiwiZXhwIjoxNzUwNjE3MTY5fQ.2FfCScFQRsg7NQCedlX84ltRizE3OgXf0zJoOysb5GU

        if 'Authorization' in request.headers:
            auth_header = request.headers['Authorization']
            if auth_header.startswith("Bearer "):
                token = auth_header.split(" ")[1]
                print(token)
            else:
                return jsonify({'message': 'Formato de token inválido'}), 401


        if not token:
            return jsonify({'message': 'Token faltante'}), 401

        try:
            # Aquí decodificamos el token usando la clave secreta
            data = jwt.decode(token, JWT_SECRET_KEY, algorithms=["HS256"])
            print("Payload:", data)

            # Puedes acceder a `data['usuario']` u otro payload aquí si lo usaste
        except jwt.ExpiredSignatureError:
            return jsonify({'message': 'Token expirado'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'message': 'Token inválido'}), 403

        return f(*args, **kwargs)

    return decorated
