from django.db import models


# Create your models here.
class CBVViews(models.Model):
    BASEVIEW = 'Base view'
    GENERICDISPLAYVIEWS = 'Generic display views'
    GENERICEDITINGVIEWS = 'Generic editing views'
    UNKNOWN = 'Unknown'

    VIEW = 'View'
    TEMPLATEVIEW = 'Template view'
    REDIRECTVIEW = 'Redirect view'
    DETAILVIEW = 'Detail view'
    LISTVIEW = 'List view'
    FORMVIEW = 'Form view'
    CREATEVIEW = 'Create view'
    UPDATEVIEW = 'Update view'
    DELETEVIEW = 'Delete view'

    VIEWS_TYPES = (
        (BASEVIEW, 'Base View'),
        (GENERICDISPLAYVIEWS, 'Generic Display Views'),
        (GENERICEDITINGVIEWS, 'Generic Editing Views'),
        (UNKNOWN, 'Unknown'),
    )

    VIEWS_NAMES =(
        (VIEW, 'View'),
        (TEMPLATEVIEW, 'Template View'),
        (REDIRECTVIEW, 'Redirect View'),
        (DETAILVIEW, 'Detail View'),
        (FORMVIEW, 'Form View'),
        (CREATEVIEW, 'Create View'),
        (UPDATEVIEW, 'Update View'),
        (DELETEVIEW, 'Delete View'),
        (UNKNOWN, 'Unknown'),
    )



    type = models.CharField(max_length=25, choices=VIEWS_TYPES, default=UNKNOWN)
    name = models.CharField(max_length=25, choices=VIEWS_NAMES, default=UNKNOWN)
    description = models.TextField(max_length=300)
    example = models.ImageField()

    def __str__(self):
        return self.name