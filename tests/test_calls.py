import pytest
import requests
import os
from py_babelnet.calls import BabelnetAPI

@pytest.fixture(scope = "session")
def api():
    key = os.environ['BABELNET_KEY']
    return BabelnetAPI(key)

def test_get_version(api):
    out = api.get_version()
    assert out["version"] == "V4_0"

def test_get_synset_ids(api):
    out = api.get_synset_ids(lemma = "apple", searchLang = "EN")
    assert len(out) > 0

def test_get_synset(api):
    out = api.get_synset(id = "bn:14792761n")
    assert len(out["senses"]) > 0

def test_get_senses(api):
    out = api.get_senses(lemma = "BabelNet", searchLang = "EN")
    assert len(out) > 0

def test_get_synset_ids_from_resource_id(api):
    out = api.get_synset_ids_from_resource_id(id = "BabelNet",
            searchLang = "EN", pos = "NOUN", source = "WIKI")
    assert len(out) == 1

def test_outgoing_edges(api):
    out = api.get_outgoing_edges(id = "bn:03083790n")
    assert len(out) > 0

def test_wrong_call(api):
    with pytest.raises(requests.exceptions.HTTPError):
        api.get_outgoing_edges(ids = "asd")
