<template>
    <b-container
    fluid="xl">
        <h1 class="mt-5">Welcome</h1>
            <b-row class="mt-5">
                <b-col class="mb-3 col-10">
                    <b-input class="mb-2" v-model="name" placeholder="Search ..."></b-input>
                </b-col>
                <b-col class=" col-1">
                    <b-button class="form-control" variant="outline-primary" @click="getAnimebyName()">Search</b-button>
                </b-col>
            </b-row>
            <b-row id="animeRow">
                   <b-card no-body>
                            <b-row
                                class="mt-3"
                            >
                                <b-col 
                                    class="col-3"
                                    v-for="item in animeData"
                                    :key="item.mal_id"
                                >
                                <b-card 
                                no-body
                                img-top
                                :img-src="item.images.webp.large_image_url"
                                img-alt="Card image"
                                style="height: fit-content;"
                                img-height="450"
                                class="mb-4"
                                >
                                <b-card-title
                                   style="height: 100px"
                                >
                                    <h5 class="mt-3 ms-3">{{item.title}}</h5>
                                </b-card-title>
                            
                                <b-card-footer>
                                    <b-button @click="viewDetail(item.mal_id)" variant="primary">See Details</b-button>
                                </b-card-footer>
                                </b-card>
                            </b-col>
                            </b-row>
                            <div class="d-flex justify-content-end me-4">
                                <b-pagination-nav
                                :link-gen="linkGen"
                                :number-of-pages="this.num"
                                base-url="/"
                                first-text="First"
                                prev-text="Prev"
                                next-text="Next"
                                last-text="Last">
                                </b-pagination-nav>
                            </div>
                   </b-card>
            </b-row>

    </b-container>
    
</template>
<script>
import axios from '../plugin/axios'
export default {
    name: "mainPage",
    data(){
        return{
            show: true,
            animeData:[],
            loadseasonNow: false,
            loadAnimeByName: false,
            hasnextpage:false,
            current_page:1,
            per_page:25,
            row: 0,
            num: null,
            name:'',
            count: 0
        }
    }
    ,
    mounted()
    {
        if(this.$route.params.type == "byName"){
            this.getAnimebyName()
        }else{
            this.getSeasonsNow()
        }
    },
    methods: {
        getAnimebyName(){
            let result = null
            if (this.name == "") {
                result = localStorage.getItem("name")
            }
            if(result != null || result == ""){
                this.name = result
            }
            if (this.name == ""){
                this.animeData = []
                alert("plaese type something")
            }
            else{
            this.loadAnimeByName = true
            axios.get(`/anime?letter=${this.name}&page=${this.$route.params.current_page}`)
            .then((res)=>{
                this.animeData = []
                console.log(res.data)
                this.loadseasonNow = false
                this.loadAnimeByName = true
                this.hasnextpage = res.data.pagination.has_next_page
                this.current_page = res.data.pagination.current_page
                this.row = res.data.pagination.items.total
                this.per_page = res.data.pagination.items.per_page
                this.animeData = res.data.data
                this.num = Math.ceil(this.row / this.per_page)
            }).catch((err)=>{
                console.log(err)
            })
            localStorage.setItem("name", this.name)
            this.count = 1;
            }
        },
        getSeasonsNow(){
            axios.get(`/seasons/now?page=${this.$route.params.current_page}`)
            .then((res)=>{
                // console.log(res)
                this.loadAnimeByName = false
                this.hasnextpage = res.data.pagination.has_next_page
                this.current_page = res.data.pagination.current_page
                this.row = res.data.pagination.items.total
                this.per_page = res.data.pagination.items.per_page
                this.animeData = res.data.data
                this.num = Math.ceil(this.row / this.per_page)
                // console.log(this.num)
                this.loadseasonNow = true
            })
            .catch((err)=>{
                console.log(err)
            })
        },
        linkGen(pageNum) {
            if(this.count == 1){
                return "/main"+"/"+pageNum+"/"+"byName"
            }else{
                return "/main"+"/"+pageNum+"/"+this.$route.params.type
            }
        },
        viewDetail(mal_id){
            this.$router.push({path: `/detailpage/${mal_id}`})
        },

    }
}
</script>
<style>
.col-3 :hover{
    transform: scale(1.05);
    background-color: pink;
    transition: all 0.5s;
    color:black;
}
</style>