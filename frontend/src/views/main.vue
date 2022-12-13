<template>
    <div>
    </div>
</template>

<script>
export default {
    data(){
        return{
            name:"",
            text:""
        }
    },
    created() {
        localStorage.clear()
        this.$router.push("/main/"+1+"/"+"season")
    },

};
</script>