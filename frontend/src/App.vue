<template>
<div id="app">
<UploadRoutes />
<Chatbot />
</div>
</template>
 
    <script>
    import UploadRoutes from './components/UploadRoutes.vue';
    import Chatbot from './components/Chatbot.vue';
 
    export default {
      name: 'App',
      components: {
        UploadRoutes,
        Chatbot,
      },
    };
</script>
 
    <style>
    #app {
      font-family: Avenir, Helvetica, Arial, sans-serif;
      -webkit-font-smoothing: antialiased;
      -moz-osx-font-smoothing: grayscale;
      text-align: center;
      color: #000000;
      margin-top: 1000px;
    }
</style>