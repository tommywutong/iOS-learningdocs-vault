---
title: AVLoupe
apple_id: DTS40012894
resource_type: Sample Code
platform: iOS
topic: Audio, Video, & Visual Effects
technology: AVFoundation
published: '2016-08-12'
source_url: https://developer.apple.com/library/archive/samplecode/AVLoupe/Listings/AVLoupe_APLViewController_h.html
archived_at: '2026-07-18T03:00:18.399056Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AVLoupe](AVLoupe.md)


[Next](AVLoupe-APLAppDelegate.m.md)[Previous](AVLoupe-APLAppDelegate.h.md)

# AVLoupe/APLViewController.h

```objc
/*
 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 The player's UIViewController class. 
  This controller manages the main view and a sublayer; the mainPlayerLayer. This controller also manages as a subview a UIImageView nammed loupeView. loupeView hosts a layer hirearchy that manages the zoomPlayerLayer.
  Users interact with the position of loupeView in respose to IBActions from a UIPanGestureRecognizer.
 */

@import UIKit;
@import AVFoundation;

@interface APLViewController : UIViewController <UIImagePickerControllerDelegate, UINavigationControllerDelegate, UIPopoverControllerDelegate>

@end
```

[Next](AVLoupe-APLAppDelegate.m.md)[Previous](AVLoupe-APLAppDelegate.h.md)

