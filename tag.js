$(document).ready(function() {

    /* Retrieving an element's text */

    //You can find any DOM element and it's text using this syntax:
    // text() is a method offered by jQuery
    var color=['00','33','66','99','cc','ff']
    var rand=function(){
        return Math.floor(Math.random()*6);
    };
    var randomColor =function(){
        var r =color[rand()];
        var g =color[rand()];
        var b =color[rand()];
        return "#"+r+g+b;
    }

    $("#but1").click(function(){
        $('div').each(function(){
            $(".box").css("background-color",randomColor());
        })
   });

   $("#but2").click(function(){
            $(".box").css("border-radius","50%")
   });

    $("#but3").click(function(){
   $(".container").append(`<div class="box" style="height:100px;width:100px; border:1px solid black"></div>`);
});

});