from django.conf import settings

if settings.APP_NAME == 'study_subject_validations':
    from .tests import models