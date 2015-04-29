$(function () {
    $('button').on('click', function () {
        $.ajax({
            url: $SCRIPT_ROOT + '/api/my_model',
            method: 'POST',
            contentType: "application/json",
            data: JSON.stringify({
                some_string: Math.random().toString(36).substring(7),
                some_integer: Math.floor((Math.random() * 100) + 1)
            })
        })
            .success(function () {
                window.location.reload();
            })
            .error(function (e) {
                alert(JSON.parse(e.responseText).message);
            })
        ;
    })
});
