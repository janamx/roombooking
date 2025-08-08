from django.shortcuts import redirect
from django.conf import settings
from django.urls import reverse

class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.exempt_urls = [
            reverse('login'),
            reverse('logout'),
            reverse('admin:login'),
            reverse('admin:index'),
        ]
        # Optional: URLs, die öffentlich zugänglich bleiben sollen
        self.exempt_urls += getattr(settings, 'LOGIN_EXEMPT_URLS', ['/accounts/login/', '/accounts/logout/', '/admin/', '/accounts/signup/'])

    def __call__(self, request):
        if not request.user.is_authenticated and request.path not in self.exempt_urls:
            return redirect(settings.LOGIN_URL)
        return self.get_response(request)