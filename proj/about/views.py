from django.views.generic.base import TemplateView


class AboutAuthorView(TemplateView):
    template_name = 'about/author.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['author_title'] = 'Авторы: Хатунцев Спартак Владимировчик, Ершов Александр Александрович, Фидрик Лев Горбенко'
        context['author_text'] = ('Готов в открытым предложениям - писать в telegram @excelvrn')

        return context