---
title: SceneKit slides for WWDC 2014
apple_id: TP40014551
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2014-10-16'
source_url: https://developer.apple.com/library/archive/samplecode/SceneKitWWDC2014/Listings/Scene_Kit_Session_WWDC_2014_Sources_Slides_AAPLSlideFlattening_m.html
archived_at: '2026-07-18T03:23:16.503573Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [SceneKit slides for WWDC 2014](SceneKit%20slides%20for%20WWDC%202014.md)


[Next](Scene%20Kit%20Session%20WWDC%202014-Sources-Slides-AAPLSlidePhysics.m.md)[Previous](Scene%20Kit%20Session%20WWDC%202014-Sources-Slides-AAPLSlideTechniques.m.md)

# Scene Kit Session WWDC 2014/Sources/Slides/AAPLSlideFlattening.m

```objc
/*
 <codex>
 <abstract>Explains how flattening nodes can help with performance.</abstract>
 </codex>
 */

#import "AAPLPresentationViewController.h"
#import "AAPLSlideTextManager.h"
#import "AAPLSlide.h"
#import "Utils.h"

@interface AAPLSlideFlattening : AAPLSlide
@end

@implementation AAPLSlideFlattening

- (NSUInteger)numberOfSteps {
    return 2;
}

- (void)presentStepIndex:(NSUInteger)index withPresentationViewController:(AAPLPresentationViewController *)presentationViewController {
    switch (index) {
        case 0:
        {
            // Set the slide's title and subtitle and add some text.
            self.textManager.title = @"Performance";
            self.textManager.subtitle = @"Flattening";

            [self.textManager addBullet:@"Flatten node tree into single node" atLevel:0];
            [self.textManager addBullet:@"Minimize draw calls" atLevel:0];

            [self.textManager addCode:
             @"// Flatten node hierarchy \n"
             @"SCNNode *flattenedNode = [aNode #flattenedClone#];"];

            break;
        }
        case 1:
        {
            // Discard the text and show a 2D image.
            // Animate the image's position when it appears.

            [self.textManager flipOutTextOfType:AAPLTextTypeCode];
            [self.textManager flipOutTextOfType:AAPLTextTypeBullet];

            SCNNode *imageNode = [SCNNode asc_planeNodeWithImageNamed:@"flattening" size:20 isLit:NO];
            imageNode.position = SCNVector3Make(0, 4.8, 16);
            [self.groundNode addChildNode:imageNode];

            [SCNTransaction begin];
            [SCNTransaction setAnimationDuration:1.0];
            {
                imageNode.position = SCNVector3Make(0, 4.8, 8);
            }
            [SCNTransaction commit];
        }
    }
}

@end
```

[Next](Scene%20Kit%20Session%20WWDC%202014-Sources-Slides-AAPLSlidePhysics.m.md)[Previous](Scene%20Kit%20Session%20WWDC%202014-Sources-Slides-AAPLSlideTechniques.m.md)

