function openNav() {
    document.getElementById("mySidenav").style.width = "10%";
}

function closeNav() {
    document.getElementById("mySidenav").style.width = "0";
}

document.body.addEventListener('click', function (event) {
    let modals = document.getElementsByClassName('modal');
    for (const element of modals) {
        if (event.target === element) {
            element.style.display = 'none';
        }
    }
});

function submitUser(event) {
    event.preventDefault();

    let username = document.getElementById('username').value;
    let password = document.getElementById('password').value;

    let formData = new FormData();
    formData.append('username', username);
    formData.append('password', password);

    fetch('/Grooming/html/python/index.py', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
        // Handle the response from the server
        // You can perform additional actions based on the server response
    })
    .catch(error => {
        console.error('Error:', error);
    });

    document.getElementById('loginModal').style.display = 'none';
}

function submitDogDetails() {

    let dogName = document.getElementById('dogName').value;
    let breed = document.getElementById('breedSelect').value;
    let age = document.getElementById('age').value;

    let formData = new FormData();
    formData.append('dog_name', dogName);
    formData.append('breed', breed);
    formData.append('age', age);

    fetch('/Grooming/html/python/index.py', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
        // Handle the response from the server
        // You can perform additional actions based on the server response
    })
    .catch(error => {
        console.error('Error:', error);
    });

    document.getElementById('dogDetailsModal').style.display = 'none';
}


function signupUser(event) {
    event.preventDefault();

    let username = document.getElementById('userName').value;
    let email = document.getElementById('email').value;
    let password = document.getElementById('paswd').value;

    let formData = new FormData();
    formData.append('username', username);
    formData.append('email', email);
    formData.append('password', password);

    fetch('/Grooming/html/python/index.py', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
        // Handle the response from the server
        // You can perform additional actions based on the server response
    })
    .catch(error => {
        console.error('Error:', error);
    });

    document.getElementById('signupModal').style.display = 'none';
}

function showDogDetailsForm() {
    // Add logic to show the Dog Details form, for example:
    document.getElementById('signupModal').style.display = 'none';
    document.getElementById('dogDetailsModal').style.display = 'block';
}

function validateSignUpForm() {
    let username = document.getElementById('userName').value;
    let email = document.getElementById('email').value;
    let password = document.getElementById('paswd').value;

    if (username === '' || email === '' || password === '') {
        alert('Please fill in all fields.');
        return false;
    }

    // Add more validation logic as needed

    return true;
}

function validateDogDetailsForm() {
    let dogName = document.getElementById('dogName').value;
    let breed = document.getElementById('breedSelect').value;
    let age = document.getElementById('age').value;

    if (dogName === '' || breed === '' || age === '') {
        alert('Please fill in all fields.');
        return false;
    }

    // Add more validation logic as needed

    return true;
}

function filterBreeds() {
    let input = document.getElementById('breedSearch').value.toUpperCase();
    let select = document.getElementById('breedSelect');
    let options = select.getElementsByTagName('option');

    for (const element of options) {
        let option = element;
        let txtValue = option.textContent || option.innerText;

        if (txtValue.toUpperCase().indexOf(input) > -1) {
            option.style.display = '';
        } else {
            option.style.display = 'none';
        }
    }
}

// Event listeners
document.getElementById('signupCancelBtn').addEventListener('click', function() {
    document.getElementById('signupModal').style.display = 'none';
});

document.getElementById('signupNextBtn').addEventListener('click', showDogDetailsForm);

document.getElementById('dogDetailsSubmitBtn').addEventListener('click', function() {
    if (confirm('Are you sure you want to submit the form?')) {
        submitDogDetails();
    }
});

document.getElementById('dogDetailsCancelBtn').addEventListener('click', function() {
    document.getElementById('dogDetailsModal').style.display = 'none';
});

function flipCard(card) {
    card.classList.toggle('clicked');
}



