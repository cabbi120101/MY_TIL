import React from 'react';
import { Link } from 'react-router-dom';
import {
  FaExclamationTriangle,
  FaTint,
  FaThermometerHalf,
  FaArrowsAlt,
  FaUserCircle,
} from 'react-icons/fa';
import liveSampleImage from '../../assets/images/live_sample.jpg';
import './Home.css';

const Home: React.FC = () => {
  return (
    <div className="home-container">
      <nav className="navbar">
        <Link to="/" className="logo">
          <img src="/path/to/logo.jpg" alt="Logo" className="logo-image" />
        </Link>
        <div className="nav-links">
          <Link to="/welcome">About</Link>
          <Link to="/realtime">Live Video</Link>
          <Link to="/videolist">Incident Log</Link>
          <Link to="/dashboard">Dashboard</Link>
          <Link to="/crimesummary">Crime Summary</Link>
        </div>
        <Link to="/profile" className="profile-icon">
          <FaUserCircle size={30} />
        </Link>
      </nav>
      <div className="content">
        <div className="live-view">
          <img
            src={liveSampleImage}
            alt="Live Cam Thumbnail"
            className="live-thumbnail"
          />
          <Link to="/realtime" className="watch-live">
            Watch Live
          </Link>
        </div>
        <div className="status-cards">
          <div className="status-card">
            <FaArrowsAlt size={50} />
            <div className="status-card-info">
              <h3>Movement</h3>
              <p>10</p>
            </div>
          </div>
          <div className="status-card">
            <FaExclamationTriangle size={50} />
            <div className="status-card-info">
              <h3>Alerts</h3>
              <p>12</p>
            </div>
          </div>
          <div className="status-card">
            <FaTint size={50} />
            <div className="status-card-info">
              <h3>Humidity</h3>
              <p>60%</p>
            </div>
          </div>
          <div className="status-card">
            <FaThermometerHalf size={50} />
            <div className="status-card-info">
              <h3>Temperature</h3>
              <p>25°C</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Home;
