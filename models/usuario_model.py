from extensions import db

class Usuario(db.Model):

    __tablename__ = "cuentas"

    id= db.Column(db.Integer,primary_key=True)
    nombre_usuario = db.Column(db.String(30),nullable =False)
    password = db.Column(db.String(30),nullable =False)
    correo_electronico = db.Column(db.String(50),nullable =False) 

    def to_dict(self):
        return {

            "id": self.id,
            "nombre_usuario": self.nombre_usuario,
            "password": self.password,
            "correo_electronico": self.correo_electronico,

        }