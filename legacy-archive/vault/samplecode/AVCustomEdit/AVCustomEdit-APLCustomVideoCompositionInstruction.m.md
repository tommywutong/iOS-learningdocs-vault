---
title: AVCustomEdit
apple_id: DTS40013411
resource_type: Sample Code
platform: iOS
topic: Audio, Video, & Visual Effects
technology: AVFoundation
published: '2017-08-17'
source_url: https://developer.apple.com/library/archive/samplecode/AVCustomEdit/Listings/AVCustomEdit_APLCustomVideoCompositionInstruction_m.html
archived_at: '2026-07-18T03:00:09.971327Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AVCustomEdit](AVCustomEdit.md)


[Next](AVCustomEdit-APLDiagonalWipeRenderer.h.md)[Previous](AVCustomEdit-APLCrossDissolveRenderer.h.md)

# AVCustomEdit/APLCustomVideoCompositionInstruction.m

```objc
/*
 Copyright (C) 2017 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Custom video composition instruction class implementing AVVideoCompositionInstruction protocol.
 */

#import "APLCustomVideoCompositionInstruction.h"

@implementation APLCustomVideoCompositionInstruction

@synthesize timeRange = _timeRange;
@synthesize enablePostProcessing = _enablePostProcessing;
@synthesize containsTweening = _containsTweening;
@synthesize requiredSourceTrackIDs = _requiredSourceTrackIDs;
@synthesize passthroughTrackID = _passthroughTrackID;

- (id)initPassThroughTrackID:(CMPersistentTrackID)passthroughTrackID forTimeRange:(CMTimeRange)timeRange
{
    self = [super init];
    if (self) {
        _passthroughTrackID = passthroughTrackID;
        _requiredSourceTrackIDs = nil;
        _timeRange = timeRange;
        _containsTweening = FALSE;
        _enablePostProcessing = FALSE;
    }

    return self;
}

- (id)initTransitionWithSourceTrackIDs:(NSArray *)sourceTrackIDs forTimeRange:(CMTimeRange)timeRange
{
    self = [super init];
    if (self) {
        _requiredSourceTrackIDs = sourceTrackIDs;
        _passthroughTrackID = kCMPersistentTrackID_Invalid;
        _timeRange = timeRange;
        _containsTweening = TRUE;
        _enablePostProcessing = FALSE;
    }

    return self;
}

@end
```

[Next](AVCustomEdit-APLDiagonalWipeRenderer.h.md)[Previous](AVCustomEdit-APLCrossDissolveRenderer.h.md)

