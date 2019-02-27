 (function ($) {
	"use strict";



		function unitegallery (){
	      // Home 6 Slider
	      jQuery("#gallery2").unitegallery({
	        gallery_theme: "slider",
	        gallery_width:"100%",  
	        gallery_height:650,
	        slider_enable_bullets: false, 
	        gallery_autoplay:false,
	      });
	    };
	    unitegallery ();

	function unitegallery_slider (){
      // Home 6 Slider
      jQuery("#gallery").unitegallery({
        gallery_theme: "slider",
        gallery_width:"100%",  
        gallery_height:650,
        slider_scale_mode_media: "fill", 
        slider_enable_bullets: false, 
        gallery_autoplay:false,
      });
    };
     unitegallery_slider(); 


 
}(jQuery));

