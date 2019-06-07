from django.contrib import admin
from apps.author.models import Author

@admin.register(Author)

class AuthorAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'age',
        'gender',
        'biography',
        'photo'
    )

    class Meta:
        model = Author
