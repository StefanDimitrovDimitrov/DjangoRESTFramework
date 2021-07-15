Generic steps

* [ ]  create postgres_db giving a name 
* [ ]  add db settings
* [ ]  look at Installations
* [ ]  start new app for the project in manage.py startapp name
* [ ]  add the name of the app to the main project'
* [ ]  add the app in settings
* [ ]  create file urls 
* [ ]  add urlpatterns us empty list in it
* [ ]  add in the main url folder path using include django module

Installations
* [ ]  install psycopg2 using pip install psycopg2 binary
* [ ]  install Pillow using pip install pillow


Settings.py 

* [ ] STATICFILES_DIRS = (join(BASE_DIR, 'static'),)
        (os.path.join)

* [ ] MEDIA_URL = '/media/'
        MEDIA_ROOT = join(BASE_DIR, 'media/')
  
* [ ] LOGIN_URL = '/auth/login/'
  
urlPatterns = [

]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

Create user_auth_app:
 * [] startapp NAME_auth
 * [] do everything applicable for new app Settings, urls and etc,
 * []      urlpatterns = [
            path('sign-in/', views.sign_in, name='sign in'),
            path('sign-out/', views.sign_out, name ='sign out'),
        ]


App steps

* [ ] create models based on the requirements
* [ ] make relation between each models
* [ ] register your models in admin
* [ ] makemigrations and migrate
* [ ] create superuser
* [ ] test the admin panel
* [ ] create item in it
* [ ] create empty views based on the requirements
* [ ] add them to the urls
* [ ] test the index page
* [ ] create ModelForms based on Model
    inherited from forms.ModelForm or forms.Form
* [ ] fill in the views with content
* [ ] templates management
    * [ ] crate folder shared and file main.html
    * [ ] move the nav bar there
        use the following syntax:
            {% extends 'shared/main.html' %}
        {% block main_container %}
        {% endblock %}
    * [ ] put {% csrf_token %} on each form
    * [ ] urls
* [ ] validations
* [ ] test the application

xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx


