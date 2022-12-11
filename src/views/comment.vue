<template>
    <div class="row">
        <div class="col-12">
            <span>Comment</span>
            <b-form-textarea
            id="textarea"
            v-model="text"
            placeholder="Enter something..."
            rows="2"
            max-rows="5"
        ></b-form-textarea>
        </div>
        <div class="col-6">
            <span for="b-input1">Name</span>
            <b-input id="b-input1" v-model="name" placeholder="input your Name"/>
        </div>
        <div class="col-2">
            <b-button class="mt-4" variant="outline-primary"
            @click="postComment()"
            >
            Submit
        </b-button>
        </div>
    <pre class="mt-3 mb-0">{{ text }}</pre>
    <div class="col-12">
        <b-card no-body 
       >
            <div v-for="i in dataComment" :key="i[0]">
                <b-card :title="i[2]"  >
                <div class="bg-secondary text-light">
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
            dataComment:[]
        }
    },
    created(){
        console.log("id is comming", this.animedata)
        // this.getComment(this.animedata)
    },
    watch:{
        animedata() {
            console.log("Update animedata:", this.animedata)
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
        },
        getComment(animeid){
            axios.get(`http://127.0.0.1:5000/getcomment/${animeid}`)
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