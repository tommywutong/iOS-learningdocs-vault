---
title: 'CloudKit Catalog: An Introduction to CloudKit (Cocoa and JavaScript)'
apple_id: TP40014599
resource_type: Sample Code
platform: CloudKit JS|iOS
topic: null
technology: CloudKit
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/CloudAtlas/Listings/Node_node_client_s2s_index_js.html
archived_at: '2026-07-18T03:03:26.752981Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [CloudKit Catalog: An Introduction to CloudKit (Cocoa and JavaScript)](CloudKit%20Catalog-%20An%20Introduction%20to%20CloudKit%20%28Cocoa%20and%20JavaScript%29.md)


[Next](iOS-README.md.md)[Previous](Node-node-client-s2s-config.js.md)

# Node/node-client-s2s/index.js

```
/*
 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 This node script uses a server-to-server key to make public database calls with CloudKit JS
 */


process.env.NODE_TLS_REJECT_UNAUTHORIZED = "0";

(function() {
  var fetch = require('node-fetch');

  var CloudKit = require('./cloudkit');
  var containerConfig = require('./config');

  // A utility function for printing results to the console.
  var println = function(key,value) {
    console.log("--> " + key + ":");
    console.log(value);
    console.log();
  };

  //CloudKit configuration
  CloudKit.configure({
    services: {
      fetch: fetch,
      logger: console
    },
    containers: [ containerConfig ]
  });


  var container = CloudKit.getDefaultContainer();
  var database = container.publicCloudDatabase; // We'll only make calls to the public database.

  // Sign in using the keyID and public key file.
  container.setUpAuth()
    .then(function(userInfo){
      println("userInfo",userInfo);

      return database.performQuery({ recordType: 'Test' });
    })
    .then(function(response) {
      println("Queried Records",response.records);

      return database.saveRecords({recordType: 'Test', recordName: 'hello-u'});
    })
    .then(function(response) {
      var record = response.records[0];
      println("Saved Record",record);

      return database.fetchRecords(record);
    })
    .then(function(response) {
      var record = response.records[0];
      println("Fetched Record", record);

      return database.deleteRecords(record);
    })
    .then(function(response) {
      var record = response.records[0];
      println("Deleted Record", record);

      console.log("Done");
      process.exit();
    })
    .catch(function(error) {
      console.warn(error);
      process.exit(1);
    });

})();
```

[Next](iOS-README.md.md)[Previous](Node-node-client-s2s-config.js.md)

