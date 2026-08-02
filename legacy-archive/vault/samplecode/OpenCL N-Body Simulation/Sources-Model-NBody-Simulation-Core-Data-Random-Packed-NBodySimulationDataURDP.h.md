---
title: OpenCL N-Body Simulation
apple_id: TP40016610
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenCL
published: '2015-12-10'
source_url: https://developer.apple.com/library/archive/samplecode/OpenCL_NBody_Simulation/Listings/Sources_Model_NBody_Simulation_Core_Data_Random_Packed_NBodySimulationDataURDP_h.html
archived_at: '2026-07-18T03:17:40.086415Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [OpenCL N-Body Simulation](OpenCL%20N-Body%20Simulation.md)


[Next](Sources-Model-NBody-Simulation-Core-Data-Split-NBodySimulationDataSplit.mm.md)[Previous](Sources-Model-NBody-Simulation-Core-Data-Random-Packed-NBodySimulationDataURDP.m.md)

# Sources/Model/NBody/Simulation/Core/Data/Random/Packed/NBodySimulationDataURDP.h

```objc
/*
 <codex>
 <abstract>
 Functor for generating random packed-data sets for the cpu or gpu bound simulator using uniform random distribution.
 </abstract>
 </codex>
 */

#ifndef _NBODY_SIMULATION_DATA_URDP_H_
#define _NBODY_SIMULATION_DATA_URDP_H_

#import "NBodySimulationDataURDB.h"

#ifdef __cplusplus

namespace NBody
{
    namespace Simulation
    {
        namespace Data
        {
            class URDP : public URDB
            {
            public:
                URDP(const Properties& rProperties);

                virtual ~URDP();

                bool operator()(GLfloat* pPosition, GLfloat* pVelocity);

            private:
                void configRandom(simd::float4* pPosition, simd::float4* pVelocity);
                void configShell(simd::float4* pPosition, simd::float4* pVelocity);
                void configMWM31(simd::float4* pPosition, simd::float4* pVelocity);
                void configExpand(simd::float4* pPosition, simd::float4* pVelocity);

                GLfloat mnCount;
                GLfloat mnBCScale;
                GLfloat mnTCScale;
                GLfloat mnVCScale;
            }; // URDP
        } // Data
    } // Simulation
} // NBody

#endif

#endif
```

[Next](Sources-Model-NBody-Simulation-Core-Data-Split-NBodySimulationDataSplit.mm.md)[Previous](Sources-Model-NBody-Simulation-Core-Data-Random-Packed-NBodySimulationDataURDP.m.md)

