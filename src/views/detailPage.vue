<template>
    <b-container
        fluid="xl"
        style="height: 100vh"
    >
        <b-row class="mt-5" v-if="check">
            <b-col class="col-9">
                <h1>{{animedata.title}} ({{animedata.mal_id}})</h1>
                <h6>{{animedata.title_english}}</h6>
                <h6>{{animedata.title_japanese}}</h6>
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
        <b-row class="mt-3">
            <b-col class="col-2">
                <b-img
                    :src="animedata.images.webp.image_url"
                />
            </b-col>
            <b-col class="col-4 px-5 text-start">
                <ul class="list-group">
                    <li class="list-group-item d-flex justify-content-between align-items-center">
                        SEASON
                        <span class="badge bg-primary rounded-pill text-uppercase">{{animedata.season}}</span>
                    </li>
                    <li class="list-group-item d-flex justify-content-between align-items-center">
                        THEMES
                        <div>
                            <span
                                class="badge bg-primary rounded-pill text-uppercase ms-1"
                                v-for="item in animedata.themes"
                                :key="item.mal_id"
                            >{{item.name}}</span><br>
                        </div>
                    </li>
                    <li class="list-group-item d-flex justify-content-between align-items-center">
                        STUDIO
                        <div>
                            <span 
                                class="badge bg-primary rounded-pill text-uppercase ms-1"
                                v-for="item in animedata.studios"
                                :key="item.mal_id"
                            >{{item.name}}</span><br>
                        </div>
                    </li>
                </ul>
            </b-col>
            <b-col class="col-6 ps-3 border-start">
                <p>
                    {{animedata.synopsis}}
                </p>
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