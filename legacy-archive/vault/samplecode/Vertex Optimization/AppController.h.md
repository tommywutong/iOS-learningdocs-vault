---
title: Vertex Optimization
apple_id: DTS10000553
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenGL
published: '2003-07-07'
source_url: https://developer.apple.com/library/archive/samplecode/Vertex_Optimization/Listings/AppController_h.html
archived_at: '2026-07-18T03:27:49.516898Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Vertex Optimization](Vertex%20Optimization.md)


[Next](AppController.m.md)[Previous](main.m.md)

# AppController.h

```objc
#import <Cocoa/Cocoa.h>

#import "MainOpenGLView.h"

@interface AppController : NSObject
{
    IBOutlet MainOpenGLView     *mainGLView;
}

- (void)UpdateDrawing;
@end
```

[Next](AppController.m.md)[Previous](main.m.md)

