---
title: OpenCL N-Body Simulation
apple_id: TP40016610
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenCL
published: '2015-12-10'
source_url: https://developer.apple.com/library/archive/samplecode/OpenCL_NBody_Simulation/Listings/Sources_Model_NBody_UI_Meters_Mediator_NBodyMeters_h.html
archived_at: '2026-07-18T03:17:41.743004Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [OpenCL N-Body Simulation](OpenCL%20N-Body%20Simulation.md)


[Next](Sources-Model-NBody-UI-Meters-Mediator-NBodyMeters.mm.md)[Previous](Sources-Model-NBody-UI-Meters-Core-NBodyMeter.h.md)

# Sources/Model/NBody/UI/Meters/Mediator/NBodyMeters.h

```objc
/*
 <codex>
 <abstract>
 Mediator object for managing multiple hud objects for n-body simulators.
 </abstract>
 </codex>
 */

#import <string>

#import <Cocoa/Cocoa.h>
#import <OpenGL/OpenGL.h>

@interface NBodyMeters: NSObject

@property (nonatomic, readonly) size_t count;

@property (nonatomic) BOOL         isVisible;
@property (nonatomic) BOOL         useTimer;
@property (nonatomic) BOOL         useHostInfo;
@property (nonatomic) std::string  label;
@property (nonatomic) size_t       index;
@property (nonatomic) size_t       max;
@property (nonatomic) GLsizei      bound;
@property (nonatomic) GLfloat      speed;
@property (nonatomic) GLfloat      value;
@property (nonatomic) CGSize       frame;
@property (nonatomic) CGPoint      point;

- (instancetype) initWithCount:(size_t)count;

- (BOOL) acquire;

- (void) toggle;
- (void) show:(BOOL)doShow;

- (void) update;
- (void) reset;

- (void) resize:(NSSize)size;

- (void) draw;
- (void) draw:(NSArray *)positions;

@end
```

[Next](Sources-Model-NBody-UI-Meters-Mediator-NBodyMeters.mm.md)[Previous](Sources-Model-NBody-UI-Meters-Core-NBodyMeter.h.md)

