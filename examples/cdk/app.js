#!/usr/bin/env node
// CDK Example - S3 Bucket with Starward

const cdk = require('aws-cdk-lib');
const s3 = require('aws-cdk-lib/aws-s3');

class StarwardStack extends cdk.Stack {
  constructor(scope, id, props) {
    super(scope, id, props);

    // Create an S3 bucket
    new s3.Bucket(this, 'StarwardBucket', {
      bucketName: 'my-starward-cdk-bucket',
      versioned: true,
      removalPolicy: cdk.RemovalPolicy.DESTROY,
      autoDeleteObjects: true,
    });
  }
}

const app = new cdk.App();
new StarwardStack(app, 'StarwardStack', {
  env: {
    account: '000000000000',
    region: 'us-east-1',
  },
});
