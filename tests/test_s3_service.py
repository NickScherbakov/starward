"""Tests for S3 service."""

import pytest

from starward.services.s3 import MockS3Service


@pytest.mark.unit
async def test_s3_create_bucket(s3_service: MockS3Service) -> None:
    """Test bucket creation."""
    result = await s3_service.create_bucket("test-bucket")
    assert result["name"] == "test-bucket"
    assert "created_at" in result


@pytest.mark.unit
async def test_s3_list_buckets(s3_service: MockS3Service) -> None:
    """Test listing buckets."""
    await s3_service.create_bucket("bucket1")
    await s3_service.create_bucket("bucket2")
    
    buckets = await s3_service.list_buckets()
    assert len(buckets) == 2
    assert any(b["name"] == "bucket1" for b in buckets)


@pytest.mark.unit
async def test_s3_delete_bucket(s3_service: MockS3Service) -> None:
    """Test bucket deletion."""
    await s3_service.create_bucket("test-bucket")
    await s3_service.delete_bucket("test-bucket")
    
    buckets = await s3_service.list_buckets()
    assert len(buckets) == 0


@pytest.mark.unit
async def test_s3_put_get_object(s3_service: MockS3Service) -> None:
    """Test object upload and retrieval."""
    await s3_service.create_bucket("test-bucket")
    
    data = b"test data"
    result = await s3_service.put_object("test-bucket", "test-key", data)
    assert result["key"] == "test-key"
    assert result["size"] == len(data)
    
    retrieved = await s3_service.get_object("test-bucket", "test-key")
    assert retrieved == data


@pytest.mark.unit
async def test_s3_delete_object(s3_service: MockS3Service) -> None:
    """Test object deletion."""
    await s3_service.create_bucket("test-bucket")
    await s3_service.put_object("test-bucket", "test-key", b"data")
    
    await s3_service.delete_object("test-bucket", "test-key")
    
    with pytest.raises(ValueError):
        await s3_service.get_object("test-bucket", "test-key")


@pytest.mark.unit
async def test_s3_list_objects(s3_service: MockS3Service) -> None:
    """Test listing objects."""
    await s3_service.create_bucket("test-bucket")
    await s3_service.put_object("test-bucket", "key1", b"data1")
    await s3_service.put_object("test-bucket", "key2", b"data2")
    
    objects = await s3_service.list_objects("test-bucket")
    assert len(objects) == 2
    assert any(o["key"] == "key1" for o in objects)


@pytest.mark.unit
async def test_s3_bucket_not_found(s3_service: MockS3Service) -> None:
    """Test error handling for non-existent bucket."""
    with pytest.raises(ValueError, match="Bucket not found"):
        await s3_service.delete_bucket("nonexistent")
