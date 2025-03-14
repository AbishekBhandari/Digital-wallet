document.addEventListener("DOMContentLoaded", function () {
    const seeMoreBtn = document.getElementById("see-more-btn");
    const olderTransactions = document.getElementById("older-transactions");

    seeMoreBtn.addEventListener("click", function () {
        if (olderTransactions.style.display === "none" || olderTransactions.style.display === "") {
            olderTransactions.style.display = "block";
            seeMoreBtn.textContent = "See Less";
        } else {
            olderTransactions.style.display = "none";
            seeMoreBtn.textContent = "See More";
        }
    });
});

document.getElementById('register-form').addEventListener('submit', function(event) {
        let valid = true;

        // Get the dynamically generated username and email fields
        let usernameField = document.getElementById('id_username');
        let emailField = document.getElementById('id_email');

        let usernameError = document.getElementById('username-error');
        let emailError = document.getElementById('email-error');

        // Reset previous errors
        usernameError.style.display = 'none';
        emailError.style.display = 'none';

        // Validate username
        if (!usernameField || usernameField.value.trim() === '') {
            usernameError.style.display = 'block';
            valid = false;
        }

        // Validate email
        if (!emailField || emailField.value.trim() === '' || !emailField.value.includes('@')) {
            emailError.style.display = 'block';
            valid = false;
        }

        // Prevent form submission if validation fails
        if (!valid) {
            event.preventDefault();
        }
    });
