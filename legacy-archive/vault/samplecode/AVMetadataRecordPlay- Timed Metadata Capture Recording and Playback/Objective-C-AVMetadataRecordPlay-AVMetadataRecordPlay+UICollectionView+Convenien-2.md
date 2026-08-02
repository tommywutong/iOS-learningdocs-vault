---
title: 'AVMetadataRecordPlay: Timed Metadata Capture Recording and Playback'
apple_id: TP40016165
resource_type: Sample Code
platform: iOS
topic: Audio, Video, & Visual Effects
technology: AVFoundation
published: '2017-03-09'
source_url: https://developer.apple.com/library/archive/samplecode/AVMetadataRecordPlay/Listings/Objective_C_AVMetadataRecordPlay_AVMetadataRecordPlay_UICollectionView_Convenience_m.html
archived_at: '2026-07-18T03:00:20.712255Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AVMetadataRecordPlay: Timed Metadata Capture Recording and Playback](AVMetadataRecordPlay-%20Timed%20Metadata%20Capture%20Recording%20and%20Playback.md)


[Next](README.md.md)[Previous](Objective-C-AVMetadataRecordPlay-AVMetadataRecordPlayPlayerViewController.m.md)

# Objective-C/AVMetadataRecordPlay/AVMetadataRecordPlay+UICollectionView+Convenience.m

```objc
/*
    Copyright (C) 2017 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    UICollectionView convenience extensions.
*/

#import "AVMetadataRecordPlay+UICollectionView+Convenience.h"

@implementation UICollectionView (Convenience)

- (NSArray<NSIndexPath *> *)avMetadataRecordPlay_indexPathsForElementsInRect:(CGRect)rect
{
    NSArray *allLayoutAttributes = [self.collectionViewLayout layoutAttributesForElementsInRect:rect];
    if ( allLayoutAttributes.count == 0 ) { return nil; }
    NSMutableArray<NSIndexPath *> *indexPaths = [NSMutableArray arrayWithCapacity:allLayoutAttributes.count];
    for ( UICollectionViewLayoutAttributes *layoutAttributes in allLayoutAttributes ) {
        NSIndexPath *indexPath = layoutAttributes.indexPath;
        [indexPaths addObject:indexPath];
    }
    return indexPaths;
}

@end
```

[Next](README.md.md)[Previous](Objective-C-AVMetadataRecordPlay-AVMetadataRecordPlayPlayerViewController.m.md)

