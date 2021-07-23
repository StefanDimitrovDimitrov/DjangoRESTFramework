# Build-in Class Based Views

    - Base views:
        * View
        * TemplateView
        * RedirectView

    - Generic display views:
        * DeleteView
        * ListView

    - Generic editing views
        * FormView
        * CreateView
        * UpdateView
        * DeleteView
___________________________________________________________________

    [] Views

        Description: 
            * The master class-based base view. 
            * All other class-based views inherit from this base class.

        Methods:
            * setup()
            * deispatch()
            * http_method_not_allowed()
            * options()


    [] Template Views

        Description: 
            * Renders a given template, with the context.

        Methods:
            * setup()
            * dispatch()
            * http_method_not_allowed()
            * get_context_data()

        Syntax example:
            class ExapmpleIndexView(TemplateView):
                template_name = 'index.html'
            
            def get_contex_data(self, **kwargs):
                return {
                    'title': 'Hello from CBV',
                }

    [] RedirectView

        Description: 
            * Redirects to a given URL.

        Methods:
            * setup()
            * dispatch()
            * http_method_not_allowed()
            * get_redirect_url()

        * Doncho said not to use this one. To use Reverse_lazy instead

    - -- - - -- - - - - - - - - - - -  - -- - - -- - - - - - - - - - - -
    [] DetailViews

        Description: 
            * Display an object

        Methods:
            * setup()
            * dispatch()
            * http_method_not_allowed()
            * get_template_names()
            * get_slug_field()
            * get_queryset()
            * get_object()
            * get_context_object_name()
            * get()
            * grender_to_response()

        Syntax:
            class DetailsExample(DetailView):    
                model = Example
                template_name = 'detail_view.html'
                context_object_name = 'current_example'

                def get_context_data(self,**kwargs):
                    context = super().get_context_data(**kwargs)
                    return context


    [] ListViews

        Description: 
            * A page representing a list of objects.

        Methods:
            * setup()
            * dispatch()
            * http_method_not_allowed()
            * get_template_names()
            * get_queryset()
            * get_context_object_name()
            * get_context_data()
            * get()
            * render_to_response()

        Syntax Example:
            class showExamplesListView(ListView):
                model = ExampleModel
                template_name = 'Examples-list.html'
                context_object_name = 'Examples' 
                    *(this is our context it's contained all objects in ExampleModel which we have in our DB, If we don't use it our contex will be with name: object_list))

                def get_context_data(self, **kwargs)
                    context = super().get_context_data(**klwargs)
                    context['name'] = 'User'
                    return context
- -- - - -- - - - - - - - - - - -  - -- - - -- - - - - - - - - - - -
    [] FormViews

        Description: 
            * A view that displays a form. 
            * On error, redisplays the form with validation errors; on success, redirects to a new URL.

        Syntax example:

            class ContactFormView(FormView):
                template_name = 'contact.html'
                form_class = ContactForm
                success_url = '/thanks/'

                def form_valid(self, form):
                    # This method is called when valid form data has been POSTed.
                    # It should return an HttpResponse.
                    form.send_email()
                    return super().form_valid(form)

    [] CreatinView

        Description:
            * A view that displays a form for creating an object, redisplaying the form with validation errors (if there are any) and saving the object.
        
        Methods:
            * get(request, *args, **kwargs)
            * post(request, *args, **kwargs)

        Syntax Example:
            class ExampleCreateView(CreateView)
                fields = '__all__'
                model - models.Example
                template_name = 'create_example.html'
                *form_class= exmapleForm - (we can use even a form if we want)


    [] UpdateView

        Description:
            * A view that displays a form for editing an existing object, redisplaying the form with validation errors (if there are any) and saving changes to the object. 
            * This uses a form automatically generated from the object’s model class (unless a form class is manually specified).
        
        Methods:
            * get(request, *args, **kwargs)
            * post(request, *args, **kwargs)

        
        Syntax Example:
            class ExampleUpdateView(UpdateView)
                fields = '__all__'
                model - models.Example
                template_name = 'update_example.html'


    [] DeleteView

        Description:
            * The DeleteView page displayed to a GET request uses a template_name_suffix of '_confirm_delete'. For example, changing this attribute to '_check_delete' for a view deleting objects for the example Author model would cause the default template_name to be 'myapp/author_check_delete.html'.
   
        Syntax Example:
            class ExampleDeleteView(DeleteView)
                fields = '__all__'
                model - models.Example
                template_name = 'delete_example.html'
                success_url = reverse_lazy('app:example')

    - -- - - -- - - - - - - - - - - -  - -- - - -- - - - - - - - - - - -