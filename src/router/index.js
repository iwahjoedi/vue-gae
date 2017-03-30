import Vue from 'vue'
import Router from 'vue-router'
import VueHead from 'vue-head'

import Hello from '@/components/Hello'
import Home from '@/components/Home'

Vue.use(VueHead)
Vue.use(Router)

export default new Router({
   mode: 'history',
  routes: [
    { path: '/home', name: 'Hello', component: Hello },
    { path: '/', name: 'Home', component: Home },
  ]
})

/**
 *  route: /home, desc:  Track your service code
 *  route: /admin, 
 *         /admin/login
 *         /admin/
 * 
 * 
 * 
 * 
 * 
 * 
 */ 