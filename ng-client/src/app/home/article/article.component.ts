import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-article',
  templateUrl: './article.component.html',
  styleUrls: ['./article.component.css']
})
export class ArticleComponent implements OnInit {
  public articleList : any[] = [
    {
    id :1,
    name: "article one",
    small_description: "We live in an impatient world. Everything needs to happen fast and now! But life as we know it has its own way and sometimes things don’t go as per plan. Situations that don’t go our way often provoke angry reactions, and while getting angry doesn’t usually affect the problem, it certainly affects our health.",
    tag_string: "Anger",
    title: "Anger: Control it before it consumes you!",
    type: "Wellness News Feed",
    image_url : "assets/img/article1.jpg"
  },
    {
    id :2,
    name: "article two",
    small_description: "We live in an impatient world. Everything needs to happen fast and now! But life as we know it has its own way and sometimes things don’t go as per plan. Situations that don’t go our way often provoke angry reactions, and while getting angry doesn’t usually affect the problem, it certainly affects our health.",
    tag_string: "Anger",
    title: "Anger: Control it before it consumes you!",
    type: "Wellness News Feed",
    image_url : "assets/img/article2.jpg"
  },
    {
    id :3,
    name: "article three",
    small_description: "We live in an impatient world. Everything needs to happen fast and now! But life as we know it has its own way and sometimes things don’t go as per plan. Situations that don’t go our way often provoke angry reactions, and while getting angry doesn’t usually affect the problem, it certainly affects our health.",
    tag_string: "Anger",
    title: "Anger: Control it before it consumes you!",
    type: "Wellness News Feed",
    image_url : "assets/img/article3.jpg"
  },
  {
    id :3,
    name: "live articlwe",
    small_description: "We live in an impatient world. Everything needs to happen fast and now! But life as we know it has its own way and sometimes things don’t go as per plan. Situations that don’t go our way often provoke angry reactions, and while getting angry doesn’t usually affect the problem, it certainly affects our health.",
    tag_string: "Anger",
    title: "Anger: Control it before it consumes you!",
    type: "Wellness News Feed",
    image_url : "https://image2.healthforu.com/media/articles/docx/newsfeed/18_nov___anger_rohan_1.png"
  }
];
  constructor() { }

  ngOnInit() {
  }

}
