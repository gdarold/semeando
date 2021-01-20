from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from endereco.models import Endereco


class EnderecoCreate(CreateView):
    model = Endereco
    fields = ['usuario', 'cep', 'logradouro', 'bairro', 'numero', 'complemento', 'cidade', 'uf', 'is_available']

    def form_valid(self, form):
        endereco = form.save(commit=False)
        endereco.usuario = self.request.user
        endereco.save()

        return super(EnderecoCreate, self).form_valid(form)


class EnderecoList(ListView):
    model = Endereco


class EnderecoEdit(UpdateView):
    model = Endereco
    fields = ['cep', 'logradouro', 'bairro', 'numero', 'complemento', 'cidade', 'uf']


class EnderecoDelete(DeleteView):
    model = Endereco

    success_url = reverse_lazy('endereco:list')
