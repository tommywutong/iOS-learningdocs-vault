---
title: SceneKit slides for WWDC 2014
apple_id: TP40014551
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2014-10-16'
source_url: https://developer.apple.com/library/archive/samplecode/SceneKitWWDC2014/Listings/Scene_Kit_Session_WWDC_2014_Sources_Slides_AAPLSlideChapter5_m.html
archived_at: '2026-07-18T03:23:15.362326Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [SceneKit slides for WWDC 2014](SceneKit%20slides%20for%20WWDC%202014.md)


[Next](Scene%20Kit%20Session%20WWDC%202014-Sources-Slides-AAPLSlideChapter4.m.md)[Previous](Scene%20Kit%20Session%20WWDC%202014-Sources-Slides-AAPLSlideIntroduction.m.md)

# Scene Kit Session WWDC 2014/Sources/Slides/AAPLSlideChapter5.m

```objc
/*
 Copyright (C) 2014-2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Chapter 5 slide
 */


#import "AAPLPresentationViewController.h"
#import "AAPLSlideTextManager.h"
#import "AAPLSlide.h"

@interface AAPLSlideChapter5 : AAPLSlide
{
    SCNNode *footPrintNode;
}
@end

@implementation AAPLSlideChapter5

- (void)setupSlideWithPresentationViewController:(AAPLPresentationViewController *)presentationViewController
{
    [self.textManager setChapterTitle:@"Rendering"];
}

- (void) didOrderInWithPresentationViewController:(AAPLPresentationViewController *)presentationViewController
{

    //add footprint
    footPrintNode = [SCNNode node];

    SCNNode *presenter = [self.textManager addText:@"Aymeric Bard" atLevel:0];
    SCNNode *title = [self.textManager addFootPrint:@"Software Engineer"];
    SCNNode *footPrint = [self.textManager addFootPrint:@""];

    presenter.renderingOrder = 100;
    title.renderingOrder = 100;
    title.geometry.firstMaterial = footPrint.geometry.firstMaterial;
    presenter.geometry.firstMaterial.readsFromDepthBuffer = NO;
    title.geometry.firstMaterial.readsFromDepthBuffer = NO;

    presenter.position = SCNVector3Make(footPrint.position.x, footPrint.position.y+1.38, footPrint.position.z);
    title.position = SCNVector3Make(footPrint.position.x, footPrint.position.y+0.93, footPrint.position.z);

#define SCALE 0.007
    SCNVector3 scale = SCNVector3Make(SCALE, SCALE, SCALE);
    presenter.scale = scale;
    title.scale = scale;


    [footPrintNode addChildNode:presenter];
    [footPrintNode addChildNode:footPrint];
    [footPrintNode addChildNode:title];

    footPrintNode.opacity = 0;

    [presentationViewController.cameraNode addChildNode:footPrintNode];

    [SCNTransaction begin];
    [SCNTransaction setAnimationDuration:1.0];
    footPrintNode.opacity = 1.0;
    [SCNTransaction commit];
}

- (void) willOrderOutWithPresentationViewController:(AAPLPresentationViewController *)presentationViewController
{
    [footPrintNode removeFromParentNode];
}


@end
```

[Next](Scene%20Kit%20Session%20WWDC%202014-Sources-Slides-AAPLSlideChapter4.m.md)[Previous](Scene%20Kit%20Session%20WWDC%202014-Sources-Slides-AAPLSlideIntroduction.m.md)

