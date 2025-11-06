#!/usr/bin/env python3
"""Benchmark script for S3-like operations."""

import asyncio
import time
import json
import statistics
from typing import List

from starward.services.s3 import MockS3Service
from starward.core.state_engine import StateEngine


async def benchmark_create_delete_bucket(iterations: int = 100) -> List[float]:
    """Benchmark bucket create/delete operations."""
    engine = StateEngine()
    service = MockS3Service(engine)
    await service.start()

    timings = []

    for i in range(iterations):
        bucket_name = f"test-bucket-{i}"

        start = time.perf_counter()
        await service.create_bucket(bucket_name)
        await service.delete_bucket(bucket_name)
        end = time.perf_counter()

        timings.append((end - start) * 1000)  # Convert to ms

    await service.stop()
    return timings


def calculate_stats(timings: List[float]) -> dict:
    """Calculate statistics from timings."""
    return {
        "count": len(timings),
        "mean": statistics.mean(timings),
        "median": statistics.median(timings),
        "p50": statistics.quantiles(timings, n=100)[49],
        "p90": statistics.quantiles(timings, n=100)[89],
        "p95": statistics.quantiles(timings, n=100)[94],
        "p99": statistics.quantiles(timings, n=100)[98],
        "min": min(timings),
        "max": max(timings),
    }


async def run_benchmarks() -> None:
    """Run all benchmarks."""
    print("\n" + "=" * 70)
    print("STARWARD BENCHMARK RESULTS")
    print("=" * 70)

    print("\nBenchmark: S3 Create/Delete Bucket (100 iterations)")
    print("-" * 70)

    timings = await benchmark_create_delete_bucket(100)
    stats = calculate_stats(timings)

    print(f"Operations:  {stats['count']}")
    print(f"Mean:        {stats['mean']:.2f} ms")
    print(f"Median:      {stats['median']:.2f} ms")
    print(f"P50:         {stats['p50']:.2f} ms")
    print(f"P90:         {stats['p90']:.2f} ms")
    print(f"P95:         {stats['p95']:.2f} ms")
    print(f"P99:         {stats['p99']:.2f} ms")
    print(f"Min:         {stats['min']:.2f} ms")
    print(f"Max:         {stats['max']:.2f} ms")

    print("\n" + "=" * 70)

    # Save results to JSON
    results = {
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "benchmarks": {
            "s3_create_delete_bucket": stats,
        },
    }

    with open("benchmark_results.json", "w") as f:
        json.dump(results, f, indent=2)

    print("\nResults saved to: benchmark_results.json")

    # Compare against baseline (mock)
    print("\nBaseline Comparison:")
    print("-" * 70)
    baseline_p50 = 1.5
    baseline_p90 = 2.5
    improvement_p50 = ((baseline_p50 - stats["p50"]) / baseline_p50 * 100)
    improvement_p90 = ((baseline_p90 - stats["p90"]) / baseline_p90 * 100)

    print(f"P50: {stats['p50']:.2f} ms vs {baseline_p50:.2f} ms baseline "
          f"({improvement_p50:+.1f}%)")
    print(f"P90: {stats['p90']:.2f} ms vs {baseline_p90:.2f} ms baseline "
          f"({improvement_p90:+.1f}%)")

    print("=" * 70)


if __name__ == "__main__":
    asyncio.run(run_benchmarks())
