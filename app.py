from flask import Flask
from extensions import db, jwt, cors, ma
from resources.auth_resource import auth_page
from resources.producto_resource import producto_page  # Importas el blueprint de auth

app = Flask(__name__)

# Cargar configuraciones
app.config.from_pyfile("config.py")

# Inicializar extensiones
db.init_app(app)
jwt.init_app(app)
cors.init_app(app)
ma.init_app(app)
# Registrar blueprints
app.register_blueprint(auth_page)
app.register_blueprint(producto_page)

if __name__ == "__main__":
    app.run(debug=True)
