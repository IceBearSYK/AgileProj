document.addEventListener('DOMContentLoaded', function() {
    var searchInput = document.getElementById('search-input');
    var forums = document.querySelectorAll('.btn.thread');

    searchInput.addEventListener('input', function() {
        var filter = searchInput.value.trim().toLowerCase(); // Trim whitespace and convert to lowercase
        console.log('Search query:', filter);
        
        forums.forEach(function(forum) {
            var text = forum.textContent.trim().toLowerCase(); // Trim whitespace and convert to lowercase
            if (text.includes(filter)) {
                forum.style.display = '';
            } else {
                forum.style.display = 'none';
            }
        });
    });
});

