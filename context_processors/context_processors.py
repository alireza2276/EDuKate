from courses.models import Category,Course
from pages.models import Information


def show_category(request):
    category = Category.objects.order_by('datetime_created')

    return {'category': category}


def recent_courses(request):

    recent_course = Course.objects.order_by('-datetime_modified')[:4]

    return {'recent_course': recent_course}


def show_information(request):
    information = Information.objects.all().last()

    return {'information': information}


