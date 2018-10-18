# -*- coding: utf-8 -*-

from .. import Provider as TaxProvider


class Provider(TaxProvider):
    """
    A Faker provider for the Empto project
    """

    def tax_id(self):
        """
        Returns a random generated Tax ID
        """

        return "DE" + str(self.bothify('#########'))

    def tax_number(self):
        """
        Generates a random tax number
        """

        return str(self.random_number(3, True)) + '/' + str(self.random_number(3, True)) + '/' + \
            str(self.random_number(3, True))
