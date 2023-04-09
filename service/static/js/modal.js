// This code assumes that you're using jQuery for DOM manipulation
$("form").on("submit", function (event) {
  event.preventDefault(); // Prevent the form from submitting normally

  // Get the values of the username and password fields
  var username = $("#username").val();
  var password = $("#password").val();

  // Send an AJAX request to the Flask server to authenticate the user
  $.ajax({
    url: "/login",
    method: "POST",
    data: {
      username: username,
      password: password,
    },
    success: function (response) {
      // If authentication succeeds, redirect the user to the main.html page
      window.location.href = "/index.html";
    },
    error: function (xhr, status, error) {
      // If authentication fails, display an error message
      alert("Invalid username or password");
    },
  });
});
