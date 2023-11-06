var body = document.querySelector('body')
const menuBtn = document.querySelector(".menu__btn");
const menuList = document.querySelector(".menu__list");
function toggleMenuVisibility() {
menuList.classList.toggle("hide");
}
menuBtn.addEventListener("click", toggleMenuVisibility);
function myFunction() {
    document.getElementById("myDropdown").classList.toggle("show");
}
window.onclick = function(event) {
    if (!event.target.matches('.dropbtn')) {
  
      var dropdowns = document.getElementsByClassName("dropdown-content");
      var i;
      for (i = 0; i < dropdowns.length; i++) {
        var openDropdown = dropdowns[i];
        if (openDropdown.classList.contains('show')) {
          openDropdown.classList.remove('show');
        }
      }
    }
  }