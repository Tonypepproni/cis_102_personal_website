var navItems=document.getElementsByClassName("nav-item")
var colapsed = false

function collapse(){
    if (colapsed==false){
        colapsed = true
        for (var i=0; i < navItems.length; i++){
            navItems[i].style.display = "none"
        }
    }
    else{
        colapsed=false
        for (var i=0; i < navItems.length; i++){
            navItems[i].style.display = "flex"
        }
    }
}

