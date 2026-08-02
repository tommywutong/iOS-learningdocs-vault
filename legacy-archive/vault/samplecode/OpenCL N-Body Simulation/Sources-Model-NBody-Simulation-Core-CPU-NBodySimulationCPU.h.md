---
title: OpenCL N-Body Simulation
apple_id: TP40016610
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenCL
published: '2015-12-10'
source_url: https://developer.apple.com/library/archive/samplecode/OpenCL_NBody_Simulation/Listings/Sources_Model_NBody_Simulation_Core_CPU_NBodySimulationCPU_h.html
archived_at: '2026-07-18T03:17:39.246349Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [OpenCL N-Body Simulation](OpenCL%20N-Body%20Simulation.md)


[Next](Sources-Model-NBody-Simulation-Core-Data-Galaxy-NBodySimulationDataGalaxy.h.md)[Previous](Sources-Model-NBody-Simulation-Core-CPU-NBodySimulationCPU.mm.md)

# Sources/Model/NBody/Simulation/Core/CPU/NBodySimulationCPU.h

```objc
/*
 <codex>
 <abstract>
 Utility class for managing cpu bound computes for n-body simulation.
 </abstract>
 </codex>
 */

#ifndef _NBODY_SIMULATION_CPU_H_
#define _NBODY_SIMULATION_CPU_H_

#import <OpenCL/OpenCL.h>

#import "NBodySimulationDataMediator.h"
#import "NBodySimulationBase.h"

#ifdef __cplusplus

namespace NBody
{
    namespace Simulation
    {
        class CPU : public Base
        {
        public:
            CPU(const Properties& properties,
                const bool& vectorized,
                const bool& threaded = true);

            virtual ~CPU();

            void initialize(const std::string& options);

            GLint reset();
            void  step();
            void  terminate();

            GLint positionInRange(GLfloat* pDst);

            GLint position(GLfloat* pDst);
            GLint velocity(GLfloat* pDst);

            GLint setPosition(const GLfloat * const pSrc);
            GLint setVelocity(const GLfloat * const pSrc);

        private:
            GLint setup(const std::string& options,
                        const bool& vectorized,
                        const bool& threaded = true);

            GLint bind();
            GLint execute();
            GLint restart();

        private:
            bool              mbVectorized;
            bool              mbThreaded;
            bool              mbTerminated;
            GLuint            mnUnits;
            cl_device_id      mpDevice;
            cl_command_queue  mpQueue;
            cl_context        mpContext;
            cl_program        mpProgram;
            cl_kernel         mpKernel;
            Data::Mediator*   mpData;
        }; // CPU
    } // Simulation
} // NBody

#endif

#endif
```

[Next](Sources-Model-NBody-Simulation-Core-Data-Galaxy-NBodySimulationDataGalaxy.h.md)[Previous](Sources-Model-NBody-Simulation-Core-CPU-NBodySimulationCPU.mm.md)

