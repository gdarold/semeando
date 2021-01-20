from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView
from cart.forms import CartAddDoacaoForm
from .models import TipoDoacao, Doacao


class DoacaoDetailView(DetailView):
    queryset = Doacao.available.all()
    extra_context = {"form": CartAddDoacaoForm()}


class DoacaoListView(ListView):
    tipo_doacao = None
    paginate_by = 6

    def get_queryset(self):
        queryset = Doacao.available.all()

        tipo_doacao_slug = self.kwargs.get("slug")
        if tipo_doacao_slug:
            self.tipo_doacao = get_object_or_404(TipoDoacao, slug=tipo_doacao_slug)
            queryset = queryset.filter(tipo_doacao=self.tipo_doacao)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tipo_doacao"] = self.tipo_doacao
        context["tipos_doacoes"] = TipoDoacao.objects.all()
        return context
