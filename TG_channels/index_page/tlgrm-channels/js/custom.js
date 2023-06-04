jQuery(document).ready(function($){
	//slider
	$('.slide-items').slick({ //add in your correct containing element
		slidesToShow: 3,
		slidesToScroll: 1,
		// autoplay: true,
		// autoplaySpeed: 2000,
		dots: true,
		swipeToSlide: true,
		waitForAnimate: false,
			responsive: [
			{
				breakpoint: 991,
				settings: {
					slidesToShow: 2
				}
			},
			{
				breakpoint: 767,
				settings: {
					slidesToShow: 1
				}
			}
		]
	});

	$('.slide-articles').slick({ //add in your correct containing element
  		slidesToShow: 3,
		// autoplay: true,
		// autoplaySpeed: 2000,
		dots: true,
		arrows:false,
		swipeToSlide: true,
		waitForAnimate: false,
			responsive: [
			{
				breakpoint: 991,
				settings: {
					slidesToShow: 2
				}
			},
			{
				breakpoint: 767,
				settings: {
					slidesToShow: 1
				}
			}
		]
	});


	//menu
	$(function () {
	    $('.burger').click(function(evt) {
	    evt.stopPropagation(); //stops the document click action
	        $('body').toggleClass('menu--open');
	    });
	    $(document).click(function() {
	        $('body').removeClass('menu--open'); //make all inactive
	    });
	});
});