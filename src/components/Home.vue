<template>
  <div class="">
    <nav class="light-blue lighten-1" role="navigation">
        
    <div class="nav-wrapper container"><a id="logo-container" href="#" class="brand-logo">BANTECH - SUNTECH</a>
      <ul class="right hide-on-med-and-down">
        <li><a href="#">Navbar Link</a></li>
      </ul>

      <ul id="nav-mobile" class="side-nav">
        <li><a href="#">Navbar Link</a></li>
      </ul>
      <a href="#" data-activates="nav-mobile" class="button-collapse"><i class="material-icons">menu</i></a>
    </div>
    
    <div class="parallax-container">
      <div class="parallax"><img src="https://lorempixel.com/920/847/city/4"></div>
    </div>

    </nav>
  </div>
</template>

<script>
    export default {
        name: 'hello',
        data() {
            return {
                msg: 'Selamat Datang Your Vue.js App'
            }
        }
    }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
