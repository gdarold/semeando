from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from doacao.models import Doacao
from endereco.models import Endereco
from users.forms import UserCreationForm
from users.models import User
from pycorreios3 import calc_preco_prazo


class CreateUser(CreateView):
    template_name = 'users_form.html'
    model = User()
    fields = '__all__'

    def form_valid(self, form):
        user = form.save(commit=False)
        user.username = self.request.user
        user.first_name = form.cleaned_data['first_name']
        user.last_name = form.cleaned_data['last_name']
        user.cpf = form.cleaned_data['cpf']
        user.telefone = form.cleaned_data['telefone']

        user.save()

        return super(CreateUser, self).form_valid(form)




@login_required
def profile(request):
    user_log = request.user.pk
    use = get_object_or_404(User, pk=user_log)
    doacoes = Doacao.objects.filter(doador=user_log)
    endereco = None
    exists = False
    try:

        endereco = Endereco.objects.get(usuario=user_log)
        exists = True
    except:
        print("deu pau")

    if(exists):

        return render(request, 'profile.html', {'user': use, 'doe': doacoes, 'end': endereco, })
    else:
        return redirect('endereco:new')


class UpdateUser(UpdateView):
    model = User


class DeleteUser(DeleteView):
    model = User
    success_url = reverse_lazy('users:profile')
