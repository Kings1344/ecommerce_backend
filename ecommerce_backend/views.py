from django.http import JsonResponse


def home(request):
    return JsonResponse({
        "message": "Welcome to the E-commerce Backend API",
        "status": "Running",
        "version": "1.0",
        "developer": "kingsley"
    })