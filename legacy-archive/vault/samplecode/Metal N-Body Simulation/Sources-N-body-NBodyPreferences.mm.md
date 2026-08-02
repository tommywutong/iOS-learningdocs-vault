---
title: Metal N-Body Simulation
apple_id: TP40016621
resource_type: Sample Code
platform: iOS
topic: General
technology: Metal
published: '2015-12-10'
source_url: https://developer.apple.com/library/archive/samplecode/Metal_NBody_Simulation/Listings/Sources_N_body_NBodyPreferences_mm.html
archived_at: '2026-07-18T03:14:58.646038Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Metal N-Body Simulation](Metal%20N-Body%20Simulation.md)


[Next](Sources-N-body-MetalNBodyPresenter.h.md)[Previous](Sources-N-body-MetalNBodyComputeStage.mm.md)

# Sources/N-body/NBodyPreferences.mm

```objc
/*
 Copyright (C) 2015-2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Keys for the N-Body application preferences, global parameters, and simulation properties.
 */

#import <Foundation/Foundation.h>

// Keys for the N-Body application prefs property list      // For values
NSString* kNBodyGlobals    = @"NBody_Globals";              // Dictionary
NSString* kNBodyParameters = @"NBody_Parameters";           // Array of dictionaries

// Keys for the N-Body globals parameters                   // For values
NSString* kNBodyParticles = @"NBody_Particles";             // Unsigned Integer 32
NSString* kNBodyTexRes    = @"NBody_Tex_Res";               // Unsigned Integer 32
NSString* kNBodyChannels  = @"NBody_Channels";              // Unsigned Integer 32

// Keys for the N-Body simulation properties                // For values
NSString* kNBodyTimestep      = @"NBody_Timestep";          // Float
NSString* kNBodyClusterScale  = @"NBody_Cluster_Scale";     // Float
NSString* kNBodyVelocityScale = @"NBody_Velocity_Scale";    // Float
NSString* kNBodySoftening     = @"NBody_Softening";         // Float
NSString* kNBodyDamping       = @"NBody_Damping";           // Float
NSString* kNBodyPointSize     = @"NBody_PointSize";         // Float
```

[Next](Sources-N-body-MetalNBodyPresenter.h.md)[Previous](Sources-N-body-MetalNBodyComputeStage.mm.md)

