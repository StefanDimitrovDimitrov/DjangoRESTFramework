#ExtendingUserModel
1.Create app NAME_auth
2.Create two classes in Models: ProjectNameUser, and ProjectUserManager
3.Settings: AUTH_USER_MODEL = our_project_auth.OurUser
4.ProjectUser(AbstractBaseUser, PermissionsMixin)
    Example:
        email = models.EmailField(unique=True,)
        USERNAME_FIELD = 'email'
        objects = ProjectUserManager()
5.ProjectUserManager(BaseUserManager)
    - remove all unnecessary fields
6.We can access our new USERMODEL through UserModel = get_user_model()
7.admin.py register the Model
8.makemigrations
9.migrate