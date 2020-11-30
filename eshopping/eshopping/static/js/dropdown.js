var drop = document.getElementsByName('item');
var list_of_sizes = []

if (drop) {
    for(var i=0; i < drop.length; i++){
        drop[i].id = String(i)
        drop[i].addEventListener('click', returnNum)
    }
}

function returnNum() {
    if (drop[0].click()){
        console.log(0)
    }
}



