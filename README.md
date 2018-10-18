# Faker Tax

[![PyPI
Package](https://badge.fury.io/py/faker-tax.svg)](https://badge.fury.io/py/faker-tax)
[![Build
Status](https://travis-ci.org/mastacheata/faker-tax.svg)](https://travis-ci.org/mastacheata/faker-tax)

[Faker](https://github.com/joke2k/faker/) provider for Tax IDs and
numbers.

[![Faker Tax -
Demo](docs/img/demo.png)](https://asciinema.org/a/207271)

# Usage

```python
from faker import Faker
from faker_tax import Provider as TaxProvider 
fake = Faker()
fake.add_provider(TaxProvider)
fake.tax_id()
fake.tax_number()
```

# License

[MIT](https://opensource.org/licenses/MIT)
