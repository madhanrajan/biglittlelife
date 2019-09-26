from django.core.exceptions import ValidationError
from profanity_check import predict


def validate_profane(text):
    if predict([text]):
        raise ValidationError('Please remove any swear words!')
    else:
        return text
