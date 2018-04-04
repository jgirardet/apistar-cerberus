# -*- coding: utf-8 -*-
from apistar import Component, exceptions
import cerberus
import inspect

from apistar.server.validation import ValidatedRequestData


class CerberusComp(Component):
    def can_handle_parameter(self, parameter: inspect.Parameter):
        return isinstance(parameter.annotation, cerberus.Validator)

    def resolve(self, parameter: inspect.Parameter,
                data: ValidatedRequestData):

        v = parameter.annotation
        validated_data = v.validated(data)
        if validated_data:
            return validated_data
        else:
            raise exceptions.BadRequest(v.errors)
