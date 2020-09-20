from django.shortcuts import render, HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import ArticleForm, AuthUserForm, RegisterUserForm, CommentsForm
from .models import Article, Comment
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormMixin
from django.http import HttpResponseRedirect
from django.views.generic.list import MultipleObjectMixin


class CustomSuccessMessageMixin:
    @property
    def success_msg(self):
        return False

    def form_valid(self, form):
        messages.success(self.request,
                         self.success_msg)
        return super().form_valid(form)


class HomeListView(ListView):
    model = Article
    template_name = 'base.html'
    context_object_name = 'list_articles'


class DetailPageListView(CustomSuccessMessageMixin, FormMixin, DetailView, MultipleObjectMixin):
    model = Article
    template_name = 'post_detail.html'
    context_object_name = 'get_article'
    form_class = CommentsForm
    success_msg = 'Комментарий успешно создан, ожидайте модерации'
    paginate_by = 20

    def get_context_data(self, **kwargs):
        object_list = Comment.objects.filter(
            article=self.get_object()
        )
        context = super(DetailPageListView, self).get_context_data(
            object_list=object_list,
            **kwargs
        )
        return context

    def get_success_url(self):
        return reverse_lazy(
            'detail_page',
            kwargs={
                'pk': self.get_object().i
            }
        )

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.article = self.get_object()
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)


def update_comment_status(request, pk, type):
    item = Comment.objects.get(pk=pk)
    if request.user != item.article.author:
        return HttpResponse('deny')

    elif request.user != item.article.author:
        return HttpResponse('deny')

    if type == 'delete':
        item.delete()
        template = 'delete_comment.html'
        return render(
            request,
            template
        )


class ArticleCreateView(LoginRequiredMixin, CustomSuccessMessageMixin, CreateView,):
    login_url = reverse_lazy('login_page')
    model = Article
    template_name = 'edit_page.html'
    form_class = ArticleForm
    success_url = reverse_lazy('edit_page')
    success_msg = 'Запись создана'

    def get_context_data(self, **kwargs):
        kwargs['list_articles'] = Article.objects.all().order_by('-id')
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)


class ArticleUpdateView(CustomSuccessMessageMixin, UpdateView, LoginRequiredMixin):
    model = Article
    template_name = 'edit_page.html'
    form_class = ArticleForm
    success_url = reverse_lazy('edit_page')
    success_msg = 'Запись обновлена'

    def get_context_data(self, **kwargs):
        kwargs['update'] = True
        return super().get_context_data(**kwargs)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if self.request.user != kwargs['instance'].author:
            return self.handle_no_permission()
        return kwargs


class ForumLoginView(LoginView):
    template_name = 'login.html'
    form_class = AuthUserForm
    success_url = reverse_lazy('edit_page')

    def get_success_url(self):
        return self.success_url


class RegisterUserView(CreateView):
    model = User
    template_name = 'register_page.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('edit_page')
    success_msg = 'Пользователь успешно создан'

    def form_valid(self, form):
        form_valid = super().form_valid(form)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        aut_user = authenticate(
            username=username,
            password=password
        )
        login(
            self.request,
            aut_user
        )
        return form_valid


class ForumLogoutView(LogoutView):
    next_page = reverse_lazy('edit_page')


class ArticleDeleteView(DeleteView, LoginRequiredMixin):
    model = Article
    template_name = 'edit_page.html'
    success_url = reverse_lazy('edit_page')
    success_msg = 'Запись удалена'

    def post(self, request, *args, **kwargs):
        messages.success(
            self.request,
            self.success_msg
        )
        return super().post(request)

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.request.user != self.object.author:
            return self.handle_no_permission()
        success_url = self.get_success_url()
        self.object.delete()
        return HttpResponseRedirect(success_url)




