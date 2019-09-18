import { Component, OnInit } from '@angular/core';
import { Meta } from '@angular/platform-browser';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent {
  url = 'http://jasonwatmore.com';
    text = `Jason Watmore's Blog | A Web Developer in Sydney`;
    // imageUrl = 'http://jasonwatmore.com/_content/images/jason.jpg';
    imageUrl = '"http://localhost:4200/assets/img/article3.jpg"';


    public articleList : any[] = [
      {
        // url_article : "https://www.healthforu.com/health-newscast/anger-control-it-before-it-consumes-you/613",
        url : "http://localhost:4200/",
        small_description: "We live in an impatient world. Everything needs to happen fast and now! But life as we know it has its own way and sometimes things don’t go as per plan. Situations that don’t go our way often provoke angry reactions, and while getting angry doesn’t usually affect the problem, it certainly affects our health.",
        tag_string: "Anger",
        title: "Anger: Control it before it consumes you!",
        type: "Wellness News Feed",
        imageUrl : "http://localhost:4200/assets/img/article3.jpg"
      }
    ]

  constructor(private meta: Meta) {
    this.meta.addTag({ name: 'twitter:card', content: 'summary_large_image' });
    this.meta.addTag({ name: 'twitter:site', content: '@alligatorio' });
    this.meta.addTag({ name: 'twitter:title', content: 'Front-end Web Development, Chewed Up' });
    this.meta.addTag({ name: 'twitter:description', content: 'Learn frontend web development...' });
    this.meta.addTag({ name: 'twitter:image', content: 'https://alligator.io/images/front-end-cover.png' });
  }

  


  ngOnInit() {
  }

}
