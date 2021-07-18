import infrastructure as infra
import pinject


class DomainServiceBindingSpec(pinject.BindingSpec):
    def configure(self, bind):
        bind(
            'user_repo',
            to_class=infra.UserRepository,
            in_scope=pinject.SINGLETON,
        )

    def dependencies(self):
        return [infra.InfraServiceBindingSpec()]
