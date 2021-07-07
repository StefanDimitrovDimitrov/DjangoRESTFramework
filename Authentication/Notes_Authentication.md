
        #ATHENTICATION

[] Authentication
 - What is Authentication?
    * the process of verifying the identity of a user
 - How Authentication works?
    * credentials provided by the user are compared to those in a database
 - Authentication Factors
    * attribute that can be used to authenticate a user
    * single-factor authentication is authentication with ID and password
    * two-factor authentication can be ID + password + security token
 - Cookies
    * used to store information on the client-side machine
 - Sessions
    * used to store information creating a file on the server

[] Authentication in Django
    * Django has authentication system
        - handles: user accounts, groups, permissions, cookie-based and user sessions
        - manage both authentication and authorization process

    * User objects are the core of the authentication system
        - primary attributes:
            - username
            - password
            - email
            - first_name
            - last_name
    * core functions
        - create_user() or use Django Admin
        - authenticate() - verify credentials(for login)
        - logout(request)
[] Authorization
 - What is Authorization?
    * This is the process of granting or denying access to a network resource based on the user's identity.



[] Permissions and Authorization in Django

    * Groups add permissions to the Group so it applies to each member

    * Build-In Decorators
        - @login_required(login_url='login') - Example only login user are allowed to create somthong

    * Custom Decorators
        - create decorators.py in our app.
        - we can show for example article only if the user has permission to see it
___________________________
        from django.http import HttpResponse

        def group_required(groups=[]):
            groups_set = set(groups)

            def decorator(view_func):
                def wrapper(request, *args, **kwargs):
                    if request.user.is_superuser:
                        return view_func(request, *args, **kwargs)
                    
                    user_groups = set([group.name for group in request.user.groups.all()])

                    if user_groups.intersection(groups_set):
                        return view_func(request, *args, **kwargs)
                    else:
                        return HttpResponse('You are not authorized')

                return wrapper

            return decorator
_______________________

____________________________________

pip install -r requirements.txt

