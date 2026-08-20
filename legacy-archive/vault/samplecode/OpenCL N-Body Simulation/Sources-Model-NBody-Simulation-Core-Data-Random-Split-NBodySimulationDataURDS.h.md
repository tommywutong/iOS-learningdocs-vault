---
title: OpenCL N-Body Simulation
apple_id: TP40016610
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenCL
published: '2015-12-10'
source_url: https://developer.apple.com/library/archive/samplecode/OpenCL_NBody_Simulation/Listings/Sources_Model_NBody_Simulation_Core_Data_Random_Split_NBodySimulationDataURDS_h.html
archived_at: '2026-07-18T03:17:40.229421Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [OpenCL N-Body Simulation](OpenCL%20N-Body%20Simulation.md)


[Next](Sources-Model-NBody-Simulation-Core-Data-Random-Split-NBodySimulationDataURDS.mm.md)[Previous](Sources-Model-NBody-Simulation-Core-Data-Random-Base-NBodySimulationDataURDB.mm.md)

# Sources/Model/NBody/Simulation/Core/Data/Random/Split/NBodySimulationDataURDS.h

```objc
/*
 <codex>
 <abstract>
 Functor for generating random split-data sets for the cpu or gpu bound simulator using uniform random distribution.
 </abstract>
 </codex>
 */

#ifndef _NBODY_SIMULATION_DATA_URDS_H_
#define _NBODY_SIMULATION_DATA_URDS_H_

#import "NBodySimulationDataURDB.h"
#import "NBodySimulationDataSplit.h"

#ifdef __cplusplus

namespace NBody
{
    namespace Simulation
    {
        namespace Data
        {
            class URDS : public URDB
            {
            public:
                URDS(const Properties& rProperties);

                virtual ~URDS();

                bool operator()(Split* pSplit);

            private:
                void configRandom();
                void configShell();
                void configMWM31();
                void configExpand();

                GLfloat mnCount;
                GLfloat mnBCScale;

                GLfloat* mpMass;
                GLfloat* mpPosition[3];
                GLfloat* mpVelocity[3];
            }; // URDS
        } // Data
    } // Simulation
} // NBody

#endif

#endif
```

[Next](Sources-Model-NBody-Simulation-Core-Data-Random-Split-NBodySimulationDataURDS.mm.md)[Previous](Sources-Model-NBody-Simulation-Core-Data-Random-Base-NBodySimulationDataURDB.mm.md)

