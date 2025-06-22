from extensions import db

class Producto(db.Model):
    #definimos el nombre de la tabla: 
    __tablename__ = "productos"

    #Luego declaramos los atributos
    id = db.Column(db.Integer,primary_key=True) #identificador unico de cada registro
    nombre = db.Column(db.String(100), nullable=False) #para q no este vacio
    precio = db.Column(db.Double(10,2), nullable=False)
    image_url = db.Column(db.String(255), nullable=False) #para q no este vacio
    stock = db.Column(db.Integer,primary_key=True) 
    categoria = db.Column(db.String(50), nullable=False) 
 
    #metodo para convertirlo a diccionario el objeto
    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "precio": self.precio,
            "image_url": self.image_url,
            "stock": self.stock,
            "categoria": self.categoria
        }
