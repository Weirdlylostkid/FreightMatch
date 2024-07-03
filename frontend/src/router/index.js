import Vue from 'vue';
import Router from 'vue-router';
import UploadRoutes from '../components/UploadRoutes.vue';
import Chatbot from '../components/Chatbot.vue';

Vue.use(Router);

export default new Router({
    routes: [
    {
        path: '/',
        name: 'Home',
        component: {
        template: '<div><h2>Welcome to FreightMatch</h2></div>'
        }
    },
    {
        path: '/upload',
        name: 'UploadRoutes',
        component: UploadRoutes
    },
    {
        path: '/chatbot',
        name: 'Chatbot',
        component: Chatbot
    }
    ]
});