$(document).ready(function(){
    $(".commentBtn").click(function()
    {
        var closestBtn = $(this).closest(".commentBtn")
        closestBtn.next("#comments").slideToggle(100)
    });
});

$(document).ready(function()
{
    $(".col1").fadeIn("1000")
})