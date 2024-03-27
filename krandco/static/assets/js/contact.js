
// Contact Form
$(document).ready(function(){
    $('#submit-btn').click(function(){

        let name = $('#name').val()
        let email = $('#email').val()
        let phone = $('#phone').val()
        let address = $('#address').val()
        let comments = $('#comments').val()
        let csrfmiddlewaretoken = $('input[name=csrfmiddlewaretoken]').val()

        let data = new FormData()
        data.append('name',name),
        data.append('email',email),
        data.append('phone',phone),
        data.append('address',address),
        data.append('comments',comments),
        data.append('csrfmiddlewaretoken',csrfmiddlewaretoken)

        $.ajax({
            type:'POST',
            url:'/contact/',
            processData:false,
            contentType:false,
            cache:false,
            data:data,
            success:function(data, status, xhr){
                $('#form-submit')[0].reset();
                if(data.success === true){
                  alert("Form Submission Successfull")
                } else{
                    alert("Invalid Form Submission")
                }   
            },
            error:function(data){
                alert("Form Submission Failed")
            }
            
        })

    })
})