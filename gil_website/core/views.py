import django.contrib.auth.views as auth_views
from django.urls import reverse


class LoginView(auth_views.LoginView):
    template_name = 'registration/login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse('cross:profile_detail', kwargs={'pk': self.request.user.id})
