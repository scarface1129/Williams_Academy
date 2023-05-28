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
            <a href="#"><span class="icon-shopping-cart"></span></a>
            <span class='badge badge-warning cart' id='lblCartCount'> ${instance} </span>
        </div>
        <div class="main-menu__right-search-box">
        <a href="#" class="thm-btn search-toggler">Search</a>
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