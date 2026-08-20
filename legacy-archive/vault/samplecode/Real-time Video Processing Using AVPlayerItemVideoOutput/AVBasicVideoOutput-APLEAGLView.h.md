---
title: Real-time Video Processing Using AVPlayerItemVideoOutput
apple_id: DTS40013109
resource_type: Sample Code
platform: iOS
topic: Audio, Video, & Visual Effects
technology: AVFoundation
published: '2015-10-01'
source_url: https://developer.apple.com/library/archive/samplecode/AVBasicVideoOutput/Listings/AVBasicVideoOutput_APLEAGLView_h.html
archived_at: '2026-07-18T03:00:01.338225Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Real-time Video Processing Using AVPlayerItemVideoOutput](Real-time%20Video%20Processing%20Using%20AVPlayerItemVideoOutput.md)


[Next](AVBasicVideoOutput-APLAppDelegate.m.md)[Previous](AVBasicVideoOutput-Shaders-Shader.vsh.md)

# AVBasicVideoOutput/APLEAGLView.h

```objc
/*
    Copyright (C) 2015 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    This class contains an UIView backed by a CAEAGLLayer. It handles rendering input textures to the view. The object loads, compiles and links the fragment and vertex shader to be used during rendering.
 */

#import <UIKit/UIKit.h>
#import <OpenGLES/ES2/gl.h>
#import <OpenGLES/ES2/glext.h>

@interface APLEAGLView : UIView

@property GLfloat preferredRotation;
@property CGSize presentationRect;
@property GLfloat chromaThreshold;
@property GLfloat lumaThreshold;

- (void)setupGL;
- (void)displayPixelBuffer:(CVPixelBufferRef)pixelBuffer;

@end
```

[Next](AVBasicVideoOutput-APLAppDelegate.m.md)[Previous](AVBasicVideoOutput-Shaders-Shader.vsh.md)

