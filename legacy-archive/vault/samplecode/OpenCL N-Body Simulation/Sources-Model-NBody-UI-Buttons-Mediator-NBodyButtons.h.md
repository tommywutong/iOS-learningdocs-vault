---
title: OpenCL N-Body Simulation
apple_id: TP40016610
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenCL
published: '2015-12-10'
source_url: https://developer.apple.com/library/archive/samplecode/OpenCL_NBody_Simulation/Listings/Sources_Model_NBody_UI_Buttons_Mediator_NBodyButtons_h.html
archived_at: '2026-07-18T03:17:41.504753Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [OpenCL N-Body Simulation](OpenCL%20N-Body%20Simulation.md)


[Next](Sources-Model-NBody-UI-Buttons-Mediator-NBodyButtons.mm.md)[Previous](Sources-Model-NBody-UI-Buttons-Core-NBodyButton.h.md)

# Sources/Model/NBody/UI/Buttons/Mediator/NBodyButtons.h

```objc
/*
 <codex>
 <abstract>
 Mediator object for managing buttons associated with N-Body simulator types.
 </abstract>
 </codex>
 */

#import <string>

#import <Cocoa/Cocoa.h>
#import <OpenGL/OpenGL.h>

@interface NBodyButtons : NSObject

@property (nonatomic, readonly) size_t   count;
@property (nonatomic, readonly) CGRect   bounds;
@property (nonatomic, readonly) CGPoint  position;

@property (nonatomic) BOOL         isVisible;
@property (nonatomic) BOOL         isSelected;
@property (nonatomic) BOOL         isItalic;
@property (nonatomic) size_t       index;
@property (nonatomic) CGFloat      fontSize;
@property (nonatomic) CGPoint      origin;
@property (nonatomic) CGSize       size;
@property (nonatomic) std::string  label;
@property (nonatomic) GLfloat      speed;

- (instancetype) initWithCount:(size_t)count;

- (BOOL) acquire;
- (void) toggle;
- (void) draw;

@end
```

[Next](Sources-Model-NBody-UI-Buttons-Mediator-NBodyButtons.mm.md)[Previous](Sources-Model-NBody-UI-Buttons-Core-NBodyButton.h.md)

