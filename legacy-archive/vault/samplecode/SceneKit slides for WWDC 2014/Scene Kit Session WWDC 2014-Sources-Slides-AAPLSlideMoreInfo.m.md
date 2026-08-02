---
title: SceneKit slides for WWDC 2014
apple_id: TP40014551
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2014-10-16'
source_url: https://developer.apple.com/library/archive/samplecode/SceneKitWWDC2014/Listings/Scene_Kit_Session_WWDC_2014_Sources_Slides_AAPLSlideMoreInfo_m.html
archived_at: '2026-07-18T03:23:17.560589Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [SceneKit slides for WWDC 2014](SceneKit%20slides%20for%20WWDC%202014.md)


[Next](Scene%20Kit%20Session%20WWDC%202014-Sources-Slides-AAPLSlideDelegateRendering.m.md)[Previous](Scene%20Kit%20Session%20WWDC%202014-Sources-Slides-AAPLSlideIK.m.md)

# Scene Kit Session WWDC 2014/Sources/Slides/AAPLSlideMoreInfo.m

```objc
/*
 Copyright (C) 2014-2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Explains how to get more information about SceneKit.
 */

#import "AAPLPresentationViewController.h"
#import "AAPLSlideTextManager.h"
#import "AAPLSlide.h"
#import "Utils.h"

@interface AAPLSlideMoreInfo : AAPLSlide
@end

@implementation AAPLSlideMoreInfo

- (void)setupSlideWithPresentationViewController:(AAPLPresentationViewController *)presentationViewController {
    self.textManager.title = @"More Information";

    [self.textManager addText:@"Allan Schaffer" atLevel:0];
    SCNNode *node = [self.textManager addText:@"Graphics and Game Technologies Evangelist" atLevel:1];
    node.opacity = 0.56;
    [self.textManager addText:@"aschaffer@apple.com" atLevel:2];
    [self.textManager addEmptyLine];

    [self.textManager addText:@"Filip Iliescu" atLevel:0];
    node = [self.textManager addText:@"Graphics and Game Technologies Evangelist" atLevel:1];
    node.opacity = 0.56;
    [self.textManager addText:@"filiescu@apple.com" atLevel:2];
    [self.textManager addEmptyLine];

    [self.textManager addText:@"Documentation" atLevel:0];
    node = [self.textManager addText:@"SceneKit Framework Reference" atLevel:1];
    node.opacity = 0.56;
    [self.textManager addText:@"http://developer.apple.com" atLevel:2];
    [self.textManager addEmptyLine];

    [self.textManager addText:@"Apple Developer Forums" atLevel:0];
    [self.textManager addText:@"http://devforums.apple.com" atLevel:2];
}

@end
```

[Next](Scene%20Kit%20Session%20WWDC%202014-Sources-Slides-AAPLSlideDelegateRendering.m.md)[Previous](Scene%20Kit%20Session%20WWDC%202014-Sources-Slides-AAPLSlideIK.m.md)

