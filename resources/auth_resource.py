from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from repositoris.usuario_repo import UsuarioRepo
from utils.security import verify_password
auth_page = Blueprint("auth", __name__, url_prefix="/auth")

@auth_page.route("/register", methods=["POST"])
def register():
    data = request.get_json()  # Deberías usar request.get_json() para recibir JSON
    nombre_usuario = data.get("nombre_usuario")
    password = data.get("password")
    correo_electronico = data.get("correo_electronico")

    # Crear usuario
    usuario = UsuarioRepo.createUser(nombre_usuario, password, correo_electronico)
    if not usuario:
        return jsonify({"MensajeError": "Error al crear el usuario"}), 400

    return jsonify({"Mensaje": "Usuario creado correctamente"}), 201


@auth_page.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    nombre_usuario = data.get("nombre_usuario")
    password = data.get("password")

    # Buscar usuario por nombre de usuario (asumiendo que la función buscará por nombre)
    usuario = UsuarioRepo.find_by_username(nombre_usuario)  # Aquí cambié find_by_email por find_by_username
    if not usuario or not verify_password(password, usuario.password):
        return jsonify({"MensajeError": "Nombre de usuario o contraseña incorrecta"}), 400

    # Crear el JWT
    access_token = create_access_token(identity=usuario.id)
    #aca creamos un fiuccionario con clave "acces_tyoken" y el valor de acces token
    return jsonify(access_token=access_token), 200
