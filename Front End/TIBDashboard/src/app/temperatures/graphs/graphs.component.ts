import { Component, OnInit, ViewChildren, ElementRef, QueryList, AfterViewInit } from '@angular/core';
import { SensorsService } from '../../sensorservice.service'
import {BaseChartDirective} from 'ng2-charts/ng2-charts';

@Component({
  selector: 'app-graphs',
  templateUrl: './graphs.component.html',
  styleUrls: ['./graphs.component.sass']
})
export class GraphsComponent implements OnInit, AfterViewInit {
  @ViewChildren(BaseChartDirective) charts: QueryList<BaseChartDirective>;

  // Options
  public barChartOptions: any = {
    responsive: true
  };

  // Rain Switch Button
  public isChecked: boolean = false;
  public switch: string = ''

  // Humidity Chart
  public lineChartHumidityType = 'line';
  public lineChartHumidityLegend = true;
  public lineChartHumidityData: Array<any> = [{ data: [], label: 'Humidity' }];
  public lineChartHumidityLabels: Array<any> = [];


  // Temperature Chart
  public lineChartTempType = 'line';
  public lineChartTempLegend = true;
  public lineChartTempData: Array<any> = [{ data: [], label: 'Temperatures' }];
  public lineChartTempLabels: Array<any> = [];

  // Colors
  public lineChartColors: Array<any> = [
    { // Blue
      backgroundColor: 'rgba(148,159,177,0.2)',
      borderColor: 'rgba(148,159,177,1)',
      pointBackgroundColor: 'rgba(148,159,177,1)',
      pointBorderColor: '#fff',
      pointHoverBackgroundColor: '#fff',
      pointHoverBorderColor: 'rgba(148,159,177,0.8)'
    }
  ];

  // Events
  public chartClicked(e: any): void {
    console.log(e);
  }

  public chartHovered(e: any): void {
    console.log(e);
  }

  public isRainingToogle(e: any): void {
    this.switch = this.setRaining(e.checked)
  }

  public setRaining(value: boolean): string {
    return value ? 'Is Raining!' : 'Not Raining!'
  }
  constructor(private api: SensorsService) { }

  ngOnInit() {
    this.getDataRain();
    this.getDataTemp();
    this.getDataHumidity();
    
    setInterval(() => {
      this.getDataRain();
      this.getLastDataTemp();
      this.getLastDataHumidity();
      this.charts.first.chart.update();
      this.charts.last.chart.update();
    }, 1000);
  }

  ngAfterViewInit() {
    // console.log(this.charts);
}

  getDataRain() {
    this.api.getRain().subscribe((data: Array<object>) => {
      this.isChecked = data['value'];
      this.switch = this.setRaining(this.isChecked);
    });
  }

  getDataHumidity() {
    this.api.getHumidity().subscribe((data: Array<object>) => {
      this.lineChartHumidityData[0].data = data.values;
      this.lineChartHumidityLabels = data['dates'];
    });
  }

  getDataTemp() {
    this.api.getTemp().subscribe((data: Array<object>) => {
      this.lineChartTempData[0].data = data.values;
      this.lineChartTempLabels = data['dates'];
    });
  }

  getLastDataHumidity() {
    this.api.getHumidity().subscribe((data: Array<object>) => {
      this.lineChartHumidityData[0].data.push(data.values[data.values.length - 1]);
      this.lineChartHumidityLabels.push(data['dates'][data['dates'].length - 1]);
    });
  }

  getLastDataTemp() {
    this.api.getTemp().subscribe((data: Array<object>) => {
      this.lineChartTempData[0].data.push(data.values[data.values.length - 1]);
      this.lineChartTempLabels.push(data['dates'][data['dates'].length - 1]);
    });
  }
}