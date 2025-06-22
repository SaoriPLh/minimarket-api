from models.usuario_model import Usuario
from extensions import db
from utils.security import hash_password, verify_password


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
    def find_by_username(nombre_usuario: str):
        """Buscar un usuario por su nombre de usuario"""
        return Usuario.query.filter_by(nombre_usuario=nombre_usuario).first()

    @staticmethod
    def verify_user(nombre_usuario: str, plain_password: str):
        """Verifica si un usuario y contraseña son válidos"""
        usuario = UsuarioRepo.find_by_username(nombre_usuario)
        if usuario and verify_password(plain_password, usuario.password):
            return usuario
        return None

    @staticmethod
    def get_all():
        """Devuelve todos los usuarios"""
        return Usuario.query.all()

    @staticmethod
    def get_by_id(user_id: int):
        """Buscar usuario por ID"""
        return Usuario.query.get(user_id)

    @staticmethod
    def update_user(user_id: int, data: dict):
        """Actualizar los datos del usuario"""
        usuario = Usuario.query.get(user_id)
        if not usuario:
            return None

        usuario.nombre_usuario = data.get('nombre_usuario', usuario.nombre_usuario)
        usuario.correo_electronico = data.get('correo_electronico', usuario.correo_electronico)

        # Actualiza la contraseña si viene en los datos
        if 'password' in data:
            usuario.password = hash_password(data['password'])

        db.session.commit()
        return usuario

    @staticmethod
    def delete_user(user_id: int):
        """Eliminar usuario por ID"""
        usuario = Usuario.query.get(user_id)
        if not usuario:
            return False
        db.session.delete(usuario)
        db.session.commit()
        return True
