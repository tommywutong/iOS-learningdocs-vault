---
title: SceneKit slides for WWDC 2014
apple_id: TP40014551
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2014-10-16'
source_url: https://developer.apple.com/library/archive/samplecode/SceneKitWWDC2014/Listings/Scene_Kit_Session_WWDC_2014_Sources_Slides_AAPLSlideAssetsCollection_m.html
archived_at: '2026-07-18T03:23:15.083722Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [SceneKit slides for WWDC 2014](SceneKit%20slides%20for%20WWDC%202014.md)


[Next](Scene%20Kit%20Session%20WWDC%202014-Sources-Slides-AAPLSlideIntroduction.m.md)[Previous](Scene%20Kit%20Session%20WWDC%202014-Sources-AAPLSlide.h.md)

# Scene Kit Session WWDC 2014/Sources/Slides/AAPLSlideAssetsCollection.m

```objc
/*
 Copyright (C) 2014-2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Presents how dae files are supported on OS X.
 */

#import "AAPLPresentationViewController.h"
#import "AAPLSlideTextManager.h"
#import "AAPLSlide.h"
#import "Utils.h"

@interface AAPLSlideAssetsCollection : AAPLSlide
@end

@implementation AAPLSlideAssetsCollection

- (void)setupSlideWithPresentationViewController:(AAPLPresentationViewController *)presentationViewController {
    // Slide's title and subtitle
    self.textManager.title = @"Assets Catalog";
    self.textManager.subtitle = @".scnassets folders";

    [self.textManager addBullet:@"Manage your assets" atLevel:0];
    [self.textManager addBullet:@"Add DAE files and referenced textures" atLevel:0];
    [self.textManager addBullet:@"Optimized at build time" atLevel:0];
    [self.textManager addBullet:@"Compilation options" atLevel:0];
    [self.textManager addBullet:@"Geometry interleaving" atLevel:1];
    [self.textManager addBullet:@"PVRTC, Up axis" atLevel:1];

    SCNNode *intermediateNode = [SCNNode node];
    intermediateNode.position = SCNVector3Make(0, 0, 7);
    [self.groundNode addChildNode:intermediateNode];

    // Load the "folder" model
    SCNNode *folder = [intermediateNode asc_addChildNodeNamed:@"folder" fromSceneNamed:@"Scenes.scnassets/assetCatalog/assetCatalog" withScale:8];
    folder.position = SCNVector3Make(5, 0, 2);
    folder.rotation = SCNVector4Make(0, 1, 0, -M_PI_4*0.9);


}

@end
```

[Next](Scene%20Kit%20Session%20WWDC%202014-Sources-Slides-AAPLSlideIntroduction.m.md)[Previous](Scene%20Kit%20Session%20WWDC%202014-Sources-AAPLSlide.h.md)

