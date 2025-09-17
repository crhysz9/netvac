from flask import request, jsonify
from netvac.backend.models.user import User
from functools import wraps

def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        auth_header = request.headers.get('Authorization')
        if auth_header:
            try:
                auth_token = auth_header.split(" ")[1]
                # Incluir lógica de verificação de token aqui. Substitua pelo seu método de autenticação.
                user = verify_auth_token(auth_token)  
                if user:
                    return func(*args, **kwargs)
                else:
                    return jsonify({'message': 'Token inválido'}), 401
            except IndexError:
                return jsonify({'message': 'Formato de token inválido'}), 401
        else:
            return jsonify({'message': 'Token de autenticação ausente'}), 401
    return wrapper

def verify_auth_token(auth_token):
    # Substitua este método pela sua implementação real de verificação de token.
    # Este é um exemplo e deve ser substituído por um método seguro de verificação de tokens.
    # Exemplo: verificação de token JWT, token baseado em banco de dados etc.
    # ... lógica de verificação ...
    # Exemplo de retorno (substitua pela sua lógica)
    user = User.find_by_username("testuser") # Substitua por lógica de busca de usuário baseado no token
    return user



def authenticate():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'message': 'Username e password são obrigatórios'}), 400

    user = User.find_by_username(username)
    if user and user.password == password: # Substitua pela sua lógica de comparação de senha
        # Aqui você geraria o token JWT ou outro método de autenticação.
        # Substitua por sua lógica de geração de token.
        token = generate_auth_token(user.id) #Função de geração de token (implementar)
        return jsonify({'token': token}), 200
    else:
        return jsonify({'message': 'Credenciais inválidas'}), 401

def generate_auth_token(user_id):
    # Implemente sua lógica de geração de token aqui (ex: JWT)
    # ... lógica para gerar token JWT ou outro método de autenticação ...
    return "token_de_exemplo" # Substitua por um token gerado adequadamente


#Exemplo de uso da rota de autenticação
# from flask import Flask
# app = Flask(__name__)

# @app.route('/login', methods=['POST'])
# def login():
#     return authenticate()


#Exemplo de uso do decorator
# @app.route('/protected', methods=['GET'])
# @login_required
# def protected_route():
#     return jsonify({'message':'Rota protegida acessada com sucesso!'})

# app.run(debug=True)