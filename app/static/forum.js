document.addEventListener('DOMContentLoaded', function() {
    var searchInput = document.getElementById('search-input');
    var threads = document.querySelectorAll('.thread');

    searchInput.addEventListener('input', function() {
        var filter = searchInput.value.trim().toLowerCase(); // Trim whitespace and convert to lowercase
        console.log('Search query:', filter);
        
        threads.forEach(function(thread) {
            var text = thread.textContent.trim().toLowerCase(); // Trim whitespace and convert to lowercase
            if (text.includes(filter)) {
                thread.style.display = '';
            } else {
                thread.style.display = 'none';
            }
        });
    });
});

