"""Tests for SQS service."""

import pytest

from starward.services.sqs import MockSQSService


@pytest.mark.unit
async def test_sqs_create_queue(sqs_service: MockSQSService) -> None:
    """Test queue creation."""
    result = await sqs_service.create_queue("test-queue")
    assert result["name"] == "test-queue"
    assert "url" in result


@pytest.mark.unit
async def test_sqs_list_queues(sqs_service: MockSQSService) -> None:
    """Test listing queues."""
    await sqs_service.create_queue("queue1")
    await sqs_service.create_queue("queue2")
    
    queues = await sqs_service.list_queues()
    assert len(queues) == 2


@pytest.mark.unit
async def test_sqs_send_message(sqs_service: MockSQSService) -> None:
    """Test sending a message."""
    await sqs_service.create_queue("test-queue")
    result = await sqs_service.send_message("test-queue", "test message")
    
    assert "message_id" in result
    assert "md5_of_body" in result


@pytest.mark.unit
async def test_sqs_receive_messages(sqs_service: MockSQSService) -> None:
    """Test receiving messages."""
    await sqs_service.create_queue("test-queue")
    await sqs_service.send_message("test-queue", "message1")
    await sqs_service.send_message("test-queue", "message2")
    
    messages = await sqs_service.receive_messages("test-queue", max_messages=2)
    assert len(messages) == 2
    assert any(m["body"] == "message1" for m in messages)


@pytest.mark.unit
async def test_sqs_delete_message(sqs_service: MockSQSService) -> None:
    """Test deleting a message."""
    await sqs_service.create_queue("test-queue")
    await sqs_service.send_message("test-queue", "test message")
    
    messages = await sqs_service.receive_messages("test-queue")
    assert len(messages) == 1
    
    receipt_handle = messages[0]["receipt_handle"]
    await sqs_service.delete_message("test-queue", receipt_handle)
    
    messages = await sqs_service.receive_messages("test-queue")
    assert len(messages) == 0


@pytest.mark.unit
async def test_sqs_queue_attributes(sqs_service: MockSQSService) -> None:
    """Test getting queue attributes."""
    await sqs_service.create_queue("test-queue")
    await sqs_service.send_message("test-queue", "message")
    
    attrs = await sqs_service.get_queue_attributes("test-queue")
    assert attrs["ApproximateNumberOfMessages"] == 1
