(function($){
"use strict"

var openedSidePanel;	
	
// Page Preloader //
		$(window).on('load', function(){
		$('.fade-in').css({ position: 'relative', opacity: 0, top: -14 });
		setTimeout(function(){
			$('#preload-content').fadeOut(400, function(){
				$('#preload').fadeOut(800);
				setTimeout(function(){
					$('.fade-in').each(function(index) {
						$(this).delay(400*index).animate({ top : 0, opacity: 1 }, 800);
					});
				}, 800);
			});
		}, 400);
	});	
	
	
// Parallax //
	$("#parallax").each(function() {
		$('#parallax,header .container').parallax({
			scalarX: 25,
			scalarY: 15,
			frictionX: 0.1,
			frictionY: 0.1,
			calibrateX: false,
		});
	});
	
// Form Validation & Send Mail code
	if(typeof($('.contactForm form')) != 'undefined') {
		$.each($('.contactForm form'), function(index, el) {
			var cform = $(el),
				cResponse = $('<div class="cf_response"></div>');
			cform.prepend(cResponse);
			cform.h5Validate();

			cform.submit(function(e) {
				e.preventDefault();
				if(cform.h5Validate('allValid')) {
					cResponse.hide();
					$.post(
						$(this).attr('action'),
						cform.serialize(),
						function(data){
							cResponse.html(data).fadeIn('fast');
							if(data.match('success') != null) {
								cform.get(0).reset();
							}
						}
					); // end post
				}
				return false;
			});
		});
	};
	
	
//  Modal windows //	
	 if( $(".tse-scrollable").length ){
        $(".tse-scrollable").TrackpadScrollEmulator();
    }

    $(".open-side-panel, [data-toggle=modal]").on("click", function(e){
        e.preventDefault();
        $("body").addClass("show-panel");
        $( $(this).attr("href") ).addClass("show-it");
        $(this).addClass("is-active");
        openedSidePanel = $( $(this).attr("href") );
    });

    $(".backdrop, .modal-backdrop, .modal .close, .close-panel").on("click", function(e){
        $(".open-side-panel").removeClass("is-active");
        if( $("body").hasClass("show-panel") ){
            $("body").removeClass("show-panel");
            openedSidePanel.removeClass("show-it");
        }
    });

    $(document).keydown(function(e) {
        switch(e.which) {
            case 27: // ESC
                $(".close-panel").trigger("click");
                break;
        }
    });

    $(".modal").on("hide.bs.modal", function (e) {
        if( $("body").hasClass("show-panel") ){
            $("body").removeClass("show-panel");
        }
    });

    $(".nav-btn").on("click", function(e){
        $(".nav-btn-only").toggleClass("show-nav");
    });
	
	
// Count Down //
    if( $(".count-down").length ){
        var year = parseInt( $(".count-down").attr("data-countdown-year"), 10 );
        var month = parseInt( $(".count-down").attr("data-countdown-month"), 10 ) - 1;
        var day = parseInt( $(".count-down").attr("data-countdown-day"), 10 );
        $(".count-down").countdown({until: new Date(year, month, day), padZeroes: true});
    }
	
    if( $(".count-down").length ){
        var year = parseInt( $(".count-down").attr("data-countdown-year"), 10 );
        var month = parseInt( $(".count-down").attr("data-countdown-month"), 10 ) - 1;
        var day = parseInt( $(".count-down").attr("data-countdown-day"), 10 );
        $(".count-down").countdown({until: new Date(year, month, day), padZeroes: true});
    }

	


    $(".bg-transfer").each(function() {
        $(this).css("background-image", "url("+ $(this).find("img").attr("src") +")" );
    });

   

   $(window).load(function(){
    $(".animate").addClass("in");

});	
	
})(jQuery);