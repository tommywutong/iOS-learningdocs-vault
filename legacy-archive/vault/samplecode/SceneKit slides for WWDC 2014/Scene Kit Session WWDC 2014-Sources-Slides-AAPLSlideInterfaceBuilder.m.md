---
title: SceneKit slides for WWDC 2014
apple_id: TP40014551
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2014-10-16'
source_url: https://developer.apple.com/library/archive/samplecode/SceneKitWWDC2014/Listings/Scene_Kit_Session_WWDC_2014_Sources_Slides_AAPLSlideInterfaceBuilder_m.html
archived_at: '2026-07-18T03:23:16.826347Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [SceneKit slides for WWDC 2014](SceneKit%20slides%20for%20WWDC%202014.md)


[Next](Scene%20Kit%20Session%20WWDC%202014-Sources-Slides-AAPLSlideLOD.m.md)[Previous](Scene%20Kit%20Session%20WWDC%202014-Sources-Slides-AAPLSlideParticles.m.md)

# Scene Kit Session WWDC 2014/Sources/Slides/AAPLSlideInterfaceBuilder.m

```objc
/*
 Copyright (C) 2014-2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Explains how to use SCNView within Interface Builder.
 */

#import "AAPLPresentationViewController.h"
#import "AAPLSlideTextManager.h"
#import "AAPLSlide.h"
#import "Utils.h"

@interface AAPLSlideInterfaceBuilder : AAPLSlide
@end

@implementation AAPLSlideInterfaceBuilder

- (void)setupSlideWithPresentationViewController:(AAPLPresentationViewController *)presentationViewController {
    // Add some text
    self.textManager.title = @"Displaying the Scene";
    self.textManager.subtitle = @"Game template";

    [self.textManager addBullet:@"Start with the Xcode game template" atLevel:0];
    [self.textManager addBullet:@"Or drag an SCNView from the library" atLevel:0];

    // And an image
    SCNNode *imageNode = [SCNNode asc_planeNodeWithImageNamed:@"Interface Builder" size:8.3 isLit:NO];
    imageNode.position = SCNVector3Make(-4.0, 3.2, 11.0);
    [self.contentNode addChildNode:imageNode];

    imageNode = [SCNNode asc_planeNodeWithImageNamed:@"game_big" size:7 isLit:NO];
    imageNode.position = SCNVector3Make(5.0, 3.5, 11.0);
    imageNode.geometry.firstMaterial.diffuse.magnificationFilter = SCNFilterModeNearest;
    [self.contentNode addChildNode:imageNode];
}

@end
```

[Next](Scene%20Kit%20Session%20WWDC%202014-Sources-Slides-AAPLSlideLOD.m.md)[Previous](Scene%20Kit%20Session%20WWDC%202014-Sources-Slides-AAPLSlideParticles.m.md)

