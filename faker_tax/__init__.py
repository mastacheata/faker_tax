# -*- coding: utf-8 -*-
from faker.providers import BaseProvider

localized = True
default_locale = 'de_DE'


class Provider(BaseProvider):
    """
    A Faker provider for the Empto project
    """

    def tax_id(self):
        """
        Returns a random generated Tax ID
        """

        return "DE" + str(self.random_number(9, True))

    def tax_number(self):
        """
        Generates a random tax number
        """

        return str(self.random_number(3, True)) + '/' + str(self.random_number(3, True)) + '/' + \
            str(self.random_number(3, True))
