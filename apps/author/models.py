from django.db import models

class Author(models.Model):


    CHOICES_GENDER = [
        ('MASCULINO' , 'Masculino'),
        ('FEMENINO' , 'Femenino')
    ]

    first_name = models.CharField(
        max_length = 255,
        verbose_name = "Nombre autor",
        default = "Anonimo"
    )

    last_name = models.CharField(
        max_length = 255,
        verbose_name = "Apellido autor",
        default = "Anonimo apellido"
    )

    age = models.IntegerField(
        verbose_name = "Edad del Author",
        default = 0
    )

    gender = models.CharField(
        verbose_name = "genero del Autor",
        choices = CHOICES_GENDER,
        max_length = 255
    )

    biography = models.TextField(
        verbose_name = "Biografia del autor"
    )

    photo = models.ImageField(
        upload_to = "images/author",
        blank=True, 
        null=True
    )


    def __str__(self):
        return self.first_name