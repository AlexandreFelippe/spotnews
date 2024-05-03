from django.core.exceptions import ValidationError


def validate_title(title):
    if len(title.split()) < 2:
        raise ValidationError("O título deve conter pelo menos 2 palavras.")


def validate_date(value):
    try:
        import datetime
        datetime.datetime.strptime(value, "%Y-%m-%d")
    except ValueError:
        raise ValidationError(
            f"O valor {value} tem um formato de data inválido. Deve ser no formato YYYY-MM-DD."
        )


def validate_empty(value):
    if not value:
        raise ValidationError("Este campo não pode estar vazio.")
