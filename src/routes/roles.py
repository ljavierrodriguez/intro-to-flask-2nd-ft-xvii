from flask import Blueprint, jsonify
from models import Role

rolesRoutes = Blueprint('rolesRoutes', __name__)

@rolesRoutes.route('/roles', methods=['GET']) # devuelve todos los roles en la base de datos
def listar_roles():
    roles = Role.query.all() # [<Role 1>, <Role 2>, ...<Role n>]
    roles = list(map(lambda role: role.serialize(), roles)) # {"id": 1, "name": "admin" }
    return jsonify(roles), 200

@rolesRoutes.route('/roles/store', methods=['POST'])
def guardar_roles():
    role = Role()
    role.name = "Messenger"
    role.save() 
    #db.session.add(role)
    #db.session.commit()
    return jsonify(role.serialize()), 201


@rolesRoutes.route('/roles/<int:id>/update', methods=['PUT']) # devuelve todos los roles en la base de datos
def update_roles(id):
    role = Role.query.get(id) # [<Role 1>, <Role 2>, ...<Role n>]
    role.delete()
    return jsonify({ "msg": "Role deleted!"}), 200

@rolesRoutes.route('/roles/<int:id>/delete', methods=['DELETE']) # devuelve todos los roles en la base de datos
def delete_roles(id):
    role = Role.query.get(id) # [<Role 1>, <Role 2>, ...<Role n>]
    role.delete()
    return jsonify({ "msg": "Role deleted!"}), 200