---
title: 'AVMovieEditor: Editing the QuickTime File Format'
apple_id: TP40016208
resource_type: Sample Code
platform: macOS
topic: Audio, Video, & Visual Effects
technology: AVFoundation
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/samplecode/AVMovieEditor/Listings/AVMovieEditor_AVMovieEditor_AAPLMovieTimeline_h.html
archived_at: '2026-07-18T03:00:22.162146Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AVMovieEditor: Editing the QuickTime File Format](AVMovieEditor-%20Editing%20the%20QuickTime%20File%20Format.md)


[Next](AVMovieEditor-AVMovieEditor-AAPLTimeRangeView.m.md)[Previous](AVMovieEditor-AVMovieEditor-AAPLMovieMutator.h.md)

# AVMovieEditor/AVMovieEditor/AAPLMovieTimeline.h

```objc
/*
    Copyright (C) 2015 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    The `AAPLMovieTimeline` and `AAPLMovieTimelineDelegate` protocols provide the infrastructure for drawing video track images in a timeline like view and track cursor movements and selections.
 */

#import <Cocoa/Cocoa.h>

@class AAPLMovieTimeline;

@protocol AAPLMovieTimelineUpdateDelgate <NSObject>

- (void)movieTimeline:(AAPLMovieTimeline *)timeline didUpdateCursorToPoint:(NSPoint)toPoint;
- (void)didSelectTimelineRangeFromPoint:(NSPoint)fromPoint toPoint:(NSPoint)toPoint;
- (void)didSelectTimelinePoint:(NSPoint)point;

@end

@interface AAPLMovieTimeline : NSView

@property id<AAPLMovieTimelineUpdateDelgate> delegate;

- (void)removeAllPositionalSubviews;
- (NSUInteger)countOfImagesRequiredToFillView;
- (void)addImageView:(NSImage *)image;
- (void)updateTimeLabel:(NSString *)newLabel;

@end
```

[Next](AVMovieEditor-AVMovieEditor-AAPLTimeRangeView.m.md)[Previous](AVMovieEditor-AVMovieEditor-AAPLMovieMutator.h.md)

