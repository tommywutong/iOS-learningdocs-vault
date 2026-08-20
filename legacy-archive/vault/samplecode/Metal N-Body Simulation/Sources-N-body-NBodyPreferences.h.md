---
title: Metal N-Body Simulation
apple_id: TP40016621
resource_type: Sample Code
platform: iOS
topic: General
technology: Metal
published: '2015-12-10'
source_url: https://developer.apple.com/library/archive/samplecode/Metal_NBody_Simulation/Listings/Sources_N_body_NBodyPreferences_h.html
archived_at: '2026-07-18T03:14:58.604020Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Metal N-Body Simulation](Metal%20N-Body%20Simulation.md)


[Next](Sources-N-body-MetalNBodyRenderPipeline.mm.md)[Previous](Sources-N-body-MetalNBodyRenderPassDescriptor.mm.md)

# Sources/N-body/NBodyPreferences.h

```objc
/*
 Copyright (C) 2015-2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Keys for the N-Body application preferences, global parameters, and simulation properties.
 */

#import <Foundation/Foundation.h>

// Keys for the N-Body application prefs property list      // For values
extern NSString* kNBodyGlobals;                             // Dictionary
extern NSString* kNBodyParameters;                          // Array of dictionaries

// Keys for the N-Body globals parameters                   // For values
extern NSString* kNBodyParticles;                           // Unsigned Integer 32
extern NSString* kNBodyTexRes;                              // Unsigned Integer 32
extern NSString* kNBodyChannels;                            // Unsigned Integer 32

// Keys for the N-Body simulation properties                // For values
extern NSString* kNBodyTimestep;                            // Float
extern NSString* kNBodyClusterScale;                        // Float
extern NSString* kNBodyVelocityScale;                       // Float
extern NSString* kNBodySoftening;                           // Float
extern NSString* kNBodyDamping;                             // Float
extern NSString* kNBodyPointSize;                           // Float
```

[Next](Sources-N-body-MetalNBodyRenderPipeline.mm.md)[Previous](Sources-N-body-MetalNBodyRenderPassDescriptor.mm.md)

