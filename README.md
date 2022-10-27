# Foobar

Foobar is a Python library for dealing with word pluralization.

## Installation

Clone the repository

```bash
~: $ git clone <repo>
~: $ cd project/
```

Use the python virtual environment to install all required python modules (django, azure, bootstrap, etc...).

```bash
~/project: $ python3 -m venv venv
~/project: $ source venv/bin/activate
(venv) ~/project: $ pip install -r requirements.txt

```

## Usage

```python
import foobar

# returns 'words'
foobar.pluralize('word')

# returns 'geese'
foobar.pluralize('goose')

# returns 'phenomenon'
foobar.singularize('phenomena')
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
