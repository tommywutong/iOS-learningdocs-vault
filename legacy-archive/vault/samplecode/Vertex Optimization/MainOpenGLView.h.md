---
title: Vertex Optimization
apple_id: DTS10000553
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenGL
published: '2003-07-07'
source_url: https://developer.apple.com/library/archive/samplecode/Vertex_Optimization/Listings/MainOpenGLView_h.html
archived_at: '2026-07-18T03:27:49.570275Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Vertex Optimization](Vertex%20Optimization.md)


[Next](MainOpenGLView.m.md)[Previous](AppController.m.md)

# MainOpenGLView.h

```objc
#import <Cocoa/Cocoa.h>
#import "PerfBarOpenGLView.h"
#include "newave.h"

#include <OpenGL/gl.h>
#include <OpenGL/glext.h>
#include <OpenGL/glu.h>

#define COMPUTATION_QUEUE  0
#define DISPLAY_QUEUE      1

@interface MainOpenGLView : NSOpenGLView
{
    GLdouble tottime, comptime, ogltime, prev_tottime;
    GLint passes;

    GLint appOptLevel;
    GLint openglOptLevel;
    GLint multi_threaded;
    GLint fillmode;

    struct timeval cycle_time;
    struct timeval display_time;

    WaveOject  *wave;

    NSConditionLock *buffer_lock[2];
    GLint work_queue[2][2];

    IBOutlet PerfBarOpenGLView *perfBarGLView;
    IBOutlet NSButton    *selectMP;
    IBOutlet NSTextField *setFPS;
    IBOutlet NSTextField *setTriRate;
    IBOutlet NSTextField *optLevelLabel_0;
    IBOutlet NSTextField *optLevelLabel_1;
    IBOutlet NSTextField *optLevelLabel_2;
    IBOutlet NSTextField *optLevelLabel_3;
    IBOutlet NSTextField *optLevelLabel_4;
    IBOutlet NSTextField *optLevelLabel_5;
}

- (IBAction)setAppOptLevelAction:(id)sender;
- (IBAction)setOptLevelAction:(id)sender;
- (IBAction)setMPAction:(id)sender;
- (IBAction)setBarScaleFactor:(id)sender;

@end
```

[Next](MainOpenGLView.m.md)[Previous](AppController.m.md)

