---
title: SceneKit's presentation for WWDC2013
apple_id: DTS40013423
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: SceneKit
published: '2014-01-07'
source_url: https://developer.apple.com/library/archive/samplecode/SceneKit_Slides_WWDC2013/Listings/Scene_Kit_Session_WWDC_2013_Sources_Slides_ASCSlideLoadingDAE_m.html
archived_at: '2026-07-18T03:23:23.385260Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [SceneKit's presentation for WWDC2013](Scene%20Kit%27s%20presentation%20for%20WWDC2013.md)


[Next](Scene%20Kit%20Session%20WWDC%202013-Sources-Slides-ASCSlideLOD.m.md)[Previous](Scene%20Kit%20Session%20WWDC%202013-Sources-Slides-ASCSlideLighting.m.md)

# Scene Kit Session WWDC 2013/Sources/Slides/ASCSlideLoadingDAE.m

```objc
/*
     File: ASCSlideLoadingDAE.m
 Abstract: Presents what dae documents are.
  Version: 1.1

 Disclaimer: IMPORTANT:  This Apple software is supplied to you by Apple
 Inc. ("Apple") in consideration of your agreement to the following
 terms, and your use, installation, modification or redistribution of
 this Apple software constitutes acceptance of these terms.  If you do
 not agree with these terms, please do not use, install, modify or
 redistribute this Apple software.

 In consideration of your agreement to abide by the following terms, and
 subject to these terms, Apple grants you a personal, non-exclusive
 license, under Apple's copyrights in this original Apple software (the
 "Apple Software"), to use, reproduce, modify and redistribute the Apple
 Software, with or without modifications, in source and/or binary forms;
 provided that if you redistribute the Apple Software in its entirety and
 without modifications, you must retain this notice and the following
 text and disclaimers in all such redistributions of the Apple Software.
 Neither the name, trademarks, service marks or logos of Apple Inc. may
 be used to endorse or promote products derived from the Apple Software
 without specific prior written permission from Apple.  Except as
 expressly stated in this notice, no other rights or licenses, express or
 implied, are granted by Apple herein, including but not limited to any
 patent rights that may be infringed by your derivative works or by other
 works in which the Apple Software may be incorporated.

 The Apple Software is provided by Apple on an "AS IS" basis.  APPLE
 MAKES NO WARRANTIES, EXPRESS OR IMPLIED, INCLUDING WITHOUT LIMITATION
 THE IMPLIED WARRANTIES OF NON-INFRINGEMENT, MERCHANTABILITY AND FITNESS
 FOR A PARTICULAR PURPOSE, REGARDING THE APPLE SOFTWARE OR ITS USE AND
 OPERATION ALONE OR IN COMBINATION WITH YOUR PRODUCTS.

 IN NO EVENT SHALL APPLE BE LIABLE FOR ANY SPECIAL, INDIRECT, INCIDENTAL
 OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
 SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
 INTERRUPTION) ARISING IN ANY WAY OUT OF THE USE, REPRODUCTION,
 MODIFICATION AND/OR DISTRIBUTION OF THE APPLE SOFTWARE, HOWEVER CAUSED
 AND WHETHER UNDER THEORY OF CONTRACT, TORT (INCLUDING NEGLIGENCE),
 STRICT LIABILITY OR OTHERWISE, EVEN IF APPLE HAS BEEN ADVISED OF THE
 POSSIBILITY OF SUCH DAMAGE.

 Copyright (C) 2014 Apple Inc. All Rights Reserved.

 */

#import "ASCPresentationViewController.h"
#import "ASCSlideTextManager.h"
#import "ASCSlide.h"
#import "Utils.h"

@interface ASCSlideLoadingDae : ASCSlide
@end

@implementation ASCSlideLoadingDae

- (void)setupSlideWithPresentationViewController:(ASCPresentationViewController *)presentationViewController {
    // Add some text
    self.textManager.title = @"Loading a 3D Scene";
    self.textManager.subtitle = @"DAE Documents";

    [self.textManager addBullet:@"Geometries" atLevel:0];
    [self.textManager addBullet:@"Animations" atLevel:0];
    [self.textManager addBullet:@"Textures" atLevel:0];
    [self.textManager addBullet:@"Lighting" atLevel:0];
    [self.textManager addBullet:@"Cameras" atLevel:0];
    [self.textManager addBullet:@"Skinning" atLevel:0];
    [self.textManager addBullet:@"Morphing" atLevel:0];

    // And an image resting on the ground
    SCNNode *imageNode = [SCNNode asc_planeNodeWithImageNamed:@"dae file icon" size:10 isLit:NO];
    imageNode.position = SCNVector3Make(6, 4.5, 1);
    [self.groundNode addChildNode:imageNode];
}

@end
```

[Next](Scene%20Kit%20Session%20WWDC%202013-Sources-Slides-ASCSlideLOD.m.md)[Previous](Scene%20Kit%20Session%20WWDC%202013-Sources-Slides-ASCSlideLighting.m.md)

