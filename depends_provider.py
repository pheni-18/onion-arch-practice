from common.singleton import MetaSingleton

import application.services as app_services
import pinject


class DependsProvider(metaclass=MetaSingleton):
    _obj_graph: pinject.object_graph.ObjectGraph

    def __init__(self):
        self._obj_graph = pinject.new_object_graph(
            binding_specs=[
                app_services.AppServiceBindingSpec(),
            ],
            only_use_explicit_bindings=True,
        )

    # TODO: type hint cls
    def provide(self, cls):
        return self._obj_graph.provide(cls)
