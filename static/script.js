document.addEventListener('DOMContentLoaded', function () {
    // Select elements using their IDs
    let hill1 = document.getElementById('hill1');
    let hill2 = document.getElementById('hill2');
    let hill3 = document.getElementById('hill3');
    let hill4 = document.getElementById('hill4');
    let hill5 = document.getElementById('hill5');
    let tree = document.getElementById('tree');
    let text = document.getElementById('text');
    let leaf = document.getElementById('leaf');
    let plant = document.getElementById('plant');

    // Add event listener for the scroll event
    window.addEventListener('scroll', () => {
        // Calculate the scroll value
        let value = window.scrollY;

        // Apply parallax effect to elements based on scroll value
        hill1.style.top = value * 0.5 + 'px';
        hill2.style.top = value * 0.3 + 'px';
        hill3.style.top = value * 0.2 + 'px';
        hill4.style.top = value * 0.1 + 'px';
        hill5.style.top = value * 0.05 + 'px';
        tree.style.top = value * -0.2 + 'px';
        text.style.marginTop = value * 1.5 + 'px'; // Adjusted multiplier for the title
        leaf.style.marginTop = value * 0.5 + 'px';
        plant.style.marginTop = value * 0.4 + 'px';
    });
});
// Get the "About" link element by its ID
let aboutLink = document.getElementById('aboutLink');

// Add event listener to the "About" link
aboutLink.addEventListener('click', function(event) {
    event.preventDefault(); // Prevent the default behavior of the link

    // Scroll to the second section
    document.querySelector('.sec').scrollIntoView({
        behavior: 'smooth' // Use smooth scrolling behavior
    });
});


// JavaScript code to show the alert message
function showAlert(message) {
    var alertDiv = document.getElementById('alertMessage');
    alertDiv.innerHTML = message;
    alertDiv.style.display = 'block';
    setTimeout(function() {
        alertDiv.style.display = 'none';
    }, 3000); // Hide the alert message after 3 seconds (adjust as needed)
}
