from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView

from endereco.models import Endereco


class EnderecoDetailView(DetailView):
    queryset = Endereco.available.all()


class EnderecoListView(ListView):
    cidade = None
    paginate_by = 6

    def get_queryset(self):
        queryset = Endereco.available.all()

        #cidade_slug = self.kwargs.get("slug")
        #if cidade_slug:
         #   self.cidade = get_object_or_404(slug=cidade_slug)# deve dar pau aqui
          #  queryset = queryset.filter(cidade=self.cidade)

        return queryset
