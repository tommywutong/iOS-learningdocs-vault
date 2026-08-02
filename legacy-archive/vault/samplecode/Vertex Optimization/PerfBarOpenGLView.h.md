---
title: Vertex Optimization
apple_id: DTS10000553
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenGL
published: '2003-07-07'
source_url: https://developer.apple.com/library/archive/samplecode/Vertex_Optimization/Listings/PerfBarOpenGLView_h.html
archived_at: '2026-07-18T03:27:49.825718Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Vertex Optimization](Vertex%20Optimization.md)


[Next](PerfBarOpenGLView.m.md)[Previous](newave.m.md)

# PerfBarOpenGLView.h

```objc
#import <Cocoa/Cocoa.h>

#include <sys/time.h>

@interface PerfBarOpenGLView : NSOpenGLView
{
    float total_time;
    float draw_time;
    float comp_time;

    float bar_scale;

    int bar_width;
    int bar_height;

    int cpu_threaded;
}

- (void)setPerfTimes:(float)tottime:(float)comptime:(float)drawtime:(int)threaded:(float)lag;
- (void)setBarScaleFactor:(float)factor;

@end
```

[Next](PerfBarOpenGLView.m.md)[Previous](newave.m.md)

