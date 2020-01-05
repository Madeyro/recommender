import React, { Component } from 'react';
import { Image, Card, Container } from 'semantic-ui-react';
import './resultgames.scss';
import BaseApi from '../../api/BaseApi';


class ResultLineGame extends Component {
  state = {
    randomGames: [],
  };
  render() {
    const {
        array,
      nameAlgo
    } = this.props;
    return (
      <div className='game-line'>
        <h1 className='header-line'>{nameAlgo}</h1>
        <Container>
        <Card.Group itemsPerRow={6}>
          {array.map((game)=>
              <Card  className='custom-card' color='olive'  href={`${game.rank}`}  header={game.names} image={game.image_url} />
            )
          }
        </Card.Group>
        </Container>
      </div>
    );
  }
}

export default ResultLineGame;
