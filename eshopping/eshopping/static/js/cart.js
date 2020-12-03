var updateBtns = document.getElementsByClassName('update-cart')
var value = '8'

$(".dropdown-menu li button").click(function(){
    $(this).parents(".dropdown").find('.btn').html($(this).text() + ' <span class="caret"></span>');
    $(this).parents(".dropdown").find('.btn').val($(this).data('value'));
    value = $(this).parents(".dropdown").find('.btn').val();
  //  $(this).parents(".dropdown").find('#AddProduct').val($(this).data('value'));
  });

for(var i=0; i < updateBtns.length; i++){
    updateBtns[i].addEventListener('click', function(){
        var productId = this.dataset.product
        var size = 0
        if (this.dataset.value){
            size = this.dataset.value
            console.log(size)
        }else{
            size = value
        }
        var action = this.dataset.action
        console.log('productId:', productId, 'action:', action, 'size:', size)

        console.log('USER', user)
        if(user == 'AnonymousUser'){
            //console.log('Not logged in')
            addCookieItem(productId, action, size)
        }else{
            updateUserOrder(productId, action, size)
        }
    })

}


function addCookieItem(productId, action, size){
    console.log('Not logged in....')

    if (action == 'add'){
        let position = (Number(productId)*Number(size))*(Number(size))
        if(cart[position] == undefined){
            cart[position]= {'quantity': 1, 'size': size}
        }else{
            cart[position]['quantity'] +=1
        }
    }

    if(action == 'remove'){
        let position = (Number(productId)*Number(size))*(Number(size))
        cart[position]['quantity'] -= 1

        if(cart[position]['quantity']<=0){
            console.log('Remove item!')
            delete cart[position]
        }
    }
    console.log('Cart: ',cart)
    console.log('size', size)
    document.cookie = 'cart=' + JSON.stringify(cart) + ";domain=;path=/"
    location.reload()
}

function updateUserOrder(productId, action, size){
    console.log('User is logged in, sending data...')

    var url = '/update_item/'
    var position = (Number(productId)*Number(size))*(Number(size))

    fetch(url, {
        method: 'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken':csrftoken,
        },
        body:JSON.stringify({'productId': productId, 'action': action, 'size': size})
    })
    
    .then((response) =>{
        return response.json()
    })
    .then((data) =>{
        console.log('data:', data)
        location.reload()
    })
}