// Vue.js front end for the divorce haiku generator
// A silly little project by Michael Lance
// birthed on/ 4/30/2024
// Last touched 5/2/2024
//-------------------------------------------------------------------------------------------------------------/

// construct a vue app when the page loads
document.addEventListener('DOMContentLoaded', () => {
    const {createApp} = Vue;
    
    const app = createApp({
        data() {
            return {
                generatedHaiku: '',
                activeTab: 1,
                image: '../images/anger1.webp'
            };
            
        },
//-------------------------------------------------------------------------------------------------------------/
        methods: {
            send_haiku() {
                let name = this.$refs.nameInputRef.value;
                let reason = this.$refs.reasonInputRef.value;
                let anger_level =  this.$refs.angerInputRef.value;
                // inform the user to wait for the flask server to respond with the haiku
                this.generatedHaiku = 'generating haiku... please wait...'
                console.log('Sending haiku for:', name, reason, anger_level);
                
                axios({ // asynchronous request sent to the server to generate a haiku
                    method: 'post',
                    url: '/get_haiku',
                    data: {
                        name: name,
                        reason: reason,
                        anger_level: anger_level,
                    },
                    timeout: 12000
                }).then(response => { // response handling
                    if (response.status === 500) {
                        alert('Request failed, please check your OpenAi API key');
                    } else {
                        this.generatedHaiku = response.data.haiku;
                        console.log('Haiku updated to:', this.generatedHaiku); 
                    }
                }).catch(error => {
                    console.error('Failed generate haiu:', error);
                });
//-------------------------------------------------------------------------------------------------------------/
            },
            set_custom_key(){ // save a custom key to .env
            let api_key = this.$refs.apiInputRef.value;
            console.log(api_key)
            axios({ // asynchronous request sent to the server to generate a haiku
                method: 'post',
                url: '/set_api_key',
                data: {
                    key: api_key
                },
                timeout:6000
            }).then(response => {
                if (response.status === 204) {
                    alert('your api_key sucks, get a better one')
                } else {
                    alert('Api key was ingested successfully')
                }
            }) 
            },
//-------------------------------------------------------------------------------------------------------------/
            activate_gen_tab(tabId) {
                this.activeTab = tabId;
            },
        }
    });
    app.mount('#vue-container') // target the app to the vue-container div in the template
})
//-------------------------------------------------------------------------------------------------------------/
/* NOTES
I have a sneaking suspicion that this vue.js implementaiton is not very good. It is lacking in error handling
and does not handle 100% of the JavaScript feature set. I had to force myself to stop working on this part
of the project as I would never have finished in time (to do other finals). I have some intentions to revisit
this project this summer and add the features I decided to cut for time purposes. (saving haikus to a database)
*/
