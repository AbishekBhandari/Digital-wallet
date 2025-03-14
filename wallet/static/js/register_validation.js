let form = document.getElementById('register-form');
let usernameField = document.getElementById('id_username');
    let emailField = document.getElementById('id_email');
    let passwordField1 = document.getElementById('id_password1');
    let passwordField2 = document.getElementById('id_password2')

    let usernameError = document.getElementById('username-error');
    let emailError = document.getElementById('email-error');
    let passwordError1 = document.getElementById('password1-error');
    let passwordError2 = document.getElementById('password2-error');

    function hideError(event) {
    let target = event.target;
    if (target === usernameField) {
        usernameError.style.display = 'none';
    } else if (target === emailField) {
        emailError.style.display = 'none';
    }
    else if (target === passwordField1) {
        passwordError1.style.display = 'none';
    }
    else if (target === passwordField2) {
        passwordError2.style.display = 'none';
    }
}
usernameField.addEventListener('input', hideError);
emailField.addEventListener('input', hideError);
passwordField1.addEventListener('input', hideError);
passwordField2.addEventListener('input', hideError);

form.addEventListener('submit', function(event) {

    let valid = true;

    usernameError.style.display = 'none';
    emailError.style.display = 'none';
    passwordError1.style.display = 'none';
    passwordError2.style.display = 'none';
    // Validate username
    if (!usernameField || usernameField.value.trim() === '') {
        console.warn("⚠️ Username is empty!");
        usernameError.style.display = 'block';
        valid = false;
    }

    // Validate email
    if (!emailField || emailField.value.trim() === '' || !emailField.value.includes('@')) {
        console.warn("⚠️ Email is invalid!");
        emailError.style.display = 'block';
        valid = false;
    }

    if (passwordField1.value.trim() === '' || passwordField2.value.trim() === '') {
        console.warn("⚠️ Password is required and must match!");
        passwordError1.style.display = 'block';
        passwordError1.style.display = 'block';
        valid = false;
    }

    if (!valid) {
        console.log("❌ Form validation failed, preventing submission.");
        event.preventDefault();
    }
});