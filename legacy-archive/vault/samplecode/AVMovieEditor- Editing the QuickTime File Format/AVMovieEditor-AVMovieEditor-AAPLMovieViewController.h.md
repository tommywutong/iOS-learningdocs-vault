---
title: 'AVMovieEditor: Editing the QuickTime File Format'
apple_id: TP40016208
resource_type: Sample Code
platform: macOS
topic: Audio, Video, & Visual Effects
technology: AVFoundation
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/samplecode/AVMovieEditor/Listings/AVMovieEditor_AVMovieEditor_AAPLMovieViewController_h.html
archived_at: '2026-07-18T03:00:22.310119Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AVMovieEditor: Editing the QuickTime File Format](AVMovieEditor-%20Editing%20the%20QuickTime%20File%20Format.md)


[Next](AVMovieEditor-AVMovieEditor-AAPLDocument.h.md)[Previous](AVMovieEditor-AVMovieEditor-AAPLMovieViewController.m.md)

# AVMovieEditor/AVMovieEditor/AAPLMovieViewController.h

```objc
/*
    Copyright (C) 2015 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    The 'AAPLMovieViewController' and 'AAPLMovieViewControllerDelegate' provide a way for this ViewController and it's subviews to talk to a data source that understands how to manipulate the QuickTime File Format and edit movies.
 */

@import Cocoa;
@import AVFoundation;
@import AVKit;

typedef void (^ImageGenerationCompletionHandler)(NSImage *);

@class AAPLMovieViewController;

@protocol AAPLMovieViewControllerDelegate

- (void)movieViewController:(AAPLMovieViewController *)movieViewController needsNumberOfImages:(NSUInteger)numberOfImages completionHandler:(ImageGenerationCompletionHandler)completionHandler;
- (CMTime)timeAtPercentage:(float)percentage;
- (BOOL)cutMovieTimeRange:(CMTimeRange)timeRange error:(NSError *)error;
- (BOOL)copyMovieTimeRange:(CMTimeRange)timeRange error:(NSError *)error;
- (BOOL)pasteMovieAtTime:(CMTime)time error:(NSError *)error;

@end

@interface AAPLMovieViewController : NSViewController

@property (weak) IBOutlet AVPlayerView *playerView;
@property id<AAPLMovieViewControllerDelegate> delegate;
- (void)updateMovieTimeline;

@end
```

[Next](AVMovieEditor-AVMovieEditor-AAPLDocument.h.md)[Previous](AVMovieEditor-AVMovieEditor-AAPLMovieViewController.m.md)

