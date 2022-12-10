import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

const routes = [    
    {
        path: '/:current_page',
        name: 'home',
        component: () => import('../views/mainPage.vue')
    },
    {
        path: '/detailpage/:id',
        name: 'detailpage',
        component: () => import('../views/detailPage.vue')
    },
]

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
})

export default router