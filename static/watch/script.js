var menu_icon = document.querySelector(".menu-icon");
var side_bar = document.querySelector(".sidebar");
var container = document.querySelector(".play-container");
var side_bar_info = document.querySelector(".side-bar-info");
var comment_field = document.querySelector(".comment-input");
var toggler = document.querySelector(".toggler");
var cancel_btn = document.querySelector(".toggler button");

menu_icon.onclick = function () {
    side_bar.classList.toggle("small-sidebar");
    container.classList.toggle("large-container");
    side_bar_info.classList.toggle("small-side-bar-info");
}

comment_field.onfocus = function () {
    toggler.style.display = "flex";
}

function show_reply(v) {
    document.querySelector('.comment-replies-' + v).style.display = "block";
};

function cancel_reply(v) {
    console.log('saved2');
    document.querySelector('.comment-replies-' + v).style.display = "none";
    console.log('saved3');
};
