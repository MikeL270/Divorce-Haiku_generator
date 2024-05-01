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
                genTabs: [{isVisible: true}, {isVisible: false}],
                outTabs: [{isVisible: true}, {isVisible: false}],
            };
        },
        computed: {
            displayState: function () {
                return this.isVisible ? "flex" : "none"; 
            }
        },
        methods: {
            send_haiku() {
                var name = this.$refs.nameInputRef.value;
                var reason = this.$refs.reasonInputRef.value;
                var anger_level =  this.$refs.angerInputRef.value;

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
            toggle_tab(tabArray, index) {
                this[tabArray][index].isVisible = !this[tabArray][index].isVisible;
            },
        }
    });

    app.mount('#vue-container')
})