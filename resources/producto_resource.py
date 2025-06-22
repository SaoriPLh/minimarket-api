from flask import Blueprint, request, jsonify
from marshmallow import ValidationError
from schemas.producto_schema import ProductoRequestSchema
from flask_jwt_extended import jwt_required, get_jwt_identity
producto_page = Blueprint("productos", __name__, url_prefix="/productos")
from repositoris.producto_repo import ProductoRepositorio

@producto_page.route("/crearProducto", methods=["POST"])
@jwt_required()
def crearProducto():
    try:
        # Validar datos con marshmallow
        producto_data = ProductoRequestSchema().load(request.json)

        # Llamar al repositorio para crear el producto
        response = ProductoRepositorio.crear_producto(producto_data)

        if response:
            return jsonify({"Message": "Producto creado correctamente"}), 200
        else:
            return jsonify({"Error": "No se pudo crear el producto"}), 500

    except ValidationError as err:
        return jsonify({"Error": err.messages}), 400
