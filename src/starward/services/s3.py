"""Mock S3-like storage service."""

from typing import Any, Dict, Optional
from datetime import datetime
import hashlib


class MockS3Service:
    """Mock S3-compatible storage service."""

    service_name = "s3"

    def __init__(self, state_engine: Any = None) -> None:
        self.buckets: Dict[str, Dict[str, Any]] = {}
        self.objects: Dict[str, Dict[str, bytes]] = {}
        self.state_engine = state_engine

    async def start(self) -> None:
        """Start the service."""
        if self.state_engine:
            state = self.state_engine.get_state("s3", {})
            self.buckets = state.get("buckets", {})
            self.objects = state.get("objects", {})

    async def stop(self) -> None:
        """Stop the service."""
        if self.state_engine:
            self.state_engine.set_state(
                "s3", {"buckets": self.buckets, "objects": self.objects}
            )

    async def reset(self) -> None:
        """Reset service state."""
        self.buckets.clear()
        self.objects.clear()

    async def create_bucket(self, bucket_name: str) -> Dict[str, Any]:
        """Create a new bucket."""
        if bucket_name in self.buckets:
            raise ValueError(f"Bucket already exists: {bucket_name}")

        self.buckets[bucket_name] = {
            "name": bucket_name,
            "created_at": datetime.utcnow().isoformat(),
        }
        self.objects[bucket_name] = {}
        return self.buckets[bucket_name]

    async def delete_bucket(self, bucket_name: str) -> None:
        """Delete a bucket."""
        if bucket_name not in self.buckets:
            raise ValueError(f"Bucket not found: {bucket_name}")

        if self.objects[bucket_name]:
            raise ValueError(f"Bucket not empty: {bucket_name}")

        del self.buckets[bucket_name]
        del self.objects[bucket_name]

    async def list_buckets(self) -> list[Dict[str, Any]]:
        """List all buckets."""
        return list(self.buckets.values())

    async def put_object(
        self, bucket_name: str, key: str, data: bytes, metadata: Optional[Dict[str, str]] = None
    ) -> Dict[str, Any]:
        """Put an object in a bucket."""
        if bucket_name not in self.buckets:
            raise ValueError(f"Bucket not found: {bucket_name}")

        etag = hashlib.md5(data).hexdigest()
        self.objects[bucket_name][key] = data

        return {
            "bucket": bucket_name,
            "key": key,
            "etag": etag,
            "size": len(data),
            "metadata": metadata or {},
        }

    async def get_object(self, bucket_name: str, key: str) -> bytes:
        """Get an object from a bucket."""
        if bucket_name not in self.buckets:
            raise ValueError(f"Bucket not found: {bucket_name}")

        if key not in self.objects[bucket_name]:
            raise ValueError(f"Object not found: {key}")

        return self.objects[bucket_name][key]

    async def delete_object(self, bucket_name: str, key: str) -> None:
        """Delete an object from a bucket."""
        if bucket_name not in self.buckets:
            raise ValueError(f"Bucket not found: {bucket_name}")

        if key in self.objects[bucket_name]:
            del self.objects[bucket_name][key]

    async def list_objects(self, bucket_name: str, prefix: str = "") -> list[Dict[str, Any]]:
        """List objects in a bucket."""
        if bucket_name not in self.buckets:
            raise ValueError(f"Bucket not found: {bucket_name}")

        objects = []
        for key, data in self.objects[bucket_name].items():
            if key.startswith(prefix):
                objects.append(
                    {
                        "key": key,
                        "size": len(data),
                        "etag": hashlib.md5(data).hexdigest(),
                    }
                )
        return objects
