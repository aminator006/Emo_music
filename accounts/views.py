from django.contrib.auth import login, logout
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView

from . import forms

class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy("login")
    template_name = "accounts/signup.html"


from accounts.models import ProfilePic

class CreateProfilePhoto(CreateView):
    model = ProfilePic
    fields = ['profilephoto',]

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.name = self.request.user
        self.object.save()
        return super().form_valid(form)
