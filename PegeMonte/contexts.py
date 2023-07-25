from .models import Tema


def lista_temas_girl(request):
    lista_temas_girl = Tema.objects.filter(categoria="girl")

    return {'lista_temas_girl':lista_temas_girl}


def lista_temas_boy(request):
    lista_temas_boy = Tema.objects.filter(categoria="boy")
    lista_temas_boy = reversed(lista_temas_boy)
    return {'lista_temas_boy':lista_temas_boy}