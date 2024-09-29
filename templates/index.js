function onSubmit(coming) {
    var name = document.getElementById('name').value;
    console.info("name", name);
    if (!name) {
        return;
    }
    fadeForm();
    return;

    // Create JSON object
    const formData = { name: name, coming: coming };

    // Send the form data as JSON using the fetch API
    fetch('/submit', {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(formData)
    })
        .then((response) => {
            if (response.ok) { return response; }
            throw new Error('Something went wrong');
        })
        .then((response) => {
            console.info(response);
            fade()
        })
        .catch((error) => {
            console.error('Error:', error);
            alert('An error occurred during form submission.');
        });

}

function handleInput() {
    const text = document.getElementById('name').value.trim();

    var container = document.getElementById('button-container');
    if (text) {
        container.style.opacity = 1;
        container.style.pointerEvents = "";
    } else {
        container.style.opacity = 0;
        container.style.pointerEvents = "none";
    }
  }


function fadeForm() {
    console.log("fade");
    var rsvp_container = document.getElementById('rsvp-container');

    rsvp_container.style.opacity = 0;
    rsvp_container.style.pointerEvents = "none";

    var title = document.getElementById('title');
    console.log(title.innerText);
    title.innerText = "Thank you\n" + document.getElementById('name').value;
    title.setAttribute("align", "center");
}
