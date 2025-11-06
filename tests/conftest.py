"""Test configuration and fixtures."""

import pytest
import asyncio
from typing import AsyncGenerator

from starward.core.state_engine import StateEngine
from starward.core.registry import ServiceRegistry
from starward.services.s3 import MockS3Service
from starward.services.sqs import MockSQSService


@pytest.fixture
def state_engine() -> StateEngine:
    """Provide a state engine instance."""
    return StateEngine()


@pytest.fixture
async def s3_service(state_engine: StateEngine) -> AsyncGenerator[MockS3Service, None]:
    """Provide an S3 service instance."""
    service = MockS3Service(state_engine)
    await service.start()
    yield service
    await service.stop()


@pytest.fixture
async def sqs_service(state_engine: StateEngine) -> AsyncGenerator[MockSQSService, None]:
    """Provide an SQS service instance."""
    service = MockSQSService(state_engine)
    await service.start()
    yield service
    await service.stop()


@pytest.fixture
def service_registry() -> ServiceRegistry:
    """Provide a service registry instance."""
    return ServiceRegistry()
