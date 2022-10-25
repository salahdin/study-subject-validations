from django.core.exceptions import ValidationError
from django.test import TestCase
from edc_constants.constants import YES
from ..form_validators import CommunityFormValidator


class TestCommunityForm(TestCase):

    def test_had_chemo_treatment_details_required(self):

        cleaned_data = {
            'marriage_certificate': YES,
            'marriage_certificate_no': None}
        form_validator = CommunityFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('marriage_certificate_no', form_validator._errors)