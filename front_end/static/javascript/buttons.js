// The button does whatever it does
// Poorly written by Michael Lance (I don't know much JS)
// Date of oopsie: 4/28/2024
// Last ruined: 4/28.2024
// If they make it illegal for me to program, I understand
//-------------------------------------------------------------------------------------------------------------------//

function changeBackground() {
    var anger = document.getElementById('anger_input').value;
    document.body.style.backgroundImage =  `url('static/images/anger${anger}.webp')`
}