# Standard Libraries
import inspect

# Third Party Libraries
import cerberus
from apistar import Component, exceptions
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


class ApistarValidator(cerberus.Validator):
    @property
    def __name__(self):
        return repr(self)

    def validate(self, *args, **kwargs):
        kwargs['update'] = self._config.get("update", False)
        super().validate(*args, **kwargs)