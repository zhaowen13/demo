import Vue from 'vue'
import Router from 'vue-router'
import index from '@/components/index'
import label from '@/components/label'
import test from '@/components/test'
import login from '@/components/login'
import apitest from '@/components/apitest'


Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/index',
      name: 'index',
      component: index
    },
    {
      path: '/label',
      name: 'label',
      component: label
    },
    {
      path: '/test',
      name: 'test',
      component: test
    },
    {
      path: '/login',
      name: 'login',
      component: login
    },
    {
      path: '/apitest',
      name: 'apitest',
      component: apitest
    },
   
  ]
})
