$(document).ready(function(){
    $(window).scroll(function(){
        if(this.scrollY > 30){
            $('.navig').addClass("pers");
        }else{
            $('.navig').removeClass("pers");
        }
    });


    $('.button').click(function(){
        $('.navig .list').toggleClass("active");
        $('.button i').toggleClass("active");
    });
});