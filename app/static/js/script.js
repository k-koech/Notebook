$(document).ready(function(){
    $(".commentBtn").click(function()
    {
        var closestBtn = $(this).closestBtn(".commentBtn")
        closestBtn.next("#comments").slideToggle(100)
    });
});