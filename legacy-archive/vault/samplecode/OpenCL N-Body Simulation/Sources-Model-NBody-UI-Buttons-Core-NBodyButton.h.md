---
title: OpenCL N-Body Simulation
apple_id: TP40016610
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenCL
published: '2015-12-10'
source_url: https://developer.apple.com/library/archive/samplecode/OpenCL_NBody_Simulation/Listings/Sources_Model_NBody_UI_Buttons_Core_NBodyButton_h.html
archived_at: '2026-07-18T03:17:41.384389Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [OpenCL N-Body Simulation](OpenCL%20N-Body%20Simulation.md)


[Next](Sources-Model-NBody-UI-Buttons-Mediator-NBodyButtons.h.md)[Previous](Sources-Model-NBody-UI-Buttons-Core-NBodyButton.mm.md)

# Sources/Model/NBody/UI/Buttons/Core/NBodyButton.h

```objc
/*
 <codex>
 <abstract>
 Utility  class for managing a button associated with N-Body simulator.
 </abstract>
 </codex>
 */

#import <string>

#import <Cocoa/Cocoa.h>
#import <OpenGL/OpenGL.h>

@interface NBodyButton : NSObject

@property (nonatomic, readonly) CGRect   bounds;
@property (nonatomic, readonly) CGPoint  position;

@property (nonatomic) BOOL         isVisible;
@property (nonatomic) BOOL         isSelected;
@property (nonatomic) BOOL         isItalic;
@property (nonatomic) CGFloat      fontSize;
@property (nonatomic) CGPoint      origin;
@property (nonatomic) CGSize       size;
@property (nonatomic) std::string  label;
@property (nonatomic) GLfloat      speed;

+ (instancetype) button;

- (BOOL) acquire;
- (void) toggle;
- (void) draw;

@end
```

[Next](Sources-Model-NBody-UI-Buttons-Mediator-NBodyButtons.h.md)[Previous](Sources-Model-NBody-UI-Buttons-Core-NBodyButton.mm.md)

