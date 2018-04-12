# Standard Libraries
import inspect
import json

# Third Party Libraries
import cerberus
from apistar import App, Route, TestClient
from apistar_cerberus import ApistarValidator, CerberusComp

schema = {
    "a": {
        "type": "string",
        "required": True
    },
    "b": {
        "type": "string"
    },
}

RienCerbCreate = ApistarValidator(schema)
RienCerbUpdate = ApistarValidator(schema, update=True)


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
