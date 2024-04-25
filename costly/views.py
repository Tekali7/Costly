from django.shortcuts import render


# Custom error handling views for handling HTTP errors in Django.

def handler404(request, exception):
    """
    **handler404**

    Renders a custom 404 page when a page is not found
    (HTTP 404 Not Found).
    """
    return render(request, "errors/404.html", status=404)


def handler500(request):
    """
    **handler500**

    Renders a custom 500 page when an internal server error occurs
    (HTTP 500 Internal Server Error).
    """
    return render(request, "errors/500.html", status=500)


def handler403(request, exception):
    """
    **handler403**

    Renders a custom 403 page when access to a resource is forbidden
    (HTTP 403 Forbidden).
    """
    return render(request, "errors/403.html", status=403)


def handler405(request, exception):
    """
    **handler405**

    Renders a custom 405 page when a method is not allowed for a resource
    (HTTP 405 Method Not Allowed).
    """
    return render(request, "errors/405.html", status=405)