$("#add_to_cart").submit(function (e) {
    // preventing from page reload and default actions
    e.preventDefault();
    var Data = $(this).serialize();
    $.ajax({
        type:'POST',
        // url:"{% url 'courses:reviews' %}",
        url:"/cart/create/",
        data:Data,
        success:function(response){
            var instance = JSON.parse(response["instance"]);
            if(instance != ''){
                document.getElementById('lblCartCount').innerHTML = instance;
            document.getElementById('cart_').innerHTML = `<div class="main-menu__right-cart-box">
            <a href="/cart/"><span class="icon-shopping-cart"></span></a>
            <span class='badge badge-warning cart' id='lblCartCount'> ${instance} </span>
        </div>
        <div class="main-menu__right-search-box">
         <a href="{% url 'logout' %}" class="thm-btn">Logout</a>
        </div>
    `;
            }
            
            // $("#cart_").prepend(
            //     `<div class="main-menu__right-cart-box">
            //     <a href="#"><span class="icon-shopping-cart"></span></a>
            //     <span class='badge badge-warning cart' id='lblCartCount'> ${instance} </span>
            // </div>`)
        },
        error: function (response) {
            // alert the error if any error occured
            alert(response["responseJSON"]["error"]);
        }

    })
})


$("#add_to_cart2").submit(function (e) {
    // preventing from page reload and default actions
    e.preventDefault();
    var Data = $(this).serialize();
    $.ajax({
        type:'POST',
        // url:"{% url 'courses:reviews' %}",
        url:"/cart/create/",
        data:Data,
        success:function(response){
            var instance = JSON.parse(response["instance"]);
            if(instance != ''){
                document.getElementById('lblCartCount').innerHTML = instance;
            document.getElementById('cart_').innerHTML = `<div class="main-menu__right-cart-box">
            <a href="/cart/"><span class="icon-shopping-cart"></span></a>
            <span class='badge badge-warning cart' id='lblCartCount'> ${instance} </span>
        </div>
        <div class="main-menu__right-search-box">
        <a href="{% url 'logout' %}" class="thm-btn search-toggler">Logout</a>
    </div>`;
            }
            
            // $("#cart_").prepend(
            //     `<div class="main-menu__right-cart-box">
            //     <a href="#"><span class="icon-shopping-cart"></span></a>
            //     <span class='badge badge-warning cart' id='lblCartCount'> ${instance} </span>
            // </div>`)
        },
        error: function (response) {
            // alert the error if any error occured
            alert(response["responseJSON"]["error"]);
        }

    })
})