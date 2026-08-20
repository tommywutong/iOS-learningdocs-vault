---
title: AVCustomEdit
apple_id: DTS40013411
resource_type: Sample Code
platform: iOS
topic: Audio, Video, & Visual Effects
technology: AVFoundation
published: '2017-08-17'
source_url: https://developer.apple.com/library/archive/samplecode/AVCustomEdit/Listings/AVCustomEdit_APLCustomVideoCompositionInstruction_h.html
archived_at: '2026-07-18T03:00:09.922103Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AVCustomEdit](AVCustomEdit.md)


[Next](AVCustomEdit-APLViewController.h.md)[Previous](AVCustomEdit-APLOpenGLRenderer.m.md)

# AVCustomEdit/APLCustomVideoCompositionInstruction.h

```objc
/*
 Copyright (C) 2017 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Custom video composition instruction class implementing AVVideoCompositionInstruction protocol.
 */

#import <Foundation/Foundation.h>
#import <AVFoundation/AVFoundation.h>

@interface APLCustomVideoCompositionInstruction : NSObject <AVVideoCompositionInstruction>

@property CMPersistentTrackID foregroundTrackID;
@property CMPersistentTrackID backgroundTrackID;

- (id)initPassThroughTrackID:(CMPersistentTrackID)passthroughTrackID forTimeRange:(CMTimeRange)timeRange;
- (id)initTransitionWithSourceTrackIDs:(NSArray*)sourceTrackIDs forTimeRange:(CMTimeRange)timeRange;

@end
```

[Next](AVCustomEdit-APLViewController.h.md)[Previous](AVCustomEdit-APLOpenGLRenderer.m.md)

