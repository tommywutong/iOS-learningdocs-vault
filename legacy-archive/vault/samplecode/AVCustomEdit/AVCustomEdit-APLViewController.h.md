---
title: AVCustomEdit
apple_id: DTS40013411
resource_type: Sample Code
platform: iOS
topic: Audio, Video, & Visual Effects
technology: AVFoundation
published: '2017-08-17'
source_url: https://developer.apple.com/library/archive/samplecode/AVCustomEdit/Listings/AVCustomEdit_APLViewController_h.html
archived_at: '2026-07-18T03:00:10.857833Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AVCustomEdit](AVCustomEdit.md)


[Next](AVCustomEdit-APLAppDelegate.h.md)[Previous](AVCustomEdit-APLCustomVideoCompositionInstruction.h.md)

# AVCustomEdit/APLViewController.h

```objc
/*
 Copyright (C) 2017 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 UIViewController subclasses which handles setup, playback and export of AVMutableComposition along with other user interactions like scrubbing, toggling play/pause, selecting transition type.
 */

#import <UIKit/UIKit.h>
#import "APLTransitionTypeController.h"

@class AVPlayer, AVPlayerItem, APLSimpleEditor, APLPlayerView;

@interface APLViewController : UIViewController <UIGestureRecognizerDelegate, APLTransitionTypePickerDelegate, UIPopoverPresentationControllerDelegate, UIAdaptivePresentationControllerDelegate>

@end
```

[Next](AVCustomEdit-APLAppDelegate.h.md)[Previous](AVCustomEdit-APLCustomVideoCompositionInstruction.h.md)

