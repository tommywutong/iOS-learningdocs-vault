---
title: OpenCL N-Body Simulation
apple_id: TP40016610
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenCL
published: '2015-12-10'
source_url: https://developer.apple.com/library/archive/samplecode/OpenCL_NBody_Simulation/Listings/Sources_Model_NBody_Simulation_Core_GPU_NBodySimulationGPU_h.html
archived_at: '2026-07-18T03:17:40.488984Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [OpenCL N-Body Simulation](OpenCL%20N-Body%20Simulation.md)


[Next](Sources-Model-NBody-Simulation-Core-Properties-NBodySimulationProperties.h.md)[Previous](Sources-Model-NBody-Simulation-Core-GPU-NBodySimulationGPU.mm.md)

# Sources/Model/NBody/Simulation/Core/GPU/NBodySimulationGPU.h

```objc
/*
 <codex>
 <abstract>
 Utility class for managing gpu bound computes for n-body simulation.
 </abstract>
 </codex>
 */

#ifndef _NBODY_SIMULATION_GPU_H_
#define _NBODY_SIMULATION_GPU_H_

#import <OpenCL/OpenCL.h>

#import "NBodySimulationBase.h"

#ifdef __cplusplus

namespace NBody
{
    namespace Simulation
    {
        class GPU : public Base
        {
        public:
            GPU(const Properties& rProperties,
                const GLuint& nIndex = 0);

            virtual ~GPU();

            void initialize(const std::string& options);

            GLint reset();
            void  step();
            void  terminate();

            GLint positionInRange(GLfloat *pDst);

            GLint position(GLfloat *pDst);
            GLint velocity(GLfloat *pDst);

            GLint setPosition(const GLfloat * const pSrc);
            GLint setVelocity(const GLfloat * const pSrc);

        private:
            GLint setup(const std::string& options);

            GLint bind();
            GLint execute();
            GLint restart();

        private:
            bool              mbTerminated;
            GLfloat*          mpHostPosition;
            GLfloat*          mpHostVelocity;
            GLuint            mnReadIndex;
            GLuint            mnWriteIndex;
            GLuint            mnWorkItemX;
            GLint             mnDeviceIndex;
            cl_context        mpContext;
            cl_program        mpProgram;
            cl_kernel         mpKernel;
            cl_device_id      mpDevice[2];
            cl_command_queue  mpQueue[2];
            cl_mem            mpDevicePosition[2];
            cl_mem            mpDeviceVelocity[2];
            cl_mem            mpBodyRangeParams;
        }; // GPU
    } // Simulation
} // NBody

#endif

#endif
```

[Next](Sources-Model-NBody-Simulation-Core-Properties-NBodySimulationProperties.h.md)[Previous](Sources-Model-NBody-Simulation-Core-GPU-NBodySimulationGPU.mm.md)

