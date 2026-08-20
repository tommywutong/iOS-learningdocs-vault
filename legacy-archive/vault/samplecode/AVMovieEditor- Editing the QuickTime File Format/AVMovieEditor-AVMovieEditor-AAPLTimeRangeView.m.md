---
title: 'AVMovieEditor: Editing the QuickTime File Format'
apple_id: TP40016208
resource_type: Sample Code
platform: macOS
topic: Audio, Video, & Visual Effects
technology: AVFoundation
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/samplecode/AVMovieEditor/Listings/AVMovieEditor_AVMovieEditor_AAPLTimeRangeView_m.html
archived_at: '2026-07-18T03:00:22.465669Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AVMovieEditor: Editing the QuickTime File Format](AVMovieEditor-%20Editing%20the%20QuickTime%20File%20Format.md)


[Next](AVMovieEditor-AVMovieEditor-AAPLMovieTimeline.m.md)[Previous](AVMovieEditor-AVMovieEditor-AAPLMovieTimeline.h.md)

# AVMovieEditor/AVMovieEditor/AAPLTimeRangeView.m

```objc
/*
    Copyright (C) 2015 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    'AAPLTimeRangView' is a simple view that draws a yellow highlight.
 */

#import "AAPLTimeRangeView.h"

@implementation AAPLTimeRangeView

- (void)drawRect:(NSRect)dirtyRect {
    [super drawRect:dirtyRect];

    CGContextRef currentContext = [NSGraphicsContext currentContext].CGContext;
    CGContextSaveGState(currentContext);

    [[NSColor yellowColor] set];

    NSBezierPath *bezierPath = [NSBezierPath bezierPathWithRoundedRect:dirtyRect xRadius:0.0 yRadius:2.0];
    bezierPath.lineWidth = 5.0;
    [bezierPath stroke];

    CGContextRestoreGState(currentContext);
}

@end
```

[Next](AVMovieEditor-AVMovieEditor-AAPLMovieTimeline.m.md)[Previous](AVMovieEditor-AVMovieEditor-AAPLMovieTimeline.h.md)

