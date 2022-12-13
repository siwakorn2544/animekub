<template>
    <div class="row mt-4">
        <div class="col-12">
            <p class="my-2">Comment</p>
            <b-form-textarea
                id="textarea"
                v-model="text"
                placeholder="Enter something ..."
                rows="2"
                max-rows="5"
            ></b-form-textarea>
        </div>
        <div class="col-6 mt-3">
            <p class="my-2" for="b-input1">Name</p>
            <div class="input-group">
                <b-input class="form-control" id="b-input1" v-model="name" placeholder="Name ..."/>
                <b-button variant="outline-primary"
                    @click="postComment()"
                    >
                    Submit
                </b-button>
            </div>
        </div>
    <pre class="m-3 mb-0">{{ text }}</pre>
    <div class="col-12">
        <b-card no-body 
        class="mt-3" 
       >
            <div v-for="i in dataComment" :key="i[0]">
                <b-card :title="i[2]" class="m-2" >
                <div class="text-dark">
                    {{i[3]}}
                </div>
                </b-card>
            </div>
            
        </b-card>
    </div>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    name:"comments",
    props: ['animedata'],
    data(){
        return{
            name:"",
            text:"",
            animeid_1: this.animedata,
            dataComment:[],
            chk:true
        }
    },
    created(){
        console.log("id is comming", this.animedata)
        this.getComment(this.animedata)
    },
    watch:{
        animedata() {
            console.log("Update animedata:", this.animedata)
            this.getComment(this.animedata)
            this.chk = true
        },
        postComment(){
            this.getComment(this.animedata)
        }
    },
    methods:{
        postComment(){
            let data = {
                animeid:this.$props.animedata,
                personname:this.name,
                comment:this.text
            }
            console.log(data)
            axios.post(`http://127.0.0.1:5000/postcomment`,data,{
                headers: {"Access-Control-Allow-Origin": "*"}
            })

            .then((res)=>{
                console.log(res);
            }).catch((err)=>{
                console.log(err)
            })
            this.text =""
            this.name =""
        },
        getComment(animeid){
            axios.get(`https://animekub-2i4f4rj7c-siwakorn2544.vercel.app/getcomment/44511/${animeid}`)
            .then((res)=>{
                console.log("Heelooo",res.data)
                this.dataComment = res.data
                console.log(this.dataComment[0][2])
            }).catch((err)=>{
                console.log(err)
            })
        }
    },
};

</script>