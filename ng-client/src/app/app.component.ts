import { Component } from '@angular/core';
import {TitleService} from "./core/services/SEO.service";

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {

  constructor(private titleService: TitleService){

  }
  title = 'ng-client';
  ngOnInit(): void {
    this.titleService.init();
  }
  
}
