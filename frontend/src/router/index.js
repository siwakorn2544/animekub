import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

const routes = [
    {
        path: '/main/:current_page/:type',
        name: 'home',
        component: () => import('../views/mainPage.vue')
    },
    {
        path: '/detailpage/:id',
        name: 'detailpage',
        component: () => import('../views/detailPage.vue')
    },
    {
        path: '/',
        name: '',
        component: () => import("../views/main.vue")
    },
]

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
})

export default router