// Look up on my creation
// Poorly written by Michael Lance (I don't know much JS)
// Date of oopsie: 4/30/2024
// Last ruined: 4/30/2024
// If they make it illegal for me to program, I understand
//-------------------------------------------------------------------------------------------------------------------//


document.addEventListener('DOMContentLoaded', function() {
    var mainContent = document.getElementById('main-window');

    document.getElementById('peek-background').addEventListener('mousedown', function() {
        mainContent.style.display = 'none';
    });

    window.addEventListener('mouseup', function() {
        mainContent.style.display = 'flex'; 
    });
});