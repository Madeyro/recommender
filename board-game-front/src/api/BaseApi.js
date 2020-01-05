import PreBaseApi from './PreBaseApi';

export default class CitiesApi extends PreBaseApi {
  static getRandomGame() {
    return this.get(`http://127.0.0.1:8000/api/games_short`);
  }
  static getGame(id) {
    return this.get(`/api/games_full/${id}`);
  }
}
