---
title: SceneKit slides for WWDC 2014
apple_id: TP40014551
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2014-10-16'
source_url: https://developer.apple.com/library/archive/samplecode/SceneKitWWDC2014/Listings/Scene_Kit_Session_WWDC_2014_Sources_AAPLPresentationViewController_h.html
archived_at: '2026-07-18T03:23:14.085096Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [SceneKit slides for WWDC 2014](SceneKit%20slides%20for%20WWDC%202014.md)


[Next](Scene%20Kit%20Session%20WWDC%202014-Sources-GLUtils.m.md)[Previous](Scene%20Kit%20Session%20WWDC%202014-Sources-AAPLPresentationViewController.m.md)

# Scene Kit Session WWDC 2014/Sources/AAPLPresentationViewController.h

```objc
/*
 Copyright (C) 2014-2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 AAPLPresentationViewController controls the presentation, including ordering the slides in and out, updating the position of the camera, the light intensites and more.
 */

#import <SceneKit/SceneKit.h>

@class AAPLSlide;
@protocol AAPLPresentationDelegate;

@interface AAPLPresentationViewController : NSViewController

@property (weak) id <AAPLPresentationDelegate> delegate;

// Main view
- (SCNView *) presentationView;

- (id)initWithContentsOfFile:(NSString *)path;
- (void)applicationDidFinishLaunching;

// Presentation outline
- (NSInteger)numberOfSlides;
- (Class)classOfSlideAtIndex:(NSInteger)slideIndex;

// Navigation within the presentation
- (void)goToNextSlideStep;
- (void)goToPreviousSlide;
- (void)goToSlideAtIndex:(NSInteger)slideIndex;

// Nodes used to control the position and orientation of the main camera
@property (readonly) SCNNode *cameraHandle;
@property (readonly) SCNNode *cameraPitch; // child of 'cameraHandle'
@property (readonly) SCNNode *cameraNode;  // child of 'cameraPitch'

// Scene decorations
@property (nonatomic) BOOL showsNewInSceneKitBadge;

// Lighting the scene
- (void)updateLightingWithIntensities:(NSArray *)intensities; //[ omni, front, top spot, left, right, ambient]
- (void)narrowSpotlight:(BOOL)narrow;
- (void)riseMainLight:(BOOL)rise;

// Nodes used to control the lighting
- (SCNNode *)spotLight;
- (SCNNode *)mainLight;

// actions
- (IBAction) exportSlidesToImages:(id) sender;
- (IBAction) exportSlidesToSCN:(id) sender;
- (IBAction) autoPlay:(id) sender;

@end

@protocol AAPLPresentationDelegate <NSObject>
@optional

- (void)presentationViewController:(AAPLPresentationViewController *)presentationViewController willPresentSlideAtIndex:(NSUInteger)slideIndex step:(NSUInteger)step;

@end
```

[Next](Scene%20Kit%20Session%20WWDC%202014-Sources-GLUtils.m.md)[Previous](Scene%20Kit%20Session%20WWDC%202014-Sources-AAPLPresentationViewController.m.md)

