from unittest import mock
from unittest.mock import Mock

import pytest

from src.dependencies.class_dependency import StringProvider
from src.dependencies.field_dependency import Settings
from src.service import Service


@pytest.mark.foo
def test_get_from_service():
    provider_mock = Mock(StringProvider)
    provider_mock.provide.return_value = "World"

    service = Service(provider_mock)

    assert service.get_from_service() == "Hello, World"
    assert not service.get_from_service() == "Hello, Universe"


@pytest.mark.bar
def test_get_from_global_variable():
    with mock.patch("src.service.global_variable", Settings(value="World")):
        service = Service()
        assert service.get_from_global_variable() == "Hello, World"
        assert not service.get_from_global_variable() == "Hello, Universe"


@pytest.mark.bar
def test_get_from_global_function():
    function_mock = Mock()
    function_mock.return_value = "World"
    with mock.patch("src.service.global_function", function_mock):
        service = Service()
        assert service.get_from_function() == "Hello, World"
        assert not service.get_from_function() == "Hello, Universe"
