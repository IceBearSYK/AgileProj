function fetchChats() {
    $.ajax({
        url: '/get_chats',
        method: 'GET',
        success: function(response) {
            $('#chat-container').empty();
            response.forEach(function(chat) {
            if (chat.topic == "fishing") {
                $('#chat-container').append(`<div class="chat"><strong>${chat.username}:</strong> ${chat.message}</div>`);
                }
            });
        }
    });
}

function sendChat() {
    const message = $('#chat-message').val();
    const username = "User" + Math.floor(Math.random() * 100); // Simple username generation
    const topic = "gaming"
    if (message.trim() === "") return;

    $.ajax({
        url: '/send_chat',
        method: 'POST',
        contentType: 'application/json',
        data: JSON.stringify({username: username, message: message, topic: topic}),
        success: function(response) {
          $('#chat-message').val(''); // Clear the input
          fetchChats();
        }
    });
}

// Fetch chats every 2 seconds
setInterval(fetchChats, 2000);