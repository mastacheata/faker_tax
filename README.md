=================
Faker Tax
=================

|PyPI Package| |Build Status|

`Faker <https://github.com/joke2k/faker/>`__ provider for Tax IDs and numbers.

.. image:: docs/img/faker_tax_demo.gif
   :target: https://asciinema.org/a/207271
   :alt: Faker Tax - Demo

Usage
=====

```python
from faker import Faker
from faker_tax import Provider as TaxProvider

fake = Faker()
fake.add_provider(TaxProvider)

fake.tax_id()
fake.tax_number()

```

License
=======

`MIT <https://opensource.org/licenses/MIT>`__

.. |Build Status| image:: https://travis-ci.org/mastacheata/faker-tax.svg
   :target: https://travis-ci.org/mastacheata/faker-tax
   :alt: Build Status
.. |PyPI Package| image:: https://badge.fury.io/py/faker-tax.svg
   :target: https://badge.fury.io/py/faker-tax
   :alt: PyPI Package
