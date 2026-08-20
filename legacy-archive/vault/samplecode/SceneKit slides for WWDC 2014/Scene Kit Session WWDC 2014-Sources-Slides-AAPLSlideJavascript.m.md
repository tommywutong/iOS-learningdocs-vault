---
title: SceneKit slides for WWDC 2014
apple_id: TP40014551
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2014-10-16'
source_url: https://developer.apple.com/library/archive/samplecode/SceneKitWWDC2014/Listings/Scene_Kit_Session_WWDC_2014_Sources_Slides_AAPLSlideJavascript_m.html
archived_at: '2026-07-18T03:23:16.931643Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [SceneKit slides for WWDC 2014](SceneKit%20slides%20for%20WWDC%202014.md)


[Next](Scene%20Kit%20Session%20WWDC%202014-Sources-Slides-AAPLSlideGeometry.m.md)[Previous](Scene%20Kit%20Session%20WWDC%202014-Sources-Slides-AAPLSlideRenderAScene.m.md)

# Scene Kit Session WWDC 2014/Sources/Slides/AAPLSlideJavascript.m

```objc
#import "AAPLPresentationViewController.h"
#import "AAPLSlideTextManager.h"
#import "AAPLSlide.h"
#import "Utils.h"

@interface AAPLSlideJS : AAPLSlide
@end

@implementation AAPLSlideJS {
}

- (NSUInteger)numberOfSteps {
    return 3;
}

- (void)setupSlideWithPresentationViewController:(AAPLPresentationViewController *)presentationViewController {
    // Set the slide's title and subtitle and add some code
    self.textManager.title = @"Scriptability";

    [self.textManager addBullet:@"Javascript bridge" atLevel:0];
    [self.textManager addCode:@"// setup a JSContext for SceneKit\n#SCNExportJavaScriptModule#(aJSContext);\n\n// reference a SceneKit object from JS\naJSContext.#globalObject#[@\"aNode\"] = aNode;\n\n// execute a script\n[aJSContext #evaluateScript#:@\"aNode.scale = {x:2, y:2, z:2};\";"];
}

- (void)presentStepIndex:(NSUInteger)index withPresentationViewController:(AAPLPresentationViewController *)presentationViewController {
    switch (index) {
        case 0:
            break;
        case 1:
            [self.textManager flipOutTextOfType:AAPLTextTypeCode];
            [self.textManager flipOutTextOfType:AAPLTextTypeBullet];
            [self.textManager addEmptyLine];
            [self.textManager addBullet:@"Javascript code example" atLevel:0];
            [self.textManager addCode:@"\n#//allocate a node#\n"
             "var aNode = SCNNode.node();\n\n"

             "#//change opacity#\n"
             "aNode.opacity = 0.5;\n\n"

             "#//remove from parent#\n"
             "aNode.removeFromParentNode();\n\n"

             "#//animate implicitly#\n"
             "SCNTransaction.begin();\n"
             "SCNTransaction.setAnimationDuration(1.0);\n"
             "aNode.scale = {x:2, y:2, z:2};\n"
             "SCNTransaction.commit();"
             ];

            [self.textManager flipInTextOfType:AAPLTextTypeBullet];
            [self.textManager flipInTextOfType:AAPLTextTypeCode];

            break;
        case 2:
            [self.textManager flipOutTextOfType:AAPLTextTypeBullet];
            [self.textManager flipOutTextOfType:AAPLTextTypeCode];
            [self.textManager addBullet:@"Tools" atLevel:0];
            [self.textManager addBullet:@"Debugging" atLevel:0];
            [self.textManager flipInTextOfType:AAPLTextTypeBullet];
            break;

    }
}

@end
```

[Next](Scene%20Kit%20Session%20WWDC%202014-Sources-Slides-AAPLSlideGeometry.m.md)[Previous](Scene%20Kit%20Session%20WWDC%202014-Sources-Slides-AAPLSlideRenderAScene.m.md)

