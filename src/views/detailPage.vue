<template>
    <b-container
        fluid="xl"
        style="height: 100vh"
    >
        <b-row class="mt-5">
            <b-col class="col-9">
                <h1>{{animedata.title}} {{animedata.mal_id}}</h1>
            </b-col>
            <b-col class="col-3">
                <div class="d-flex justify-content-between">
                    <div>Rating</div>
                    <div>{{animedata.score}}</div>
                </div>
                <div class="progress mt-2">
                    <div
                        class="progress-bar bg-warning"
                        :style="{width: (animedata.score*10)+'%'}"></div>
                </div>
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
            animedata:{},
            check : false
        }
    },
    created(){
        // console.log("Hello");
        this.getDetailAnime(this.$route.params.id);
    },

    watch:{
        animedata(){
            this.check = true
            commentVue
        }
    },
    
    methods:{
        getDetailAnime(id){
            // console.log(id)
            axios.get(`/anime/${id}/full`).then((res)=>{
                console.log(res.data)
                this.animedata = res.data.data
                console.log(this.animedata)
            })
        }
    }
}
</script>