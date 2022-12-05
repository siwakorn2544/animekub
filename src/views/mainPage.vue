<template>
    <b-container>
        <h1>HelloWorld1</h1>
        <div class="mr-5">{{ msg }}</div>
        <b-button size="sm" variant="success" @click="toggle">
            {{ show ? 'Hide' : 'Show' }} Alert
        </b-button>
        <b-alert
            v-model="show"
            class="mt-3"
            dismissible
            @dismissed="dismissed"
            >
            {{ msg }}!
        </b-alert>
        
    </b-container>
    
</template>
<script>
import  DATA from '../dtest'
export default{
    name: "mainPage",
    data(){
        return{
            msg: "Hello world Pete",
            show: true,
            res: DATA
        }
    },
    methods: {
        toggle() {
        console.log('Toggle button clicked')
        this.show = !this.show
        },
    }
}
</script>