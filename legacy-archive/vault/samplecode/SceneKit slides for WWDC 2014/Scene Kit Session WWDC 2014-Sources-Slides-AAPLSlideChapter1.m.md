---
title: SceneKit slides for WWDC 2014
apple_id: TP40014551
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2014-10-16'
source_url: https://developer.apple.com/library/archive/samplecode/SceneKitWWDC2014/Listings/Scene_Kit_Session_WWDC_2014_Sources_Slides_AAPLSlideChapter1_m.html
archived_at: '2026-07-18T03:23:15.190345Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [SceneKit slides for WWDC 2014](SceneKit%20slides%20for%20WWDC%202014.md)


[Next](Scene%20Kit%20Session%20WWDC%202014-Sources-Slides-AAPLSlideChapter7.m.md)[Previous](Scene%20Kit%20Session%20WWDC%202014-Sources-Slides-AAPLSlideCreateAScene.m.md)

# Scene Kit Session WWDC 2014/Sources/Slides/AAPLSlideChapter1.m

```objc
/*
 Copyright (C) 2014-2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Chapter 1 slide
 */


#import "AAPLPresentationViewController.h"
#import "AAPLSlideTextManager.h"
#import "AAPLSlide.h"

@interface AAPLSlideChapter1 : AAPLSlide
{
    SCNNode *footPrintNode;
}
@end

@implementation AAPLSlideChapter1

- (void)setupSlideWithPresentationViewController:(AAPLPresentationViewController *)presentationViewController {
    [self.textManager setChapterTitle:@"What's New in SceneKit"];

    //add footprint
    footPrintNode = [SCNNode node];

    SCNNode *sessionID = [self.textManager addText:@"Session 609" atLevel:0];
    SCNNode *presenter = [self.textManager addText:@"Thomas Goossens" atLevel:0];
    SCNNode *title = [self.textManager addFootPrint:@"Software Engineer"];
    SCNNode *footPrint = [self.textManager addFootPrint:@"© 2014 Apple Inc. All rights reserved. Redistribution or public display not permitted without written permission from Apple."];

    sessionID.renderingOrder = 100;
    presenter.renderingOrder = 100;
    title.renderingOrder = 100;
    sessionID.geometry.firstMaterial = footPrint.geometry.firstMaterial;
    title.geometry.firstMaterial = footPrint.geometry.firstMaterial;
    presenter.geometry.firstMaterial.readsFromDepthBuffer = NO;
    title.geometry.firstMaterial.readsFromDepthBuffer = NO;

    sessionID.position = SCNVector3Make(footPrint.position.x, footPrint.position.y+1.78, footPrint.position.z);
    presenter.position = SCNVector3Make(footPrint.position.x, footPrint.position.y+1.38, footPrint.position.z);
    title.position = SCNVector3Make(footPrint.position.x, footPrint.position.y+0.93, footPrint.position.z);

#define SCALE 0.007
    SCNVector3 scale = SCNVector3Make(SCALE, SCALE, SCALE);
    sessionID.scale = scale;
    presenter.scale = scale;
    title.scale = scale;

    [footPrintNode addChildNode:sessionID];
    [footPrintNode addChildNode:presenter];
    [footPrintNode addChildNode:footPrint];
    [footPrintNode addChildNode:title];

    [presentationViewController.cameraNode addChildNode:footPrintNode];
}

- (void) willOrderOutWithPresentationViewController:(AAPLPresentationViewController *)presentationViewController
{
    [footPrintNode removeFromParentNode];
}

@end
```

[Next](Scene%20Kit%20Session%20WWDC%202014-Sources-Slides-AAPLSlideChapter7.m.md)[Previous](Scene%20Kit%20Session%20WWDC%202014-Sources-Slides-AAPLSlideCreateAScene.m.md)

