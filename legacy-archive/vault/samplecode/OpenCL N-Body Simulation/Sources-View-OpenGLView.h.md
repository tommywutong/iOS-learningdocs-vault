---
title: OpenCL N-Body Simulation
apple_id: TP40016610
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenCL
published: '2015-12-10'
source_url: https://developer.apple.com/library/archive/samplecode/OpenCL_NBody_Simulation/Listings/Sources_View_OpenGLView_h.html
archived_at: '2026-07-18T03:17:43.774420Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [OpenCL N-Body Simulation](OpenCL%20N-Body%20Simulation.md)


[Next](Sources-Model-Foundation-Bitmap-CGBitmap.mm.md)[Previous](Sources-View-OpenGLView.mm.md)

# Sources/View/OpenGLView.h

```objc
/*
 <codex>
 <abstract>
 OpenGL view class with idle timer and fullscreen mode support.
 </abstract>
 </codex>
 */

#import <Cocoa/Cocoa.h>
#import <OpenGL/OpenGL.h>

@interface OpenGLView : NSOpenGLView

- (IBAction) toggleHelp:(id)sender;
- (IBAction) toggleFullscreen:(id)sender;

@end
```

[Next](Sources-Model-Foundation-Bitmap-CGBitmap.mm.md)[Previous](Sources-View-OpenGLView.mm.md)

