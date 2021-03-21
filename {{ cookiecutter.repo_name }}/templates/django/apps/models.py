{% raw %}from django.db import models


class {{ camel_case_app_name|title }}(models.Model):

    def __str__(self):
        return f"{self.id}"{% endraw %}
