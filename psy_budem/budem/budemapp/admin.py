from django.contrib import admin
from django.utils.safestring import mark_safe
from budemapp.models import Seminar, Category, Review
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class SeminarAdmin(admin.ModelAdmin):
    actions = ['mark_is_active', 'mark_not_active']
    list_display = ('category', 'title', 'date_of_seminar', 'on_main_page', 'is_active', 'get_photo')
    list_display_links = ('title', )
    search_fields = ('title', 'description', 'on_main_page')
    list_editable = ('is_active', 'date_of_seminar', 'on_main_page')
    list_filter = ('is_active', 'category', 'on_main_page')
    # fields = (('id', 'title', 'category'), 'description', ('photo', 'get_photo'), 'is_active')
    readonly_fields = ('id', 'get_photo', 'created_date')
    save_on_top = True

    def mark_is_active(self, request, queryset):
        queryset.update(is_active=True)

    def mark_not_active(self, request, queryset):
        queryset.update(is_active=False)

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="90">')
        else:
            return 'Нет фото'

    mark_is_active.short_description = 'Опубликовать'
    mark_not_active.short_description = 'Скрыть публикацию'
    get_photo.short_description = 'Текущее фото'


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('author', 'is_active', 'text')
    search_fields = ('author', 'text')
    list_editable = ('is_active',)
    list_filter = ('is_active', 'author')
    save_on_top = True


admin.site.register(Review, ReviewAdmin)
admin.site.register(Seminar, SeminarAdmin)
admin.site.register(Category)
