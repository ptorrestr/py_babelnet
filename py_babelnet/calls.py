import requests

class RestAPI(object):
    """ Class to handle calls to Rest service
    Args:
        url: service base url
    """
    def __init__(self, url):
        self.base = url

    def _endpoint(self, resource):
        """ Generate the endpoint using the url and the resource
        name
        Args:
            resource: the name of the resource
        Response:
            str of the endpoint
        """
        return '{}/{}'.format(self.base, resource)

    def _encode_params(self, params):
        """ Generate string of the dict of params.
        Args:
            params: the dictionary of params
        Response:
            str of the params
        """
        return "&".join("{}={}".format(k,v) for k,v in params.items())

    def _call(self, method, resource, **kargs):
        """ Do a call to resource using the given method. Additional
        parameters are sent directly to requests (e.g. headers, data).
        Args:
            method: The requests function to employ (e.g. get, post).
            resource: The name of the resource to call.
        Response:
            The requests response obtained
        """
        r = method(self._endpoint(resource), **kargs)
        r.raise_for_status()
        return r

class BabelnetAPI(RestAPI):
    """ Class to handle REST calls to BabelNet API.
    Args:
        key: the key to the rest service.
    """

    def __init__(self, key, url = "https://babelnet.io/v5"):
        self.key = key
        super().__init__(url)

    def _add_key(self, args):
        """ Add the key to the parameter dictionary
        Args:
            args: dictionary of parameters
        Response:
            dictionary of parameters including the key.
        """
        args['key'] = self.key
        return args

    def _headers(self):
        """ Return default headers for all methods
        Response:
            dictionary of headers.
        """
        return {'Accept': 'application/json'}

    def get_version(self, **kargs):
        """ Method to call getVersion
        See: https://babelnet.org/guide
        Response:
            json output as a dictionary
        """
        r = self._call(requests.get, "getVersion",
                params = self._encode_params(self._add_key(kargs)),
                headers = self._headers())
        return r.json()

    def get_synset_ids(self, **kargs):
        """ Method to call getSynsetIds
        See: https://babelnet.org/guide
        Response:
            json output as a dictionary
        """
        r = self._call(requests.get, "getSynsetIds",
                params = self._encode_params(self._add_key(kargs)),
                headers = self._headers())
        return r.json()

    def get_synset(self, **kargs):
        """ Method to call getSynset
        See: https://babelnet.org/guide
        Response:
            json output as a dictionary
        """
        r = self._call(requests.get, "getSynset",
                params = self._encode_params(self._add_key(kargs)),
                headers = self._headers())
        return r.json()

    def get_senses(self, **kargs):
        """ Method to call getSenses
        See: https://babelnet.org/guide
        Response:
            json output as a dictionary
        """
        r = self._call(requests.get, "getSenses",
                params = self._encode_params(self._add_key(kargs)),
                headers = self._headers())
        return r.json()

    def get_synset_ids_from_resource_id(self, **kargs):
        """ Method to call getSynsetIdsFromResourceID
        See: https://babelnet.org/guide
        Response:
            json output as a dictionary
        """
        r = self._call(requests.get, "getSynsetIdsFromResourceID",
                params = self._encode_params(self._add_key(kargs)),
                headers = self._headers())
        return r.json()

    def get_outgoing_edges(self, **kargs):
        """ Method to call getOutgoingEdges
        See: https://babelnet.org/guide
        Response:
            json output as a dictionary
        """
        r = self._call(requests.get, "getOutgoingEdges",
                params = self._encode_params(self._add_key(kargs)),
                headers = self._headers())
        return r.json()
