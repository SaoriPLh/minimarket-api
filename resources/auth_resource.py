from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required
from repositoris.usuario_repo import UsuarioRepo
from utils.security import verify_password

auth_page = Blueprint("auth", __name__, url_prefix="/auth")


@auth_page.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    nombre_usuario = data.get("nombre_usuario")
    password = data.get("password")
    correo_electronico = data.get("correo_electronico")

    usuario = UsuarioRepo.createUser(nombre_usuario, password, correo_electronico)
    if not usuario:
        return jsonify({"MensajeError": "Usuario ya existe"}), 400

    return jsonify({"Mensaje": "Usuario creado correctamente"}), 201


@auth_page.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    print("DATA:", data)

    nombre_usuario = data.get("nombre_usuario")
    password = data.get("password")

    usuario = UsuarioRepo.find_by_username(nombre_usuario)
    if not usuario or not verify_password(password, usuario.password):
        return jsonify({"MensajeError": "Nombre de usuario o contraseña incorrecta"}), 400
    #aca decimos este token que vamos a crear representa este usaurio que es de usuario.id exige un string identity es sub en el payload
    access_token = create_access_token(identity=str(usuario.id))
    return jsonify(access_token=access_token), 200


#  Obtener todos los usuarios
@auth_page.route("/usuarios", methods=["GET"])
@jwt_required()
def get_all_users():
    usuarios = UsuarioRepo.get_all()
    return jsonify([u.to_dict() for u in usuarios]), 200


#  Obtener usuario por ID
@auth_page.route("/usuario/<int:id>", methods=["GET"])
@jwt_required()
def get_user(id):
    usuario = UsuarioRepo.get_by_id(id)
    if not usuario:
        return jsonify({"MensajeError": "Usuario no encontrado"}), 404
    return jsonify(usuario.to_dict()), 200


#  Actualizar 
@auth_page.route("/usuario/<int:id>", methods=["PUT"])
@jwt_required()
def update_user(id):
    data = request.get_json()
    usuario_actualizado = UsuarioRepo.update_user(id, data)
    if not usuario_actualizado:
        return jsonify({"MensajeError": "No se pudo actualizar"}), 400
    return jsonify(usuario_actualizado.to_dict()), 200


#elimninar
@auth_page.route("/usuario/<int:id>", methods=["DELETE"])
@jwt_required()
def delete_user(id):
    eliminado = UsuarioRepo.delete_user(id)
    if not eliminado:
        return jsonify({"MensajeError": "No se pudo eliminar"}), 400
    return jsonify({"Mensaje": "Usuario eliminado"}), 200
