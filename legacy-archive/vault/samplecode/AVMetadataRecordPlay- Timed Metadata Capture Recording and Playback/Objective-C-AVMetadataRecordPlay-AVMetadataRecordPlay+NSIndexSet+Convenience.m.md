---
title: 'AVMetadataRecordPlay: Timed Metadata Capture Recording and Playback'
apple_id: TP40016165
resource_type: Sample Code
platform: iOS
topic: Audio, Video, & Visual Effects
technology: AVFoundation
published: '2017-03-09'
source_url: https://developer.apple.com/library/archive/samplecode/AVMetadataRecordPlay/Listings/Objective_C_AVMetadataRecordPlay_AVMetadataRecordPlay_NSIndexSet_Convenience_m.html
archived_at: '2026-07-18T03:00:20.618613Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AVMetadataRecordPlay: Timed Metadata Capture Recording and Playback](AVMetadataRecordPlay-%20Timed%20Metadata%20Capture%20Recording%20and%20Playback.md)


[Next](Objective-C-AVMetadataRecordPlay-AVMetadataRecordPlayCameraAppDelegate.h.md)[Previous](Objective-C-AVMetadataRecordPlay-AVMetadataRecordPlayCameraPreviewView.h.md)

# Objective-C/AVMetadataRecordPlay/AVMetadataRecordPlay+NSIndexSet+Convenience.m

```objc
/*
    Copyright (C) 2017 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    NSIndexSet convenience extensions.
*/

#import "AVMetadataRecordPlay+NSIndexSet+Convenience.h"

@import UIKit;

@implementation NSIndexSet (Convenience)

- (NSArray<NSIndexPath *> *)avMetadataRecordPlay_indexPathsFromIndexesWithSection:(NSUInteger)section
{
    NSMutableArray<NSIndexPath *> *indexPaths = [NSMutableArray arrayWithCapacity:self.count];
    [self enumerateIndexesUsingBlock:^(NSUInteger idx, BOOL *stop) {
        [indexPaths addObject:[NSIndexPath indexPathForItem:idx inSection:section]];
    }];
    return indexPaths;
}

@end
```

[Next](Objective-C-AVMetadataRecordPlay-AVMetadataRecordPlayCameraAppDelegate.h.md)[Previous](Objective-C-AVMetadataRecordPlay-AVMetadataRecordPlayCameraPreviewView.h.md)

