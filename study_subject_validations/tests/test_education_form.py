from django.core.exceptions import ValidationError
from django.test import TestCase
from edc_constants.constants import YES
from ..form_validators import EducationFormValidator


class TestEducationFormValidator(TestCase):

    def test_employment_type_required(self):
        cleaned_data = {
            'employment': YES,
            'employment_type': None}
        form_validator = EducationFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('employment_type', form_validator._errors)
