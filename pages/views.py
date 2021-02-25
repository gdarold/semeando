from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from pages.forms import ContactForm


class HomePageView(TemplateView):
    template_name = "home.html"


class AboutPageView(TemplateView):
    template_name = "about.html"


def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        "title": "Contact",
        "content": " Bem vindo a página de contato.",
        "form": contact_form,
    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)

        return HttpResponse({"<h1>Obrigado por sua mensagem</h1>"})

    if contact_form.errors:
        errors = contact_form.errors.as_json()
        if request.is_ajax():
            return HttpResponse(errors, status=400, content_type='application/json')

    # if request.method == "POST":
    #     #print(request.POST)
    #     print(request.POST.get('fullname'))
    #     print(request.POST.get('email'))
    #     print(request.POST.get('content'))
    return render(request, "contact.html", context)
