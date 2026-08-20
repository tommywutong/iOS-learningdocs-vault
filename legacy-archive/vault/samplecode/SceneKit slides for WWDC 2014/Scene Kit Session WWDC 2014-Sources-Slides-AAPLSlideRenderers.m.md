---
title: SceneKit slides for WWDC 2014
apple_id: TP40014551
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2014-10-16'
source_url: https://developer.apple.com/library/archive/samplecode/SceneKitWWDC2014/Listings/Scene_Kit_Session_WWDC_2014_Sources_Slides_AAPLSlideRenderers_m.html
archived_at: '2026-07-18T03:23:18.269075Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [SceneKit slides for WWDC 2014](SceneKit%20slides%20for%20WWDC%202014.md)


[Next](Scene%20Kit%20Session%20WWDC%202014-Sources-Slides-AAPLSlideShaderModifiers.m.md)[Previous](Scene%20Kit%20Session%20WWDC%202014-Sources-Slides-AAPLSlideFog.m.md)

# Scene Kit Session WWDC 2014/Sources/Slides/AAPLSlideRenderers.m

```objc
/*
 Copyright (C) 2014-2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Presents the three possibilities that SceneKit offers to render a scene.
 */

#import "AAPLPresentationViewController.h"
#import "AAPLSlideTextManager.h"
#import "AAPLSlide.h"
#import "Utils.h"

@interface AAPLSlideRenderers : AAPLSlide
@end

@implementation AAPLSlideRenderers

- (void)setupSlideWithPresentationViewController:(AAPLPresentationViewController *)presentationViewController {
    self.textManager.title = @"Displaying the Scene";

    // Add labels
    SCNNode *node = [SCNNode asc_labelNodeWithString:@"SCNView" size:AAPLLabelSizeNormal isLit:NO];
    node.position = SCNVector3Make(-14, 8, 0);
    [self.contentNode addChildNode:node];

    node = [SCNNode asc_labelNodeWithString:@" SCNLayer\n(OS X only)" size:AAPLLabelSizeNormal isLit:NO];
    node.position = SCNVector3Make(-2.2, 7, 0);
    [self.contentNode addChildNode:node];

    node = [SCNNode asc_labelNodeWithString:@"SCNRenderer" size:AAPLLabelSizeNormal isLit:NO];
    node.position = SCNVector3Make(9.5, 8, 0);
    [self.contentNode addChildNode:node];

    // Add images - SCNView
    SCNNode* box = [SCNNode asc_planeNodeWithImageNamed:@"renderer-window" size:8 isLit:NO];
    box.position = SCNVector3Make(-10, 3, 5);
    [self.contentNode addChildNode:box];

    box = [SCNNode asc_planeNodeWithImageNamed:@"teapot" size:6 isLit:NO];
    box.position = SCNVector3Make(-10, 3, 5.1);
    [self.contentNode addChildNode:box];

    // Add images - SCNLayer
    box = [SCNNode asc_planeNodeWithImageNamed:@"renderer-layer" size:7.4 isLit:NO];
    box.position = SCNVector3Make(0, 3.5, 5);
    box.rotation = SCNVector4Make(0, 0, 1, M_PI / 20);
    [self.contentNode addChildNode:box];

    box = [SCNNode asc_planeNodeWithImageNamed:@"teapot" size:6 isLit:NO];
    box.position = SCNVector3Make(0, 3.5, 5.1);
    box.rotation = SCNVector4Make(0, 0, 1, M_PI / 20);
    [self.contentNode addChildNode:box];

    // Add images - SCNRenderer
    box = [SCNNode asc_planeNodeWithImageNamed:@"renderer-framebuffer" size:8 isLit:NO];
    box.position = SCNVector3Make(10, 3.2, 5);
    [self.contentNode addChildNode:box];

    box = [SCNNode asc_planeNodeWithImageNamed:@"teapot" size:6 isLit:NO];
    box.position = SCNVector3Make(10, 3, 5.1);
    [self.contentNode addChildNode:box];
}

@end
```

[Next](Scene%20Kit%20Session%20WWDC%202014-Sources-Slides-AAPLSlideShaderModifiers.m.md)[Previous](Scene%20Kit%20Session%20WWDC%202014-Sources-Slides-AAPLSlideFog.m.md)

