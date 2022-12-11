<template>
  <div id="app">
    <b-navbar variant="faded" type="light" class="bg-info">
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
      text: 'Home',
    }
  }
}
</script>

