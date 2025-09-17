import React from 'react';
import { render, screen, fireEvent } from '@testing-library/react';
import App from '../../frontend/src/App'; // Ajustado o caminho para importar App.jsx
import { BrowserRouter as Router } from 'react-router-dom'; // Import necessário para o roteamento

// Teste para a página inicial
test('Home page renders correctly', () => {
  render(
    <Router>
      <App />
    </Router>
  );
  expect(screen.getByText(/Bem-vindo/i)).toBeInTheDocument(); // Texto exemplo, ajuste conforme seu conteúdo
});


// Teste para a página de agendamentos
test('Appointments page renders correctly', () => {
  render(
    <Router>
      <App />
    </Router>
  );
  // Simula navegação para a página de agendamentos.  Ajuste o seletor se necessário.
  fireEvent.click(screen.getByRole('link', { name: /Agendamentos/i })); 
  expect(screen.getByText(/Agendamentos/i)).toBeInTheDocument(); // Texto exemplo, ajuste conforme seu conteúdo
});

// Teste para a página de login
test('Login page renders correctly', () => {
  render(
    <Router>
      <App />
    </Router>
  );
  fireEvent.click(screen.getByRole('link', { name: /Login/i }));
  expect(screen.getByText(/Login/i)).toBeInTheDocument(); // Texto exemplo, ajuste conforme seu conteúdo
});

// Teste para a página de cadastro
test('Register page renders correctly', () => {
    render(
      <Router>
        <App />
      </Router>
    );
    fireEvent.click(screen.getByRole('link', { name: /Cadastro/i }));
    expect(screen.getByText(/Cadastro/i)).toBeInTheDocument(); // Texto exemplo, ajuste conforme seu conteúdo
  });


// Adicione mais testes conforme necessário para cobrir outras funcionalidades.
// Lembre-se de ajustar os seletores e textos esperados para corresponder ao seu aplicativo.