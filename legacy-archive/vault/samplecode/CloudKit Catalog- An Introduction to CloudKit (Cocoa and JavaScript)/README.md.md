---
title: 'CloudKit Catalog: An Introduction to CloudKit (Cocoa and JavaScript)'
apple_id: TP40014599
resource_type: Sample Code
platform: CloudKit JS|iOS
topic: null
technology: CloudKit
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/CloudAtlas/Listings/README_md.html
archived_at: '2026-07-18T03:03:26.854574Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [CloudKit Catalog: An Introduction to CloudKit (Cocoa and JavaScript)](CloudKit%20Catalog-%20An%20Introduction%20to%20CloudKit%20%28Cocoa%20and%20JavaScript%29.md)


[Next](Node-node-client-s2s-README.md.md)[Previous](CloudKit%20Catalog-%20An%20Introduction%20to%20CloudKit%20%28Cocoa%20and%20JavaScript%29.md)

# README.md

```
# CloudKit Catalog: An Introduction to CloudKit

CloudKit Catalog consists of a native iOS application and a web application which demonstrate use of 
Swift and JavaScript CloudKit APIs respectively.

# Schema

The two apps share an *Items* record type which has fields

* name : String
* location : Location
* asset : Asset

# Records, Notifications and Sync

Both apps allow an authenticated user to write *Items* records to a zone in his/her private database. Additionally they
allow you to subscribe to changes to Items. So if you create or delete Items in the web app you will get notifications
of these changes in the native app and vice versa. Upon receipt of a notification, you can use the sync APIs in either app to
update a local cache of records with subscribed changes.

# Discoverability

A user of the native app can opt to be discoverable to other users of the app through the sign-in
flow (the Authentication tab). In the native app a user is typically already signed in to iCloud on their device and
they can opt in to discoverability with the *requestApplicationPermission* method in the Discoverability section.


Copyright (C) 2015 Apple Inc. All rights reserved.
```

[Next](Node-node-client-s2s-README.md.md)[Previous](CloudKit%20Catalog-%20An%20Introduction%20to%20CloudKit%20%28Cocoa%20and%20JavaScript%29.md)

