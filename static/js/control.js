

window.onload = function(){

	$('#file').change(function(e){

		var form = new FormData();
		form.append('file', e.target.files[0],{
			contentType: 'multipart/form-data; boundary="your-boundary-string"'
		})

		$.ajax({
            url: '/pdf',
            type: 'POST',
            async: true,
            headers: {
                'Access-Control-Allow-Origin':'*',
            },
			contentType: false,
			processData: false,
            data: form,
            success: function(res){
              console.log(res);
            },
            error: function(error){
              console.log(error)
            }
        });
	})


    $('#submit').click(function(){
        $.ajax({
            url:"/upload",
            type: 'post',
            async: true,
            headers: {
                'Access-Control-Allow-Origin':'*',
                'Content-Type': 'application/json'
            },
            dataType: "json",
            data: JSON.stringify({'article': $('#article').val(), 'content': $('#content').val()}),
            success: function(res){
              console.log(res);
            },
            error: function(error){
              console.log(error)
            }
        });
    })
}