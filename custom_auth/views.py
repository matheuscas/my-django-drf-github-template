import json

from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.http import require_POST
from rest_framework import status


@require_POST
def login(request):
    data = json.loads(request.body)
    email = data.get('email')
    password = data.get('password')

    if email is None or password is None:
        return JsonResponse({'detail': 'Please provide email and password.'}, status=status.HTTP_400_BAD_REQUEST)

    user = authenticate(email=email, password=password)

    if user is None:
        return JsonResponse({'detail': 'Invalid credentials.'}, status=status.HTTP_400_BAD_REQUEST)

    django_login(request, user)
    return JsonResponse({'detail': 'Successfully logged in.'})


def logout(request):
    if not request.user.is_authenticated:
        return JsonResponse({'detail': 'You\'re not logged in.'}, status=status.HTTP_400_BAD_REQUEST)

    django_logout(request)
    return JsonResponse({'detail': 'Successfully logged out.'})


@ensure_csrf_cookie
def session(request):
    if not request.user.is_authenticated:
        return JsonResponse({'isAuthenticated': False}, status=status.HTTP_401_UNAUTHORIZED)

    return JsonResponse({'isAuthenticated': True})


def whoami(request):
    if not request.user.is_authenticated:
        return JsonResponse({'isAuthenticated': False}, status=status.HTTP_401_UNAUTHORIZED)

    return JsonResponse({'email': request.user.email})
