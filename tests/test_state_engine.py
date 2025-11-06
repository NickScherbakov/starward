"""Tests for state engine."""

import pytest
from datetime import datetime

from starward.core.state_engine import StateEngine, Snapshot


@pytest.mark.unit
def test_state_engine_set_get(state_engine: StateEngine) -> None:
    """Test basic state get/set."""
    state_engine.set_state("key1", "value1")
    assert state_engine.get_state("key1") == "value1"
    assert state_engine.get_state("nonexistent") is None
    assert state_engine.get_state("nonexistent", "default") == "default"


@pytest.mark.unit
def test_state_engine_clear(state_engine: StateEngine) -> None:
    """Test state clearing."""
    state_engine.set_state("key1", "value1")
    state_engine.set_state("key2", "value2")
    state_engine.clear_state()
    assert state_engine.get_state("key1") is None
    assert state_engine.get_state("key2") is None


@pytest.mark.unit
async def test_snapshot_create(state_engine: StateEngine) -> None:
    """Test snapshot creation."""
    state_engine.set_state("test_key", "test_value")
    snapshot = await state_engine.create_snapshot("test_snapshot")
    
    assert snapshot.id == "test_snapshot"
    assert snapshot.state["test_key"] == "test_value"
    assert isinstance(snapshot.timestamp, datetime)


@pytest.mark.unit
async def test_snapshot_restore(state_engine: StateEngine) -> None:
    """Test snapshot restoration."""
    state_engine.set_state("key1", "value1")
    await state_engine.create_snapshot("snapshot1")
    
    state_engine.set_state("key1", "value2")
    assert state_engine.get_state("key1") == "value2"
    
    await state_engine.restore_snapshot("snapshot1")
    assert state_engine.get_state("key1") == "value1"


@pytest.mark.unit
def test_time_freeze(state_engine: StateEngine) -> None:
    """Test time freezing."""
    frozen_time = datetime(2025, 1, 1, 12, 0, 0)
    state_engine.freeze_time(frozen_time)
    
    assert state_engine.now() == frozen_time
    
    state_engine.unfreeze_time()
    assert state_engine.now() != frozen_time


@pytest.mark.unit
def test_random_seed(state_engine: StateEngine) -> None:
    """Test deterministic random seed."""
    state_engine.set_seed(42)
    # Random operations would be deterministic here
    assert state_engine._random_seed == 42
