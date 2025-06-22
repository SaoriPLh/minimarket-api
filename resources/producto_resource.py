from flask import Blueprint, request, jsonify
from marshmallow import ValidationError
from schemas.producto.schema import ProductoRequestSchema
from repositoris.producto_repo import ProductoRepositorio

producto_page = Blueprint("productos",__name__,url_prefix="/productos")

@producto_page.route("/crearProducto", methods="POST")
def crearProducto():
    try:
        producto_data = ProductoRequestSchema.load(request.json)
    except ValidationError as err:
        return jsonify({"Error": err.messages}),400
    
    