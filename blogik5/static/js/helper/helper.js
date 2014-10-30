(function (){
	// -------------------------------------------------------------------------------------- windows
	$('.all_news .more_link').on('click', function(event){	
		event.preventDefault();

		console.log(1111);

		var	text = $(this).closest('.article').find('.info').html(),
			head = $(this).closest('.article').find('.h3').html();

		console.log(head);
		console.log(text);

		$('#modal-9 .modal-body').html(text);
		$('#modal-9 .modal-title').html(head);

		$('#modal-9').modal();
	});	
})();

