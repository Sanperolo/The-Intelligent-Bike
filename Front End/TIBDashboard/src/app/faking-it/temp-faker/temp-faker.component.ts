import {Component, OnDestroy, OnInit} from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {TempReading} from '../../shared/models/temp-reading';
import {MzToastService} from 'ngx-materialize';
import {Subscription} from 'rxjs';

@Component({
  selector: 'app-temp-faker',
  templateUrl: './temp-faker.component.html',
  styleUrls: ['./temp-faker.component.sass']
})
export class TempFakerComponent implements OnInit, OnDestroy {
  private sub: Subscription;
  constructor(private toastService: MzToastService,
              private http: HttpClient) { }

  ngOnInit() {
  }

  onEnter(value) {
    if (value < -30 || value > 120) {
      this.toastService.show('Ah ah ahhhhh not allowed, go between -30 and 120 degrees', 2000, 'red');
      return;
    }
    const date = Date.now();
    this.sub = this.http.post<TempReading>('https://restapi2-ost.herokuapp.com/tempsensors', {
      time: date, value: value
    }).subscribe(() => {
        this.toastService.show('New Value Added', 2000, 'green');
      });
  }

  ngOnDestroy(): void {
    if (this.sub) {
      this.sub.unsubscribe();
    }
  }

}
