import datetime

from django.conf import settings


def get_project_detail(request):
    return {
        'PROJECT_NAME': settings.PROJECT_NAME,
        'PROJECT_TAGLINE': settings.PROJECT_TAGLINE,
    }
