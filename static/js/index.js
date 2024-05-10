document.getElementById('myButton').addEventListener('click', function() {
    // Send an HTTP request to the Django view
    fetch(`{% url '${my_function()}' %}`)
    .then(response => {
        if (response.ok) {
            console.log('Button click successful');
        } else {
            console.error('Error while clicking button');
        }
    });
});