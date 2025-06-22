from models.producto_model import Producto
from extensions import db

class ProductoRepositorio:
    def crear_producto(self, data: dict): #nos llegara el producto schema
        nuevo_producto = Producto(        # vamos a sacar la data contruyendolo en un producto
            nombre=data["nombre"],
            precio=data["precio"],
            image_url=data["image_url"],
            stock=data["stock"],
            categoria=data["categoria"]
        )
        db.session.add(nuevo_producto)
        db.session.commit()
        return nuevo_producto
