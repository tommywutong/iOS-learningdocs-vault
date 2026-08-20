---
title: AVCustomEdit
apple_id: DTS40013411
resource_type: Sample Code
platform: iOS
topic: Audio, Video, & Visual Effects
technology: AVFoundation
published: '2017-08-17'
source_url: https://developer.apple.com/library/archive/samplecode/AVCustomEdit/Listings/AVCustomEdit_APLCustomVideoCompositor_h.html
archived_at: '2026-07-18T03:00:10.037864Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AVCustomEdit](AVCustomEdit.md)


[Next](AVCustomEdit-APLSimpleEditor.h.md)[Previous](AVCustomEdit-APLDiagonalWipeRenderer.m.md)

# AVCustomEdit/APLCustomVideoCompositor.h

```objc
/*
 Copyright (C) 2017 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Custom video compositor class implementing the AVVideoCompositing protocol.
 */

#import <Foundation/Foundation.h>
#import <AVFoundation/AVFoundation.h>

@interface APLCustomVideoCompositor : NSObject <AVVideoCompositing>

@end

@interface APLCrossDissolveCompositor : APLCustomVideoCompositor

@end

@interface APLDiagonalWipeCompositor : APLCustomVideoCompositor

@end
```

[Next](AVCustomEdit-APLSimpleEditor.h.md)[Previous](AVCustomEdit-APLDiagonalWipeRenderer.m.md)

