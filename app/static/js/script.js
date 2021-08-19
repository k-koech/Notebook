$(document).ready(function(){
    $(".commentBtn").click(function()
    {
        var closestBtn = $(this).closest(".commentBtn")
        closestBtn.next("#comments").slideToggle(100)
    });
});