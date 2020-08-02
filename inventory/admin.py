from openpyxl import Workbook
from openpyxl.writer.excel import save_virtual_workbook

from django.contrib import admin
from django.http import HttpResponse

from inventory.models import Book


class BookAdmin(admin.ModelAdmin):
    actions = ['download_xlsx']
    actions_selection_counter = True
    list_filter = ('author__first_name',)
    search_fields = ['title', 'author__first_name', 'author__last_name', 'author__username']
    
    def download_xlsx(self, request, queryset):
        workbook = Workbook()
        worksheet = workbook.active
        worksheet.append(['ID', 'Title', 'Author Last Name', 'Author Fist Name'])
        for book in queryset.order_by('id'):
            worksheet.append([book.id, book.title, book.author.last_name, book.author.first_name])
        response = HttpResponse(
            content=save_virtual_workbook(workbook),
            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )
        response['Content-Disposition'] = 'attachment; filename=myexport.xlsx'
        return response
    download_xlsx.short_description = 'Download selected books'

admin.site.register(Book, BookAdmin)
