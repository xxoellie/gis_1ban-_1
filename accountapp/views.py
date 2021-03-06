from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from accountapp.decorators import account_ownership_required
from accountapp.forms import AccountCreationForm
from accountapp.models import HelloWorld

@login_required(login_url=reverse_lazy('accountapp:login'))
def hello_world(request):

    # if request.user.is_authenticated:

    if request.method == 'POST':

        temp = request.POST.get('hello_world_input')

        new_hello_world = HelloWorld()
        new_hello_world.text = temp
        new_hello_world.save()

        return HttpResponseRedirect(reverse('accountapp:hello_world'))

    else:
        hello_world_list = HelloWorld.objects.all()
        return render(request, 'accountapp/hello_world.html',
                      context={'hello_world_list': hello_world_list})
    # else :
    #     return HttpResponseRedirect(reverse('accountapp:login'))


class AccountCreatView(CreateView):
    model = User
    form_class = UserCreationForm
    # success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/create.html'

    def get_success_url(self):
        return reverse('accountapp:detail', kwargs={'pk': self.object.pk})


class AccountDetailView(DetailView) :
    model = User
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'

has_ownership = [login_required,account_ownership_required]

@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountUpdateView(UpdateView) :
    model = User
    form_class = AccountCreationForm
    context_object_name = "target_user"
    # success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/update.html'

    def get_success_url(self):
        return reverse('accountapp:detail', kwargs={'pk': self.object.pk})

    # def get(self,request,*args, **kwargs):
    #     if request.user.is_authenticated and self.get_object() == request.user:
    #         return super().get(request,*args, **kwargs)
    #     else :
    #         # return HttpResponseRedirect(reverse('accountapp:login'))
    #         return HttpResponseForbidden()
    #
    # def post(self, request, *args, **kwargs):
    #     if request.user.is_authenticated and self.get_object() == request.user:
    #         return super().post(request,*args, **kwargs)
    #     else:
    #         return HttpResponseForbidden()

@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountDeleteView(DeleteView) :
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/delete.html'

    # def get(self,request,*args, **kwargs):
    #     if request.user.is_authenticated and self.get_object() == request.user:
    #         return super().get(request,*args, **kwargs)
    #     else :
    #         # return HttpResponseRedirect(reverse('accountapp:login'))
    #         return HttpResponseForbidden()
    #
    # def post(self, request, *args, **kwargs):
    #     if request.user.is_authenticated and self.get_object() == request.user:
    #         return super().post(request,*args, **kwargs)
    #     else:
    #         return HttpResponseForbidden()
