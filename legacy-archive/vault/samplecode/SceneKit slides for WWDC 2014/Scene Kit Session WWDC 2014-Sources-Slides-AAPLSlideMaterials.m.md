---
title: SceneKit slides for WWDC 2014
apple_id: TP40014551
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2014-10-16'
source_url: https://developer.apple.com/library/archive/samplecode/SceneKitWWDC2014/Listings/Scene_Kit_Session_WWDC_2014_Sources_Slides_AAPLSlideMaterials_m.html
archived_at: '2026-07-18T03:23:17.519871Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [SceneKit slides for WWDC 2014](SceneKit%20slides%20for%20WWDC%202014.md)


[Next](Scene%20Kit%20Session%20WWDC%202014-Sources-Slides-AAPLSlideScenegraph.m.md)[Previous](Scene%20Kit%20Session%20WWDC%202014-Sources-Slides-AAPLSlideCamera.m.md)

# Scene Kit Session WWDC 2014/Sources/Slides/AAPLSlideMaterials.m

```objc
/*
 Copyright (C) 2014-2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Explains what a material is.
 */

#import "AAPLPresentationViewController.h"
#import "AAPLSlideTextManager.h"
#import "AAPLSlideSceneGraph.h"
#import "Utils.h"

@interface AAPLSlideMaterials: AAPLSlide
@end

@implementation AAPLSlideMaterials {
    SCNNode *_sceneKitDiagramNode;
}

- (void)setupSlideWithPresentationViewController:(AAPLPresentationViewController *)presentationViewController {
    // Add some text
    self.textManager.title = @"Materials";

    [self.textManager addBullet:@"Determines the appearance of the geometry" atLevel:0];
    [self.textManager addBullet:@"SCNMaterial" atLevel:0];
    [self.textManager addBullet:@"Material properties" atLevel:0];
    [self.textManager addBullet:@"SCNMaterialProperty" atLevel:1];
    [self.textManager addBullet:@"Contents is a color or an image" atLevel:1];

    // Prepare the diagram but hide it for now
    _sceneKitDiagramNode = [AAPLSlideSceneGraph sharedScenegraphDiagramNode];
    [AAPLSlideSceneGraph scenegraphDiagramGoToStep:0];

    _sceneKitDiagramNode.position = SCNVector3Make(3.0, 8.0, 0);
    _sceneKitDiagramNode.opacity = 0.0;

    [self.contentNode addChildNode:_sceneKitDiagramNode];
}

- (void)didOrderInWithPresentationViewController:(AAPLPresentationViewController *)presentationViewController {
    // Reveal and animate
    [SCNTransaction begin];
    [SCNTransaction setAnimationDuration:1.0];
    {
        [AAPLSlideSceneGraph scenegraphDiagramGoToStep:5];
        _sceneKitDiagramNode.opacity = 1.0;
    }
    [SCNTransaction commit];
}

@end
```

[Next](Scene%20Kit%20Session%20WWDC%202014-Sources-Slides-AAPLSlideScenegraph.m.md)[Previous](Scene%20Kit%20Session%20WWDC%202014-Sources-Slides-AAPLSlideCamera.m.md)

