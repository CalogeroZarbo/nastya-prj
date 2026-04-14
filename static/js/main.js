// Auto-dismiss flash messages after 4 seconds
document.addEventListener('DOMContentLoaded', function () {
    setTimeout(function () {
        document.querySelectorAll('.alert-dismissible').forEach(function (el) {
            el.classList.remove('show');
        });
    }, 4000);
});
