from django.core.exceptions import ValidationError
import datetime


def validate_fields(value):
    value_without_spaces = value.replace(" ", "")
    if 1 > len(value_without_spaces) > 200:
        raise ValidationError


def validate_title(value):
    title = value.split()
    if len(title) < 2:
        raise ValidationError("O título deve conter pelo menos 2 palavras.")


def validate_date(value):
    try:
        date_string = str(value)
        datetime.datetime.strptime(date_string, "%Y-%m-%d")
    except ValueError:
        raise ValidationError("Incorrect data format, should be YYYY-MM-DD")


most_common_validation = {"max_length": 200, "validators": [validate_fields]}
validation_for_news_title = {
    "max_length": 200,
    "validators": [validate_fields, validate_title],
}
