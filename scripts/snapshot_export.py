#!/usr/bin/env python3
"""Export snapshot to a file."""

import asyncio
import sys
from pathlib import Path

from starward.core.state_engine import StateEngine


async def export_snapshot(snapshot_id: str, output_path: str) -> None:
    """Export a snapshot."""
    engine = StateEngine()
    await engine.export_snapshot(snapshot_id, output_path)
    print(f"Snapshot {snapshot_id} exported to {output_path}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python snapshot_export.py <snapshot_id> <output_path>")
        sys.exit(1)

    snapshot_id = sys.argv[1]
    output_path = sys.argv[2]

    asyncio.run(export_snapshot(snapshot_id, output_path))
