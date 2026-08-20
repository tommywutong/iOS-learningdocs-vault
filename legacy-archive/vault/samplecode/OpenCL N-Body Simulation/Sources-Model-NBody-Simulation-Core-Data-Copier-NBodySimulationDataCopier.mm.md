---
title: OpenCL N-Body Simulation
apple_id: TP40016610
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenCL
published: '2015-12-10'
source_url: https://developer.apple.com/library/archive/samplecode/OpenCL_NBody_Simulation/Listings/Sources_Model_NBody_Simulation_Core_Data_Copier_NBodySimulationDataCopier_mm.html
archived_at: '2026-07-18T03:17:39.507887Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [OpenCL N-Body Simulation](OpenCL%20N-Body%20Simulation.md)


[Next](Sources-Model-NBody-Simulation-Core-Data-Mediator-NBodySimulationDataMediator.mm.md)[Previous](Sources-Model-NBody-Simulation-Core-Data-Copier-NBodySimulationDataCopier.h.md)

# Sources/Model/NBody/Simulation/Core/Data/Copier/NBodySimulationDataCopier.mm

```objc
/*
 <codex>
 <import>NBodySimulationDataCopier.h</import>
 </codex>
 */

#import "CFQueue.h"

#import "NBodySimulationDataCopier.h"

using namespace NBody::Simulation::Data;

Copier::Copier(const size_t& nCount)
{
    CF::Queue queue;

    mnCount = nCount;
    m_Queue = queue("com.apple.nbody.simulation.data.copier.main");
} // Constructor

Copier::~Copier()
{
    dispatch_release(m_Queue);
} // Destructor

bool Copier::operator()(const Split  * const pSplit,
                        Packed* pPacked)
{
    bool bSuccess = (pSplit != nullptr) && (pPacked != nullptr);

    if(bSuccess)
    {
        GLfloat* pData = pPacked->data();

        const GLfloat * const pMass      = pSplit->mass();
        const GLfloat * const pPositionX = pSplit->position(eAxisX);
        const GLfloat * const pPositionY = pSplit->position(eAxisY);
        const GLfloat * const pPositionZ = pSplit->position(eAxisZ);

        dispatch_apply(mnCount, m_Queue, ^(size_t i) {
            const size_t j = 4 * i;

            pData[j]   = pPositionX[i];
            pData[j+1] = pPositionY[i];
            pData[j+2] = pPositionZ[i];
            pData[j+3] = pMass[i];
        });
    } // if

    return bSuccess;
} // operator()

bool Copier::operator()(const Packed * const pPacked,
                        Split* pSplit)
{
    bool bSuccess = (pSplit != nullptr) && (pPacked != nullptr);

    if(bSuccess)
    {
        const GLfloat * const pData = pPacked->data();

        GLfloat* pMass      = pSplit->mass();
        GLfloat* pPositionX = pSplit->position(eAxisX);
        GLfloat* pPositionY = pSplit->position(eAxisY);
        GLfloat* pPositionZ = pSplit->position(eAxisZ);

        dispatch_apply(mnCount, m_Queue, ^(size_t i) {
            const size_t j = 4 * i;

            pPositionX[i] = pData[j];
            pPositionY[i] = pData[j+1];
            pPositionZ[i] = pData[j+2];
            pMass[i]      = pData[j+3];
        });
    } // if

    return bSuccess;
} // operator()
```

[Next](Sources-Model-NBody-Simulation-Core-Data-Mediator-NBodySimulationDataMediator.mm.md)[Previous](Sources-Model-NBody-Simulation-Core-Data-Copier-NBodySimulationDataCopier.h.md)

