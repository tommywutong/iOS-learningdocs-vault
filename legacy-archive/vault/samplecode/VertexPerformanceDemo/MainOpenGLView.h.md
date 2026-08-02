---
title: VertexPerformanceDemo
apple_id: DTS10003726
resource_type: Sample Code
platform: macOS
topic: Performance
technology: OpenGL
published: '2005-06-01'
source_url: https://developer.apple.com/library/archive/samplecode/VertexPerformanceDemo/Listings/MainOpenGLView_h.html
archived_at: '2026-07-18T03:27:48.244104Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [VertexPerformanceDemo](VertexPerformanceDemo.md)


[Next](MainOpenGLView.m.md)[Previous](main.m.md)

# MainOpenGLView.h

```objc
#import <Cocoa/Cocoa.h>
#include "newave.h"

#include <OpenGL/gl.h>
#include <OpenGL/glext.h>
#include <OpenGL/glu.h>

@interface MainOpenGLView : NSOpenGLView
{
    GLdouble tottime;
    GLint passes;

    struct timeval cycle_time;
    struct timeval display_time;

    WaveOject  *wave;

    IBOutlet NSTextField *setFPS;
    IBOutlet NSTextField *setTriRate;

    NSTimer* timer;
}

@end
```

[Next](MainOpenGLView.m.md)[Previous](main.m.md)

