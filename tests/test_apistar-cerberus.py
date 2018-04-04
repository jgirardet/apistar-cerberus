import inspect
import cerberus
from apistar import Route, App, TestClient

from apistar_cerberus import CerberusComp
import inspect
import json


class RienValidator(cerberus.Validator):
    @property  # add __name__ needed by apistar
    def __name__(self):
        return repr(self)

    def validate(self, *args,
                 **kwargs):  #  to disable property at instanciation
        kwargs['update'] = self._config.get("update", False)
        super().validate(*args, **kwargs)


schema = {
    "a": {
        "type": "string",
        "required": True
    },
    "b": {
        "type": "string"
    },
}

RienCerbCreate = RienValidator(schema)
RienCerbUpdate = RienValidator(schema, update=True)


def helloCerb(rien: RienCerbCreate):
    return rien


def helloCerbUpdate(rien: RienCerbUpdate):
    return rien


routen = Route(url='/n/', method='POST', handler=helloCerb)
routeupdate = Route(url='/update/', method='POST', handler=helloCerbUpdate)

app = App(routes=[routen, routeupdate], components=[CerberusComp()])

cli = TestClient(app)


def test_wrong_type():
    rn = cli.post('/n/', data=json.dumps({'a': 1}))
    assert rn.json() == {'a': ['must be of string type']}


def test_field_required():
    rn = cli.post('/n/', data=json.dumps({'b': "hello Cerberus"}))
    assert rn.json() == {'a': ['required field']}


def test_good_required_and_not():
    rn = cli.post(
        '/n/',
        data=json.dumps({
            "a": "whith required field",
            'b': "hello Cerberus"
        }))
    assert rn.json() == {'a': 'whith required field', 'b': 'hello Cerberus'}


def test_update_trus_at_instantiate():
    rn = cli.post('/update/', data=json.dumps({'b': "hello Cerberus"}))
    assert rn.json() == {'b': 'hello Cerberus'}
