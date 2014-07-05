$(function() {
    console.log('Yay back to semi colon world!');
    console.log('If you really want to have fun enter the Konami Code ^_^');

    /*
        http://www.paulirish.com/2009/cornify-easter-egg-with-jquery/
        Cornify Konami Easter Egg Plugin With jQuery
        Because Reasons!
        I had t put this in here! HAD TOO!
     */
    var kkeys = [], konami = "38,38,40,40,37,39,37,39,66,65";
    $(document).keydown(function(e) {
      kkeys.push( e.keyCode );
      if ( kkeys.toString().indexOf( konami ) >= 0 ){
        $(document).unbind('keydown',arguments.callee);
        $.getScript('http://www.cornify.com/js/cornify.js',function(){
          cornify_add();
          $(document).keydown(cornify_add);
        });
      }
    });
});