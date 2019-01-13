import { Injectable }from '@angular/core';
import { HttpClient, HttpHeaders }from '@angular/common/http';
import { map } from 'rxjs/operators';

@Injectable()
export class SensorsService {

  private sensorsUrl: string = 'https://api-tib.herokuapp.com/sensors/';
  constructor (private http: HttpClient) {}

  getRain() {
    const url = this.sensorsUrl+"action_raining";
    return this.http.get(url);
  }

  getHumidity() {
    const url = this.sensorsUrl+"chart_humidity";
    return this.http.get(url);
  }
  getTemp() {
    const url = this.sensorsUrl+"chart_temp";
    return this.http.get(url);
  }
}
