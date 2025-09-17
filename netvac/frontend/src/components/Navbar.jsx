import React from 'react';
import { Link } from 'react-router-dom';
import '../styles/Navbar.css';

const Navbar = () => {
  return (
    <nav>
      <div className="navbar-container">
        <Link to="/" className="navbar-logo">
          NetVac
        </Link>
        <ul className="navbar-menu">
          <li className="navbar-item">
            <Link to="/" className="navbar-link">
              Início
            </Link>
          </li>
          <li className="navbar-item">
            <Link to="/sobre" className="navbar-link">
              Sobre
            </Link>
          </li>
          <li className="navbar-item">
            <Link to="/contato" className="navbar-link">
              Contato
            </Link>
          </li>
        </ul>
      </div>
    </nav>
  );
};

export default Navbar;