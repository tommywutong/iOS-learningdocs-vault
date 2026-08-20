---
title: 'CloudCaptions: How integrate CloudKit into your application'
apple_id: TP40014732
resource_type: Sample Code
platform: iOS
topic: null
technology: CloudKit
published: '2014-09-17'
source_url: https://developer.apple.com/library/archive/samplecode/CloudCaptions/Listings/CloudCaptions_AAPLExistingImageViewController_h.html
archived_at: '2026-07-18T03:03:30.121189Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [CloudCaptions: How integrate CloudKit into your application](CloudCaptions-%20How%20integrate%20CloudKit%20into%20your%20application.md)


[Next](CloudCaptions-AAPLAppDelegate.m.md)[Previous](CloudCaptions-AAPLPostManager.m.md)

# CloudCaptions/AAPLExistingImageViewController.h

```objc
/*
 Copyright (C) 2014 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:

  Responsible for downloading the Image records and sending them to the AAPLExistingImageCollectionView
  Passes the selected AAPLImage to the AAPLTableViewController

 */

@import UIKit;
@import CloudKit;

@class AAPLImage;

@interface AAPLExistingImageViewController : UIViewController

@property (weak, atomic) id delegate;

@end

// Delegate with method that returns the selected AAPLImage
@protocol AAPLExistingImageViewControllerDelegate <NSObject>

@optional
- (void) AAPLExisitingImageViewController:(AAPLExistingImageViewController *)controller selectedImage:(AAPLImage *)image;

@end
```

[Next](CloudCaptions-AAPLAppDelegate.m.md)[Previous](CloudCaptions-AAPLPostManager.m.md)

