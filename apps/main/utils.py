from django.http import HttpResponse

import json as simplejson


class JsonResponse(HttpResponse):
    def __init__(self, data):
        content = json_dumps(data)
        super(JsonResponse, self).__init__(content=content,
                                           mimetype='application/json')


class DecimalEncoder(simplejson.JSONEncoder):
    """JSON encoder which understands decimals."""

    def default(self, obj):
        '''Convert object to JSON encodable type.'''
        if isinstance(obj, decimal.Decimal):
            return "%s" % obj

        return super(DecimalEncoder, self).default(self, obj)


def json_dumps(data):
    return simplejson.dumps(data,
                            indent=2,
                            ensure_ascii=False,
                            cls=DecimalEncoder)