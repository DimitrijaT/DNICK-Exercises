from django.contrib import admin
from .models import Author, Book, Publication, PublicationAuthor


# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "year_of_birth")
    list_filter = ("first_name", "year_of_birth")


admin.site.register(Author, AuthorAdmin)


class BookAdmin(admin.ModelAdmin):
    pass


admin.site.register(Book, BookAdmin)


class PublicationAdmin(admin.ModelAdmin):
    pass


admin.site.register(Publication, PublicationAdmin)


class PublicationAuthorAdmin(admin.ModelAdmin):
    pass


admin.site.register(PublicationAuthor, PublicationAuthorAdmin)
