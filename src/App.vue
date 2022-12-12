<template>
  <div
    id="app"
    style="background-image: linear-gradient(rgba(255,255,255,0.6), rgba(255,255,255,0.6)), url('/bg.png');"
  >
    <b-navbar variant="faded" type="light" class="py-3" style="background-color: pink;">
    <b-navbar-brand tag="h1" class="ps-5" variant="primary" to="/" >{{ text }}</b-navbar-brand>

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
      text: 'Animekub',
    }
  }
}
</script>

