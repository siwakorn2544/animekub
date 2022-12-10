<template>
    <b-card no-body>
        
    <b-form-textarea
      id="textarea"
      v-model="text"
      placeholder="Enter something..."
      rows="3"
      max-rows="6"
    ></b-form-textarea>

    <pre class="mt-3 mb-0">{{ text }}</pre>
    </b-card>
</template>

<script>
export default {
    name:"comments",
    data(){
        return{
            name:"",
            text:""
        }
    }

};



</script>