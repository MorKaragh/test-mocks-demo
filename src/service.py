from src.dependencies.class_dependency import StringProvider
from src.dependencies.field_dependency import global_variable
from src.dependencies.function_dependency import global_function


class Service:

    def __init__(self, provider=StringProvider()):
        self.stored_text = "Hello, "
        self.string_provider = provider

    def get_from_service(self):
        return self.stored_text + self.string_provider.provide()

    def get_from_global_variable(self):
        return self.stored_text + global_variable.value

    def get_from_function(self):
        return self.stored_text + global_function()

#
# service = Service()
# print(service.get_from_service())
# print(service.get_from_function())
# print(service.get_from_global_variable())