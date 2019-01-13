import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import {GraphsComponent} from './temperatures/graphs/graphs.component';
import {HomeComponent} from './home/home.component';
import {TempFakerComponent} from './faking-it/temp-faker/temp-faker.component';

const routes: Routes = [
  { path: 'temp-faker', component: TempFakerComponent },
  { path: 'temp-graphs', component: GraphsComponent },
  { path: '', component: HomeComponent }];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
