---
title: 'AVMetadataRecordPlay: Timed Metadata Capture Recording and Playback'
apple_id: TP40016165
resource_type: Sample Code
platform: iOS
topic: Audio, Video, & Visual Effects
technology: AVFoundation
published: '2017-03-09'
source_url: https://developer.apple.com/library/archive/samplecode/AVMetadataRecordPlay/Listings/Objective_C_AVMetadataRecordPlay_AVMetadataRecordPlayGridViewCell_m.html
archived_at: '2026-07-18T03:00:20.269664Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AVMetadataRecordPlay: Timed Metadata Capture Recording and Playback](AVMetadataRecordPlay-%20Timed%20Metadata%20Capture%20Recording%20and%20Playback.md)


[Next](Objective-C-AVMetadataRecordPlay-AVMetadataRecordPlayGridViewCell.h.md)[Previous](Objective-C-AVMetadataRecordPlay-AVMetadataRecordPlayAssetGridViewController.m.md)

# Objective-C/AVMetadataRecordPlay/AVMetadataRecordPlayGridViewCell.m

```objc
/*
    Copyright (C) 2017 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    Thumbnail image collection view cell.
*/

#import "AVMetadataRecordPlayGridViewCell.h"

@interface AVMetadataRecordPlayGridViewCell ()

@property (nonatomic, weak) IBOutlet UIImageView *imageView;

@end

@implementation AVMetadataRecordPlayGridViewCell

- (UIImage *)thumbnailImage
{
    return self.imageView.image;
}

- (void)setThumbnailImage:(UIImage *)thumbnailImage
{
    self.imageView.image = thumbnailImage;
}

- (void)prepareForReuse
{
    [super prepareForReuse];

    self.imageView.image = nil;
}

@end
```

[Next](Objective-C-AVMetadataRecordPlay-AVMetadataRecordPlayGridViewCell.h.md)[Previous](Objective-C-AVMetadataRecordPlay-AVMetadataRecordPlayAssetGridViewController.m.md)

