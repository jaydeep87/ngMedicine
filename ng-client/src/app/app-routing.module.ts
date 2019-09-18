import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { LoginComponent } from './login/login.component';
import { SignupComponent } from './signup/signup.component';
import { HomeComponent } from './home/home.component';

const routes: Routes = [
  {
    path: '',
    component: HomeComponent,
    data: {
      title: 'Home',
      description: '...',
      keywords: '...'
    }
  },
  {
    path: 'login',
    component: LoginComponent,
    data: {
      title: 'login',
      description: '...',
      keywords: '...'
    }
  },
  {
    path: 'signup',
    component: SignupComponent,
    data: {
      title: 'signup',
      description: '...',
      keywords: '...'
    }
  }];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
