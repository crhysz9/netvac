import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Home from './pages/Home';
import Appointments from './pages/Appointments';
import Login from './pages/Login';
import Register from './pages/Register'; // Importando a página de cadastro

const App = () => {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/agendamentos" element={<Appointments />} />
        <Route path="/login" element={<Login />} />
        <Route path="/cadastro" element={<Register />} /> {/* Rota para a página de cadastro */}
      </Routes>
    </Router>
  );
};

export default App;