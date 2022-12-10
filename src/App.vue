<template>
  <div id="app">
    <b-navbar variant="faded" type="light" class="bg-info">
    <b-navbar-brand tag="h1" class="ps-5" variant="primary" to="/1" v-if="!clickgo" @click="click()"> {{ text }}</b-navbar-brand>
    <b-navbar-brand tag="h1" class="ps-5" variant="primary" to="/1" v-else >{{ page1 }}</b-navbar-brand>
  </b-navbar>
    <router-view :key="$route.fullPath" />
  </div>
</template>

<script>
export default {
  name: 'App',
  data() {
    return{
      clickgo: false,
      text: 'Click me',
      page1: 'Home'
    }
  },
  methods: {
      click(){
        this.clickgo = true
      }
    },
}
</script>

