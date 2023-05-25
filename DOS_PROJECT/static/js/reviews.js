$("#commentform").submit(function (e) {
    // preventing from page reload and default actions
    e.preventDefault();
    var serializedData = $(this).serialize();
    $.ajax({
        type:'POST',
        // url:"{% url 'courses:reviews' %}",
        url:"/course/review/",
        data:serializedData,
        success:function(response){
            $("#commentform").trigger('reset');
            var instance = JSON.parse(response["instance"]);
            var fields = instance[0]["fields"];
            $("#comment").prepend(
                `<div class="course-details__comment-single">
                <div class="course-details__comment-img">
                    <img src="/static/images/resources/course-details-comment-img1.png" alt="logo"/>
                </div>
                <div class="course-details__comment-text">
                    <div class="course-details__comment-text-top">
                        <h3 class="course-details__comment-text-name">${fields["name"]||""}</h3>
                        <p>${fields["created_at"]||""}</p>
                        <div class="course-details__comment-review-stars">
                            <i class="fas fa-star"></i><!-- /.fas fa-star -->
                            <i class="fas fa-star"></i><!-- /.fas fa-star -->
                            <i class="fas fa-star"></i><!-- /.fas fa-star -->
                            <i class="fas fa-star"></i><!-- /.fas fa-star -->
                            <i class="fas fa-star"></i><!-- /.fas fa-star -->
                        </div>
                    </div>
                    <p class="course-details__comment-text-bottom">${fields["comment"]||""}</p>
                </div>
            </div>`
            )
        },
        error: function (response) {
            // alert the error if any error occured
            alert(response["responseJSON"]["error"]);
        }

    })
})