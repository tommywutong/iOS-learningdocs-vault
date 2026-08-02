---
title: OpenCL N-Body Simulation
apple_id: TP40016610
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenCL
published: '2015-12-10'
source_url: https://developer.apple.com/library/archive/samplecode/OpenCL_NBody_Simulation/Listings/Sources_Model_NBody_Simulation_Core_Data_Packed_NBodySimulationDataPacked_h.html
archived_at: '2026-07-18T03:17:39.843353Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [OpenCL N-Body Simulation](OpenCL%20N-Body%20Simulation.md)


[Next](Sources-Model-NBody-Simulation-Core-Data-Packed-NBodySimulationDataPacked.mm.md)[Previous](Sources-Model-NBody-Simulation-Core-Data-Split-NBodySimulationDataSplit.h.md)

# Sources/Model/NBody/Simulation/Core/Data/Packed/NBodySimulationDataPacked.h

```objc
/*
 <codex>
 <abstract>
 Utility class for managing cpu bound device and host packed mass and position data.
 </abstract>
 </codex>
 */

#ifndef _NBODY_SIMULATION_PACKED_DATA_H_
#define _NBODY_SIMULATION_PACKED_DATA_H_

#import <vector>

#import <OpenCL/OpenCL.h>

#import "NBodySimulationProperties.h"

#ifdef __cplusplus

namespace NBody
{
    namespace Simulation
    {
        namespace Data
        {
            typedef struct Packed3D* Packed3DRef;

            class Packed
            {
            public:
                Packed(const Properties& rProperties);

                virtual ~Packed();

                GLint acquire(cl_context pContext);

                GLint bind(const cl_uint& nIndex,
                           cl_kernel pKernel);

                GLint update(const cl_uint& nIndex,
                             cl_kernel pKernel);

                GLfloat* data();

                const GLfloat* data() const;

            private:
                size_t        mnParticles;
                size_t        mnSamples;
                size_t        mnLength;
                size_t        mnSize;
                cl_mem_flags  mnFlags;
                Packed3DRef   mpPacked;
            }; // Packed
        } // Data
    } // Simulation
} // NBody

#endif

#endif
```

[Next](Sources-Model-NBody-Simulation-Core-Data-Packed-NBodySimulationDataPacked.mm.md)[Previous](Sources-Model-NBody-Simulation-Core-Data-Split-NBodySimulationDataSplit.h.md)

