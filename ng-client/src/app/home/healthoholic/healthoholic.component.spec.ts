import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { HealthoholicComponent } from './healthoholic.component';

describe('HealthoholicComponent', () => {
  let component: HealthoholicComponent;
  let fixture: ComponentFixture<HealthoholicComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ HealthoholicComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(HealthoholicComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
