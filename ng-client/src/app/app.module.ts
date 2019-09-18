import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import {TitleService} from "./core/services/SEO.service";

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HeaderComponent } from './shared/header/header.component';
import { FooterComponent } from './shared/footer/footer.component';
import { LoginComponent } from './login/login.component';
import { SignupComponent } from './signup/signup.component';
import { HomeComponent } from './home/home.component';
import { ArticleComponent } from './home/article/article.component';
import { HealthoholicComponent } from './home/healthoholic/healthoholic.component';
import { JwSocialButtonsModule } from 'jw-angular-social-buttons';
import { FbLikeComponent } from './home/fb-like/fb-like.component';

@NgModule({
  declarations: [
    AppComponent,
    HeaderComponent,
    FooterComponent,
    LoginComponent,
    SignupComponent,
    HomeComponent,
    ArticleComponent,
    HealthoholicComponent,
    FbLikeComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    JwSocialButtonsModule
  ],
  providers: [TitleService],
  bootstrap: [AppComponent]
})
export class AppModule { }
