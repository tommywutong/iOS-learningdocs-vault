---
title: SceneKit slides for WWDC 2014
apple_id: TP40014551
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2014-10-16'
source_url: https://developer.apple.com/library/archive/samplecode/SceneKitWWDC2014/Listings/Scene_Kit_Session_WWDC_2014_Sources_Slides_AAPLSlideLight_m.html
archived_at: '2026-07-18T03:23:17.132299Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [SceneKit slides for WWDC 2014](SceneKit%20slides%20for%20WWDC%202014.md)


[Next](Scene%20Kit%20Session%20WWDC%202014-Sources-Slides-AAPLSlideAnimationOutline.m.md)[Previous](Scene%20Kit%20Session%20WWDC%202014-Sources-Slides-AAPLSlideDOF.m.md)

# Scene Kit Session WWDC 2014/Sources/Slides/AAPLSlideLight.m

```objc
/*
 Copyright (C) 2014-2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Illustrates the light attribute.
 */

#import "AAPLPresentationViewController.h"
#import "AAPLSlideTextManager.h"
#import "AAPLSlide.h"
#import "Utils.h"

@interface AAPLSlideLight : AAPLSlide
@end

@implementation AAPLSlideLight {
    SCNNode *_lightNode;
    SCNNode *_lightOffImageNode;
    SCNNode *_lightOnImageNode;
}

- (NSUInteger)numberOfSteps {
    return 2;
}

- (void)presentStepIndex:(NSUInteger)index withPresentationViewController:(AAPLPresentationViewController *)presentationViewController {
    [SCNTransaction begin];
    [SCNTransaction setAnimationDuration:0.0];

    switch (index) {
        case 0:
        {
            // Set the slide's title and subtitle and add some text
            self.textManager.title = @"Node Attributes";
            self.textManager.subtitle = @"SCNLights";

            [self.textManager addBullet:@"Four light types" atLevel:0];
            [self.textManager addBullet:@"Omni" atLevel:1];
            [self.textManager addBullet:@"Directional" atLevel:1];
            [self.textManager addBullet:@"Spot" atLevel:1];
            [self.textManager addBullet:@"Ambient" atLevel:1];

            // Add some code
            SCNNode *codeExampleNode = [self.textManager addCode:
                                        @"aNode.#light#       = [SCNLight light]; \n"
                                        @"aNode.light.color = [UIColor whiteColor];"];

            codeExampleNode.position = SCNVector3Make(12, 7, 1);

            // Add a light to the scene
            _lightNode = [SCNNode node];
            _lightNode.light = [SCNLight light];
            _lightNode.light.type = SCNLightTypeOmni;
            _lightNode.light.color = [NSColor blackColor]; // initially off
            _lightNode.light.attenuationStartDistance = 30;
            _lightNode.light.attenuationEndDistance = 40;
            _lightNode.position = SCNVector3Make(5, 3.5, 0);
            [self.contentNode addChildNode:_lightNode];

            // Load two images to help visualize the light (on and off)
            _lightOffImageNode = [SCNNode asc_planeNodeWithImageNamed:@"light-off" size:7 isLit:YES];
            _lightOnImageNode = [SCNNode asc_planeNodeWithImageNamed:@"light-on" size:7 isLit:YES];
            _lightOnImageNode.opacity = 0;
            _lightOnImageNode.castsShadow = NO;
            _lightOffImageNode.castsShadow = NO;

            [_lightNode addChildNode:_lightOnImageNode];
            [_lightNode addChildNode:_lightOffImageNode];
            break;
        }
        case 1:
        {
            // Switch the light on
            [SCNTransaction begin];
            [SCNTransaction setAnimationDuration:1.0];
            {
                _lightNode.light.color = [NSColor colorWithCalibratedRed:1 green:1 blue:0.8 alpha:1];
                _lightOnImageNode.opacity = 1.0;
                _lightOffImageNode.opacity = 0.0;
            }
            [SCNTransaction commit];
            break;
        }
    }
    [SCNTransaction commit];
}

- (void)willOrderOutWithPresentationViewController:(AAPLPresentationViewController *)presentationViewController {
    [SCNTransaction begin];
    {
        // Switch the light off
        _lightNode.light = nil;
    }
    [SCNTransaction commit];
}

@end
```

[Next](Scene%20Kit%20Session%20WWDC%202014-Sources-Slides-AAPLSlideAnimationOutline.m.md)[Previous](Scene%20Kit%20Session%20WWDC%202014-Sources-Slides-AAPLSlideDOF.m.md)

