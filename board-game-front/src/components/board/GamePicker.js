import React, { Component } from 'react';
import { Image, Card, Container } from 'semantic-ui-react';
import './picker.scss';
import BaseApi from '../../api/BaseApi';


class GamePicker extends Component {
  state = {
    randomGames: [],
  };
  async componentDidMount() {
    try {
      const randomGameResponse = await BaseApi.getRandomGame();
      this.setState({randomGames: randomGameResponse.data});
      console.log(randomGameResponse.data);
    } catch (err) {
      console.log(err);
    }
  }
  render() {

    return (
      <div className='game-picker'>
        <h1 className='header'>Choose the game you like</h1>
        <Container>
        <Card.Group itemsPerRow={5}>
          {this.state.randomGames.map((game)=>
            <Card  href={`${game.rank}`} >
            <Image src={game.image_url}  />
            <Card.Content>
            <Card.Header>{game.name}</Card.Header>
            </Card.Content>
            </Card>
            )
          }
        </Card.Group>
        </Container>
      </div>
    );
  }
}

export default GamePicker;
