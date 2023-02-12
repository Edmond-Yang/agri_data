

window.onload = function(){

	$('#flash').hide()

	$('#file').change(function(e){

		var form = new FormData();
		form.append('file', e.target.files[0])

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
            success: function(response){
              $('#article').val(response['data']['標題'])
              $('#content').val(response['data']['全文'])
              document.querySelector('#second').scrollIntoView();
            },
            error: function(error){
              alert('發生錯誤，請於NCHU NLP LAB聯繫')
            }
        });
	})


    $('#submit').click(function(){
		data = {'article': $('#article').val(), 'content': $('#content').val()}
		console.log($('#article').val())
		console.log($('#content').val())
        $.ajax({
            url:"/upload",
            type: 'post',
            async: true,
            headers: {
                'Access-Control-Allow-Origin':'*',
                'Content-Type': 'application/json'
            },
            dataType: "json",
            data: JSON.stringify(data),
            success: function(res){

				if(res['status'] == 'success'){
					$('#article').val('')
					$('#content').val('')
				}
				$("#flash").removeClass();
				$('#flash').addClass(res['status'])
				$('#flash').html('<p>' + res['details'] + '</p>')

				document.querySelector('#header').scrollIntoView()

				$('#flash').fadeIn("slow")
				setTimeout(function(){
					$('#flash').fadeOut("slow")
				}, 1500)
            },
            error: function(error){
				alert('發生錯誤，請於NCHU NLP LAB聯繫')
            }
        });
    })
}