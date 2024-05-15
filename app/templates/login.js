document.addEventListener("DOMContentLoaded", function() {
    document.getElementById('loginButton').addEventListener('click', validateLoginForm);
});

function validateLoginForm() {
    var username = document.getElementById('username').value;
    var password = document.getElementById('password').value;
    if (username === "" || password === "") {
        alert("Both username and password are required!");
        return false;
    } else {
        // Submit the form if both fields are filled
        document.getElementById('loginForm').submit();
    }
}
