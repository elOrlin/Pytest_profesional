from faker.providers import BaseProvider


class CustomProvider(BaseProvider):
    def custom_email(self):
        return f"{self.generator.last_name().lower()}@correo.com"
