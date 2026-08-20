---
title: 'CloudPhotos : Using CloudKit with iOS and OS X'
apple_id: TP40016061
resource_type: Sample Code
platform: iOS|macOS
topic: null
technology: CloudKit
published: '2017-03-09'
source_url: https://developer.apple.com/library/archive/samplecode/CloudPhotos/Listings/CloudPhotos__iOS__CloudPhotos_AppDelegate_h.html
archived_at: '2026-07-18T03:03:33.364985Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [CloudPhotos : Using CloudKit with iOS and OS X](CloudPhotos%20-%20Using%20CloudKit%20with%20iOS%20and%20OS%20X.md)


[Next](CloudPhotos%20%28iOS%29-CloudPhotos-APLDetailTableViewController.h.md)[Previous](CloudPhotos%20%28iOS%29-CloudPhotos-APLMainTableViewController.h.md)

# CloudPhotos (iOS)/CloudPhotos/AppDelegate.h

```objc
/*
 Copyright (C) 2017 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 This sample's application delegate for push notiications (CKSubscriptions) from CloudKit.
 */

@import UIKit;

#warning Make sure to set your real iCloud container ID
#define FINAL_CONTAINER_ID "your_real_container_id"

#define CloudManager [APLCloudManager sharedInstance:@FINAL_CONTAINER_ID]

@interface AppDelegate : NSObject <UIApplicationDelegate>

@end
```

[Next](CloudPhotos%20%28iOS%29-CloudPhotos-APLDetailTableViewController.h.md)[Previous](CloudPhotos%20%28iOS%29-CloudPhotos-APLMainTableViewController.h.md)

