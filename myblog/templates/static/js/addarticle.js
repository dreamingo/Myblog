$(function(){
	categorySelect();
	var vim = new VIM();
	$('#vimMode').change( function(){
		$('#id_content').addClass('vimField');
		$('.vimInfo').attr("style","display:block");
		// vim.on_log = function(m){ console.log('VIM: '+m) }
		vim.on_log = function(m) {
			var LENGTH = 1;
			m = "-- " + m + ' --';
			var p = $('<span></span>').text( m );
			$('#log').prepend( p );
			if ( $('#log').children().length > LENGTH ) {
				$('#log').children(':last').remove();
			}}
		var target = document.getElementsByClassName('vimField')[0];
		if (target !== null) {
			vim.attach_to( target );
			target.focus();
		}
	})}
)

function categorySelect(){
	var selector = $(".categorySelector");
	console.log(selector.val())
		selector.change(function(){
			$("#id_category").val(selector.val());
			})
}

