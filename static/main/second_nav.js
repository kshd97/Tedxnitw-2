/*  Sticky Header
    /* ========================================================= */

    var stickyHeader = jQuery('.navbar-fixed-top');

    jQuery(window).scroll(function() {
        if( stickyHeader.offset().top > 100 ) {
            stickyHeader.addClass('sticky')
        } else {
            stickyHeader.removeClass('sticky')
        }
    });