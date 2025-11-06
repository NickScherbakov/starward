#!/usr/bin/env python3
"""Import snapshot from a file."""

import asyncio
import sys

from starward.core.state_engine import StateEngine


async def import_snapshot(input_path: str) -> None:
    """Import a snapshot."""
    engine = StateEngine()
    snapshot_id = await engine.import_snapshot(input_path)
    print(f"Snapshot imported with ID: {snapshot_id}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python snapshot_import.py <input_path>")
        sys.exit(1)

    input_path = sys.argv[1]
    asyncio.run(import_snapshot(input_path))
