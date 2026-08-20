---
title: SceneKit slides for WWDC 2014
apple_id: TP40014551
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2014-10-16'
source_url: https://developer.apple.com/library/archive/samplecode/SceneKitWWDC2014/Listings/Scene_Kit_Session_WWDC_2014_Sources_AAPLSlide_m.html
archived_at: '2026-07-18T03:23:14.612610Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [SceneKit slides for WWDC 2014](SceneKit%20slides%20for%20WWDC%202014.md)


[Next](Scene%20Kit%20Session%20WWDC%202014-Sources-AAPLSlide.h.md)[Previous](README.md.md)

# Scene Kit Session WWDC 2014/Sources/AAPLSlide.m

```objc
/*
 Copyright (C) 2014-2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 The AAPLSlide class represents a slide. A slide owns a node tree, some properties and a text manager.
 */

#import "AAPLSlide.h"
#import "AAPLSlideTextManager.h"

@implementation AAPLSlide

- (id)init {
    if ((self = [super init])) {
        // Node hierarchy :
        // _contentNode
        // |__ _groundNode           : holds the rest of the scene
        // |__ _textManager.textNode : holds the text

        _contentNode = [SCNNode node];

        _groundNode = [SCNNode node];
        [_contentNode addChildNode:_groundNode];

        _textManager = [[AAPLSlideTextManager alloc] init];
        [_contentNode addChildNode:_textManager.textNode];

        // Default parameters
        _lightIntensities = @[@0.0, @0.9, @0.7];
        _mainLightPosition = SCNVector3Make(0, 3, -13);
        _floorImageName = nil;
        _floorReflectivity = 0.25;
        _floorFalloff = 3.0;
        _transitionDuration = 1.0;
        _transitionOffsetX = 0.0;
        _transitionOffsetZ = 0.0;
        _transitionRotation = 0.0;
        _altitude = 5.0;
        _pitch = 0.0;
        _isNewIn10_10 = NO;
    }
    return self;
}

#pragma mark - Navigating within the slide

- (NSUInteger)numberOfSteps {
    return 0;
}

- (void)presentStepIndex:(NSUInteger)index withPresentationViewController:(AAPLPresentationViewController *)presentationViewController {
}

- (void)setupSlideWithPresentationViewController:(AAPLPresentationViewController *)presentationViewController {
}

- (void)willOrderOutWithPresentationViewController:(AAPLPresentationViewController *)presentationViewController {
}

- (void)didOrderInWithPresentationViewController:(AAPLPresentationViewController *)presentationViewController {
}


@end
```

[Next](Scene%20Kit%20Session%20WWDC%202014-Sources-AAPLSlide.h.md)[Previous](README.md.md)

