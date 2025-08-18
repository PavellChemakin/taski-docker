from rest_framework.renderers import JSONRenderer


class NoCharsetJSONRenderer(JSONRenderer):
    charset = None
