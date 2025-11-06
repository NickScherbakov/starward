# Terraform with Starward

This example demonstrates using Terraform with Starward for local development.

## Setup

1. Start Starward:
   ```bash
   starward up
   ```

2. Initialize Terraform:
   ```bash
   terraform init
   ```

3. Plan and apply:
   ```bash
   terraform plan
   terraform apply
   ```

4. Clean up:
   ```bash
   terraform destroy
   ```

## Benefits

- **Fast feedback loop**: No cloud API latency
- **No costs**: Run unlimited iterations locally
- **Deterministic**: Snapshot/restore for reproducible tests
- **Offline development**: Work without internet connection
