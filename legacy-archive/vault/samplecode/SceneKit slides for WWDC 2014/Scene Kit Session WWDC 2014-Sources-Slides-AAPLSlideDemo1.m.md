---
title: SceneKit slides for WWDC 2014
apple_id: TP40014551
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2014-10-16'
source_url: https://developer.apple.com/library/archive/samplecode/SceneKitWWDC2014/Listings/Scene_Kit_Session_WWDC_2014_Sources_Slides_AAPLSlideDemo1_m.html
archived_at: '2026-07-18T03:23:16.312467Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [SceneKit slides for WWDC 2014](SceneKit%20slides%20for%20WWDC%202014.md)


[Next](Scene%20Kit%20Session%20WWDC%202014-Sources-Slides-AAPLSlideTechniques.m.md)[Previous](Scene%20Kit%20Session%20WWDC%202014-Sources-Slides-AAPLSlideExplicitAnimations.m.md)

# Scene Kit Session WWDC 2014/Sources/Slides/AAPLSlideDemo1.m

```objc
/*
 Copyright (C) 2014-2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Chapter 2 slide : Scene Graph
 */

#import "AAPLPresentationViewController.h"
#import "AAPLSlideTextManager.h"
#import "AAPLSlide.h"

@interface AAPLSlideDemo1 : AAPLSlide
{
    SCNNode *_chapterNode;
}
@end

@implementation AAPLSlideDemo1

- (void)setupSlideWithPresentationViewController:(AAPLPresentationViewController *)presentationViewController {
    _chapterNode = [self.textManager setChapterTitle:@"Car Toy Demo"];
}


- (void)willOrderOutWithPresentationViewController:(AAPLPresentationViewController *)presentationViewController {
    [SCNTransaction begin];
    [SCNTransaction setAnimationDuration:0.75];
    _chapterNode.position = SCNVector3Make(_chapterNode.position.x-30, _chapterNode.position.y, _chapterNode.position.z);
    [SCNTransaction commit];
}


@end
```

[Next](Scene%20Kit%20Session%20WWDC%202014-Sources-Slides-AAPLSlideTechniques.m.md)[Previous](Scene%20Kit%20Session%20WWDC%202014-Sources-Slides-AAPLSlideExplicitAnimations.m.md)

