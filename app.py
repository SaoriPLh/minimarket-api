from flask import Flask
from extensions import db, jwt, cors
from resources.auth_resource import auth_page  # Importas el blueprint de auth

app = Flask(__name__)

# Cargar configuraciones
app.config.from_pyfile("config.py")

# Inicializar extensiones
db.init_app(app)
jwt.init_app(app)
cors.init_app(app)

# Registrar blueprints
app.register_blueprint(auth_page)

if __name__ == "__main__":
    app.run(debug=True)
