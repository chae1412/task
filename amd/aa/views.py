from django.views.generic import ListView
from .models import Publisher, Book

class PublisherListView(ListView):
    # 어떤 모델을 가져올지
    model = Publisher
    # 모델 이름 바꾸기->대문자를 소문자로(하면 좋음)
    context_object_name = "publisher"


class PublisherDetailView(DetailView):
    model = Publisher

    # 세부정보를 가져오기
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['book_list'] = Book.objects.all()
        return context

class BookListView(ListView):
    # queryset 사용하는 이유 = 모델은 모든 일반 뷰에서 사용될 수 있다. 하지만 하나의 뷰에서만 모델을
    # 사용하고 싶다면 queryset을 사용하자 => 데이터 중복 접근 막을 수 있다
    # order_by => 가져오는 순서 지정
    queryset = Book.objects.order_by("-publication_date")
    context_object_name = "book_list"

class AcmeBookListView(ListView):
    context_object_name = "book_list"
    queryset = Book.objects.filter(publisher__name="ACME Publishing")
    # template_name => 어떤 템플릿?
    template_name = "books/acme_list.html"

class PublisherBookListView(ListView):
    template_name = "books_by_publisher.html"

    # get_queryset을 이용하여 특정 조건에 맞는 객체들만 반환하거나, 정렬된 순서로 객체들을 
    #반환하는 등 다양한 커스터마이징 가능

    # get_object_or_404는 객체를 가져올때 못가져올 시 404 페이지 반환
    def get_queryset(self):
        self.publisher = get_object_or_404(Publisher, name=self.kwargs["publisher"])
        return Book.objects.filter(publisher=self.publisher)