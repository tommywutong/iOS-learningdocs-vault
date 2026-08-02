---
title: 'CloudPhotos : Using CloudKit with iOS and OS X'
apple_id: TP40016061
resource_type: Sample Code
platform: iOS|macOS
topic: null
technology: CloudKit
published: '2017-03-09'
source_url: https://developer.apple.com/library/archive/samplecode/CloudPhotos/Listings/CloudPhotos__iOS__CloudPhotos_APLMainTableViewController_h.html
archived_at: '2026-07-18T03:03:32.812977Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [CloudPhotos : Using CloudKit with iOS and OS X](CloudPhotos%20-%20Using%20CloudKit%20with%20iOS%20and%20OS%20X.md)


[Next](CloudPhotos%20%28iOS%29-CloudPhotos-AppDelegate.h.md)[Previous](CloudPhotos%20%28iOS%29-CloudPhotos-APLMainTableViewController.m.md)

# CloudPhotos (iOS)/CloudPhotos/APLMainTableViewController.h

```objc
/*
 Copyright (C) 2017 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 The application's primary table view controller showing the list of photos.
 */

#import "APLDetailTableViewController.h" // for DetailViewControllerDelegate

@interface APLMainTableViewController : UITableViewController <DetailViewControllerDelegate>

// called by our AppDelegate when the user has logged in our out
- (void)loginUpdate;

@end
```

[Next](CloudPhotos%20%28iOS%29-CloudPhotos-AppDelegate.h.md)[Previous](CloudPhotos%20%28iOS%29-CloudPhotos-APLMainTableViewController.m.md)

