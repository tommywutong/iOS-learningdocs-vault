---
title: SceneKit slides for WWDC 2014
apple_id: TP40014551
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2014-10-16'
source_url: https://developer.apple.com/library/archive/samplecode/SceneKitWWDC2014/Listings/Scene_Kit_Session_WWDC_2014_Sources_Slides_AAPLSlideManipulation_m.html
archived_at: '2026-07-18T03:23:17.335791Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [SceneKit slides for WWDC 2014](SceneKit%20slides%20for%20WWDC%202014.md)


[Next](Scene%20Kit%20Session%20WWDC%202014-Sources-Slides-AAPLSlideCloning.m.md)[Previous](Scene%20Kit%20Session%20WWDC%202014-Sources-Slides-AAPLSlideCustomProgram.m.md)

# Scene Kit Session WWDC 2014/Sources/Slides/AAPLSlideManipulation.m

```objc

#import "AAPLPresentationViewController.h"
#import "AAPLSlideTextManager.h"
#import "AAPLSlide.h"
#import "Utils.h"

@interface AAPLSlideManipulation : AAPLSlide
@end

@implementation AAPLSlideManipulation

- (void)setupSlideWithPresentationViewController:(AAPLPresentationViewController *)presentationViewController {
    self.textManager.title = @"Per-Frame Updates";
    self.textManager.subtitle = @"Game loop";

    SCNNode *gameLoop = [SCNNode asc_planeNodeWithImageNamed:@"gameLoop" size:20 isLit:NO];
    gameLoop.position = SCNVector3Make(0, 5.5, 10);
    [self.groundNode addChildNode:gameLoop];
}

@end
```

[Next](Scene%20Kit%20Session%20WWDC%202014-Sources-Slides-AAPLSlideCloning.m.md)[Previous](Scene%20Kit%20Session%20WWDC%202014-Sources-Slides-AAPLSlideCustomProgram.m.md)

