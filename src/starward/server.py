"""FastAPI server for cloud service emulation."""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Any, Dict, Optional
import uvicorn

from starward.core.state_engine import StateEngine
from starward.core.registry import ServiceRegistry
from starward.core.event_bus import EventBus, Event
from starward.core.plugins import PluginManager
from starward.services.s3 import MockS3Service
from starward.services.sqs import MockSQSService


class CreateBucketRequest(BaseModel):
    bucket_name: str


class PutObjectRequest(BaseModel):
    bucket_name: str
    key: str
    data: str


class CreateQueueRequest(BaseModel):
    queue_name: str
    attributes: Optional[Dict[str, str]] = None


class SendMessageRequest(BaseModel):
    queue_name: str
    message_body: str
    attributes: Optional[Dict[str, str]] = None


class StarwardServer:
    """Main server for cloud service emulation."""

    def __init__(self, host: str = "127.0.0.1", port: int = 4566) -> None:
        self.host = host
        self.port = port
        self.app = FastAPI(title="Starward", version="0.1.0")
        self.state_engine = StateEngine()
        self.registry = ServiceRegistry()
        self.event_bus = EventBus()
        self.plugin_manager = PluginManager()

        self._setup_routes()
        self._setup_services()

    def _setup_services(self) -> None:
        """Register and initialize services."""
        self.registry.register_type("s3", MockS3Service)
        self.registry.register_type("sqs", MockSQSService)

        # Create service instances
        self.s3_service = self.registry.create_service("s3", self.state_engine)
        self.sqs_service = self.registry.create_service("sqs", self.state_engine)

    def _setup_routes(self) -> None:
        """Setup API routes."""

        @self.app.get("/health")
        async def health() -> Dict[str, str]:
            return {"status": "healthy"}

        @self.app.get("/")
        async def root() -> Dict[str, str]:
            return {"service": "starward", "version": "0.1.0"}

        # S3 endpoints
        @self.app.post("/s3/buckets")
        async def create_bucket(req: CreateBucketRequest) -> Dict[str, Any]:
            try:
                result = await self.s3_service.create_bucket(req.bucket_name)
                await self.event_bus.publish(
                    Event(
                        type="bucket.created",
                        service="s3",
                        data={"bucket": req.bucket_name},
                    )
                )
                return result
            except ValueError as e:
                raise HTTPException(status_code=400, detail=str(e))

        @self.app.get("/s3/buckets")
        async def list_buckets() -> Dict[str, Any]:
            buckets = await self.s3_service.list_buckets()
            return {"buckets": buckets}

        @self.app.delete("/s3/buckets/{bucket_name}")
        async def delete_bucket(bucket_name: str) -> Dict[str, str]:
            try:
                await self.s3_service.delete_bucket(bucket_name)
                return {"status": "deleted"}
            except ValueError as e:
                raise HTTPException(status_code=400, detail=str(e))

        @self.app.post("/s3/objects")
        async def put_object(req: PutObjectRequest) -> Dict[str, Any]:
            try:
                result = await self.s3_service.put_object(
                    req.bucket_name, req.key, req.data.encode()
                )
                return result
            except ValueError as e:
                raise HTTPException(status_code=400, detail=str(e))

        # SQS endpoints
        @self.app.post("/sqs/queues")
        async def create_queue(req: CreateQueueRequest) -> Dict[str, Any]:
            try:
                result = await self.sqs_service.create_queue(req.queue_name, req.attributes)
                await self.event_bus.publish(
                    Event(
                        type="queue.created",
                        service="sqs",
                        data={"queue": req.queue_name},
                    )
                )
                return result
            except ValueError as e:
                raise HTTPException(status_code=400, detail=str(e))

        @self.app.get("/sqs/queues")
        async def list_queues() -> Dict[str, Any]:
            queues = await self.sqs_service.list_queues()
            return {"queues": queues}

        @self.app.post("/sqs/messages")
        async def send_message(req: SendMessageRequest) -> Dict[str, Any]:
            try:
                result = await self.sqs_service.send_message(
                    req.queue_name, req.message_body, req.attributes
                )
                return result
            except ValueError as e:
                raise HTTPException(status_code=400, detail=str(e))

        # Snapshot endpoints
        @self.app.post("/snapshots")
        async def create_snapshot(snapshot_id: Optional[str] = None) -> Dict[str, Any]:
            snapshot = await self.state_engine.create_snapshot(snapshot_id)
            return {"id": snapshot.id, "timestamp": snapshot.timestamp.isoformat()}

        @self.app.post("/snapshots/{snapshot_id}/restore")
        async def restore_snapshot(snapshot_id: str) -> Dict[str, str]:
            try:
                await self.state_engine.restore_snapshot(snapshot_id)
                return {"status": "restored", "snapshot_id": snapshot_id}
            except ValueError as e:
                raise HTTPException(status_code=404, detail=str(e))

        @self.app.get("/snapshots")
        async def list_snapshots() -> Dict[str, Any]:
            snapshots = self.state_engine.list_snapshots()
            return {"snapshots": snapshots}

        # Plugin endpoints
        @self.app.get("/plugins")
        async def list_plugins() -> Dict[str, Any]:
            plugins = self.plugin_manager.list_plugins()
            return {"plugins": plugins}

    async def startup(self) -> None:
        """Startup hook."""
        await self.registry.start_all()

    async def shutdown(self) -> None:
        """Shutdown hook."""
        await self.registry.stop_all()

    def run(self) -> None:
        """Run the server."""
        uvicorn.run(
            self.app,
            host=self.host,
            port=self.port,
            log_level="info",
        )
