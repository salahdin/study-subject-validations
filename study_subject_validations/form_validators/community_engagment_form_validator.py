from edc_constants.constants import YES, NO
from edc_form_validators import FormValidator


class CommunityFormValidator(FormValidator):

    def clean(self):
        self.required_if_not_none(
            field='marriage_certificate',
            field_required='marriage_certificate_no',
        )


