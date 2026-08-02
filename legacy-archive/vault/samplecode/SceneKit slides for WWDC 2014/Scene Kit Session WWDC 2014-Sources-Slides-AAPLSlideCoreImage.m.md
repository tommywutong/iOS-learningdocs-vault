---
title: SceneKit slides for WWDC 2014
apple_id: TP40014551
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2014-10-16'
source_url: https://developer.apple.com/library/archive/samplecode/SceneKitWWDC2014/Listings/Scene_Kit_Session_WWDC_2014_Sources_Slides_AAPLSlideCoreImage_m.html
archived_at: '2026-07-18T03:23:15.686508Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [SceneKit slides for WWDC 2014](SceneKit%20slides%20for%20WWDC%202014.md)


[Next](Scene%20Kit%20Session%20WWDC%202014-Sources-Slides-AAPLSlideCreatingGeometries.m.md)[Previous](Scene%20Kit%20Session%20WWDC%202014-Sources-Slides-AAPLSlideParticleEditor.m.md)

# Scene Kit Session WWDC 2014/Sources/Slides/AAPLSlideCoreImage.m

```objc
/*
 Copyright (C) 2014-2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Shows an example of how Core Image filters can be used to achieve screen-space effects.
 */

#import <GLKit/GLKMath.h>

#import "AAPLPresentationViewController.h"
#import "AAPLSlideTextManager.h"
#import "AAPLSlide.h"
#import "Utils.h"

#pragma mark - Core Image slide

@interface AAPLSlideCoreImage : AAPLSlide
@end

@implementation AAPLSlideCoreImage {
    CGSize _viewportSize;
}

- (void)setupSlideWithPresentationViewController:(AAPLPresentationViewController *)presentationViewController {
    // Setup the image grid here to benefit from the preloading mechanism
    _viewportSize = [presentationViewController.presentationView convertSizeToBacking:presentationViewController.presentationView.frame.size];
}

- (NSUInteger)numberOfSteps {
    return 1;
}

- (void)didOrderInWithPresentationViewController:(AAPLPresentationViewController *)presentationViewController {
    SCNNode *banana = [self.contentNode asc_addChildNodeNamed:@"banana" fromSceneNamed:@"Scenes.scnassets/banana/banana" withScale:5];

    [banana runAction:[SCNAction repeatActionForever:[SCNAction rotateByX:0 y:M_PI*2 z:0 duration:1.5]]];
    banana.position = SCNVector3Make(2.5, 5, 10);
    CIFilter *filter = [CIFilter filterWithName:@"CIGaussianBlur"];
    [filter setDefaults];
    [filter setValue:@10 forKey:kCIInputRadiusKey];
    banana.filters = @[filter];

    banana = [banana copy];
    [self.contentNode addChildNode:banana];
    banana.position = SCNVector3Make(6, 5, 10);
    filter = [CIFilter filterWithName:@"CIPixellate"];
    [filter setDefaults];
    banana.filters = @[filter];


    banana = [banana copy];
    [self.contentNode addChildNode:banana];
    banana.position = SCNVector3Make(9.5, 5, 10);
    filter = [CIFilter filterWithName:@"CIEdgeWork"];
    [filter setDefaults];
    banana.filters = @[filter];
}

- (void)presentStepIndex:(NSUInteger)index withPresentationViewController:(AAPLPresentationViewController *)presentationViewController {
    switch (index) {
        case 0:
            // Set the slide's title and subtitle and add some text
            self.textManager.title = @"Core Image";
            self.textManager.subtitle = @"CI Filters";

            [self.textManager addBullet:@"Screen-space effects" atLevel:0];
            [self.textManager addBullet:@"Applies to a node hierarchy" atLevel:0];
            [self.textManager addBullet:@"Filter parameters are animatable" atLevel:0];
            [self.textManager addCode:@"aNode.#filters# = @[filter1, filter2];"];
            break;
    }
}

@end
```

[Next](Scene%20Kit%20Session%20WWDC%202014-Sources-Slides-AAPLSlideCreatingGeometries.m.md)[Previous](Scene%20Kit%20Session%20WWDC%202014-Sources-Slides-AAPLSlideParticleEditor.m.md)

