---
title: Metal N-Body Simulation
apple_id: TP40016621
resource_type: Sample Code
platform: iOS
topic: General
technology: Metal
published: '2015-12-10'
source_url: https://developer.apple.com/library/archive/samplecode/Metal_NBody_Simulation/Listings/Sources_Foundation_CFQueueGenerator_h.html
archived_at: '2026-07-18T03:14:56.376882Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Metal N-Body Simulation](Metal%20N-Body%20Simulation.md)


[Next](Sources-N-body-MetalNBodyRenderPipeline.h.md)[Previous](Sources-Foundation-CFQueueGenerator.mm.md)

# Sources/Foundation/CFQueueGenerator.h

```objc
/*
 Copyright (C) 2015-2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 A functor for creating dispatch queue with a unique identifier.
 */

#import <Foundation/Foundation.h>

@interface CFQueueGenerator : NSObject

// Desired dispatch queue attribute.  Defaults to serial.
@property (nullable) dispatch_queue_attr_t attribute;

// Dispatch queue identifier
@property (nullable, nonatomic, readonly) const char* identifier;

// Dispatch queue label
@property (nullable, nonatomic) const char* label;

// A dispatch queue created with the set attribute.
// Defaults to a serial dispatch queue.
@property (nullable, nonatomic, readonly) dispatch_queue_t queue;

@end
```

[Next](Sources-N-body-MetalNBodyRenderPipeline.h.md)[Previous](Sources-Foundation-CFQueueGenerator.mm.md)

