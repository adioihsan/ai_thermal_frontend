// toggle side nav
const sideNav = document.getElementById("side-nav")
const sideNavWidth = sideNav.offsetWidth; 

function toggleSideNav(){
    console.log("side nav toggled")
    if(!sideNav.classList.contains("close")){
        sideNav.style.marginLeft = `${sideNavWidth*-1}px`
    }
    else{
        sideNav.style.marginLeft="0px"
    }
    sideNav.classList.toggle("close")
}
// -



