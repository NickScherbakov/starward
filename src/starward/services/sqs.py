"""Mock SQS-like queue service."""

from typing import Any, Dict, List, Optional
from datetime import datetime
import uuid


class Message:
    """Represents a queue message."""

    def __init__(self, body: str, attributes: Optional[Dict[str, str]] = None):
        self.id = str(uuid.uuid4())
        self.body = body
        self.attributes = attributes or {}
        self.receipt_handle = str(uuid.uuid4())
        self.sent_timestamp = datetime.utcnow().isoformat()
        self.receive_count = 0


class MockSQSService:
    """Mock SQS-compatible queue service."""

    service_name = "sqs"

    def __init__(self, state_engine: Any = None) -> None:
        self.queues: Dict[str, Dict[str, Any]] = {}
        self.messages: Dict[str, List[Message]] = {}
        self.state_engine = state_engine

    async def start(self) -> None:
        """Start the service."""
        if self.state_engine:
            state = self.state_engine.get_state("sqs", {})
            self.queues = state.get("queues", {})
            # Messages are not persisted across restarts for simplicity

    async def stop(self) -> None:
        """Stop the service."""
        if self.state_engine:
            self.state_engine.set_state("sqs", {"queues": self.queues})

    async def reset(self) -> None:
        """Reset service state."""
        self.queues.clear()
        self.messages.clear()

    async def create_queue(self, queue_name: str, attributes: Optional[Dict[str, str]] = None) -> Dict[str, Any]:
        """Create a new queue."""
        if queue_name in self.queues:
            raise ValueError(f"Queue already exists: {queue_name}")

        queue_url = f"http://localhost:4566/queue/{queue_name}"
        self.queues[queue_name] = {
            "name": queue_name,
            "url": queue_url,
            "attributes": attributes or {},
            "created_at": datetime.utcnow().isoformat(),
        }
        self.messages[queue_name] = []
        return self.queues[queue_name]

    async def delete_queue(self, queue_name: str) -> None:
        """Delete a queue."""
        if queue_name not in self.queues:
            raise ValueError(f"Queue not found: {queue_name}")

        del self.queues[queue_name]
        del self.messages[queue_name]

    async def list_queues(self) -> list[str]:
        """List all queue URLs."""
        return [q["url"] for q in self.queues.values()]

    async def send_message(
        self, queue_name: str, message_body: str, attributes: Optional[Dict[str, str]] = None
    ) -> Dict[str, Any]:
        """Send a message to a queue."""
        if queue_name not in self.queues:
            raise ValueError(f"Queue not found: {queue_name}")

        message = Message(message_body, attributes)
        self.messages[queue_name].append(message)

        return {
            "message_id": message.id,
            "md5_of_body": "mock_md5",
        }

    async def receive_messages(
        self, queue_name: str, max_messages: int = 1, wait_time: int = 0
    ) -> list[Dict[str, Any]]:
        """Receive messages from a queue."""
        if queue_name not in self.queues:
            raise ValueError(f"Queue not found: {queue_name}")

        messages = self.messages[queue_name][:max_messages]
        result = []

        for msg in messages:
            msg.receive_count += 1
            result.append(
                {
                    "message_id": msg.id,
                    "receipt_handle": msg.receipt_handle,
                    "body": msg.body,
                    "attributes": msg.attributes,
                }
            )

        return result

    async def delete_message(self, queue_name: str, receipt_handle: str) -> None:
        """Delete a message from a queue."""
        if queue_name not in self.queues:
            raise ValueError(f"Queue not found: {queue_name}")

        self.messages[queue_name] = [
            m for m in self.messages[queue_name] if m.receipt_handle != receipt_handle
        ]

    async def get_queue_attributes(self, queue_name: str) -> Dict[str, Any]:
        """Get queue attributes."""
        if queue_name not in self.queues:
            raise ValueError(f"Queue not found: {queue_name}")

        return {
            "ApproximateNumberOfMessages": len(self.messages[queue_name]),
            "CreatedTimestamp": self.queues[queue_name]["created_at"],
        }
