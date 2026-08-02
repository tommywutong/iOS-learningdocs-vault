---
title: Vertex Optimization
apple_id: DTS10000553
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenGL
published: '2003-07-07'
source_url: https://developer.apple.com/library/archive/samplecode/Vertex_Optimization/Listings/MyApplication_m.html
archived_at: '2026-07-18T03:27:49.786731Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Vertex Optimization](Vertex%20Optimization.md)


[Next](newave.h.md)[Previous](MyApplication.h.md)

# MyApplication.m

```objc
#import "MyApplication.h"
#import "AppController.h"

@implementation MyApplication

#if 1

- (NSEvent *)nextEventMatchingMask:(unsigned int)mask
    untilDate:(NSDate *)expiration inMode:(NSString *)mode dequeue:(BOOL)flag
{
    NSEvent *event;
    NSDate *now;
    int send_event;

    do
    {
        event = [super nextEventMatchingMask:mask untilDate:[NSDate distantPast] inMode:mode dequeue:flag];

        /*if(event == nil)*/ [[self delegate] UpdateDrawing];

        now = [[NSDate alloc] initWithTimeIntervalSinceNow:0];

        if(!event && ([expiration compare:now] > 0)) send_event = false;
        else                                         send_event = true;

        [now release];

    } while(!send_event);

    return event;
}

#else

- (NSEvent *)nextEventMatchingMask:(unsigned int)mask
    untilDate:(NSDate *)expiration inMode:(NSString *)mode dequeue:(BOOL)flag
{
    NSEvent *event;

    event = [super nextEventMatchingMask:mask untilDate:expiration inMode:mode dequeue:flag];

    [[self delegate] UpdateDrawing];

    return event;
}

#endif

@end
```

[Next](newave.h.md)[Previous](MyApplication.h.md)

