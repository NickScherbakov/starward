"""Command-line interface for Starward."""

import click
import asyncio
import subprocess
import sys
import time
from pathlib import Path
from typing import Optional

from starward.core.state_engine import StateEngine


@click.group()
@click.version_option(version="0.1.0")
def main() -> None:
    """Starward - Next-generation deterministic cloud emulator."""
    pass


@main.command()
@click.option("--host", default="127.0.0.1", help="Server host")
@click.option("--port", default=4566, help="Server port")
@click.option("--detach", "-d", is_flag=True, help="Run in background")
def up(host: str, port: int, detach: bool) -> None:
    """Start the Starward server."""
    click.echo(f"Starting Starward server on {host}:{port}...")

    if detach:
        # Run in background
        subprocess.Popen(
            [sys.executable, "-m", "uvicorn", "starward.server:app", "--host", host, "--port", str(port)],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        click.echo("Server started in background.")
    else:
        # Run in foreground
        from starward.server import StarwardServer

        server = StarwardServer(host, port)
        server.run()


@main.command()
def down() -> None:
    """Stop the Starward server."""
    click.echo("Stopping Starward server...")
    # Simple implementation - in production, would track PID
    subprocess.run(["pkill", "-f", "starward.server"], check=False)
    click.echo("Server stopped.")


@main.command()
@click.option("--id", "snapshot_id", help="Snapshot ID")
def snapshot(snapshot_id: Optional[str]) -> None:
    """Create a state snapshot."""
    click.echo("Creating snapshot...")

    async def _create() -> None:
        engine = StateEngine()
        snap = await engine.create_snapshot(snapshot_id)
        click.echo(f"Snapshot created: {snap.id}")

    asyncio.run(_create())


@main.command()
@click.argument("snapshot_id")
def restore(snapshot_id: str) -> None:
    """Restore from a snapshot."""
    click.echo(f"Restoring snapshot {snapshot_id}...")

    async def _restore() -> None:
        engine = StateEngine()
        await engine.restore_snapshot(snapshot_id)
        click.echo("Snapshot restored.")

    asyncio.run(_restore())


@main.command()
def snapshots() -> None:
    """List all snapshots."""

    async def _list() -> None:
        engine = StateEngine()
        snaps = engine.list_snapshots()
        if snaps:
            click.echo("Available snapshots:")
            for snap in snaps:
                click.echo(f"  - {snap}")
        else:
            click.echo("No snapshots found.")

    asyncio.run(_list())


@main.command()
def parity() -> None:
    """Run parity analysis against cloud providers."""
    click.echo("Running parity scan...")
    click.echo("\nParity Radar - Coverage Analysis")
    click.echo("=" * 60)
    click.echo("Service      | Operations | Supported | Coverage")
    click.echo("-" * 60)
    click.echo("AWS S3       |    120     |    15     |  12.5%")
    click.echo("AWS SQS      |     45     |    10     |  22.2%")
    click.echo("GCP Storage  |    100     |     5     |   5.0%")
    click.echo("GCP PubSub   |     35     |     0     |   0.0%")
    click.echo("=" * 60)
    click.echo("\nNote: This is a mock analysis. Real parity scan coming soon.")


@main.command()
def cost() -> None:
    """Analyze cost and performance metrics."""
    click.echo("Analyzing cost and performance...")
    click.echo("\nCost Profiling Report")
    click.echo("=" * 60)
    click.echo("Operation               | Count | Avg Time | Est. Cost")
    click.echo("-" * 60)
    click.echo("S3 CreateBucket         |   10  |   5ms    |  $0.00")
    click.echo("S3 PutObject            |  100  |   3ms    |  $0.005")
    click.echo("SQS SendMessage         |  500  |   2ms    |  $0.025")
    click.echo("=" * 60)
    click.echo("Total Estimated Cost: $0.03")
    click.echo("\nNote: This is a mock report. Real profiling coming soon.")


@main.group()
def learn() -> None:
    """Learning mode commands."""
    pass


@learn.command("run")
@click.argument("scenario", required=False)
def learn_run(scenario: Optional[str]) -> None:
    """Run a learning scenario."""
    if scenario:
        click.echo(f"Running learning scenario: {scenario}")
    else:
        click.echo("Available learning scenarios:")
        click.echo("  - iam-basics: IAM policy fundamentals")
        click.echo("  - s3-security: S3 bucket security patterns")
        click.echo("  - chaos-testing: Chaos engineering introduction")
        click.echo("\nUse: starward learn run <scenario>")


@main.command()
def status() -> None:
    """Show server status."""
    import httpx

    try:
        response = httpx.get("http://localhost:4566/health", timeout=2)
        if response.status_code == 200:
            click.echo("✓ Starward server is running")
            click.echo(f"  Status: {response.json()['status']}")
        else:
            click.echo("✗ Server responded with error")
    except Exception:
        click.echo("✗ Starward server is not running")
        click.echo("  Start with: starward up")


if __name__ == "__main__":
    main()
