---
title: 'CloudCaptions: How integrate CloudKit into your application'
apple_id: TP40014732
resource_type: Sample Code
platform: iOS
topic: null
technology: CloudKit
published: '2014-09-17'
source_url: https://developer.apple.com/library/archive/samplecode/CloudCaptions/Listings/CloudCaptions_AAPLSubmitPostViewController_h.html
archived_at: '2026-07-18T03:03:30.716713Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [CloudCaptions: How integrate CloudKit into your application](CloudCaptions-%20How%20integrate%20CloudKit%20into%20your%20application.md)


[Next](CloudCaptions-AAPLExistingImageCollectionView.h.md)[Previous](CloudCaptions-AAPLAppDelegate.m.md)

# CloudCaptions/AAPLSubmitPostViewController.h

```objc
/*
 Copyright (C) 2014 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:

 View controller responsible for creating a post record and uploading it along with the Image record in the AAPLImage that was passed in

 */

#import "AAPLPost.h"
@import UIKit;

@interface AAPLSubmitPostViewController : UIViewController

@property (weak, atomic) id delegate;

@end

@protocol AAPLSubmitPostViewControllerDelegate <NSObject>

@optional
- (void) AAPLSubmitPostViewController:(AAPLSubmitPostViewController *)controller postedRecord:(AAPLPost *)record;

@end
```

[Next](CloudCaptions-AAPLExistingImageCollectionView.h.md)[Previous](CloudCaptions-AAPLAppDelegate.m.md)

