from edc_constants.constants import YES, NO
from edc_form_validators import FormValidator


class SubjectScreeningFormValidator(FormValidator):

    def clean(self):
        self.required_if(
            YES,
            field='marriage_certificate',
            field_required='marriage_certificate_no',
        )

        self.required_if(
            NO,
            field='literacy',
            field_required='witness',
        )

        self.required_if(
            NO,
            field='citizen',
            field_required='legal_marriage',
        )
