---
title: OpenCL N-Body Simulation
apple_id: TP40016610
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenCL
published: '2015-12-10'
source_url: https://developer.apple.com/library/archive/samplecode/OpenCL_NBody_Simulation/Listings/Sources_Model_NBody_Constants_NBodyConstants_h.html
archived_at: '2026-07-18T03:17:38.453567Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [OpenCL N-Body Simulation](OpenCL%20N-Body%20Simulation.md)


[Next](Sources-Model-NBody-UI-Meters-Core-NBodyMeter.mm.md)[Previous](Sources-Model-NBody-Preferences-NBodyPreferences.h.md)

# Sources/Model/NBody/Constants/NBodyConstants.h

```objc
/*
 <codex>
 <abstract>
 Common constant for NBody simulation.
 </abstract>
 </codex>
 */

#ifndef _NBODY_CONSTANTS_H_
#define _NBODY_CONSTANTS_H_

#import <OpenGL/OpenGL.h>

#ifdef __cplusplus

namespace NBody
{
    namespace Mouse
    {
        namespace Button
        {
            const GLuint kLeft = 0;
            const GLuint kDown = 1;
            const GLuint kUp   = 0;
        }; // Button

        namespace Wheel
        {
            const GLuint kDown = -1;
            const GLuint kUp   =  1;
        }; // Whell
    }; // Mouse

    namespace Button
    {
        const GLfloat kWidth   = 1000.0f;
        const GLfloat kHeight  = 48.0f;
        const GLfloat kSpacing = 32.0f;
    }; // Button

    namespace Scale
    {
        const GLfloat kTime      = 0.4f;
        const GLfloat kSoftening = 1.0f;
    }; // Scale

    namespace Window
    {
        const GLfloat kWidth  = 800.0f;
        const GLfloat kHeight = 500.0f;
    }; // Defaults

    namespace Particles
    {
        const GLuint  kCountMax = 32768;
        const GLuint  kCountMin = kCountMax / 4;
        const GLuint  kCount    = kCountMax;
    }; // Defaults

    namespace Star
    {
        const GLfloat kSize  = 4.0f;
        const GLfloat kScale = 1.0f;
    }; // Defaults

    namespace Defaults
    {
        const GLfloat kSpeed           = 0.06f;
        const GLfloat kRotationDelta   = 0.06f;
        const GLfloat kScrollZoomSpeed = 0.5f;
        const GLfloat kViewDistance    = 30.0f;
        const GLuint  kMeterSize       = 300;
    }; // Defaults

    enum Config:uint32_t
    {
        eConfigRandom = 0,
        eConfigShell,
        eConfigExpand,
        eConfigMWM31,
        eConfigCount
    }; // Config

    enum MeterType:uint32_t
    {
        eNBodyMeterPerf = 0,
        eNBodyMeterUpdates,
        eNBodyMeterFrames,
        eNBodyMeterCPU,
        eNBodyMeters,
        eNBodyMeterMax
    };

    enum RandIntervalLen:uint32_t
    {
        eNBodyRandIntervalLenIsOne = 0,
        eNBodyRandIntervalLenIsTwo
    };
}; // NBody

#endif

#endif
```

[Next](Sources-Model-NBody-UI-Meters-Core-NBodyMeter.mm.md)[Previous](Sources-Model-NBody-Preferences-NBodyPreferences.h.md)

