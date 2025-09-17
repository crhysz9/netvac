from flask import Flask
from netvac.backend.api.routes import api_bp
from netvac.backend.database.db_connection import connect_to_db, close_connection
from decouple import config

app = Flask(__name__)
app.register_blueprint(api_bp, url_prefix='/api')
app.config['SQLALCHEMY_DATABASE_URI'] = config('DATABASE_URL') # Certifique-se de ter a variável de ambiente DATABASE_URL configurada

# Conexão com o banco de dados ao iniciar o aplicativo
with app.app_context():
    conn = connect_to_db()
    if conn:
        print('Conectado ao banco de dados')
    else:
        print('Falha na conexão com o banco de dados. O aplicativo não irá funcionar corretamente.')

@app.teardown_appcontext
def close_db_connection(error):
    close_connection(conn)

if __name__ == '__main__':
    app.run(debug=True)