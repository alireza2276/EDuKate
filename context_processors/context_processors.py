from courses.models import Category,Course


def show_category(request):
    category = Category.objects.order_by('datetime_created')

    return {'category': category}


def recent_courses(request):

    recent_course = Course.objects.order_by('-datetime_modified')[:3]

    return {'recent_course': recent_course}
