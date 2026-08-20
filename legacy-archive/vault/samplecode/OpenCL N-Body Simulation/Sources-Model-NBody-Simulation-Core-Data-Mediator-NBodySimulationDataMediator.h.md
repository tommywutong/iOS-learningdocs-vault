---
title: OpenCL N-Body Simulation
apple_id: TP40016610
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenCL
published: '2015-12-10'
source_url: https://developer.apple.com/library/archive/samplecode/OpenCL_NBody_Simulation/Listings/Sources_Model_NBody_Simulation_Core_Data_Mediator_NBodySimulationDataMediator_h.html
archived_at: '2026-07-18T03:17:39.681261Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [OpenCL N-Body Simulation](OpenCL%20N-Body%20Simulation.md)


[Next](Sources-Model-NBody-Simulation-Core-Data-Random-Base-NBodySimulationDataURDB.h.md)[Previous](Sources-Model-NBody-Simulation-Core-Data-Mediator-NBodySimulationDataMediator.mm.md)

# Sources/Model/NBody/Simulation/Core/Data/Mediator/NBodySimulationDataMediator.h

```objc
/*
 <codex>
 <abstract>
 Utility class for managing cpu bound device and host memories.
 </abstract>
 </codex>
 */

#ifndef _NBODY_SIMULATION_DATA_H_
#define _NBODY_SIMULATION_DATA_H_

#import <OpenCL/OpenCL.h>

#import "NBodySimulationProperties.h"
#import "NBodySimulationDataPacked.h"
#import "NBodySimulationDataSplit.h"

#ifdef __cplusplus

namespace NBody
{
    namespace Simulation
    {
        namespace Data
        {
            class Mediator
            {
            public:
                Mediator(const Properties& rProperties);

                virtual ~Mediator();

                void swap();

                GLint acquire(cl_context pContext);
                GLint bind(cl_kernel pKernel);
                GLint update(cl_kernel pKernel);

                void reset(const Properties& rProperties);

                GLint positionInRange(const CFRange& range,
                                      GLfloat* pDst);

                GLint positionInRange(const size_t& nMin,
                                      const size_t& nMax,
                                      GLfloat* pDst);

                GLint position(const size_t& nMax,
                               GLfloat* pDst);

                GLint velocity(GLfloat* pDst);

                GLint setPosition(const GLfloat * const pSrc);
                GLint setVelocity(const GLfloat * const pSrc);

                const GLfloat* data() const;

            private:
                GLuint            mnReadIndex;
                GLuint            mnWriteIndex;
                size_t            mnParticles;
                Packed*           mpPacked;
                Split*            mpSplit[2];
                dispatch_queue_t  m_Queue;
            }; // Mediator
        } // Data
    } // Simulation
} // NBody

#endif

#endif
```

[Next](Sources-Model-NBody-Simulation-Core-Data-Random-Base-NBodySimulationDataURDB.h.md)[Previous](Sources-Model-NBody-Simulation-Core-Data-Mediator-NBodySimulationDataMediator.mm.md)

