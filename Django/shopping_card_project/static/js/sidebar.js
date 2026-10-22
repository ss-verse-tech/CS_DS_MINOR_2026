const sidebar = document.querySelector(".sidebar")
const fa_cross = document.querySelector(".fa-x")
const overlay = document.querySelector(".overlay")
function show_side_bar(){
    sidebar.style.left = "0"
    overlay.style.display = "block"
}

function hide_side_bar(){
    sidebar.style.left = "-700px"
    overlay.style.display = "none"

}