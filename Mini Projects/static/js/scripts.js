document.addEventListener("DOMContentLoaded", function() {
    const form = document.querySelector('form');
    const textarea = document.querySelector('textarea');
    form.addEventListener('submit', function() {
        setTimeout(() => {
            textarea.value = '';
        }, 10);
    });
});
