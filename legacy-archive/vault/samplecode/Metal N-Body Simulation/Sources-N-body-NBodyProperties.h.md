---
title: Metal N-Body Simulation
apple_id: TP40016621
resource_type: Sample Code
platform: iOS
topic: General
technology: Metal
published: '2015-12-10'
source_url: https://developer.apple.com/library/archive/samplecode/Metal_NBody_Simulation/Listings/Sources_N_body_NBodyProperties_h.html
archived_at: '2026-07-18T03:14:58.687845Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Metal N-Body Simulation](Metal%20N-Body%20Simulation.md)


[Next](Sources-N-body-MetalNBodyVertexStage.mm.md)[Previous](Sources-N-body-MetalNBodyVertexStage.h.md)

# Sources/N-body/NBodyProperties.h

```objc
/*
 Copyright (C) 2015-2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Utility class for managing a set of defualt initial conditions for n-body simulation.
 */

#import <Foundation/Foundation.h>

@interface NBodyProperties : NSObject

// Designated initializer for loading the property list file containing
// global and simulation parameters
- (nullable instancetype) initWithFile:(nullable NSString *)fileName;

// Select the specific type of N-body simulation
@property (nonatomic) uint32_t config;

// Number of color channels.  Default is 4 for RGBA.
@property (nonatomic) uint32_t channels;

// Number of point particles
@property (nonatomic) uint32_t particles;

// Texture resolution.  The default is 64x64.
@property (nonatomic) uint32_t texRes;

// The number of N-body simulation types
@property (readonly) uint32_t count;

// N-body simulation global parameters
@property (nullable, nonatomic, readonly) NSDictionary* globals;

// N-body parameters for simulation types
@property (nullable, nonatomic, readonly) NSDictionary* parameters;

@end
```

[Next](Sources-N-body-MetalNBodyVertexStage.mm.md)[Previous](Sources-N-body-MetalNBodyVertexStage.h.md)

