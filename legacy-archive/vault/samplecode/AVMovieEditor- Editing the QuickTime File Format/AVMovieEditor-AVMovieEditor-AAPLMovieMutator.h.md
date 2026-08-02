---
title: 'AVMovieEditor: Editing the QuickTime File Format'
apple_id: TP40016208
resource_type: Sample Code
platform: macOS
topic: Audio, Video, & Visual Effects
technology: AVFoundation
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/samplecode/AVMovieEditor/Listings/AVMovieEditor_AVMovieEditor_AAPLMovieMutator_h.html
archived_at: '2026-07-18T03:00:22.010381Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AVMovieEditor: Editing the QuickTime File Format](AVMovieEditor-%20Editing%20the%20QuickTime%20File%20Format.md)


[Next](AVMovieEditor-AVMovieEditor-AAPLMovieTimeline.h.md)[Previous](AVMovieEditor-AVMovieEditor-AAPLAppDelegate.m.md)

# AVMovieEditor/AVMovieEditor/AAPLMovieMutator.h

```objc
/*
    Copyright (C) 2015 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    'AAPLMovieMutator' wraps AVMutableMovie to implement cut, copy, and paste and provides an interface for interacting with the AVMutableMovie. This class uses an AVMutableMovie as an internal pasteboard to keep track of edits, and this class uses the general NSPasteboard to move movie header data to other documents.
 */

#import <Foundation/Foundation.h>

static NSString* const movieWasMutated = @"movieWasMutatedNotificationName";
typedef void (^ImageGenerationCompletionHandler)(NSImage *);

@interface AAPLMovieMutator : NSObject

- (instancetype)initWithMovie:(AVMovie *)movie;
- (AVPlayerItem *)makePlayerItem;
- (AVVideoComposition *)makeVideoComposition;
- (BOOL)cutTimeRange:(CMTimeRange)range error:(NSError *)error;
- (BOOL)copyTimeRange:(CMTimeRange)range error:(NSError *)error;
- (BOOL)pasteAtTime:(CMTime)time error:(NSError *)error;
- (void)generateImages:(NSUInteger)numberOfImages withCompletionHandler:(ImageGenerationCompletionHandler)completionHandler;
- (CMTime)timePercentageThroughMovie:(float)percentage;
- (BOOL)writeMovieToURL:(NSURL *)outputURL fileType:(NSString *)fileType error:(NSError *)error;

@end
```

[Next](AVMovieEditor-AVMovieEditor-AAPLMovieTimeline.h.md)[Previous](AVMovieEditor-AVMovieEditor-AAPLAppDelegate.m.md)

