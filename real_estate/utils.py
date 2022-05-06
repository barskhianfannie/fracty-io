def get_next_number(cls, field_name: str, **kwargs):
    from django.db.models import Max
    qs = cls.objects.all()
    max_number = qs.aggregate(Max(field_name))[field_name + '__max']
    if max_number:
        return int(max_number) + 1
    else:
        return
