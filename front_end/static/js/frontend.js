// Vue.js front end for the divorce haiku generator
// A silly little project by Michael Lance
// birthed on/ 4/30/2024
// Last touched 4/30/2024
//-------------------------------------------------------------------------------------------------------------//

// construct a vue app when the page loads
document.addEventListener('DOMContentLoaded', () => {
    const {createApp} = Vue;

    const app = createApp({
        data() {
            return {
                message: 'hello from Vue 3'
            };
        },
        methods: {
            updateMessage() {
                this.message = "fuck you"
            }
        }
    });

    app.mount('#vue-container')
})