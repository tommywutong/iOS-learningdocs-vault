---
title: OpenCL N-Body Simulation
apple_id: TP40016610
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenCL
published: '2015-12-10'
source_url: https://developer.apple.com/library/archive/samplecode/OpenCL_NBody_Simulation/Listings/Sources_Model_NBody_Simulation_Facade_NBodySimulationFacade_h.html
archived_at: '2026-07-18T03:17:41.025489Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [OpenCL N-Body Simulation](OpenCL%20N-Body%20Simulation.md)


[Next](Sources-Model-NBody-Simulation-Mediator-NBodySimulationMediator.mm.md)[Previous](Sources-Model-NBody-Simulation-Facade-NBodySimulationFacade.mm.md)

# Sources/Model/NBody/Simulation/Facade/NBodySimulationFacade.h

```objc
/*
 <codex>
 <abstract>
 A facade for managing cpu or gpu bound simulators, along with their labeled-button.
 </abstract>
 </codex>
 */

#ifndef _NBODY_SIMULATION_FACADE_H_
#define _NBODY_SIMULATION_FACADE_H_

#import "NBodySimulationBase.h"

#ifdef __cplusplus

namespace NBody
{
    namespace Simulation
    {
        enum Types
        {
            eComputeCPUSingle = 0,
            eComputeCPUMulti,
            eComputeGPUPrimary,
            eComputeGPUSecondary,
            eComputeMax
        }; // Types

        class Facade
        {
        public:
            Facade(const Types& nType,
                   const Properties& rProperties);

            virtual ~Facade();

            void start(const bool& paused=true);
            void stop();

            void pause();
            void unpause();

            GLfloat* data();

            Base* simulator();

            void resetProperties(const Properties& rProperties);

            void invalidate(const bool& doInvalidate = true);

            const bool isCPUSingleCore() const;
            const bool isCPUMultiCore()  const;
            const bool isGPUPrimary()    const;
            const bool isGPUSecondary()  const;

            const bool isActive()   const;
            const bool isAcquired() const;
            const bool isPaused()   const;
            const bool isStopped()  const;

            const GLdouble       performance() const;
            const GLdouble       updates()     const;
            const GLdouble       year()        const;
            const size_t         size()        const;
            const std::string&   label()       const;
            const Types&         type()        const;

            void positionInRange(GLfloat *pDst);

            void position(GLfloat *pDst);
            void velocity(GLfloat *pDst);

            void setRange(const GLint& min,
                          const GLint& max);

            void setProperties(const Properties& rProperties);

            void setData(const GLfloat * const pData);

            void setPosition(const GLfloat * const pSrc);
            void setVelocity(const GLfloat * const pSrc);

        private:
            // Acquire a label for the gpu bound simulator
            void setLabel(const GLint& nDevIndex,
                          const GLuint& nDevices,
                          const std::string& rDevice);

            // GPU bound compute
            Base* create(const GLint& nDevIndex,
                         const Properties& rProperties);

            // CPU bound compute
            Base* create(const bool& bIsThreaded,
                         const std::string& rLabel,
                         const Properties& rProperties);

        private:
            bool         mbIsGPU;
            std::string  m_Label;
            Base*        mpSimulator;
            Types        mnType;
        }; // Facade
    } // Simulation
} // NBody

#endif

#endif
```

[Next](Sources-Model-NBody-Simulation-Mediator-NBodySimulationMediator.mm.md)[Previous](Sources-Model-NBody-Simulation-Facade-NBodySimulationFacade.mm.md)

