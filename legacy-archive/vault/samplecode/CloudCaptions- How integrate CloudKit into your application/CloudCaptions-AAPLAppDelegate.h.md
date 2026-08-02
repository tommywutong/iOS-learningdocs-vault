---
title: 'CloudCaptions: How integrate CloudKit into your application'
apple_id: TP40014732
resource_type: Sample Code
platform: iOS
topic: null
technology: CloudKit
published: '2014-09-17'
source_url: https://developer.apple.com/library/archive/samplecode/CloudCaptions/Listings/CloudCaptions_AAPLAppDelegate_h.html
archived_at: '2026-07-18T03:03:29.838182Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [CloudCaptions: How integrate CloudKit into your application](CloudCaptions-%20How%20integrate%20CloudKit%20into%20your%20application.md)


[Next](CloudCaptions-AAPLPostTableViewCell.h.md)[Previous](CloudCaptions-AAPLPostManager.h.md)

# CloudCaptions/AAPLAppDelegate.h

```objc
/*
 Copyright (C) 2014 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:

  Application Delegate for ImageMessages
  Registers for notifications and will notify the AAPLTableViewController when it receives an update

 */

@import UIKit;

@class AAPLTableViewController;

@interface AAPLAppDelegate : UIResponder <UIApplicationDelegate>

@property (strong, nonatomic) UIWindow *window;
@property (weak) IBOutlet AAPLTableViewController *tableController;

@end
```

[Next](CloudCaptions-AAPLPostTableViewCell.h.md)[Previous](CloudCaptions-AAPLPostManager.h.md)

