from django.http import HttpRequest, HttpResponse


def test_view(request: HttpRequest):
    print("hey")
    return HttpResponse("hello")
