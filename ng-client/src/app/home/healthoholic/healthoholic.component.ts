import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-healthoholic',
  templateUrl: './healthoholic.component.html',
  styleUrls: ['./healthoholic.component.css']
})
export class HealthoholicComponent implements OnInit {
  public healthoholicList : any[] = [
    {
    id :1,
    name: "healthoholic one",
    image_url : "h1.jpg"
  },
    {
    id :2,
    name: "healthoholic two",
    image_url : "h2.jpg"
  },
    {
    id :3,
    name: "healthoholic three",
    image_url : "h3.jpg"
  },
];
  constructor() { }

  ngOnInit() {
  }

}
