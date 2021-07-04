from django import template

from Templates.todos.models import Todo

register = template.Library()


@register.simple_tag()
def todos_count():
    return Todo.objects.count()


@register.inclusion_tag('todo/shared/templatetags/todos/todos_preview.html',
                        takes_context=True,)
def todos_preview(context):
    return {
        'count': Todo.objects.count()
    }
