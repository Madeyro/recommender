import React, {Component} from 'react';
import {Image, Button, Card, Icon, Container} from 'semantic-ui-react';
import './game.scss';
import BaseApi from '../../api/BaseApi';
import ResultLineGame from "../resultgame";


class Game extends Component {
  state = {
    randomGame: null,
    randomGeneratedGames: [],
    unweightGeneratedGames: [],
    weightGeneratedGames: [],
  };

  async componentDidMount() {
    try {
      const gameResponse = await BaseApi.getGame(this.props.match.params.id);
      this.setState({ randomGame: gameResponse.data.game_detail });
      this.setState({ randomGeneratedGames: gameResponse.data.random_games_1 });
      this.setState({ unweightGeneratedGames: gameResponse.data. result_array_unweighted });
      this.setState({ weightGeneratedGames: gameResponse.data.result_array_weighted });
      console.log(gameResponse.data);
      console.log(gameResponse.data.game_detail);
    } catch (err) {
      console.log(err);
    }
  }

  render() {
    const {
      randomGame,
      randomGeneratedGames,
      unweightGeneratedGames,
      weightGeneratedGames
    } = this.state;
    return (
      <div className='game'>
        <Container>
          {randomGame ?
            <div>
              <div className="inline">
                <Image src={`${randomGame.image_url}`} size='medium'/>
                <Card>
                  <Card.Content>
                    <Card.Header>{randomGame.names}</Card.Header>
                    <Card.Meta>{randomGame.year}</Card.Meta>
                    <div className="rating">
                      <Icon color='yellow' name='star'/>
                      <div>{randomGame.avg_rating}</div>
                    </div>
                    <Card.Description>
                      {randomGame.category}
                    </Card.Description>
                  </Card.Content>
                  <Card.Content extra>
                    <a className='icons'>
                      <Icon name='user'/>
                      {randomGame.min_players}-{randomGame.max_players} Players
                    </a>
                    <a>
                      <Icon name='time'/>
                      {randomGame.avg_time} minutes
                    </a>
                  </Card.Content>
                </Card>
              </div>
              <ResultLineGame nameAlgo={"Weight Algorithm "} array={weightGeneratedGames}/>
              <ResultLineGame nameAlgo={"Unweight Algorithm"} array={unweightGeneratedGames}/>
              <ResultLineGame nameAlgo={"Random"} array={randomGeneratedGames}/>
            </div>
            :
            <div></div>
          }
        </Container>
      </div>
    );
  }
}

export default Game;
