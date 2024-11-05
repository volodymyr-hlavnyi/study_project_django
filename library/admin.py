from django.contrib import admin
from .models import Author, AuthorDetail, Book, Category, Library, Member


# @admin.register(Author)
# class AuthorAdmin(admin.ModelAdmin):
#     list_display = '__all__'
#     list_filter = ['deleted']
#     search_fields = ['first_name', 'last_name', 'birth_date', 'deleted']


# @admin.register(Book)
# class BookAdmin(admin.ModelAdmin):
#     list_display = '__all__'
#     list_filter = ['author_id']
#     search_fields = ['title', 'author_id', 'publishing_date', 'genre', 'page_count']


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name_initial', 'birth_date', 'rating', 'deleted']
    search_fields = ['first_name', 'last_name']

    def last_name_initial(self, obj):
        return f"{obj.last_name[0]}."

    last_name_initial.short_description = 'Last Name Initial'


@admin.register(AuthorDetail)
class AuthorDetailAdmin(admin.ModelAdmin):
    list_display = ['author', 'birth_city', 'gender']
    search_fields = ['author__first_name', 'author__last_name', 'birth_city']


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'publishing_date', 'genre', 'page_count']
    search_fields = ['title', 'author__first_name', 'author__last_name']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


@admin.register(Library)
class LibraryAdmin(admin.ModelAdmin):
    list_display = ['name', 'location', 'site']
    search_fields = ['name', 'location']


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'gender', 'phone_number', 'birth_date', 'age', 'role', 'active']
    search_fields = ['first_name', 'last_name', 'phone_number']
