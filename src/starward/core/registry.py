"""Service registry for managing cloud service implementations."""

from typing import Any, Dict, Protocol, Type
from abc import ABC, abstractmethod


class CloudService(Protocol):
    """Protocol for cloud service implementations."""

    service_name: str

    async def start(self) -> None:
        """Start the service."""
        ...

    async def stop(self) -> None:
        """Stop the service."""
        ...

    async def reset(self) -> None:
        """Reset service state."""
        ...


class ServiceRegistry:
    """Registry for managing service instances."""

    def __init__(self) -> None:
        self._services: Dict[str, Any] = {}
        self._service_types: Dict[str, Type[Any]] = {}

    def register_type(self, name: str, service_type: Type[Any]) -> None:
        """Register a service type."""
        self._service_types[name] = service_type

    def create_service(self, name: str, *args: Any, **kwargs: Any) -> Any:
        """Create and register a service instance."""
        if name not in self._service_types:
            raise ValueError(f"Unknown service type: {name}")
        service = self._service_types[name](*args, **kwargs)
        self._services[name] = service
        return service

    def get_service(self, name: str) -> Any:
        """Get a registered service instance."""
        return self._services.get(name)

    def list_services(self) -> list[str]:
        """List all registered service names."""
        return list(self._services.keys())

    async def start_all(self) -> None:
        """Start all registered services."""
        for service in self._services.values():
            await service.start()

    async def stop_all(self) -> None:
        """Stop all registered services."""
        for service in self._services.values():
            await service.stop()

    async def reset_all(self) -> None:
        """Reset all registered services."""
        for service in self._services.values():
            await service.reset()
