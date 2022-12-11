<template>
    <b-container 
    fluid="xl">
        <b-row>
            <b-col>
                <h1>{{animedata.title}} {{animedata.mal_id}}</h1>
            </b-col>
        </b-row>
        <b-row>
            <b-col>
                <commentVue :animedata="animedata.mal_id"/>
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
    name : "detailpage",
    data(){
        return{
            animedata:{}
        }
    },
    created(){
        console.log("Hello");
        this.getDetailAnime(this.$route.params.id);
    },
    methods:{
        getDetailAnime(id){
            console.log(id)
            axios.get(`/anime/${id}/full`).then((res)=>{
                console.log(res.data);
                this.animedata = res.data.data
                console.log(this.animedata);
            })
        }
    }
}
</script>