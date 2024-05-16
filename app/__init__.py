from flask import Flask
from config import SECRET_KEY
from flask_wtf.csrf import CSRFProtect

# Inititalisation de l'application Flask
app = Flask(__name__)

# mise en place du jeton d'accès (formulaire)
app.config['SECRET_KEY'] = SECRET_KEY

# Inititialisation de CSRFProtect pour la protection contre les attaques CSRF
csrf = CSRFProtect(app)

# Ajouter l'import des routes
from app.routes import other, task