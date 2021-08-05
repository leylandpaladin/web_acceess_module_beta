$(document).ready(function() {
  $('button.remote-btn').click(function(e) {
    // Stop form from sending request to server
    e.preventDefault();

    var btn = $(this);

    $.ajax({
      method: "POST",
      url: "https://jsonplaceholder.typicode.com/posts",
      dataType: "json",
      data: {
        "name": btn.attr('name'),
        //'input': $('input').val()
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