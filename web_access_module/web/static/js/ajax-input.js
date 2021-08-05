$(document).ready(function() {
  $('button#renew').click(function(e) {
    // Stop form from sending request to server
    e.preventDefault();

    var btn = $(this);

    $.ajax({
      method: "POST",
      url: "https://jsonplaceholder.typicode.com/posts",
      dataType: "json",
      data: {
        //"name": btn.attr('name'),
        'input': $('textarea').val()
      },
      success: function(data) {
        console.log(data);
      },
      error: function(er) {
        console.log(er);
      }
    });
  })
});
var timerId;
$("textarea.main-text-area").bind('input',function(e){
       e.preventDefault();
       clearTimeout(timerId);
       timerId = setTimeout(function() {
            $.ajax({
              method: "POST",
              url: "https://jsonplaceholder.typicode.com/posts",
              dataType: "json",
              data: {
                //"name": btn.attr('name'),
                'input': $('textarea').val()
              },
              success: function(data) {
                console.log(data);
              },
              error: function(er) {
                console.log(er);
              }});
            },2000);
});