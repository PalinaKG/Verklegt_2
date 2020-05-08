$(document).ready(function () {
    $('#search-btn').on('click', function (e) {
        var data = {
        name: "helloworld",
        age: 123
    };

    var json = JSON.stringify(data);

    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/products/");
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.send(json);
    console.log(xhr)


    });

});