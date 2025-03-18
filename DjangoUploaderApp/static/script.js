document.getElementById('file-upload').addEventListener('change', function(event) {
    const fileInput = event.target;
    const fileName = fileInput.files.length > 0 ? fileInput.files[0].name : 'هیچ فایلی انتخاب نشده است';
    document.getElementById('file-name').textContent = fileName;

    const submitBtn = document.getElementById('submit-btn');
    if (fileInput.files.length > 0) {
        submitBtn.removeAttribute('disabled');
    } else {
        submitBtn.setAttribute('disabled', 'true');
    }
});

setTimeout(function() {
    var errorBox = document.getElementById("error-message");
    if (errorBox) {
        errorBox.style.opacity = "0";
        setTimeout(() => errorBox.remove(), 500);
    }
}, 3000);