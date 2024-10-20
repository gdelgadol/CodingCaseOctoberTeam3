from MakersTech.MakersTechApp.views import ProductViewSet, BrandViewSet, FeatureViewSet
from rest_framework.test import APIRequestFactory
from rest_framework.request import Request

def get_products():
    factory = APIRequestFactory()
    request = factory.get('/api/product/')
    viewset = ProductViewSet()
    viewset.request = Request(request)
    response = viewset.list(request)
    return response.data

def get_brands():
    factory = APIRequestFactory()
    request = factory.get('/api/brand/')
    viewset = BrandViewSet()
    viewset.request = Request(request)
    response = viewset.list(request)
    return response.data

def get_features():
    factory = APIRequestFactory()
    request = factory.get('/api/feature/')
    viewset = FeatureViewSet()
    viewset.request = Request(request)
    response = viewset.list(request)
    return response.data

FUNCTIONS_LIST = {
    'get_products': get_products,
    'get_brands': get_brands,
    'get_features': get_features,
}

TOOLS = [
    {
        'type': 'function',
        'function': {
            'name': 'get_products',
            'description': 'Get a list of all products',
            'parameters': {
                'type': 'object',
                'properties': {},
                'required': [],
            },
        },
    },
    {
        'type': 'function',
        'function': {
            'name': 'get_brands',
            'description': 'Get a list of all brands',
            'parameters': {
                'type': 'object',
                'properties': {},
                'required': [],
            },
        },
    },
    {
        'type': 'function',
        'function': {
            'name': 'get_features',
            'description': 'Get a list of all features',
            'parameters': {
                'type': 'object',
                'properties': {},
                'required': [],
            },
        },
    },
]