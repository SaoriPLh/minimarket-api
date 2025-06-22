from models.usuario_model import Usuario
from extensions import db
from utils.security import hash_password
class UsuarioRepo:
    
    @staticmethod
    def createUser(nombre_usuario, password, correo_electronico):
        if Usuario.query.filter_by(nombre_usuario=nombre_usuario).first():
            return None  # Usuario ya existe

        hashed_password = hash_password(password)
        nuevo_usuario = Usuario(
            nombre_usuario=nombre_usuario,
            password=hashed_password,
            correo_electronico=correo_electronico
        )
        db.session.add(nuevo_usuario)
        db.session.commit()
        return nuevo_usuario

    @staticmethod
    def find_by_username(nombre_usuario:str):
        # Buscar un usuario por su nombre de usuario
        return Usuario.query.filter_by(nombre_usuario=nombre_usuario).first()
