document.getElementById('btnPopup').onclick = function() {
   alert("button was clicked");
}​;​

var btnPopup = document.getElementById('btnPopup');
var overlay = document.getElementById('overlay');
btnPopup.addEventListener('click',openMoadl);
function openMoadl() {
overlay.style.display='block';
}

var btnClose = document.getElementById('btnClose');:
btnClose.addEventListener('click',closeModal);
function closeModal() {
overlay.style.display='none';
}:
