from ..db_session import SessionGenerator

import pinject


class InfraRepositoryBindingSpec(pinject.BindingSpec):
    def configure(self, bind):
        bind(
            'session_generator',
            to_class=SessionGenerator,
            in_scope=pinject.SINGLETON,
        )
