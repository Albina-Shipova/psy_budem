from django.views.generic import ListView, DetailView
from budemapp.models import Seminar, Review
from django.urls import reverse_lazy


class Main(ListView):
    model = Seminar
    template_name = 'budemapp/main.html'
    context_object_name = 'seminar_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['psy_list'] = Seminar.objects.filter(is_active=True, category_id=1)
        context['business_list'] = Seminar.objects.filter(is_active=True, category_id=2)
        context['health_list'] = Seminar.objects.filter(is_active=True, category_id=3)
        context['review'] = Review.objects.filter(is_active=True,)
        return context

    def get_queryset(self):
        return Seminar.objects.filter(is_active=True, on_main_page=True).order_by('-created_date',)


class SeminarDetail(DetailView):
    model = Seminar
    template_name = 'budemapp/seminar_detail.html'
    context_object_name = 'seminar_item'

    def get_success_url(self):
        return reverse_lazy('seminar_detail', kwargs={'pk': self.get_object().id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['psy_list'] = Seminar.objects.filter(is_active=True, category_id=1)
        context['business_list'] = Seminar.objects.filter(is_active=True, category_id=2)
        context['health_list'] = Seminar.objects.filter(is_active=True, category_id=3)
        return context

