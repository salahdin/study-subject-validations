from edc_constants.constants import YES
from edc_form_validators import FormValidator


class EducationFormValidator(FormValidator):
    def clean(self):
        required_fields = ['employment_type', 'occupation',
                           'income']

        for required in required_fields:
            if required in self.cleaned_data:
                self.required_if(
                    YES,
                    field='employment',
                    field_required=required)
