// 10 Background Images because I hate myself
// Poorly written by Michael Lance (I don't know much JS)
// Date of oopsie: 4/30/2024
// Last ruined: 4/30/2024
// If they make it illegal for me to program, I understand
//-------------------------------------------------------------------------------------------------------------------//

document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('anger_input').addEventListener('input', function(){
        var anger = document.getElementById('anger_input').value;
        document.body.style.backgroundImage = `url('static/images/anger${anger}.webp')`
    })
})