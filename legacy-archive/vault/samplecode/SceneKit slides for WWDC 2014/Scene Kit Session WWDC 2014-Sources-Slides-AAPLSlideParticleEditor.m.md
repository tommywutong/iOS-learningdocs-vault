---
title: SceneKit slides for WWDC 2014
apple_id: TP40014551
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2014-10-16'
source_url: https://developer.apple.com/library/archive/samplecode/SceneKitWWDC2014/Listings/Scene_Kit_Session_WWDC_2014_Sources_Slides_AAPLSlideParticleEditor_m.html
archived_at: '2026-07-18T03:23:17.732603Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [SceneKit slides for WWDC 2014](SceneKit%20slides%20for%20WWDC%202014.md)


[Next](Scene%20Kit%20Session%20WWDC%202014-Sources-Slides-AAPLSlideCoreImage.m.md)[Previous](Scene%20Kit%20Session%20WWDC%202014-Sources-Slides-AAPLSlideChapter4.m.md)

# Scene Kit Session WWDC 2014/Sources/Slides/AAPLSlideParticleEditor.m

```objc

#import "AAPLPresentationViewController.h"
#import "AAPLSlideTextManager.h"
#import "AAPLSlide.h"
#import "Utils.h"

@interface AAPLSlideParticleEditor : AAPLSlide
@end

@implementation AAPLSlideParticleEditor

- (void)setupSlideWithPresentationViewController:(AAPLPresentationViewController *)presentationViewController {
    // Add some text
    self.textManager.title = @"3D Particle Editor";

    [self.textManager addBullet:@"Integrated into Xcode" atLevel:0];
    [self.textManager addBullet:@"Edit .scnp files" atLevel:0];
    [self.textManager addBullet:@"Particle templates available" atLevel:0];
}


- (void)didOrderInWithPresentationViewController:(AAPLPresentationViewController *)presentationViewController {
    // Bring up a screenshot of the editor
    SCNNode *editorScreenshotNode = [SCNNode asc_planeNodeWithImageNamed:@"particleEditor" size:14 isLit:YES];
    editorScreenshotNode.geometry.firstMaterial.diffuse.mipFilter = SCNFilterModeLinear;
    editorScreenshotNode.position = SCNVector3Make(17, 3.8, 5);
    editorScreenshotNode.rotation = SCNVector4Make(0, 1, 0, -M_PI / 1.5);
    [self.groundNode addChildNode:editorScreenshotNode];

    // Animate it (rotate and move)
    [SCNTransaction begin];
    [SCNTransaction setAnimationDuration:1.0];
    {
        editorScreenshotNode.position = SCNVector3Make(7, 3.8, 5);
        editorScreenshotNode.rotation = SCNVector4Make(0, 1, 0, -M_PI / 7.0);
    }
    [SCNTransaction commit];
}


@end
```

[Next](Scene%20Kit%20Session%20WWDC%202014-Sources-Slides-AAPLSlideCoreImage.m.md)[Previous](Scene%20Kit%20Session%20WWDC%202014-Sources-Slides-AAPLSlideChapter4.m.md)

