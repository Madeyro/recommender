import axios from 'axios';


export default class PreBaseApi {
  static get(urlPath) {
    return axios({
      method: 'GET',
      url: urlPath,
    });
  }
  static post(urlPath, data) {
    return axios({
      method: 'POST',
      url: urlPath,
      data,
      headers: {
        'Access-Control-Allow-Origin': '*',
      }
    });
  }
}
