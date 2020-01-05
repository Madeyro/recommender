import React, { Component } from 'react';
import { NavLink } from 'react-router-dom';
import './header.scss';


class Header extends Component {
  render() {

    return (
        <NavLink to="/">
          <div className='header-form'>
            <h1>Board Game Recommender</h1>
          </div>
        </NavLink>
    );
  }
}

export default Header;
