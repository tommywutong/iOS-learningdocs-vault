---
title: 'CloudKit Catalog: An Introduction to CloudKit (Cocoa and JavaScript)'
apple_id: TP40014599
resource_type: Sample Code
platform: CloudKit JS|iOS
topic: null
technology: CloudKit
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/CloudAtlas/Listings/Node_node_client_s2s_config_js.html
archived_at: '2026-07-18T03:03:26.558186Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [CloudKit Catalog: An Introduction to CloudKit (Cocoa and JavaScript)](CloudKit%20Catalog-%20An%20Introduction%20to%20CloudKit%20%28Cocoa%20and%20JavaScript%29.md)


[Next](Node-node-client-s2s-index.js.md)[Previous](Node-node-client-s2s-README.md.md)

# Node/node-client-s2s/config.js

```
/*
  Copyright (C) 2016 Apple Inc. All Rights Reserved.
  See LICENSE.txt for this sample’s licensing information

  Abstract:
  This is the container configuration that gets passed to CloudKit.configure.
        Customize this for your own environment.
 */

module.exports = {
  // Replace this with a container that you own.
  containerIdentifier:'com.example.apple-samplecode.cloudkit-catalog',

  environment: 'development',

  serverToServerKeyAuth: {
    // Generate a key ID through CloudKit Dashboard and insert it here.
    keyID: '<insert key ID>',

    // This should reference the private key file that you used to generate the above key ID.
    privateKeyFile: __dirname + '/eckey.pem'
  }
};
```

[Next](Node-node-client-s2s-index.js.md)[Previous](Node-node-client-s2s-README.md.md)

