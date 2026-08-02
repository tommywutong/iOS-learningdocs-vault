---
title: Real-time Video Processing Using AVPlayerItemVideoOutput
apple_id: DTS40013109
resource_type: Sample Code
platform: iOS
topic: Audio, Video, & Visual Effects
technology: AVFoundation
published: '2015-10-01'
source_url: https://developer.apple.com/library/archive/samplecode/AVBasicVideoOutput/Listings/AVBasicVideoOutput_APLViewController_h.html
archived_at: '2026-07-18T03:00:01.573734Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Real-time Video Processing Using AVPlayerItemVideoOutput](Real-time%20Video%20Processing%20Using%20AVPlayerItemVideoOutput.md)


[Next](AVBasicVideoOutput-Shaders-Shader.fsh.md)[Previous](AVBasicVideoOutput-APLAppDelegate.h.md)

# AVBasicVideoOutput/APLViewController.h

```objc
/*
    Copyright (C) 2015 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    This view controller handles the UI to load assets for playback and for adjusting the luma and chroma values. It also sets up the AVPlayerItemVideoOutput, from which CVPixelBuffers are pulled out and sent to the shaders for rendering.
*/

#import <UIKit/UIKit.h>
#import <AVFoundation/AVFoundation.h>

@interface APLViewController : UIViewController <AVPlayerItemOutputPullDelegate, UIImagePickerControllerDelegate, UINavigationControllerDelegate, UIPopoverControllerDelegate, UIGestureRecognizerDelegate>

@end
```

[Next](AVBasicVideoOutput-Shaders-Shader.fsh.md)[Previous](AVBasicVideoOutput-APLAppDelegate.h.md)

