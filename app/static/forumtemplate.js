var topic = window.location.pathname.split('/')[2]; // Extract the forum topic from the URL

function fetchChats() {
  $.ajax({
      url: '/get_chats/' + topic,
      method: 'GET',
      success: function(response) {
          $('#chat-container').empty();
          response.forEach(function(chat) {
              $('#chat-container').append(`<div class="chat"><strong>${chat.username}:</strong> ${chat.message}</div>`);
          });
      }
  });
}

function sendChat() {
  const message = $('#chat-message').val();
  const username = "User" + Math.floor(Math.random() * 100); // Simple username generation
  if (message.trim() === "") return;

  $.ajax({
      url: '/send_chat/' + topic,
      method: 'POST',
      contentType: 'application/json',
      data: JSON.stringify({username: username, message: message}),
      success: function(response) {
          $('#chat-message').val(''); // Clear the input
          fetchChats();
      }
  });
}

// Fetch chats every 2 seconds
setInterval(fetchChats, 2000);