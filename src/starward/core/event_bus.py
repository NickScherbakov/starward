"""Event bus for inter-service communication."""

import asyncio
from typing import Any, Callable, Dict, List
from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Event:
    """Represents a system event."""

    type: str
    service: str
    data: Dict[str, Any]
    timestamp: datetime = field(default_factory=datetime.utcnow)
    trace_id: str = ""


EventHandler = Callable[[Event], None]


class EventBus:
    """Central event bus for service communication and observability."""

    def __init__(self) -> None:
        self._handlers: Dict[str, List[EventHandler]] = {}
        self._events: List[Event] = []

    def subscribe(self, event_type: str, handler: EventHandler) -> None:
        """Subscribe to events of a specific type."""
        if event_type not in self._handlers:
            self._handlers[event_type] = []
        self._handlers[event_type].append(handler)

    async def publish(self, event: Event) -> None:
        """Publish an event to all subscribers."""
        self._events.append(event)
        handlers = self._handlers.get(event.type, [])
        for handler in handlers:
            try:
                result = handler(event)
                if asyncio.iscoroutine(result):
                    await result
            except Exception as e:
                print(f"Error in event handler: {e}")

    def get_events(self, event_type: str | None = None) -> List[Event]:
        """Get all events, optionally filtered by type."""
        if event_type is None:
            return self._events.copy()
        return [e for e in self._events if e.type == event_type]

    def clear(self) -> None:
        """Clear all events (useful for testing)."""
        self._events.clear()
