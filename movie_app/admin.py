from django.contrib import admin
from django.contrib.admin.views.main import ChangeList
from movie_app.models import User, Profile, Aktor, Sutradara, Genre, Negara, Bahasa, Film, Rating

# Register your models here.
class CustomChangeList(ChangeList):
    def get_results(self, request):
        super().get_results(request)
        self.paginator.page_size = 5  # Mengatur jumlah item per halaman

admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Genre)
admin.site.register(Rating)

@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ('judul', 'tahun', 'durasi', 'thumbnail',)
    list_filter = ('tahun',)
    search_fields = ('judul', 'tahun',)
    list_per_page = 20
    ordering = ('id',)

    def get_changelist(self, request, **kwargs):
        return CustomChangeList

@admin.register(Negara)
class NegaraAdmin(admin.ModelAdmin):
    list_display = ('negara',)
    search_fields = ('negara',)
    list_per_page = 15
    ordering = ('id',)

    def get_changelist(self, request, **kwargs):
        return CustomChangeList

@admin.register(Bahasa)
class BahasaAdmin(admin.ModelAdmin):
    list_display = ('bahasa',)
    search_fields = ('bahasa',)
    list_per_page = 15
    ordering = ('id',)

    def get_changelist(self, request, **kwargs):
        return CustomChangeList

@admin.register(Aktor)
class AktorAdmin(admin.ModelAdmin):
    list_display = ('nama_aktor',)
    search_fields = ('nama_aktor',)
    list_per_page = 20

    def get_changelist(self, request, **kwargs):
        return CustomChangeList

@admin.register(Sutradara)
class SutradaraAdmin(admin.ModelAdmin):
    list_display = ('nama_sutradara',)
    search_fields = ('nama_sutradara',)
    list_per_page = 20

    def get_changelist(self, request, **kwargs):
        return CustomChangeList