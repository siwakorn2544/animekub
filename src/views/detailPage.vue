<template>
    <b-container 
    fluid="xl">
        <b-row>
            <b-col>
                <h1>{{animedata.title_english}}</h1>
            </b-col>
        </b-row>
        <b-row>
            <b-col>
                <commentVue/>
            </b-col>
        </b-row>
    </b-container>
    
</template>
<script>
import axios from '../plugin/axios';
import commentVue from './comment.vue';
export default {
    components:{
        commentVue
    },
    name : "deailPage",
    data(){
        return{
            animedata:{}
        }
    },
    created(){
        this.getDetailAnime(this.$route.params.id);
    },
    methods:{
        getDetailAnime(id){
            axios.get(`/anime/${id}/full`).then((res)=>{
                console.log(res.data);
                this.animedata = res.data.data
                console.log(this.animedata);
            })
        }
    }
}
</script>