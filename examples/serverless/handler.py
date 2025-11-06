"""Serverless function handlers."""

import json


def hello(event, context):
    """Simple hello world handler."""
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Hello from Starward!",
            "input": event,
        }),
    }


def process_queue(event, context):
    """Process SQS messages."""
    for record in event.get("Records", []):
        message_body = record.get("body", "")
        print(f"Processing message: {message_body}")
    
    return {
        "statusCode": 200,
        "body": json.dumps({
            "processed": len(event.get("Records", [])),
        }),
    }
