<template>
    <b-container>
        <h1>HelloWorld1</h1>
        <b-card no-body>
            <b-row>
                <b-col
                v-for="(item, index) in animeData"
                :key="item.mai_id"
                class="mb-2"
                >
                <template #header>
                    <h4 class="mb-0">Hello World {{ index }}</h4>
                </template>
                <b-card-body>
                    <b-card style="height:100%;">
                        <b-card-img
                        :src="item.images.webp.image_url"
                        img-alt="Card image"
                        img-top
                        alt="Image"
                        class="mb-2 Card_hover">
                        </b-card-img>
                        <b-card-title>
                          {{ item.title }}
                        </b-card-title>
                    </b-card>
                    

                </b-card-body>

                </b-col>
            </b-row>
        </b-card>
        
    </b-container>
    
</template>
<script>
import axios from '../plugin/axios'
export default {
    name: "mainPage",
    data(){
        return{
            msg: "Hello world Pete",
            show: true,
            animeData:undefined
        }
    }
    ,
    mounted()
    {
            axios.get('/anime').then((res)=>{
                console.log(res)
                this.animeData = res.data.data
                console.log(this.animeData)
            })
            .catch((err)=>{
                console.log(err)
            })
    },
    methods: {

    }
}
</script>