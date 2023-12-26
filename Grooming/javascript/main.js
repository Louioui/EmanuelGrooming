function openNav() {
    document.getElementById("mySidenav").style.width = "10%";
}

function closeNav() {
    document.getElementById("mySidenav").style.width = "0";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
    var modals = document.getElementsByClassName('modal');
    for (var i = 0; i < modals.length; i++) {
        if (event.target == modals[i]) {
            modals[i].style.display = "none";
        }
    }
}

    function submitUser() {
        var username = document.getElementById('username').value;
        var password = document.getElementById('password').value;

        var formData = new FormData();
        formData.append('username', username);
        formData.append('password', password);

        fetch('/php/login.php', {
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

        document.getElementById('id01').style.display = 'none';
    }

    function signupUser() {
        var username = document.getElementById('userName').value;
        var email = document.getElementById('email').value;
        var password = document.getElementById('paswd').value;

        var formData = new FormData();
        formData.append('username', username);
        formData.append('email', email);
        formData.append('password', password);

        fetch('/php/process_signup.php', {
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

        document.getElementById('id02').style.display = 'none';
    }

   
    function showDogDetailsForm() {
        // Add logic to show the Dog Details form, for example:
        document.getElementById('id02').style.display = 'none';
        document.getElementById('id03').style.display = 'block';
    }

    function validateSignUpForm() {
        // Add validation logic for the Sign Up form
        var username = document.getElementById('userName').value;
        var email = document.getElementById('email').value;
        var password = document.getElementById('paswd').value;

        // Example validation: Check if fields are not empty
        if (username === '' || email === '' || password === '') {
            alert('Please fill in all fields.');
            return false;
        }

        // Add more validation logic as needed

        return true;
    }

    function validateDogDetailsForm() {
        // Add validation logic for the Dog Details form
        var dogName = document.getElementById('dogName').value;
        var breed = document.getElementById('breedSelect').value;
        var age = document.getElementById('age').value;

        // Example validation: Check if fields are not empty
        if (dogName === '' || breed === '' || age === '') {
            alert('Please fill in all fields.');
            return false;
        }

        // Add more validation logic as needed

        return true;
    }

    function filterBreeds() {
        // Add logic for filtering breeds based on user input
        var input = document.getElementById('breedSearch').value.toUpperCase();
        var select = document.getElementById('breedSelect');
        var options = select.getElementsByTagName('option');

        for (var i = 0; i < options.length; i++) {
            var option = options[i];
            var txtValue = option.textContent || option.innerText;

            if (txtValue.toUpperCase().indexOf(input) > -1) {
                option.style.display = '';
            } else {
                option.style.display = 'none';
            }
        }
    }

    // Add event listeners
    document.getElementById('id02-cancel-btn').addEventListener('click', function() {
        document.getElementById('id02').style.display = 'none';
    });

    document.getElementById('id02-next-btn').addEventListener('click', showDogDetailsForm);

    document.getElementById('id03-submit-btn').addEventListener('click', function() {
        if (confirm('Are you sure you want to submit the form?')) {
            submitDogDetails();
        }
    });

    document.getElementById('id03-cancel-btn').addEventListener('click', function() {
        document.getElementById('id03').style.display = 'none';
    });

    
    function flipCard(card) {
        card.classList.toggle('clicked');
      }








