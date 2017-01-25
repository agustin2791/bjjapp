from django.contrib import admin
from posts.models import BlogCategories, TypeOfEntry, BlogPost, BlogAuthor

# Register your models here.
class BlogCategoryAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('category',)}

class TypeOfEntryAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('type_of',)}

class BlogPostAdmin(admin.ModelAdmin):
	exclude = ['posted']
	prepopulated_fields = {'slug': ('title',)}

class BlogAuthorAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('author',)}

admin.site.register(BlogCategories, BlogCategoryAdmin)
admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(TypeOfEntry, TypeOfEntryAdmin)
admin.site.register(BlogAuthor, BlogAuthorAdmin)