
    function getToken(name) {
      let cookieValue = null;
      if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
          const cookie = cookies[i].trim();
          // Does this cookie string begin with the name we want?
          if (cookie.substring(0, name.length + 1) === (name + '=')) {
            cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
            break;
          }
        }
      }
      return cookieValue;
    }
    const csrftoken = getToken('csrftoken');
    // 
    function getCookie(name) {
      var cookieArr = document.cookie.split(";");

      for (var x = 0; x < cookieArr.length; x++) {
        var cookiePair = cookieArr[x].split("=");

        if (name == cookiePair[0].trim()) {

          return decodeURIComponent(cookiePair[1]);
        }
      }
      return null;
    }

    var cart = JSON.parse(getCookie('cart'))
    //d
    if (cart == undefined) {
      cart = {}
      console.log('Cart Created!', cart)
      document.cookie = 'cart=' + JSON.stringify(cart) + ";domain=;path=/"
    }
    console.log('Cart', cart)