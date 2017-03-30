<template>
    <router-view></router-view>
</template>

<script>
  export default {
    name: 'app',
    data: function() {
      return {
        title: 'APLIKASI LAYANAN SERVIS'
      }
    },
    head: {
      title: function() {
        return {
          inner: this.title,
          separator: '-',
          complement: 'SUNTECH'
        }
      }
    },
    mounted: function() {
    // $('.button-collapse').sideNav();
     alert("DEMO");
    }
  }
</script>

<style>

</style>
