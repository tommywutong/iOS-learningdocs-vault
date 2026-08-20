---
title: SceneKit Vehicle Demo
apple_id: TP40014549
resource_type: Sample Code
platform: iOS
topic: null
technology: SceneKit
published: '2014-09-17'
source_url: https://developer.apple.com/library/archive/samplecode/SceneKitVehicle/Listings/SceneKitVehicle_AAPLGameView_m.html
archived_at: '2026-07-18T03:23:13.140111Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [SceneKit Vehicle Demo](SceneKit%20Vehicle%20Demo.md)


[Next](Document%20Revision%20History.md)[Previous](SceneKitVehicle-AAPLOverlayScene.m.md)

# SceneKitVehicle/AAPLGameView.m

```objc
/*
 Copyright (C) 2014 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 */

#import <SpriteKit/SpriteKit.h>
#import "AAPLGameView.h"

@implementation AAPLGameView

- (void)changePointOfView
{
    // retrieve the list of point of views
    NSArray *pointOfViews = [self.scene.rootNode childNodesPassingTest:^BOOL(SCNNode *child, BOOL *stop) {
        return child.camera != nil;
    }];

    SCNNode *currentPointOfView = self.pointOfView;

    // select the next one
    NSUInteger index = [pointOfViews indexOfObject:currentPointOfView];
    index++;
    if (index >= [pointOfViews count]) index = 0;

    self.inCarView = (index==0);

    // set it with an implicit transaction
    [SCNTransaction begin];
    [SCNTransaction setAnimationDuration:0.75];
    self.pointOfView = [pointOfViews objectAtIndex:index];
    [SCNTransaction commit];
}

- (void)touchesBegan:(NSSet *)touches withEvent:(UIEvent *)event
{
    UITouch *touch = [touches anyObject];

    //test if we hit the camera button
    SKScene *scene = self.overlaySKScene;
    CGPoint p = [touch locationInView:self];
    p = [scene convertPointFromView:p];
    SKNode *node = [scene nodeAtPoint:p];

    if ([node.name isEqualToString:@"camera"]) {
        //play a sound
        [node runAction:[SKAction playSoundFileNamed:@"click.caf" waitForCompletion:NO]];

        //change the point of view
        [self changePointOfView];
        return;
    }

    //update the total number of touches on screen
    NSSet *allTouches = [event allTouches];
    _touchCount = [allTouches count];
}

- (void)touchesEnded:(NSSet *)touches withEvent:(UIEvent *)event
{
    _touchCount = 0;
}

@end
```

[Next](Document%20Revision%20History.md)[Previous](SceneKitVehicle-AAPLOverlayScene.m.md)

