---
title: SceneKit slides for WWDC 2014
apple_id: TP40014551
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2014-10-16'
source_url: https://developer.apple.com/library/archive/samplecode/SceneKitWWDC2014/Listings/Scene_Kit_Session_WWDC_2014_Sources_Slides_AAPLSlideSummary_m.html
archived_at: '2026-07-18T03:23:18.980035Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [SceneKit slides for WWDC 2014](SceneKit%20slides%20for%20WWDC%202014.md)


[Next](Scene%20Kit%20Session%20WWDC%202014-Sources-Slides-AAPLSlideLoadingDAE.m.md)[Previous](Scene%20Kit%20Session%20WWDC%202014-Sources-Slides-AAPLSlidePhysics.m.md)

# Scene Kit Session WWDC 2014/Sources/Slides/AAPLSlideSummary.m

```objc
#import "AAPLPresentationViewController.h"
#import "AAPLSlideTextManager.h"
#import "AAPLSlide.h"
#import "Utils.h"

@interface AAPLSlideSummary : AAPLSlide
@end

@implementation AAPLSlideSummary

- (void)setupSlideWithPresentationViewController:(AAPLPresentationViewController *)presentationViewController
{
    self.textManager.title = @"Summary";
    [self.textManager addBullet:@"SceneKit available on iOS" atLevel:0];
    [self.textManager addBullet:@"Casual game ready" atLevel:0];
    [self.textManager addBullet:@"Full featured rendering" atLevel:0];
    [self.textManager addBullet:@"Extendable" atLevel:0];
}

@end
```

[Next](Scene%20Kit%20Session%20WWDC%202014-Sources-Slides-AAPLSlideLoadingDAE.m.md)[Previous](Scene%20Kit%20Session%20WWDC%202014-Sources-Slides-AAPLSlidePhysics.m.md)

