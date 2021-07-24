jQuery.noConflict(); 
jQuery(document).ready(function ($) {
    $(document).on('click', '#like-button', function (e) {
        e.preventDefault();
        $.ajax({
            type: 'POST',
            url: "/likepost",
            data: {
                'postid': '{{post.id}}', 
                csrfmiddlewaretoken: '{{ csrf_token }}',
                action: 'post'
            },
            success: function (json) {
                document.getElementById("like_count").innerHTML = json['result']
                console.log(json)  
            },
            error: function (xhr, errmsg, err) {
                
            }
        });
        
    });
    });



function submit() {
    alert("Your data is Submitted :)")
}