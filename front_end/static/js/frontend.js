// Vue.js front end for the divorce haiku generator
// A silly little project by Michael Lance
// birthed on/ 4/30/2024
// Last touched 5/1/2024
//-------------------------------------------------------------------------------------------------------------//

// construct a vue app when the page loads
document.addEventListener('DOMContentLoaded', () => {
    const {createApp} = Vue;
    
    const app = createApp({
        data() {
            return {
                generatedHaiku: '',
                activeTab: 1,
            };
        },
        methods: {
            send_activate_out_tab(tabId) {
                this.activeOutTab = tabId;
            },
            send_haiku() {
                let name = this.$refs.nameInputRef.value;
                let reason = this.$refs.reasonInputRef.value;
                let anger_level =  this.$refs.angerInputRef.value;
                
                this.generatedHaiku = 'generating haiku... please wait...'
                console.log('Sending haiku for:', name, reason, anger_level);
                
                axios({
                    method: 'post',
                    url: '/get_haiku',
                    data: {
                        name: name,
                        reason: reason,
                        anger_level: anger_level,
                    },
                    timeout: 6000
                }).then(response => {
                    if (response.status === 204) {
                        alert('Request failed, please check your OpenAi API key');
                    } else {
                        this.generatedHaiku = response.data.haiku;
                        console.log('Haiku updated to:', this.generatedHaiku); 
                    }
                })
            },
            set_custom_key(){
            let api_key = this.$refs.apiInputRef.value;
            console.log(api_key)
            axios({
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
            activate_gen_tab(tabId) {
                this.activeTab = tabId;
            },
        }
    });

    app.mount('#vue-container')
})