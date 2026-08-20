---
title: OpenCL N-Body Simulation
apple_id: TP40016610
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenCL
published: '2015-12-10'
source_url: https://developer.apple.com/library/archive/samplecode/OpenCL_NBody_Simulation/Listings/Sources_Model_NBody_UI_Meters_Core_NBodyMeter_h.html
archived_at: '2026-07-18T03:17:41.603873Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [OpenCL N-Body Simulation](OpenCL%20N-Body%20Simulation.md)


[Next](Sources-Model-NBody-UI-Meters-Mediator-NBodyMeters.h.md)[Previous](Sources-Model-NBody-UI-Meters-Core-NBodyMeter.mm.md)

# Sources/Model/NBody/UI/Meters/Core/NBodyMeter.h

```objc
/*
 <codex>
 <abstract>
 A base utility class for managing performance meters.
 </abstract>
 </codex>
 */

#import <string>

#import <Cocoa/Cocoa.h>
#import <OpenGL/OpenGL.h>

@interface NBodyMeter: NSObject

@property (nonatomic) BOOL         isVisible;
@property (nonatomic) BOOL         useTimer;
@property (nonatomic) BOOL         useHostInfo;
@property (nonatomic) std::string  label;
@property (nonatomic) size_t       max;
@property (nonatomic) GLsizei      bound;
@property (nonatomic) GLfloat      speed;
@property (nonatomic) GLdouble     value;
@property (nonatomic) CGSize       frame;
@property (nonatomic) CGPoint      point;

+ (instancetype) meter;

- (BOOL) acquire;
- (void) toggle;

- (void) update;
- (void) draw;

- (void) reset;

@end
```

[Next](Sources-Model-NBody-UI-Meters-Mediator-NBodyMeters.h.md)[Previous](Sources-Model-NBody-UI-Meters-Core-NBodyMeter.mm.md)

