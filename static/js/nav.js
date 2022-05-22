function menuResponsive() {
    if (window.innerWidth < 992) {
        $("#toggle_nav").removeClass("active");
        $("#menu_wrapper").css("margin-left", "-300px");
        $("#main_section").css("margin-left", "0px");
    }
}
$("#toggle_nav").click(function () {
    if ($(this).hasClass("active")) {
        $(this).removeClass("active");
        $("#menu_wrapper").css("margin-left", "-300px");
        if (window.innerWidth > 992) {
            $("#main_section").css("margin-left", "0px");
        }
    } else {
        $(this).addClass("active")
        $("#menu_wrapper").css("margin-left", "0px");
        if (window.innerWidth > 992) {

            $("#main_section").css("margin-left", "300px");
        }
    }
});
$(".menu-item.dropdown .menu-link").click(function (e) {
    e.preventDefault();
    if ($(this).parent().hasClass("active")) {
        $(this).parent().removeClass("active");
    } else {
        $(".menu-item.dropdown").removeClass("active");
        $(this).parent().addClass("active");
    }
});