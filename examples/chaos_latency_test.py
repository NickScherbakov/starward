#!/usr/bin/env python3
"""Chaos engineering example - latency injection test."""

import asyncio
import time
import random
from typing import List

from starward.core.plugins import Plugin
from starward.services.s3 import MockS3Service
from starward.core.state_engine import StateEngine


class LatencyInjectorPlugin(Plugin):
    """Plugin that injects random latency into operations."""

    name = "latency_injector"
    version = "0.1.0"

    def __init__(self, min_delay: float = 0.01, max_delay: float = 0.1):
        self.min_delay = min_delay
        self.max_delay = max_delay

    async def on_pre_action(self, service: str, action: str, params: dict) -> None:
        """Inject latency before action."""
        delay = random.uniform(self.min_delay, self.max_delay)
        print(f"[CHAOS] Injecting {delay*1000:.1f}ms latency into {service}.{action}")
        await asyncio.sleep(delay)


async def run_chaos_test() -> None:
    """Run a chaos engineering test with latency injection."""
    print("\n" + "=" * 70)
    print("CHAOS ENGINEERING TEST - Latency Injection")
    print("=" * 70)

    # Setup
    engine = StateEngine()
    service = MockS3Service(engine)
    await service.start()

    plugin = LatencyInjectorPlugin(min_delay=0.01, max_delay=0.05)
    await plugin.on_register()

    # Test operations with latency injection
    timings: List[float] = []
    errors = 0

    print("\nRunning 20 S3 operations with random latency injection...")
    print("-" * 70)

    for i in range(20):
        bucket_name = f"chaos-bucket-{i}"

        try:
            # Simulate pre-action hook
            await plugin.on_pre_action("s3", "create_bucket", {"bucket": bucket_name})

            start = time.perf_counter()
            await service.create_bucket(bucket_name)
            end = time.perf_counter()

            elapsed = (end - start) * 1000
            timings.append(elapsed)

            print(f"Operation {i+1:2d}: {elapsed:6.2f} ms")

        except Exception as e:
            print(f"Operation {i+1:2d}: ERROR - {e}")
            errors += 1

    # Analysis
    print("\n" + "=" * 70)
    print("TEST RESULTS")
    print("=" * 70)
    print(f"Total operations: 20")
    print(f"Successful:       {len(timings)}")
    print(f"Failed:           {errors}")

    if timings:
        avg = sum(timings) / len(timings)
        min_time = min(timings)
        max_time = max(timings)

        print(f"\nLatency Stats:")
        print(f"  Average: {avg:.2f} ms")
        print(f"  Min:     {min_time:.2f} ms")
        print(f"  Max:     {max_time:.2f} ms")
        print(f"  Range:   {max_time - min_time:.2f} ms")

    print("\n" + "=" * 70)
    print("\nKEY INSIGHTS:")
    print("- Latency injection helps identify timeout vulnerabilities")
    print("- Measure impact on user experience and SLAs")
    print("- Test retry logic and circuit breaker patterns")
    print("- Validate graceful degradation under load")
    print("=" * 70)

    await service.stop()


if __name__ == "__main__":
    asyncio.run(run_chaos_test())
