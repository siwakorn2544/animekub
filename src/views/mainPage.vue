<template>
    <b-container
    fluid="xl">
        <h1>Welcome</h1>
            <b-row>
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
                    class="mb-4"
                    >
                    <b-card-title>
                        <h4 class="mt-5">{{item.title}}</h4>
                    </b-card-title>
                    
                    <b-card-footer>
                        <b-button @click="viewDetail(item.mal_id)" variant="primary">See details </b-button>
                    </b-card-footer>

                    </b-card>

                </b-col>
            </b-row>
        <div class="overflow-auto">
            <b-pagination-nav
            v-del="current_page"
            :number-of-pages="this.num"
            base-url="/"
            first-text="First"
            prev-text="Prev"
            next-text="Next"
            last-text="Last">
            </b-pagination-nav>
        </div>

    </b-container>
    
</template>
<script>

import axios from '../plugin/axios'
export default {
    name: "mainPage",

    data(){
        return{
            selected_year:[],
            selected_season:{},
            show: true,
            animeData:{},
            hasnextpage:false,
            current_page:1,
            per_page:25,
            row: 0,
            num: 1,
        }
    }
    ,
    mounted()
    {
        this.getSeasonsNow()
        console.log(this.$route)
        this.linkGen(this.$route.params.current_page)
        this.getSeasons()
    },
    methods: {
        getSeasons(){
            axios.get(`/seasons`)
            .then((res)=>{
                console.log(res.data)
                this.selected_year = res.data.data
                this.selected_season = res.data.data
                // console.log(this.selected_year)
            }).catch((err)=>{
                console.log(err)
            })
        },
        getSeasonsNow(){
            axios.get(`/seasons/now?page${this.current_page}`)
            .then((res)=>{
                console.log(res)
                this.hasnextpage = res.data.pagination.has_next_page
                this.current_page = res.data.pagination.current_page
                this.row = res.data.pagination.items.total
                this.per_page = res.data.pagination.items.per_page
                this.animeData = res.data.data
                this.num = Math.ceil(this.row / this.per_page)
                console.log(this.num)
            })
            .catch((err)=>{
                console.log(err)
            })
        },
        linkGen(pageNum) {
            axios.get(`/seasons/now?page=${pageNum}`).then((res)=>{
                this.hasnextpage = res.data.pagination.has_next_page
                this.current_page = res.data.pagination.current_page
                this.row = res.data.pagination.items.total
                this.per_page = res.data.pagination.items.per_page
                this.animeData = res.data.data
            }).catch((err)=>{
                console.log('Error from linkGen '+err)
            })
        },
        viewDetail(mal_id){
            this.$router.push({path: `/detailpage/${mal_id}`})
        },

    }
}
</script>