---
title: SprocketInvadersOld
apple_id: DTS10000061
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-10-14'
source_url: https://developer.apple.com/library/archive/samplecode/SprocketInvadersOld/Listings/Source_Particles_h.html
archived_at: '2026-07-18T03:25:27.741264Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [SprocketInvadersOld](SprocketInvadersOld.md)


[Next](Source-SIResources.h.md)[Previous](Source-Particles.c.md)

# Source/Particles.h

```c
//¥ ------------------------------------------------------------------------------------------  ¥
//¥
//¥ Copyright © 1996 Apple Computer, Inc., All Rights Reserved
//¥
//¥
//¥     You may incorporate this sample code into your applications without
//¥     restriction, though the sample code has been provided "AS IS" and the
//¥     responsibility for its operation is 100% yours.  However, what you are
//¥     not permitted to do is to redistribute the source as "DSC Sample Code"
//¥     after having made changes. If you're going to re-distribute the source,
//¥     we require that you make it clear in the source that the code was
//¥     descended from Apple Sample Code, but that you've made changes.
//¥
//¥     Authors:
//¥         Chris De Salvo
//¥
//¥ ------------------------------------------------------------------------------------------  ¥

#ifndef __PARTICLES__
#define __PARTICLES__

//¥ ------------------------------  Includes

#include <QuickDraw.h>

//¥ ------------------------------  Public Definitions

#define kNumSpecks                  50

//¥ ------------------------------  Public Types

typedef struct Speck
{
    UInt32  age;
    UInt32  lifeTime;
    SInt32  h, v;
    SInt32  speedH, speedV;
} Speck, *SpeckPtr;

typedef struct Particles
{
    UInt32      numSpecks;
    SpeckPtr    specks;
    Rect        bounds;
    UInt8       color;
} Particles, *ParticlesPtr;

//¥ ------------------------------  Public Variables
//¥ ------------------------------  Public Functions

#ifdef __cplusplus
extern "C" {
#endif

extern ParticlesPtr ParticlesAllocate(SInt32 x, SInt32 y, UInt8 color);
extern void ParticlesDispose(ParticlesPtr *theParticles);
extern Rect ParticlesDraw(ParticlesPtr, CGrafPtr dest);

#ifdef __cplusplus
}
#endif

#endif
```

[Next](Source-SIResources.h.md)[Previous](Source-Particles.c.md)

