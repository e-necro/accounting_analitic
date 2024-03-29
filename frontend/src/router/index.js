import { createRouter, createWebHashHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import Register from '@/views/Register'
import Login from '@/views/Login'
import NotFound from '@/views/NotFound'
import AutoCatalog from '@/views/AutoCatalog'
import UserProfile from '@/views/UserProfile'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/register',
    name: 'register',
    component: Register
  },
  {
    path: '/login',
    name: 'login',
    component: Login
  },
  {
    path: '/auto-catalog',
    name: 'auto-catalog',
    component: AutoCatalog
  },
  {
    path: '/user-profile',
    name: 'userProfile',
    component: UserProfile
  },
  { 
    path: '/:pathMatch(.*)*', 
    name: 'NotFound', 
    component: NotFound 
  },
 
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
