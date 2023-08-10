from django.contrib import admin
from .models import Category, Dish, Why_us, Chef, Response, Event, Gallery, About, Footer


class DishTabularInline(admin.TabularInline):
    """
    The DishTabularInline class represents an inline form for editing
    Dish model objects on the edit page of Category model.
    """
    model = Dish
    extra = 1


class CategoryAdmin(admin.ModelAdmin):
    """
    Several improvements for Category model in django.admin.
    """
    inlines = [DishTabularInline]
    list_display = ('title', 'position', 'is_visible')
    search_fields = ('title', )
    list_filter = ('title', )

    show_full_result_count = True

    list_per_page = 10


class ChefAdmin(admin.ModelAdmin):
    """
    Several improvements for Chef model in django.admin.
    """
    list_display = ('name', 'surname', 'staff')
    search_fields = ('name', 'surname')
    list_filter = ('name', 'surname')

    show_full_result_count = True

    list_per_page = 10


class DishAdmin(admin.ModelAdmin):
    """
    Several improvements for Dish model in django.admin.
    """
    list_display = ('title', 'price', 'is_visible', 'position', 'category')
    search_fields = ('title', 'category')
    list_filter = ('title', 'is_visible', 'category')

    show_full_result_count = True

    list_per_page = 10


class WhyUsAdmin(admin.ModelAdmin):
    list_display = ('num', 'title')
    search_fields = ('title', )
    list_filter = ('title',)

    show_full_result_count = True

    list_per_page = 10


class ResponseAdmin(admin.ModelAdmin):
    list_display = ('surname', 'name', 'prof', 'stars')
    search_fields = ('surname', 'name')
    list_filter = ('stars',)

    show_full_result_count = True

    list_per_page = 10


class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'is_visible')
    search_fields = ('title', )
    list_filter = ('title', )

    show_full_result_count = True

    list_per_page = 10


class GalleryAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_visible')
    search_fields = ('title', )
    list_filter = ('title', )

    show_full_result_count = True

    list_per_page = 10


class AboutAdmin(admin.ModelAdmin):
    list_display_links = ('video_link', )

    show_full_result_count = True


# Model Registration.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Dish, DishAdmin)
admin.site.register(Why_us, WhyUsAdmin)
admin.site.register(Chef, ChefAdmin)
admin.site.register(Response, ResponseAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Gallery, GalleryAdmin)
admin.site.register(About)
admin.site.register(Footer)
