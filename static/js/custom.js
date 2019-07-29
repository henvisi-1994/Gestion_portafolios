$(".sidebar-dropdown > a").click(function () {
    $(".sidebar-submenu").slideUp(200);
    if (
        $(this)
            .parent()
            .hasClass("active")
    ) {
        $(".sidebar-dropdown").removeClass("active");
        $(this)
            .parent()
            .removeClass("active");
    } else {
        $(".sidebar-dropdown").removeClass("active");
        $(this)
            .next(".sidebar-submenu")
            .slideDown(200);
        $(this)
            .parent()
            .addClass("active");
    }
});

$("#close-sidebar").click(function () {
    $(".page-wrapper").removeClass("toggled");
    $('#menu').css('-webkit-transition', 'all 0.3s ease');
    $('#menu').css('marginLeft', '0%');
    $('#content').css('-webkit-transition', 'all 0.3s ease');
    $('#content').css('marginLeft', '0%');
});

$("#show-sidebar").click(function () {
    $(".page-wrapper").addClass("toggled");
    $('#menu').css('-webkit-transition', 'all 0.3s ease');
    $('#menu').css('marginLeft', '17%');
    $('#content').css('-webkit-transition', 'all 0.3s ease');
    $('#content').css('marginLeft', '17%');
});

/**
 * UPLOAD FILES
 */

$('#file_upload').on('change', function () {
    console.log($(this).val());
    var fileName = $(this).val().split('\\').pop();
    $(this).siblings('#file-label').addClass('selected').html(fileName);
})