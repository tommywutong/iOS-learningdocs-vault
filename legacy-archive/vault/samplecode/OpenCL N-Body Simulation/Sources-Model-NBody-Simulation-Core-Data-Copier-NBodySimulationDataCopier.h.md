---
title: OpenCL N-Body Simulation
apple_id: TP40016610
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenCL
published: '2015-12-10'
source_url: https://developer.apple.com/library/archive/samplecode/OpenCL_NBody_Simulation/Listings/Sources_Model_NBody_Simulation_Core_Data_Copier_NBodySimulationDataCopier_h.html
archived_at: '2026-07-18T03:17:39.455572Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [OpenCL N-Body Simulation](OpenCL%20N-Body%20Simulation.md)


[Next](Sources-Model-NBody-Simulation-Core-Data-Copier-NBodySimulationDataCopier.mm.md)[Previous](Sources-Model-NBody-Simulation-Core-Data-Galaxy-NBodySimulationDataGalaxy.mm.md)

# Sources/Model/NBody/Simulation/Core/Data/Copier/NBodySimulationDataCopier.h

```objc
/*
 <codex>
 <abstract>
 Functor for copying split position data to/from packed position data.
 </abstract>
 </codex>
 */

#ifndef _NBODY_SIMULATION_DATA_COPIER_H_
#define _NBODY_SIMULATION_DATA_COPIER_H_

#import "NBodySimulationDataPacked.h"
#import "NBodySimulationDataSplit.h"

#ifdef __cplusplus

namespace NBody
{
    namespace Simulation
    {
        namespace Data
        {
            class Copier
            {
            public:
                Copier(const size_t& nCount);

                virtual ~Copier();

                bool operator()(const Split  * const pSplit,  Packed* pPacked);
                bool operator()(const Packed * const pPacked, Split*  pSplit);

            private:
                size_t            mnCount;
                dispatch_queue_t  m_Queue;
            }; // Copier
        } // Data
    } // Simulation
} // NBody

#endif

#endif
```

[Next](Sources-Model-NBody-Simulation-Core-Data-Copier-NBodySimulationDataCopier.mm.md)[Previous](Sources-Model-NBody-Simulation-Core-Data-Galaxy-NBodySimulationDataGalaxy.mm.md)

