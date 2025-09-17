from flask import Blueprint, request, jsonify
from netvac.backend.services import UserService, AppointmentService, InventoryService
from netvac.backend.auth.auth import login_required

api_bp = Blueprint('api', __name__)

# Usuários
@api_bp.route('/register', methods=['POST'])
def register_user():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    user_service = UserService()
    user = user_service.register_user(username, email, password)
    return jsonify({'message': 'Usuário registrado com sucesso', 'user_id': user.id}), 201

@api_bp.route('/users/<username>', methods=['GET'])
def get_user_by_username(username):
    user_service = UserService()
    user = user_service.get_user_by_username(username)
    if user:
        return jsonify({'username': user.username, 'email': user.email}), 200
    else:
        return jsonify({'message': 'Usuário não encontrado'}), 404


# Agendamentos
@api_bp.route('/appointments/<int:appointment_id>', methods=['GET'])
def get_appointment_by_id(appointment_id):
    appointment = AppointmentService.get_appointment_by_id(appointment_id)
    if appointment:
        return jsonify(appointment.to_dict()), 200
    else:
        return jsonify({'message': 'Agendamento não encontrado'}), 404

@api_bp.route('/appointments', methods=['GET'])
def get_all_appointments():
    appointments = AppointmentService.get_all_appointments()
    return jsonify([appointment.to_dict() for appointment in appointments]), 200

# Estoque
@api_bp.route('/inventory/items', methods=['POST'])
@login_required
def add_inventory_item():
    data = request.get_json()
    item_id = data.get('item_id')
    item_name = data.get('item_name')
    quantity = data.get('quantity')
    unit_price = data.get('unit_price')
    inventory_service = InventoryService()
    inventory_service.add_item(item_id, item_name, quantity, unit_price)
    return jsonify({'message': 'Item adicionado ao estoque'}), 201

@api_bp.route('/inventory/items/<item_id>', methods=['PUT'])
@login_required
def update_inventory_item(item_id):
    data = request.get_json()
    new_quantity = data.get('new_quantity')
    new_unit_price = data.get('new_unit_price')
    inventory_service = InventoryService()
    inventory_service.update_item(item_id, new_quantity, new_unit_price)
    return jsonify({'message': 'Item atualizado'}), 200

@api_bp.route('/inventory/items/<item_id>', methods=['DELETE'])
@login_required
def delete_inventory_item(item_id):
    inventory_service = InventoryService()
    inventory_service.delete_item(item_id)
    return jsonify({'message': 'Item deletado'}), 200


@api_bp.route('/inventory/items/<item_id>', methods=['GET'])
@login_required
def get_inventory_item(item_id):
    inventory_service = InventoryService()
    item = inventory_service.get_item(item_id)
    if item:
        return jsonify(item.to_dict()), 200
    else:
        return jsonify({'message': 'Item não encontrado'}), 404

# Rota de exemplo para demonstração do decorator login_required
@api_bp.route('/protected', methods=['GET'])
@login_required
def protected_route():
    return jsonify({'message': 'Rota protegida acessada com sucesso!'})