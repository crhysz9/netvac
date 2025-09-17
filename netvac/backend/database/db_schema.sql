-- criação do banco de dados
CREATE DATABASE IF NOT EXISTS netvac;

-- uso do banco de dados
USE netvac;

-- criação da tabela de usuários
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- criação da tabela de vacinas
CREATE TABLE IF NOT EXISTS vaccines (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    manufacturer VARCHAR(255) NOT NULL,
    doses INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- criação da tabela de registros de vacinação
CREATE TABLE IF NOT EXISTS vaccination_records (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    vaccine_id INT NOT NULL,
    date DATE NOT NULL,
    dose INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (vaccine_id) REFERENCES vaccines(id)
);

-- criação da tabela de lotes de vacinas
CREATE TABLE IF NOT EXISTS vaccine_batches (
    id INT AUTO_INCREMENT PRIMARY KEY,
    vaccine_id INT NOT NULL,
    batch_number VARCHAR(255) NOT NULL,
    expiration_date DATE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (vaccine_id) REFERENCES vaccines(id)
);

-- criação da tabela de locais de vacinação
CREATE TABLE IF NOT EXISTS vaccination_locations (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  address VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- adicionando um índice para melhorar o desempenho de consultas
CREATE INDEX idx_users_username ON users (username);
CREATE INDEX idx_vaccines_name ON vaccines (name);
CREATE INDEX idx_vaccination_records_user_id ON vaccination_records (user_id);
CREATE INDEX idx_vaccination_records_vaccine_id ON vaccination_records (vaccine_id);
CREATE INDEX idx_vaccine_batches_vaccine_id ON vaccine_batches (vaccine_id);

-- extensão: .sql