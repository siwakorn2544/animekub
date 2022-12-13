<template>
    <div>
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
                style="height: fit-content; "
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
    </div>
</template>

<script>
import axios from '../plugin/axios' 
export default {
    name: "animeSearch",
    data(){
        return{
            animeData:[],
        }
    },
    methods:{
        getAnimebyName(){
            if (this.name == ""){
                this.animeData = []
                alert("plaese type something")
            }
            else{
            axios.get(`/anime?letter=${this.name}`)
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
            }
        },
        linkGenAnimeName(name,pageNum) {
            axios.get(`/anime?letter=${name}&page=${pageNum}`).then((res)=>{
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