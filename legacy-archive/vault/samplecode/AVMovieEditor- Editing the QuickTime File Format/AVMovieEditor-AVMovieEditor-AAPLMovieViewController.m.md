---
title: 'AVMovieEditor: Editing the QuickTime File Format'
apple_id: TP40016208
resource_type: Sample Code
platform: macOS
topic: Audio, Video, & Visual Effects
technology: AVFoundation
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/samplecode/AVMovieEditor/Listings/AVMovieEditor_AVMovieEditor_AAPLMovieViewController_m.html
archived_at: '2026-07-18T03:00:22.375585Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AVMovieEditor: Editing the QuickTime File Format](AVMovieEditor-%20Editing%20the%20QuickTime%20File%20Format.md)


[Next](AVMovieEditor-AVMovieEditor-AAPLMovieViewController.h.md)[Previous](AVMovieEditor-AVMovieEditor-AAPLDocument.m.md)

# AVMovieEditor/AVMovieEditor/AAPLMovieViewController.m

```objc
/*
    Copyright (C) 2015 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    The 'AAPLMovieViewController' and 'AAPLMovieViewControllerDelegate' provide a way for this ViewController and it's subviews to talk to a data source that understands how to manipulate the QuickTime File Format and edit movies.
 */

#import "AAPLMovieViewController.h"
#import "AAPLMovieTimeline.h"

@interface AAPLMovieViewController () <AAPLMovieTimelineUpdateDelgate, NSMenuDelegate>

@property (weak) IBOutlet AAPLMovieTimeline *movieTimeline;
@property CMTimeRange selectedTimeRange;
@property CMTime selectedPointInTime;

@end

@implementation AAPLMovieViewController

- (void)viewWillAppear {
    [super viewWillAppear];

    self.movieTimeline.delegate = self;
    [self updateMovieTimeline];

    [[NSNotificationCenter defaultCenter] addObserverForName:NSWindowDidEndLiveResizeNotification object:nil queue:nil usingBlock:^(NSNotification * __nonnull note) {
        [self updateMovieTimeline];
    }];
}

- (void)updateMovieTimeline {
    self.movieTimeline.needsLayout = YES;
    [self.movieTimeline removeAllPositionalSubviews];

    NSUInteger numberOfImagesNeeded = [self.movieTimeline countOfImagesRequiredToFillView];
    [self.delegate movieViewController:self needsNumberOfImages:numberOfImagesNeeded completionHandler:^(NSImage * image) {

        // Add image view on the main thread.
        dispatch_async(dispatch_get_main_queue(), ^{
            [self.movieTimeline addImageView:image];
        });
    }];
}

#pragma mark - MovieTimeLine Delegate
- (void)movieTimeline:(AAPLMovieTimeline *)timeline didUpdateCursorToPoint:(NSPoint)toPoint {
    CGFloat percentage = toPoint.x / self.movieTimeline.frame.size.width;
    CMTime time = [self.delegate timeAtPercentage:percentage];

    // Update the time label for the new cursor point.
    float seconds = CMTimeGetSeconds(time) <= 0 ? 0 : CMTimeGetSeconds(time);
    NSString *timeDescription = [NSString stringWithFormat:@"%.2f", seconds];
    [self.movieTimeline updateTimeLabel:timeDescription];
}

- (void)didSelectTimelineRangeFromPoint:(NSPoint)fromPoint toPoint:(NSPoint)toPoint {
    CGFloat startPercentage = fromPoint.x / self.movieTimeline.frame.size.width;
    CGFloat endPercentage = toPoint.x / self.movieTimeline.frame.size.width;
    CMTime startTime = [self.delegate timeAtPercentage:startPercentage];
    CMTime endTime = [self.delegate timeAtPercentage:endPercentage];

    // Calculate the duration from the the time percentages.
    CMTime duration = CMTimeSubtract(endTime, startTime);
    self.selectedTimeRange = CMTimeRangeMake(startTime, duration);
}

- (void)didSelectTimelinePoint:(NSPoint)point {
    CGFloat pointPercentage = point.x / self.movieTimeline.frame.size.width;
    self.selectedPointInTime = [self.delegate timeAtPercentage:pointPercentage];
    self.selectedTimeRange = CMTimeRangeMake(kCMTimeZero, kCMTimeZero);
}

#pragma mark - Right click NSMEnu to message Cut, Copy, and Paste

- (void)rightMouseDown:(nonnull NSEvent *)theEvent {
    NSMenu *menu = [[NSMenu alloc] initWithTitle:@"Movie Style Editing"];

    // If we have not selected a time range then we can not copy or cut - only paste.
    if (CMTIME_COMPARE_INLINE(self.selectedTimeRange.start, ==, kCMTimeZero) && CMTIME_COMPARE_INLINE(self.selectedTimeRange.duration, ==, kCMTimeZero)) {
        [menu insertItemWithTitle:@"Paste" action:@selector(pasteMovie) keyEquivalent:@"" atIndex:0];
    } else {
        [menu insertItemWithTitle:@"Cut" action:@selector(cutMovie) keyEquivalent:@"" atIndex:0];
        [menu insertItemWithTitle:@"Copy" action:@selector(copyMovie) keyEquivalent:@"" atIndex:1];
    }

    menu.delegate = self;

    [NSMenu popUpContextMenu:menu withEvent:theEvent forView:self.view];
}

- (void)cutMovie {
    // Cut the movie and handle the error if necessary.
    NSError *error = nil;
    BOOL didSucceed = [self.delegate cutMovieTimeRange:self.selectedTimeRange error:error];
    if (!didSucceed || error) {
        NSLog(@"There was an error performing the cut operation");
    }
}

- (void)copyMovie {
    // Cut the movie and handle the error if necessary.
    NSError *error = nil;
    BOOL didSucceed = [self.delegate copyMovieTimeRange:self.selectedTimeRange error:error];
    if (!didSucceed || error) {
        NSLog(@"There was an error performing the copy operation.");
    }
}

- (void)pasteMovie {
    // Paste the movie and handle the error if necessary.
    NSError *error = nil;
    BOOL didSucceed = [self.delegate pasteMovieAtTime:self.selectedPointInTime error:error];
    if (!didSucceed || error) {
        NSLog(@"There was an error performing the paste operation.");
    }
}

#pragma mark - Edit Menu Cut, Copy, Paste methods

- (void)cut:(id)sender {
    [self cutMovie];
}

- (void)copy:(id)sender {
    [self copyMovie];
}

- (void)paste:(id)sender {
    [self pasteMovie];
}

@end
```

[Next](AVMovieEditor-AVMovieEditor-AAPLMovieViewController.h.md)[Previous](AVMovieEditor-AVMovieEditor-AAPLDocument.m.md)

