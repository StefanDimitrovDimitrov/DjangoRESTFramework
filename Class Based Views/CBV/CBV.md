# Class Based Views

    Build-in generic views

        * View
       
        * FormView
        * ListView
        * DetailView
    
        * CreateView
        * UpdateView
        * DeleteView
          
        * RedirectView

    1. Template View

        * Decription: renders template with the context

        * Syntax:

                in VIEW
            import render and Template View

            class IndexView(TemplateView):
                template_name = 'index.html (point the html you want to render)
            
                def get_context_data(self, **kwargs)
                    context = super().get_context_data(**klwargs)
                    context['name'] = 'User'
                    return context

                in PATTERNS
            path('', views.IndexView.as_view(), name ='index')
    
    2. List View
        
        * Description: a list view is used for representing a list of objects
        
        in the view
        class ArticleListView(ListView):
            context_object_name = 'articles'
            model = models.Article
            template_name = 'list_articles.html'

        in the template 

            {% for article in articles %}
                {% url 'details' article.id %}{{ article.title}}
            {% endfor%}

    3. Detail View Example
        

                in the view
        class ArticleListView(DetailView):
            context_object_name = 'articles'
            model = models.Article
            template_name = 'detail_articles.html'

        in the template 

            {{ article_details title }}
            {{ article_detail.content}}

        urlpatterns = [
            path('details/<int:pk>', view DetailView.as_view(), name= 'details')
            ]