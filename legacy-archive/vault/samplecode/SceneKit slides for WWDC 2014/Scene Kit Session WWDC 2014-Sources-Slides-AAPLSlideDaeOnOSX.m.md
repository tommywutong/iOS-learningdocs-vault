---
title: SceneKit slides for WWDC 2014
apple_id: TP40014551
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2014-10-16'
source_url: https://developer.apple.com/library/archive/samplecode/SceneKitWWDC2014/Listings/Scene_Kit_Session_WWDC_2014_Sources_Slides_AAPLSlideDaeOnOSX_m.html
archived_at: '2026-07-18T03:23:16.184296Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [SceneKit slides for WWDC 2014](SceneKit%20slides%20for%20WWDC%202014.md)


[Next](Scene%20Kit%20Session%20WWDC%202014-Sources-GLUtils.h.md)[Previous](Scene%20Kit%20Session%20WWDC%202014-Sources-Slides-AAPLSlideAllNew.m.md)

# Scene Kit Session WWDC 2014/Sources/Slides/AAPLSlideDaeOnOSX.m

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

@interface AAPLSlideDaeOnOSX : AAPLSlide
@end

@implementation AAPLSlideDaeOnOSX

- (void)setupSlideWithPresentationViewController:(AAPLPresentationViewController *)presentationViewController {
    // Slide's title and subtitle
    self.textManager.title = @"Working with DAE Files";
    self.textManager.subtitle = @"DAE files on OS X";

    // DAE icon
    SCNNode *daeIconNode = [SCNNode asc_planeNodeWithImageNamed:@"dae file icon" size:5 isLit:NO];
    daeIconNode.position = SCNVector3Make(0, 2.3, 0);
    [self.groundNode addChildNode:daeIconNode];

    // Preview icon and text
    SCNNode *previewIconNode = [SCNNode asc_planeNodeWithImageNamed:@"Preview.tiff" size:3 isLit:NO];
    previewIconNode.position = SCNVector3Make(-5, 1.3, 11);
    [self.groundNode addChildNode:previewIconNode];

    SCNNode *previewTextNode = [SCNNode asc_labelNodeWithString:@"Preview" size:AAPLLabelSizeSmall isLit:NO];
    previewTextNode.position = SCNVector3Make(-5.5, 0, 13);
    [self.groundNode addChildNode:previewTextNode];

    // Quicklook icon and text
    SCNNode *qlIconNode = [SCNNode asc_planeNodeWithImageNamed:@"Finder.tiff" size:3 isLit:NO];
    qlIconNode.position = SCNVector3Make(0, 1.3, 11);
    [self.groundNode addChildNode:qlIconNode];

    SCNNode *qlTextNode = [SCNNode asc_labelNodeWithString:@"QuickLook" size:AAPLLabelSizeSmall isLit:NO];
    qlTextNode.position = SCNVector3Make(-1.11, 0, 13);
    [self.groundNode addChildNode:qlTextNode];

    // Xcode icon and text
    SCNNode *xcodeIconNode = [SCNNode asc_planeNodeWithImageNamed:@"Xcode.tiff" size:3 isLit:NO];
    xcodeIconNode.position = SCNVector3Make(5, 1.3, 11);
    [self.groundNode addChildNode:xcodeIconNode];

    SCNNode *xcodeTextNode = [SCNNode asc_labelNodeWithString:@"Xcode" size:AAPLLabelSizeSmall isLit:NO];
    xcodeTextNode.position = SCNVector3Make(3.8, 0, 13);
    [self.groundNode addChildNode:xcodeTextNode];
}

@end
```

[Next](Scene%20Kit%20Session%20WWDC%202014-Sources-GLUtils.h.md)[Previous](Scene%20Kit%20Session%20WWDC%202014-Sources-Slides-AAPLSlideAllNew.m.md)

