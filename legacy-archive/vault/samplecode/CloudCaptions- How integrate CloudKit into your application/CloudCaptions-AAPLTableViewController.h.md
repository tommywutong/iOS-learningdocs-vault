---
title: 'CloudCaptions: How integrate CloudKit into your application'
apple_id: TP40014732
resource_type: Sample Code
platform: iOS
topic: null
technology: CloudKit
published: '2014-09-17'
source_url: https://developer.apple.com/library/archive/samplecode/CloudCaptions/Listings/CloudCaptions_AAPLTableViewController_h.html
archived_at: '2026-07-18T03:03:30.979108Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [CloudCaptions: How integrate CloudKit into your application](CloudCaptions-%20How%20integrate%20CloudKit%20into%20your%20application.md)


[Next](CloudCaptions-AAPLTableViewController.m.md)[Previous](CloudCaptions-AAPLExistingImageViewController.m.md)

# CloudCaptions/AAPLTableViewController.h

```objc
/*
 Copyright (C) 2014 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:

  Downloads the post and Image records as needed while the user scrolls
  Creates the AAPLPostTableViewCells to display the downloaded information

 */

@import UIKit;
#import "AAPLExistingImageViewController.h"
#import "AAPLSubmitPostViewController.h"

@class AAPLPost;

@interface AAPLTableViewController : UITableViewController

- (void) loadNewPostsWithRecordID:(CKRecordID *)recordID;

@end
```

[Next](CloudCaptions-AAPLTableViewController.m.md)[Previous](CloudCaptions-AAPLExistingImageViewController.m.md)

