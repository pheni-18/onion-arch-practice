import infrastructure.repositories as infra_repositories
import pinject


class AppServiceBindingSpec(pinject.BindingSpec):
    def configure(self, bind):
        bind(
            'user_repo',
            to_class=infra_repositories.UserRepository,
            in_scope=pinject.SINGLETON,
        )

    def dependencies(self):
        return [infra_repositories.InfraRepositoryBindingSpec()]
