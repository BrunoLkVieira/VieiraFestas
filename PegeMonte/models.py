from django.db import models

# Create your models here.

lista_categorias = (
    ("boy", "Boy"),
    ("girl", "Girl"),
    ("unisex", "Unisex"))

class Tema(models.Model):
    titulo = models.CharField(max_length=25)
    categoria = models.CharField(max_length=10, choices=lista_categorias)
    descricao = models.TextField(max_length=1000)
    thumb = models.ImageField(upload_to="thumb_filmes")


    def __str__(self):
        return self.titulo


class Festa(models.Model):
    tema = models.ForeignKey("Tema", related_name= "festas", on_delete= models.CASCADE)
    nome = models.CharField(max_length=25)
    descricao = models.TextField(max_length=1000)
    preco = models.FloatField()
    foto1 = models.ImageField( upload_to = "fotos_festa")
    foto2 = models.ImageField( upload_to = "fotos_festa")
    foto3 = models.ImageField( upload_to = "fotos_festa")
    foto4 = models.ImageField( upload_to = "fotos_festa", null=True)
    foto5 = models.ImageField( upload_to = "fotos_festa", null=True)
    foto6 = models.ImageField( upload_to = "fotos_festa", null=True)

    def __str__(self):
        return self.tema.titulo + "-" + self.nome
