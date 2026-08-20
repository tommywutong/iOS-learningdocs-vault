---
title: OpenCL N-Body Simulation
apple_id: TP40016610
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenCL
published: '2015-12-10'
source_url: https://developer.apple.com/library/archive/samplecode/OpenCL_NBody_Simulation/Listings/Sources_Model_NBody_Simulation_Core_Data_Random_Base_NBodySimulationDataURDB_h.html
archived_at: '2026-07-18T03:17:39.982685Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [OpenCL N-Body Simulation](OpenCL%20N-Body%20Simulation.md)


[Next](Sources-Model-NBody-Simulation-Core-Data-Random-Base-NBodySimulationDataURDB.mm.md)[Previous](Sources-Model-NBody-Simulation-Core-Data-Mediator-NBodySimulationDataMediator.h.md)

# Sources/Model/NBody/Simulation/Core/Data/Random/Base/NBodySimulationDataURDB.h

```objc
/*
 <codex>
 <abstract>
 Base class for generating random packed or split data sets for the cpu or gpu bound simulator using unifrom random distributuon.
 </abstract>
 </codex>
 */

#ifndef _NBODY_SIMULATION_DATA_URD_BASE_H_
#define _NBODY_SIMULATION_DATA_URD_BASE_H_

#import <OpenGL/OpenGL.h>

#import "CMRandom.h"

#import "NBodySimulationProperties.h"

#ifdef __cplusplus

namespace NBody
{
    namespace Simulation
    {
        namespace Data
        {
            class URDB
            {
            public:
                URDB(const Properties& rProperties);

                virtual ~URDB();

                const simd::float3& axis() const;

                void setAxis(const simd::float3& axis);

                void setProperties(const Properties& rProperties);

            protected:
                size_t               mnParticles;
                GLuint               mnConfig;
                GLfloat              m_Scale[2];
                simd::float3         m_Axis;
                dispatch_queue_t     m_DQueue;
                CM::URD3::generator* mpGenerator[2];
            }; // URD Base
        } // Random
    } // Simulation
} // NBody

#endif

#endif
```

[Next](Sources-Model-NBody-Simulation-Core-Data-Random-Base-NBodySimulationDataURDB.mm.md)[Previous](Sources-Model-NBody-Simulation-Core-Data-Mediator-NBodySimulationDataMediator.h.md)

