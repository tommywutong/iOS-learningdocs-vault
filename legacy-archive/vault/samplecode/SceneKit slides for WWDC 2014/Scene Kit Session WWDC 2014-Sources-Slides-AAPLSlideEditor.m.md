---
title: SceneKit slides for WWDC 2014
apple_id: TP40014551
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2014-10-16'
source_url: https://developer.apple.com/library/archive/samplecode/SceneKitWWDC2014/Listings/Scene_Kit_Session_WWDC_2014_Sources_Slides_AAPLSlideEditor_m.html
archived_at: '2026-07-18T03:23:16.352189Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [SceneKit slides for WWDC 2014](SceneKit%20slides%20for%20WWDC%202014.md)


[Next](Scene%20Kit%20Session%20WWDC%202014-Sources-Slides-AAPLSlideSpriteKitOverlays.m.md)[Previous](Scene%20Kit%20Session%20WWDC%202014-Sources-Slides-AAPLSlideGeometry.m.md)

# Scene Kit Session WWDC 2014/Sources/Slides/AAPLSlideEditor.m

```objc
/*
 Copyright (C) 2014-2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Presents the Xcode SceneKit editor.
 */

#import "AAPLPresentationViewController.h"
#import "AAPLSlideTextManager.h"
#import "AAPLSlide.h"
#import "Utils.h"

@interface AAPLSlideEditor : AAPLSlide
@end

@implementation AAPLSlideEditor

- (void)setupSlideWithPresentationViewController:(AAPLPresentationViewController *)presentationViewController {
    // Set the slide's title and add some text
    self.textManager.title = @"SceneKit Editor";
    [self.textManager addBullet:@"Built into Xcode" atLevel:0];
    [self.textManager addBullet:@"Scene graph inspection" atLevel:0];
    [self.textManager addBullet:@"Rendering preview" atLevel:0];
    [self.textManager addBullet:@"Adjust lighting and materials" atLevel:0];
}

- (void)didOrderInWithPresentationViewController:(AAPLPresentationViewController *)presentationViewController {
    // Bring up a screenshot of the editor
    SCNNode *editorScreenshotNode = [SCNNode asc_planeNodeWithImageNamed:@"editor.png" size:14 isLit:YES];
    editorScreenshotNode.position = SCNVector3Make(17, 4.1, 5);
    editorScreenshotNode.rotation = SCNVector4Make(0, 1, 0, -M_PI / 1.5);
    [self.groundNode addChildNode:editorScreenshotNode];

    // Animate it (rotate and move)
    [SCNTransaction begin];
    [SCNTransaction setAnimationDuration:1.0];
    {
        editorScreenshotNode.position = SCNVector3Make(7.5, 4.1, 5);
        editorScreenshotNode.rotation = SCNVector4Make(0, 1, 0, -M_PI / 6.0);
    }
    [SCNTransaction commit];
}

@end
```

[Next](Scene%20Kit%20Session%20WWDC%202014-Sources-Slides-AAPLSlideSpriteKitOverlays.m.md)[Previous](Scene%20Kit%20Session%20WWDC%202014-Sources-Slides-AAPLSlideGeometry.m.md)

