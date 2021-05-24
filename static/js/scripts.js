$(document).ready(function() {
    $("#screenshots > div:gt(0)").hide();

    setInterval(function() {
        $('#screenshots > div:first')
            .fadeOut(1000)
            .next()
            .fadeIn(1000)
            .end()
            .appendTo('#screenshots');
    }, 3000);
})