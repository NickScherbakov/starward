"""State engine for deterministic snapshots and replay."""

import json
import asyncio
from typing import Any, Dict, Optional
from datetime import datetime
from pathlib import Path
from dataclasses import dataclass, field, asdict
import random


@dataclass
class Snapshot:
    """Represents a state snapshot."""

    id: str
    timestamp: datetime
    state: Dict[str, Any]
    metadata: Dict[str, str] = field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        """Convert snapshot to dictionary."""
        return {
            "id": self.id,
            "timestamp": self.timestamp.isoformat(),
            "state": self.state,
            "metadata": self.metadata,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Snapshot":
        """Create snapshot from dictionary."""
        return cls(
            id=data["id"],
            timestamp=datetime.fromisoformat(data["timestamp"]),
            state=data["state"],
            metadata=data.get("metadata", {}),
        )


class StateEngine:
    """Manages deterministic state with snapshot/replay capability."""

    def __init__(self, snapshot_dir: str = "snapshots") -> None:
        self._state: Dict[str, Any] = {}
        self._snapshots: Dict[str, Snapshot] = {}
        self._snapshot_dir = Path(snapshot_dir)
        self._snapshot_dir.mkdir(parents=True, exist_ok=True)
        self._current_time = datetime.utcnow()
        self._time_frozen = False
        self._random_seed: Optional[int] = None

    def set_seed(self, seed: int) -> None:
        """Set random seed for deterministic operations."""
        self._random_seed = seed
        random.seed(seed)

    def freeze_time(self, timestamp: Optional[datetime] = None) -> None:
        """Freeze time at a specific point."""
        self._time_frozen = True
        if timestamp:
            self._current_time = timestamp

    def unfreeze_time(self) -> None:
        """Unfreeze time."""
        self._time_frozen = False

    def now(self) -> datetime:
        """Get current time (frozen or real)."""
        if self._time_frozen:
            return self._current_time
        return datetime.utcnow()

    def set_state(self, key: str, value: Any) -> None:
        """Set a state value."""
        self._state[key] = value

    def get_state(self, key: str, default: Any = None) -> Any:
        """Get a state value."""
        return self._state.get(key, default)

    def get_all_state(self) -> Dict[str, Any]:
        """Get all state."""
        return self._state.copy()

    def clear_state(self) -> None:
        """Clear all state."""
        self._state.clear()

    async def create_snapshot(self, snapshot_id: Optional[str] = None) -> Snapshot:
        """Create a new snapshot of current state."""
        if snapshot_id is None:
            snapshot_id = f"snapshot_{datetime.utcnow().strftime('%Y%m%d_%H%M%S')}"

        snapshot = Snapshot(
            id=snapshot_id,
            timestamp=self.now(),
            state=self._state.copy(),
            metadata={"seed": str(self._random_seed) if self._random_seed else ""},
        )
        self._snapshots[snapshot_id] = snapshot

        # Persist to disk
        snapshot_path = self._snapshot_dir / f"{snapshot_id}.json"
        async with asyncio.Lock():
            snapshot_path.write_text(json.dumps(snapshot.to_dict(), indent=2))

        return snapshot

    async def restore_snapshot(self, snapshot_id: str) -> None:
        """Restore state from a snapshot."""
        snapshot = self._snapshots.get(snapshot_id)
        if not snapshot:
            # Try loading from disk
            snapshot_path = self._snapshot_dir / f"{snapshot_id}.json"
            if snapshot_path.exists():
                data = json.loads(snapshot_path.read_text())
                snapshot = Snapshot.from_dict(data)
                self._snapshots[snapshot_id] = snapshot
            else:
                raise ValueError(f"Snapshot not found: {snapshot_id}")

        self._state = snapshot.state.copy()
        if snapshot.metadata.get("seed"):
            self.set_seed(int(snapshot.metadata["seed"]))

    def list_snapshots(self) -> list[str]:
        """List all snapshot IDs."""
        # Include both in-memory and on-disk snapshots
        disk_snapshots = {p.stem for p in self._snapshot_dir.glob("*.json")}
        memory_snapshots = set(self._snapshots.keys())
        return sorted(disk_snapshots | memory_snapshots)

    async def export_snapshot(self, snapshot_id: str, output_path: str) -> None:
        """Export snapshot to a file."""
        snapshot = self._snapshots.get(snapshot_id)
        if not snapshot:
            snapshot_path = self._snapshot_dir / f"{snapshot_id}.json"
            if not snapshot_path.exists():
                raise ValueError(f"Snapshot not found: {snapshot_id}")
            # Copy file
            Path(output_path).write_text(snapshot_path.read_text())
            return

        Path(output_path).write_text(json.dumps(snapshot.to_dict(), indent=2))

    async def import_snapshot(self, input_path: str) -> str:
        """Import snapshot from a file."""
        data = json.loads(Path(input_path).read_text())
        snapshot = Snapshot.from_dict(data)
        self._snapshots[snapshot.id] = snapshot

        # Also save to snapshot directory
        snapshot_path = self._snapshot_dir / f"{snapshot.id}.json"
        snapshot_path.write_text(json.dumps(snapshot.to_dict(), indent=2))

        return snapshot.id
