// Handles Axios requests sent from the client to the flask webserver. 
// Poorly written by Michael Lance (I don't know much JS)
// Date of oopsie: 4/28/2024
// Last ruined: 4/30/2024
// If they make it illegal for me to program, I understand
//-------------------------------------------------------------------------------------------------------------------//

document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('generate_button').addEventListener('click', function() {
        var name = document.getElementById('name_input').value;
        var reason = document.getElementById('reason_input').value;
        var anger_level = document.getElementById('anger_input').value;

        axios({
            method: 'post',
            url: 'get_haiku',
            data: {
                name: name,
                reason: reason,
                anger_level: anger_level,
            },
            timeout: 6000
        }).then(function(response) {
            if (response.status === 204) {
                document.getElementById('haiku-box').innerHTML = 'Haiku Request Failed, Check your OpenAI account';
            } else {
                document.getElementById('haiku-box').innerHTML = response.data.haiku;
            }
        }).catch(function(error){
            if (error.code === 'ECONNABORTED') {
                document.getElementById('haiku-box').innerHTML = 'Request timed out, please try again'
            } else {
                var errorMessage = error.response ? error.response.data : error.message;
                document.getElementById('haiku-box').innerHTML = 'Error executing command: ' + errorMessage;
            }
        });
    });
});

// vuejs -- use it or fail the class