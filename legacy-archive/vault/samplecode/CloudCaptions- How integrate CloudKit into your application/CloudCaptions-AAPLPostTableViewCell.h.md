---
title: 'CloudCaptions: How integrate CloudKit into your application'
apple_id: TP40014732
resource_type: Sample Code
platform: iOS
topic: null
technology: CloudKit
published: '2014-09-17'
source_url: https://developer.apple.com/library/archive/samplecode/CloudCaptions/Listings/CloudCaptions_AAPLPostTableViewCell_h.html
archived_at: '2026-07-18T03:03:30.493927Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [CloudCaptions: How integrate CloudKit into your application](CloudCaptions-%20How%20integrate%20CloudKit%20into%20your%20application.md)


[Next](CloudCaptions-AAPLExistingImageCollectionViewCell.m.md)[Previous](CloudCaptions-AAPLAppDelegate.h.md)

# CloudCaptions/AAPLPostTableViewCell.h

```objc
/*
 Copyright (C) 2014 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:

  Custom UITableViewCell used to display the post information

 */

@import UIKit;
@class AAPLPost;

@interface AAPLPostTableViewCell : UITableViewCell

- (void) displayInfoForPost:(AAPLPost *)post;

@end
```

[Next](CloudCaptions-AAPLExistingImageCollectionViewCell.m.md)[Previous](CloudCaptions-AAPLAppDelegate.h.md)

