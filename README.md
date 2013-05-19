django-b58-urlshortener
=======================

Url shortener service powered by django

on settings set DOMAIN = yourdomain.com it is used to build the short urls.

require:
##
https://github.com/OttoYiu/django-cors-headers

Usage:
##
    from django.test.client import Client
    c = Client()
    response = c.post('/',{'url': 'http://google.com'})
    print response.content

# it accepts calls from ajax (CORS)

    var url = "http://chuchita.com"
    $.ajax({
        url: "http://yourdomain.com/api/?url=" + url,
        type: "GET",
        success: function(data){
            console.log(data.short);
            console.log(data.long);
       }
    });
