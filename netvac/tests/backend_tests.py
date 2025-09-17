import pytest
import json
from unittest.mock import MagicMock, patch
from flask import Flask
from netvac.backend.api.routes import api_bp
from netvac.backend.services.user_service import UserService

@pytest.fixture
def client():
    app = Flask(__name__)
    app.register_blueprint(api_bp, url_prefix='/api')
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_register_user(client):
    with patch('netvac.backend.api.routes.UserService') as MockUserService:
        mock_service = MockUserService.return_value
        mock_user = MagicMock()
        mock_user.id = 123
        mock_service.register_user.return_value = mock_user

        response = client.post('/api/register',
                               data=json.dumps({
                                   'username': 'testuser',
                                   'email': 'test@example.com',
                                   'password': 'secret'
                               }),
                               content_type='application/json')

        assert response.status_code == 201
        data = json.loads(response.data)
        assert data['message'] == 'Usuário registrado com sucesso'
        assert data['user_id'] == 123

def test_get_user_by_username_found(client):
    with patch('netvac.backend.api.routes.UserService') as MockUserService:
        mock_service = MockUserService.return_value
        mock_user = MagicMock()
        mock_user.username = 'testuser'
        mock_user.email = 'test@example.com'
        mock_service.get_user_by_username.return_value = mock_user

        response = client.get('/api/users/testuser')
        assert response.status_code == 200
        data = json.loads(response.data)
        assert data['username'] == 'testuser'
        assert data['email'] == 'test@example.com'

def test_get_user_by_username_not_found(client):
    with patch('netvac.backend.api.routes.UserService') as MockUserService:
        mock_service = MockUserService.return_value
        mock_service.get_user_by_username.return_value = None

        response = client.get('/api/users/nonexistent')
        assert response.status_code == 404
        data = json.loads(response.data)
        assert data['message'] == 'Usuário não encontrado'

def test_get_appointment_by_id_found(client):
    with patch('netvac.backend.api.routes.AppointmentService.get_appointment_by_id') as mock_get:
        mock_appointment = MagicMock()
        mock_appointment.to_dict.return_value = {'id': 1, 'title': 'Consulta'}
        mock_get.return_value = mock_appointment

        response = client.get('/api/appointments/1')
        assert response.status_code == 200
        data = json.loads(response.data)
        assert data['id'] == 1

def test_get_appointment_by_id_not_found(client):
    with patch('netvac.backend.api.routes.AppointmentService.get_appointment_by_id') as mock_get:
        mock_get.return_value = None

        response = client.get('/api/appointments/999')
        assert response.status_code == 404
        data = json.loads(response.data)
        assert data['message'] == 'Agendamento não encontrado'

def test_get_all_appointments(client):
    with patch('netvac.backend.api.routes.AppointmentService.get_all_appointments') as mock_get_all:
        mock_appointment = MagicMock()
        mock_appointment.to_dict.return_value = {'id': 1, 'title': 'Consulta'}
        mock_get_all.return_value = [mock_appointment]

        response = client.get('/api/appointments')
        assert response.status_code == 200
        data = json.loads(response.data)
        assert len(data) == 1
        assert data[0]['id'] == 1

def test_user_service_register_user():
    with patch('netvac.backend.services.user_service.User.create') as mock_create:
        mock_user = MagicMock()
        mock_user.id = 456
        mock_create.return_value = mock_user

        service = UserService()
        user = service.register_user('user', 'user@example.com', 'pass')
        assert user.id == 456
        mock_create.assert_called_once_with('user', 'user@example.com', 'pass')

def test_user_service_get_user_by_username():
    with patch('netvac.backend.services.user_service.User.find_by_username') as mock_find:
        mock_user = MagicMock()
        mock_find.return_value = mock_user

        service = UserService()
        user = service.get_user_by_username('user')
        assert user == mock_user
        mock_find.assert_called_once_with('user')