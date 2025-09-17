import React from 'react';
import Navbar from '../components/Navbar';
import '../styles/Appointments.css';

const Appointments = () => {
  return (
    <div>
      <Navbar />
      <div className="appointments-container">
        <h1>Agendamentos</h1>
        {/* Aqui você adicionará a lógica para exibir os agendamentos */}
        <p>Esta página exibirá seus agendamentos.</p>
      </div>
    </div>
  );
};

export default Appointments;