# -*- coding: utf-8 -*-

import unittest

from faker import Faker
from faker_tax import Provider


class TestTaxProvider(unittest.TestCase):
    def test_default_locale(self):
        fake = Faker()
        fake.add_provider(Provider)
        for i in range(10):
            self.assertTrue(isinstance(fake.tax_id(), str))

    def test_de_DE(self):
        fake = Faker('de_DE')
        fake.add_provider(Provider)
        for i in range(10):
            tax_id = fake.tax_id()
            self.assertTrue(isinstance(tax_id, str))
            self.assertEqual(11, len(tax_id))
            self.assertEqual('DE', tax_id[:2])

    def test_dk_DK(self):
        fake = Faker('dk_DK')
        fake.add_provider(Provider)
        for i in range(10):
            tax_id = fake.tax_id()
            self.assertTrue(isinstance(tax_id, str))
            self.assertEqual('DK', tax_id[:2])
            self.assertEqual(10, len(tax_id))
