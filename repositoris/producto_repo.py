from models.producto_model import Producto
from extensions import db

class ProductoRepositorio:
    #CRUD create, read, update, delete
    @staticmethod
    def crear_producto(data: dict): #nos llegara el producto schema
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
    
    @staticmethod
    def find_by_product_name(nombre_producto: str):
        """Buscar un prodcuto por su nombre de producto"""
        return Producto.query.filter_by(nombre=nombre_producto).first()
    @staticmethod
    def get_all():
        return Producto.query.all()  #devolvemos todos los productos 