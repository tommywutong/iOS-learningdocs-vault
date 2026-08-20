---
title: OpenCL N-Body Simulation
apple_id: TP40016610
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenCL
published: '2015-12-10'
source_url: https://developer.apple.com/library/archive/samplecode/OpenCL_NBody_Simulation/Listings/Sources_Model_NBody_Engine_NBodyEngine_h.html
archived_at: '2026-07-18T03:17:38.530749Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [OpenCL N-Body Simulation](OpenCL%20N-Body%20Simulation.md)


[Next](Sources-Model-NBody-Engine-NBodyEngine.mm.md)[Previous](Sources-Model-HUD-Meter-Image-HUDMeterImage.h.md)

# Sources/Model/NBody/Engine/NBodyEngine.h

```objc
/*
 <codex>
 <abstract>
 These methods performs an NBody simulation which calculates a gravity field
 and corresponding velocity and acceleration contributions accumulated
 by each body in the system from every other body.  This example
 also shows how to mitigate computation between all available devices
 including CPU and GPU devices, as well as a hybrid combination of both,
 using separate threads for each simulator.
 </abstract>
 </codex>
 */

#import <Cocoa/Cocoa.h>
#import <OpenGL/OpenGL.h>

#import "NBodyPreferences.h"

@interface NBodyEngine : NSObject

@property (nonatomic, readonly) NBodyPreferences* preferences;

@property (nonatomic, readonly) BOOL    isResized;
@property (nonatomic, readonly) NSSize  size;

@property (nonatomic) unichar  command;
@property (nonatomic) GLuint   activeDemo;
@property (nonatomic) GLfloat  clearColor;
@property (nonatomic) GLfloat  viewDistance;
@property (nonatomic) NSRect   frame;

- (instancetype) initWithPreferences:(NBodyPreferences *)preferences;

+ (instancetype) engine;

+ (instancetype) engineWithPreferences:(NBodyPreferences *)preferences;

- (BOOL) acquire;

- (void) draw;

- (void) resize:(NSRect)frame;

- (void) scroll:(GLfloat)delta;

- (void) click:(GLint)state
         point:(NSPoint)point;

- (void) move:(NSPoint)point;

@end
```

[Next](Sources-Model-NBody-Engine-NBodyEngine.mm.md)[Previous](Sources-Model-HUD-Meter-Image-HUDMeterImage.h.md)

