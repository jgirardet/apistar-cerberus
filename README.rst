===============================
apistar-cerberus
===============================

.. image:: https://travis-ci.org/jgirardet/apistar-cerberus.svg?branch=master
    :target: https://travis-ci.org/jgirardet/apistar-cerberus
.. image:: https://coveralls.io/repos/github/jgirardet/apistar-cerberus/badge.svg
   :target: https://coveralls.io/github/jgirardet/apistar-cerberus
.. image:: https://badge.fury.io/py/apistar-cerberus.svg
   :target: https://pypi.python.org/pypi/apistar-cerberus/
   :alt: Pypi package


Add Cerberus type system in Apistar


* License : GNU General Public License v3 
* Documentation: https://apistar-cerberus.readthedocs.org/en/latest/
* Source: https://github.com/jgirardet/apistar-cerberus

Features
--------

- Add `Cerberus`_ support to `Apistar`_ as type system validator via component system.
- Provides `CerberusComp` as Apistar component and `ApistarValidator` as base validator.


Usage
-----

- just add the component to to App, and use ApistarValidator :

.. code-block:: python

	# Main app.y
    from apistar_cerberus import CerberusComp
    ...

    app = App(components= [CerberusComp()])

    # views.py

    schema = {"some":"ceberus", "schema"; "here"}

    MyValidator = ApistarValidator(schema)

    def myviews(validator: MyValidator):
   	    return WhatYouWant


- ApistarValidator is not fully required. Apistar just need a custom unique attribute `__name__` to the class to make it work. Remember if you define your own Validator : `__name__` must be unique because it's used by the Injector. ApistarValidator uses the adress in memory which is unique.

- ApistarValidator also add a custom `update` to allow `validate(update=True)` to validator which is not yet supported by Cerberus. It's needed in Apistar because we don't have access to validation after instanciation.


.. _`Apistar`: https://github.com/encode/apistar
.. _Cerberus: https://github.com/pyeve/cerberus