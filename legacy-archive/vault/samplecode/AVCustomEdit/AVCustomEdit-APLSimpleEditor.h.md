---
title: AVCustomEdit
apple_id: DTS40013411
resource_type: Sample Code
platform: iOS
topic: Audio, Video, & Visual Effects
technology: AVFoundation
published: '2017-08-17'
source_url: https://developer.apple.com/library/archive/samplecode/AVCustomEdit/Listings/AVCustomEdit_APLSimpleEditor_h.html
archived_at: '2026-07-18T03:00:10.616215Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AVCustomEdit](AVCustomEdit.md)


[Next](Document%20Revision%20History.md)[Previous](AVCustomEdit-APLCustomVideoCompositor.h.md)

# AVCustomEdit/APLSimpleEditor.h

```objc
/*
 Copyright (C) 2017 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Simple editor sets up an AVMutableComposition using supplied clips and time ranges. It also sets up an AVVideoComposition to perform custom compositor rendering.
 */

#import <Foundation/Foundation.h>

#import <CoreMedia/CMTime.h>

@class AVPlayerItem, AVAssetExportSession;

@interface APLSimpleEditor : NSObject

// Set these properties before building the composition objects.
@property (nonatomic, copy) NSArray *clips; // array of AVURLAssets
@property (nonatomic, copy) NSArray *clipTimeRanges; // array of CMTimeRanges stored in NSValues.

@property (nonatomic) NSInteger transitionType;
@property (nonatomic) CMTime transitionDuration;

// Builds the composition and videoComposition
- (void)buildCompositionObjectsForPlayback:(BOOL)forPlayback;

- (AVAssetExportSession*)assetExportSessionWithPreset:(NSString*)presetName;

- (AVPlayerItem *)playerItem;

@end
```

[Next](Document%20Revision%20History.md)[Previous](AVCustomEdit-APLCustomVideoCompositor.h.md)

