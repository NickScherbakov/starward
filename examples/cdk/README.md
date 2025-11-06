# AWS CDK with Starward

Deploy AWS CDK stacks to Starward for local testing.

## Setup

1. Start Starward:
   ```bash
   starward up
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Configure AWS CDK to use Starward endpoint (in cdk.json or environment):
   ```bash
   export AWS_ENDPOINT_URL=http://localhost:4566
   ```

4. Deploy:
   ```bash
   npm run deploy
   ```

## Benefits

- Test CDK constructs locally before cloud deployment
- Fast iteration cycle
- No cloud costs during development
