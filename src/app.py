from flask import Flask, jsonify, render_template
from flask_migrate import Migrate
from models import db, Role

from routes.roles import rolesRoutes

app = Flask(__name__)

# Configuracion de la Aplicacion
app.url_map.strict_slashes = False
app.config['DEBUG'] = True
app.config['ENV'] = 'development'

# Configuracion de la base de datos
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root@localhost:3306/blog"

# Configuracion de otros modulos

db.init_app(app) # vinculacion del archivo models con nuestra aplicacion
Migrate(app, db) # db init, db migrate, db upgrade, db downgrade


# Definicion de endpoints (rutas) de la aplicacion
@app.route('/') # metodo por defecto: GET
def root():
    return render_template('index.html')
    #return jsonify({ "message": "REST API Flask"}), 200


# CRUD (create, read, update, delete)
app.register_blueprint(rolesRoutes, url_prefix="/api")
'''
@app.route('/api/roles', methods=['GET']) # devuelve todos los roles en la base de datos
def listar_roles():
    roles = Role.query.all() # [<Role 1>, <Role 2>, ...<Role n>]
    roles = list(map(lambda role: role.serialize(), roles)) # {"id": 1, "name": "admin" }
    return jsonify(roles), 200

@app.route('/api/roles/store', methods=['POST'])
def guardar_roles():
    role = Role()
    role.name = "Messenger"
    role.save() 
    #db.session.add(role)
    #db.session.commit()
    return jsonify(role.serialize()), 201
'''

# Inicio de la aplicacion
if __name__ == '__main__':
    app.run()

'''

SQL /  NOSQL

ORM = Object Relationship Mapping (sqlalchemy, sequelize, typeorm. hibernate)

ODM = Object Document Mapping (mongoose)

'''