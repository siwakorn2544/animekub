<template>
  <div id="app">
    <b-navbar variant="faded" type="light" class="bg-info">
    <b-navbar-brand tag="h1" class="ps-5" variant="primary">Home</b-navbar-brand>
  </b-navbar>
    <router-view :key="$route.fullPath" />
  </div>
</template>

<script>
export default {
  name: 'App',
  data() {
    return{
      
    }
  }
}
</script>

<style>
/* body {
  background-image: url('https://images.pexels.com/photos/1323550/pexels-photo-1323550.jpeg');
} */
</style>
