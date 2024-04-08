function upload_loader(url){
document.getElementById(url).addEventListener('submit', function() {
    // Loader overlay when file is submitted
    document.getElementById('loader-overlay').style.display = 'flex';
});
}

function options_loader(url){
    document.getElementById(url).addEventListener('submit', function() {
        // Loader overlay when options are submitted
        document.getElementById('loader-overlay').style.display = 'flex';
    });
    }
