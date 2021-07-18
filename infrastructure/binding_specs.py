from ._fake_db import FakeDB

import pinject


class InfraServiceBindingSpec(pinject.BindingSpec):
    def configure(self, bind):
        bind(
            'db',
            to_class=FakeDB,
            in_scope=pinject.SINGLETON,
        )
