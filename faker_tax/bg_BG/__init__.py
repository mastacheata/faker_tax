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

        return "BG" + self.random_element((self.bothify('##########'), self.bothify('#########')))
