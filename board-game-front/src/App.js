import React from 'react';
import './App.css';
import Header from './components/header';
import GamePicker from "./components/board";
import Game from "./components/game";
import { Switch, Route, Redirect } from 'react-router-dom';

function App() {
  return (
    <div className="App">
      <Header/>
      <Switch>
        <Route
          exact
          path="/"
          render={({  }) => {
              return (
                <GamePicker/>
              )
          }}
        />
        <Route
          exact
          path="/:id"
          render={({ match }) => {
              return (
                <Game match={match}/>
              )
          }}
        />
        <Redirect to="/" />
      </Switch>
    </div>
  );
}

export default App;
