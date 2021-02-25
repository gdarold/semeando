from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from endereco.models import Endereco
from users.models import User


class EnderecoCreate(CreateView):
    model = Endereco
    fields = ['cep', 'logradouro','bairro','numero', 'complemento', 'cidade',
              'uf']

    def form_valid(self, form):
        endereco = form.save(commit=False)
        endereco.usuario = self.request.user
        usuario = User.objects.get(id=self.request.user.id)

        usuario.com_endereco = True

        usuario.save()
        endereco.save()

        return super(EnderecoCreate, self).form_valid(form)


class EnderecoList(ListView):
    model = Endereco


class EnderecoEdit(UpdateView):
    model = Endereco
    fields = ['cep', 'logradouro','bairro','numero', 'complemento', 'cidade', 'uf', 'is_available']




class EnderecoDelete(DeleteView):
    model = Endereco

    success_url = reverse_lazy('users:profile')





