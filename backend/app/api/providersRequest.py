import json

from flask import request, jsonify, make_response
from flask_restplus import Resource
from sqlalchemy.exc import IntegrityError
from .exceptionHandler import InvalidUsage

from . import api_rest
from ..database.entities import Provider
from ..database.operations import ProvidersStore


@api_rest.route('/providers')
class ProvidersData(Resource):
    def get(self):
        provider_store = ProvidersStore()
        provider_data = provider_store.get_providers()
        return jsonify([Provider.serialize(provider) for provider in provider_data])

    def post(self):
        payload = request.get_json()
        provider_store = ProvidersStore()
        try:
            provider_store.insert(payload.get('providerId'), payload.get('providerName'))
        except IntegrityError:
            raise InvalidUsage('Duplicated Provider', status_code=400)

        result = {'data': True}
        return json.dumps(result)


