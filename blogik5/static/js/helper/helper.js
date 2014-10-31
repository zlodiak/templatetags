(function (){
	// -------------------------------------------------------------------------------------- feedback
	$('.nav_main .mail_link').on('click', function(event){	
		event.preventDefault();

		$('#modal-10').modal();
	});

	$('#submitFeedback').on('click', function(event){	
		var	flag = false,
			author = $('#id_author'),
			subject = $('#id_subject'),
			message = $('#id_message'),
			authorVal = $.trim(author.val()),
			subjectVal = $.trim(subject.val()),
			messageVal = $.trim(message.val());

		event.preventDefault();

		if(!authorVal){
			author.addClass('shine');
			
			flag = true;
		}
		else{
			author.removeClass('shine');
		};

		if(!subjectVal){
			subject.addClass('shine');
			
			flag = true;
		}
		else{
			subject.removeClass('shine');
		};

		if(!messageVal){
			message.addClass('shine');
			
			flag = true;
		}
		else{
			message.removeClass('shine');
		};	

		if(!flag){
			$('#feedbackForm').submit();
		};	
	});

	// -------------------------------------------------------------------------------------- windows
	$('.all_news .more_link, .last_news .more_link').on('click', function(event){	
		event.preventDefault();

		//console.log(1111);

		var	text = $(this).closest('.article').find('.info').html(),
			head = $(this).closest('.article').find('.h3').html();

		//console.log(head);
		//console.log(text);

		$('#modal-9 .modal-body').html(text);
		$('#modal-9 .modal-title').html(head);

		$('#modal-9').modal();
	});	
})();

