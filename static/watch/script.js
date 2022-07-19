var menu_icon = document.querySelector(".menu-icon");
var side_bar = document.querySelector(".sidebar");
var container = document.querySelector(".play-container");
var side_bar_info = document.querySelector(".side-bar-info");


menu_icon.onclick = function(){
    side_bar.classList.toggle("small-sidebar");
    container.classList.toggle("large-container");
    side_bar_info.classList.toggle("small-side-bar-info");
}