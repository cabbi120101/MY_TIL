import React from 'react';
import { Link } from 'react-router-dom';
import styled from '@emotion/styled';

const Navbar: React.FC = () => {
  return (
    <Nav>
      <NavLink to="/">Home</NavLink>
      <NavLink to="/login">Login</NavLink>
      <NavLink to="/signup">Signup</NavLink>
      <NavLink to="/realtime">RealTime</NavLink>
      <NavLink to="/videolist">VideoList</NavLink>
      <NavLink to="/dashboard">Dashboard</NavLink>
      <NavLink to="/profile">Profile</NavLink>
      <NavLink to="/settings">Settings</NavLink>
      <NavLink to="/crimesummary">CrimeSummary</NavLink>
      <NavLink to="/welcome">Welcome</NavLink>
    </Nav>
  );
};

// 스타일
const Nav = styled.nav`
  display: flex;
  background-color: #333;
  padding: 10px;
  width: 100%;
  position: fixed;
  top: 0;
  left: 0;
  z-index: 1000;
`;

const NavLink = styled(Link)`
  color: white;
  margin-right: 10px;
  text-decoration: none;

  &:hover {
    text-decoration: underline;
  }
`;

export default Navbar;
