import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { TempFakerComponent } from './temp-faker.component';

describe('TempFakerComponent', () => {
  let component: TempFakerComponent;
  let fixture: ComponentFixture<TempFakerComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ TempFakerComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(TempFakerComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
