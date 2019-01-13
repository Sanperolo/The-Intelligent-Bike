import { TestBed } from '@angular/core/testing';

import { SensorserviceService } from './sensorservice.service';

describe('SensorserviceService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: SensorserviceService = TestBed.get(SensorserviceService);
    expect(service).toBeTruthy();
  });
});
