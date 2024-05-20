$(document).ready(function() {
    // Function to handle deleting messages
    $('.delete-message').click(function() {
        var messageId = $(this).data('message-id');
        $.ajax({
            url: '/delete_message/' + messageId,
            method: 'POST',
            success: function(response) {
                // Reload the page after successful deletion
                location.reload();
            },
            error: function(xhr, status, error) {
                console.error(xhr.responseText);
            }
        });
    });

    // Function to fetch messages
    function fetchChats() {
        $.ajax({
            url: '/get_chats',
            method: 'GET',
            success: function(response) {
                $('#message-container').empty(); // Clear the message container
                response.forEach(function(chat) {
                    // Append each message to the message container
                    $('#message-container').append('<div>' + chat.username + ': ' + chat.message + '</div>');
                });
            },
            error: function(xhr, status, error) {
                console.error(xhr.responseText);
            }
        });
    }
    
    // Fetch messages initially when the page loads
    fetchChats();
});
