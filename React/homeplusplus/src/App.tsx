import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Home from './pages/Home/Home';
import Login from './pages/Login/Login';
import Signup from './pages/Signup/Signup';
import RealTime from './pages/RealTime/RealTime';
import VideoList from './pages/VideoList/VideoList';
import Dashboard from './pages/Dashboard/Dashboard';
import Profile from './pages/Profile/Profile';
import Settings from './pages/Settings/Settings';
import Crimesummary from './pages/Crimesummary/Crimesummary';
import Welcome from './pages/Welcome/Welcome';
import Navbar from './components/Navbar/Navbar';
import styled from '@emotion/styled';

const App: React.FC = () => {
  return (
    <Router>
      <Navbar />
      <Main>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/login" element={<Login />} />
          <Route path="/signup" element={<Signup />} />
          <Route path="/realtime" element={<RealTime />} />
          <Route path="/videolist" element={<VideoList />} />
          <Route path="/dashboard" element={<Dashboard />} />
          <Route path="/profile" element={<Profile />} />
          <Route path="/settings" element={<Settings />} />
          <Route path="/crimesummary" element={<Crimesummary />} />
          <Route path="/welcome" element={<Welcome />} />
        </Routes>
      </Main>
    </Router>
  );
};

const Main = styled.main`
  padding-top: 60px;
`;

export default App;
