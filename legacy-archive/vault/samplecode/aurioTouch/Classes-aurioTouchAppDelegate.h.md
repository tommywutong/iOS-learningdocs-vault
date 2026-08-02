---
title: aurioTouch
apple_id: DTS40007770
resource_type: Sample Code
platform: iOS
topic: Audio, Video, & Visual Effects
technology: AudioUnit
published: '2016-08-12'
source_url: https://developer.apple.com/library/archive/samplecode/aurioTouch/Listings/Classes_aurioTouchAppDelegate_h.html
archived_at: '2026-07-18T03:28:52.963159Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [aurioTouch](aurioTouch.md)


[Next](PublicUtility-CADebugMacros.h.md)[Previous](Classes-DCRejectionFilter.h.md)

# Classes/aurioTouchAppDelegate.h

```objc
/*

 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 App delegate

 */

@class EAGLView;

@interface aurioTouchAppDelegate : NSObject <UIApplicationDelegate> {
    IBOutlet UIWindow       *window;
    IBOutlet EAGLView       *view;
}

@property (nonatomic, retain)   UIWindow        *window;
@property (nonatomic, retain)   EAGLView        *view;

@end
```

[Next](PublicUtility-CADebugMacros.h.md)[Previous](Classes-DCRejectionFilter.h.md)

