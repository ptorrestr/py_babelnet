# Py\_BabelNet

Python client for BabelNet API.

## Usage

```python
from py_babelnet.calls import BabelnetAPI
api = BabelnetAPI('mykey')
senses = api.get_senses(lemma = "agua", searchLang = "ES")
```

## Test

```bash
BABELNET_KEY="my-key" pipenv run setup.py test
```
