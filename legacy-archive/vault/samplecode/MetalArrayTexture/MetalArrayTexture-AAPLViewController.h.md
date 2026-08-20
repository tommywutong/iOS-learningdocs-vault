---
title: MetalArrayTexture
apple_id: TP40016608
resource_type: Sample Code
platform: iOS|macOS
topic: null
technology: null
published: '2016-03-21'
source_url: https://developer.apple.com/library/archive/samplecode/MetalArrayTexture/Listings/MetalArrayTexture_AAPLViewController_h.html
archived_at: '2026-07-18T03:14:46.726871Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MetalArrayTexture](MetalArrayTexture.md)


[Next](MetalArrayTexture-AAPLTransforms.mm.md)[Previous](MetalArrayTexture-AAPLMtkView.m.md)

# MetalArrayTexture/AAPLViewController.h

```objc
/*
 Copyright (C) 2015 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 View Controller for Metal Sample Code. Manages a MTKView and a AAPLRenderer object.
 */

#ifdef TARGET_IOS
#import <UIKit/UIKit.h>
#else
#import <AppKit/AppKit.h>
#endif

@protocol AAPLViewControllerDelegate;

#ifdef TARGET_IOS
@interface AAPLViewController : UIViewController
#else
@interface AAPLViewController : NSViewController
#endif

@end
```

[Next](MetalArrayTexture-AAPLTransforms.mm.md)[Previous](MetalArrayTexture-AAPLMtkView.m.md)

