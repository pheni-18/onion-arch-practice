import domain.services as domain_services
import pinject


class AppServiceBindingSpec(pinject.BindingSpec):
    def configure(self, bind):
        pass

    def dependencies(self):
        return [domain_services.DomainServiceBindingSpec()]
