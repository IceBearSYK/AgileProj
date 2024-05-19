function fetchChats() {
    $.ajax({
        url: '/get_chats',
        method: 'GET',
        success: function(response) {
            $('#chat-container').empty();
            response.forEach(function(chat) 
            {
                $('#chat-container').append(`<div class="chat"><strong>${chat.username}:</strong> ${chat.message}</div>`);
            });
        }
    });
}

function sendChat() {
    const message = $('#chat-message').val();
    if (message.trim() === "") return;

    $.ajax({
        url: '/send_chat',
        method: 'POST',
        contentType: 'application/json',
        data: JSON.stringify({message: message}),
        success: function(response) {
            $('#chat-message').val(''); // Clear the input
            fetchChats();
        },
        error: function(xhr) {
            if (xhr.status === 401) {
                alert('You must be logged in to send messages.');
            }
        }
    });
}

// Fetch chats every 2 seconds
setInterval(fetchChats, 2000);
  