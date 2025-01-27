from django.contrib import admin
from .models import LiveInfo


@admin.register(LiveInfo)
class LiveInfoAdmin(admin.ModelAdmin):
    list_display = ("id", "timestamp", "data_preview")  # Exibe os campos no painel
    list_filter = ("timestamp",)  # Filtros laterais baseados na data
    search_fields = ("data",)  # Permite buscar no campo de dados

    def data_preview(self, obj):
        # Retorna uma prévia dos dados JSON para exibição
        return str(obj.data)[:75] + "..." if len(str(obj.data)) > 75 else str(obj.data)

    data_preview.short_description = "Data Preview"
