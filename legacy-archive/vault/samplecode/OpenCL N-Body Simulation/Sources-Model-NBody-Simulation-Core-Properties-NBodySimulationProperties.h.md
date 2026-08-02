---
title: OpenCL N-Body Simulation
apple_id: TP40016610
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenCL
published: '2015-12-10'
source_url: https://developer.apple.com/library/archive/samplecode/OpenCL_NBody_Simulation/Listings/Sources_Model_NBody_Simulation_Core_Properties_NBodySimulationProperties_h.html
archived_at: '2026-07-18T03:17:40.845144Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [OpenCL N-Body Simulation](OpenCL%20N-Body%20Simulation.md)


[Next](Sources-Model-NBody-Simulation-Core-Properties-NBodySimulationProperties.mm.md)[Previous](Sources-Model-NBody-Simulation-Core-GPU-NBodySimulationGPU.h.md)

# Sources/Model/NBody/Simulation/Core/Properties/NBodySimulationProperties.h

```objc
/*
 <codex>
 <abstract>
 N-Body simulation Properties.
 </abstract>
 </codex>
 */

#ifndef _NBODY_SIMULATION_PROPERTIES_H_
#define _NBODY_SIMULATION_PROPERTIES_H_

#import <Cocoa/Cocoa.h>
#import <OpenGL/OpenGL.h>

#import "NBodyPreferences.h"

#ifdef __cplusplus

namespace NBody
{
    namespace Simulation
    {        
        class Properties
        {
        public:
            Properties(const uint32_t& demoType = 1);
            Properties(NSDictionary* pDictionary);
            Properties(NBodyPreferences* pPreferences);

            Properties(const Properties& rProperties);

            virtual ~Properties();

            Properties& operator=(const Properties& rProperties);
            Properties& operator=(NSDictionary* pDictionary);
            Properties& operator=(NBodyPreferences* pPreferences);

            NSDictionary*   dictionary();

            void update(NBodyPreferences* pPreferences);

            static Properties* create(const size_t& nCount);

            static Properties* create();
            static Properties* create(NSString* pFilename);

        public:
            bool      mbIsGPUOnly;
            int64_t   mnDemos;
            uint32_t  mnDemoType;
            uint32_t  mnParticles;
            uint32_t  mnConfig;
            float     mnTimeStep;
            float     mnClusterScale;
            float     mnVelocityScale;
            float     mnSoftening;
            float     mnDamping;
            float     mnPointSize;
            float     mnViewDistance;
            double    mnRotateX;
            double    mnRotateY;
        }; // Properties
    } // Simulation
} // NBody

#endif

#endif
```

[Next](Sources-Model-NBody-Simulation-Core-Properties-NBodySimulationProperties.mm.md)[Previous](Sources-Model-NBody-Simulation-Core-GPU-NBodySimulationGPU.h.md)

