# Login and Register

IN Settings LOGIN_IN = LOGIN_URL = '/auth/login/'

    Topics:
        * User
        * Registers
            build in USER class
            builf in UserCrationForm
        * Login
        * How to 


    What we learn:
        Register - we can use build in User class. 
        UserCreationForm - build in form we can use if we want to have password confirmation



    How to do it:


notes: 
    primary_key=True, - same primary_key in the user and in the Profile


    * we have to add validation for field email to make it requierd field
        def clean_email(self):
        email = self.cleaned_data.get('email', False)
        if not email:
            raise forms.ValidationError('Email is required')
        return email


Create: 
    new app for register, login, logout,
    new app for the profile
    add to settings
        AUTH_USER_MODEL='pythoon_auth.PythonsUser' 




Today's Topics :
    Register Form
    Login Form
    Logout Form
    User Class
    UserCreatinForm
    authenticate()
    ProfileModel
    ProfileForm
    DjangoSignal
        - function
        - authomated peace of code
    AbstractUser
    AbstractBaseUser
        * USERNAME_FIELD
    AUTH_USER_MODEL='pythoon_auth.PythonsUser'
    get_user_model()
    BaseUserManager


[] Register
    * we create а new app called NAME_auth for example pythons_auth
    * mainly we write code in the views.py
    * we check if there is a POST request and then perform an action
    * We can use build in UserCreationForm()
    * If we want to save the information directly to the database we use user.save()
    * If we want to add to the user a profile we can use "commite=False":
        Example:
            user_form = RegisterForm(request.POST)
            profile_form = ProfileForm(request.POST, request.FILES)

            if user_form.is_valid() and profile_form.is_valid():
                user = user_form.save()
                profile = profile_form.save(commit=False)
                profile.user = user
                profile.save()
    * we have to add in urlpaterns path for register views
    * and to register our new app in settings

[] Login
    * Settings:
        LOGIN_URL = reverse.lazy('sign in) - that way we can use only @login_required decorator without additional code
    * create Login Form ( there is't build in LoginCreationForm like UserCreationForm() )
        Example:
        class SignInForm(forms.Form)
            username = forms.CharField()
            password = forms.CharField()
            def clean_password(self):
            def save(self):
    * check if the user is authenticate() in the form if not raise a ValidationError
    * use def save(self) to return self.user
    * in View we have standard view where we check if the request is POST if the form is Valid we have to form.save() and to login the user if not our validation in the form will raise an error

[] Logout
    Example:
        def sign_out(request):
            logout(request)
            return redirect('index')


[] Custom User Model + profile model
    + Full Control over the user model
    + Pure user model
     
    - Some code for login/register
