---
title: SceneKit slides for WWDC 2014
apple_id: TP40014551
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2014-10-16'
source_url: https://developer.apple.com/library/archive/samplecode/SceneKitWWDC2014/Listings/Scene_Kit_Session_WWDC_2014_Sources_Slides_AAPLSlideSpriteKitOverlays_m.html
archived_at: '2026-07-18T03:23:18.868763Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [SceneKit slides for WWDC 2014](SceneKit%20slides%20for%20WWDC%202014.md)


[Next](Scene%20Kit%20Session%20WWDC%202014-Sources-Slides-AAPLSlideCreateAScene2.m.md)[Previous](Scene%20Kit%20Session%20WWDC%202014-Sources-Slides-AAPLSlideEditor.m.md)

# Scene Kit Session WWDC 2014/Sources/Slides/AAPLSlideSpriteKitOverlays.m

```objc

#import "AAPLPresentationViewController.h"
#import "AAPLSlideTextManager.h"
#import "AAPLSlide.h"
#import "Utils.h"

@interface AAPLSlideSpriteKitOverlays : AAPLSlide
@end

@implementation AAPLSlideSpriteKitOverlays

- (void)setupSlideWithPresentationViewController:(AAPLPresentationViewController *)presentationViewController {
    self.textManager.title = @"SpriteKit Overlays";

    [self.textManager addBullet:@"Game score, gauges, time, menus..." atLevel:0];
    [self.textManager addBullet:@"Event handling" atLevel:0];
    SCNNode *node = [self.textManager addCode:@"scnView.#overlaySKScene# = aSKScene;"];
    node.position = SCNVector3Make(9, 0.7, 0);

    SCNNode *gameLoop = [SCNNode asc_planeNodeWithImageNamed:@"overlays" size:10 isLit:NO];
    gameLoop.position = SCNVector3Make(0, 2.9, 13);
    [self.groundNode addChildNode:gameLoop];
}

- (NSUInteger)numberOfSteps
{
    return 2;
}

- (void)presentStepIndex:(NSUInteger)index withPresentationViewController:(AAPLPresentationViewController *)presentationViewController
{
    switch(index){
        case 0:
            break;
        case 1:
            [self.textManager flipOutTextOfType:AAPLTextTypeBullet];
            [self.textManager addEmptyLine];
            [self.textManager addBullet:@"Portability" atLevel:0];
            [self.textManager addBullet:@"Performance" atLevel:0];
            [self.textManager flipInTextOfType:AAPLTextTypeBullet];
            break;
    }
}

@end
```

[Next](Scene%20Kit%20Session%20WWDC%202014-Sources-Slides-AAPLSlideCreateAScene2.m.md)[Previous](Scene%20Kit%20Session%20WWDC%202014-Sources-Slides-AAPLSlideEditor.m.md)

