from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from flask_marshmallow import Marshmallow
#estamos creando instancias de las cosas q vamos necesitar en disintas partes del programa
#por ejemplo donde inicializamos la app vamos a vincular estas intancias con esa app
#revisar por que es mejor hacerlo asi ejemplos donde podemos de alguna manera aplicar este concepto
db = SQLAlchemy()
jwt= JWTManager()
cors = CORS()
ma = Marshmallow()