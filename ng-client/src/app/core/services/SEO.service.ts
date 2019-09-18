import { Injectable } from '@angular/core';

import { Title, Meta } from '@angular/platform-browser';
import { Router, NavigationEnd, ActivatedRoute } from '@angular/router';
import { filter, map, switchMap } from 'rxjs/operators';

const APP_TITLE = 'NG-APP ';
const SEPARATOR = ' > ';

@Injectable()
export class TitleService {
  constructor(
    private router: Router,
    private activatedRoute: ActivatedRoute,
    private titleService: Title,
    private meta: Meta
  ) {}


  updateDescription(desc: string, keywords: string, title: string) {
    this.titleService.setTitle(title);
    this.meta.updateTag({ name: 'description', content: desc })
    this.meta.updateTag({ name: 'keywords', content: keywords })
    this.meta.updateTag({ name: 'og:title', content: title })
    this.meta.updateTag({ name: 'og:description', content: desc })
}

  init() {
      this.router.events
      
      .pipe(
        filter(event => event instanceof NavigationEnd),
        map(() => this.activatedRoute),
        map(route => route.firstChild),
        switchMap(route => route.data),
        map((data) => {
          if (data.title) {
            // If a route has a title set (e.g. data: {title: "Foo"}) then we use it
            return data.title;
          } else {
            // If not, we do a little magic on the url to create an approximation
            return this.router.url.split('/').reduce((acc, frag) => {
              if (acc && frag) { acc += SEPARATOR; }
              return this.router.url.split('/').reduce((acc, frag) => {
                if ( acc && frag ) { acc += SEPARATOR; }
                return acc + TitleService.ucFirst(frag);
              });
            });
          }
        })
      )
      .subscribe((pathString) => {
           this.titleService.setTitle(`${APP_TITLE} ${pathString}`)
        // this.updateDescription(event['description'], event['keywords'], event['title'])
      });
  }

  static ucFirst(string) {
    if ( !string ) { return string; }
    return string.charAt(0).toUpperCase() + string.slice(1);
  }
}