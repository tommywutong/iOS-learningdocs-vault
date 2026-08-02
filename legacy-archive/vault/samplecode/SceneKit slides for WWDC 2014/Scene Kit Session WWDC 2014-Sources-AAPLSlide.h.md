---
title: SceneKit slides for WWDC 2014
apple_id: TP40014551
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2014-10-16'
source_url: https://developer.apple.com/library/archive/samplecode/SceneKitWWDC2014/Listings/Scene_Kit_Session_WWDC_2014_Sources_AAPLSlide_h.html
archived_at: '2026-07-18T03:23:14.571097Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [SceneKit slides for WWDC 2014](SceneKit%20slides%20for%20WWDC%202014.md)


[Next](Scene%20Kit%20Session%20WWDC%202014-Sources-Slides-AAPLSlideAssetsCollection.m.md)[Previous](Scene%20Kit%20Session%20WWDC%202014-Sources-AAPLSlide.m.md)

# Scene Kit Session WWDC 2014/Sources/AAPLSlide.h

```objc
/*
 Copyright (C) 2014-2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 The AAPLSlide class represents a slide. A slide owns a node tree, some properties and a text manager.
 */

#import <SceneKit/SceneKit.h>

@class AAPLPresentationViewController, AAPLSlideTextManager;
@interface AAPLSlide : NSObject

#pragma mark - Accessing to specific places in the slide

@property (readonly) SCNNode *contentNode; // Top level node of the slide
@property (readonly) SCNNode *groundNode; // A node positioned on the floor

#pragma mark - Managing text inside the slide

@property (readonly) AAPLSlideTextManager *textManager;

#pragma mark - Navigating within the slide

- (NSUInteger)numberOfSteps;
- (void)presentStepIndex:(NSUInteger)index withPresentationViewController:(AAPLPresentationViewController *)presentationViewController;
- (void)setupSlideWithPresentationViewController:(AAPLPresentationViewController *)presentationViewController;
- (void)willOrderOutWithPresentationViewController:(AAPLPresentationViewController *)presentationViewController;
- (void)didOrderInWithPresentationViewController:(AAPLPresentationViewController *)presentationViewController;

#pragma mark - Lighting the scene

@property (copy) NSArray *lightIntensities;
@property SCNVector3 mainLightPosition;

#pragma mark - Customizing the floor

@property (strong) SCNMaterial *floorWarmupMaterial; // used to retain a material to prevent it from being released before the slide is presented. This used for preloading and caching.
@property (copy) NSString *floorImageName;
@property CGFloat floorReflectivity;
@property CGFloat floorFalloff;

#pragma mark - Managing transitions

@property CGFloat transitionDuration;
@property CGFloat transitionOffsetX;
@property CGFloat transitionOffsetZ;
@property CGFloat transitionRotation;

#pragma mark - Placing the slide

@property CGFloat altitude;
@property CGFloat pitch;

#pragma mark - Diplaying the 'New' badge

@property BOOL isNewIn10_10;

@end
```

[Next](Scene%20Kit%20Session%20WWDC%202014-Sources-Slides-AAPLSlideAssetsCollection.m.md)[Previous](Scene%20Kit%20Session%20WWDC%202014-Sources-AAPLSlide.m.md)

