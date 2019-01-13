import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { GraphsComponent } from './temperatures/graphs/graphs.component';
import { HomeComponent } from './home/home.component';
import {MzButtonModule, MzInputModule, MzNavbarModule, MzToastModule} from 'ngx-materialize';
import {ChartsModule} from 'ng2-charts';
import {HttpClientModule} from '@angular/common/http';
import {DatePipe} from '@angular/common';
import { TempFakerComponent } from './faking-it/temp-faker/temp-faker.component';
import {IMqttServiceOptions, MqttModule} from 'ngx-mqtt';
import {MatGridListModule} from '@angular/material/grid-list';
import {MatSlideToggleModule} from '@angular/material/slide-toggle';
import { SensorsService } from './sensorservice.service';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import {MatButtonModule} from '@angular/material/button';



@NgModule({
  declarations: [
    AppComponent,
    GraphsComponent,
    HomeComponent,
    TempFakerComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    MzButtonModule,
    ChartsModule,
    MzNavbarModule,
    HttpClientModule,
    MzInputModule,
    MzToastModule,
    MatGridListModule,
    MatSlideToggleModule,
    BrowserAnimationsModule,
    MatButtonModule,
  ],
  exports: [
    MzButtonModule,
    MatGridListModule,
    MatButtonModule
  ],
  providers: [
    DatePipe,
    SensorsService
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
