document.getElementById('file-upload').addEventListener('change', function(event) {
    const fileName = event.target.files[0] ? event.target.files[0].name : 'هیچ فایلی انتخاب نشده است';
    document.getElementById('file-name').textContent = fileName;
});
