(function($) {

  $.fn.menumaker = function(options) {
      
      var cssmenu = $(this), settings = $.extend({
        title: "Menu",
        format: "dropdown",
        sticky: false
      }, options);

      var count = 0;
      return this.each(function() {
            cssmenu.prepend('<div id="menu-button'+count+'" class="menu-button">' + settings.title + '</div>');
            $(this).find(".menu-button").on('click', function(){
              $(this).toggleClass('menu-opened');
              var mainmenu = $(this).next('ul');
              if (mainmenu.hasClass('open')) { 
                mainmenu.slideUp().removeClass('open');
              }
              else {
                mainmenu.slideDown().addClass('open');
                if (settings.format === "dropdown") {
                  mainmenu.find('ul').slideDown();
                }
              }
              count++; 
        });
           

        cssmenu.find('li ul').parent().addClass('has-sub');

        multiTg = function() {
          cssmenu.find(".has-sub").prepend('<span class="submenu-button"></span>');
          cssmenu.find('.submenu-button').on('click', function() {
            $(this).toggleClass('submenu-opened');
            if ($(this).siblings('ul').hasClass('open')) {
              $(this).siblings('ul').removeClass('open').slideUp();
            }
            else {
              $(this).siblings('ul').addClass('open').slideDown();
            }
          });
        };

        if (settings.format === 'multitoggle') multiTg();
        else cssmenu.addClass('dropdown');

        if (settings.sticky === true) cssmenu.css('position', 'fixed');

        resizeFix = function() {
          if ($( window ).width() > 800) {
            cssmenu.find('ul').show();
          }

          if ($(window).width() <= 800) {
            cssmenu.find('ul').hide().removeClass('open');
          }
        };
        resizeFix();
        return $(window).on('resize', resizeFix);

      });
  };

  
})(jQuery);
