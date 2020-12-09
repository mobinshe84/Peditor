$(document).ready(function () {
    $(window).scroll(function () {
        var Scroll = $(window).scrollTop();
        if (Scroll >= 100) {
            $(".first-image").css("opacity", "100%");
        }
    });
    $(window).scroll(function () {
        var Scroll = $(window).scrollTop();
        if (Scroll >= 400) {
            $(".second-image").css("opacity", "100%");
        }
    });
});