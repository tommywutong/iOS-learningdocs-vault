---
title: OpenCL N-Body Simulation
apple_id: TP40016610
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenCL
published: '2015-12-10'
source_url: https://developer.apple.com/library/archive/samplecode/OpenCL_NBody_Simulation/Listings/Sources_Model_NBody_Simulation_Core_Data_Random_Split_NBodySimulationDataURDS_mm.html
archived_at: '2026-07-18T03:17:40.276343Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [OpenCL N-Body Simulation](OpenCL%20N-Body%20Simulation.md)


[Next](Sources-Model-NBody-Simulation-Core-Data-Random-Packed-NBodySimulationDataURDP.m.md)[Previous](Sources-Model-NBody-Simulation-Core-Data-Random-Split-NBodySimulationDataURDS.h.md)

# Sources/Model/NBody/Simulation/Core/Data/Random/Split/NBodySimulationDataURDS.mm

```objc
/*
 <codex>
 <import>NBodySimulationDataURDS.h</import>
 </codex>
 */

#import "NBodyConstants.h"
#import "NBodySimulationDataGalaxy.h"
#import "NBodySimulationDataURDS.h"

#pragma mark -
#pragma mark Private - Namespace

using namespace NBody::Simulation::Data;

#pragma mark -
#pragma mark Private - Utilities

void URDS::configExpand()
{
    const GLfloat pscale = m_Scale[0] * std::max(1.0f, mnBCScale);
    const GLfloat vscale = pscale * m_Scale[1];

    dispatch_apply(mnParticles, m_DQueue, ^(size_t i) {
        simd::float3 position = pscale * mpGenerator[eNBodyRandIntervalLenIsTwo]->rand();
        simd::float3 velocity = vscale * position;

        mpPosition[eAxisX][i] = position.x;
        mpPosition[eAxisY][i] = position.y;
        mpPosition[eAxisZ][i] = position.z;

        mpVelocity[eAxisX][i] = velocity.x;
        mpVelocity[eAxisY][i] = velocity.y;
        mpVelocity[eAxisZ][i] = velocity.z;

        mpMass[i] = 1.0f;
    });
} // configExpand

void URDS::configRandom()
{
    const GLfloat pscale = m_Scale[0] * std::max(1.0f, mnBCScale);
    const GLfloat vscale = m_Scale[1] * pscale;

    dispatch_apply(mnParticles, m_DQueue, ^(size_t i) {
        simd::float3 position = pscale * mpGenerator[eNBodyRandIntervalLenIsTwo]->nrand();
        simd::float3 velocity = vscale * mpGenerator[eNBodyRandIntervalLenIsTwo]->nrand();

        mpPosition[eAxisX][i] = position.x;
        mpPosition[eAxisY][i] = position.y;
        mpPosition[eAxisZ][i] = position.z;

        mpMass[i] = 1.0f; // mass

        mpVelocity[eAxisX][i] = velocity.x;
        mpVelocity[eAxisY][i] = velocity.y;
        mpVelocity[eAxisZ][i] = velocity.z;
    });
} // configRandom

void URDS::configShell()
{
    const GLfloat pscale = m_Scale[0];
    const GLfloat vscale = pscale * m_Scale[1];
    const GLfloat inner  = 2.5f * pscale;
    const GLfloat outer  = 4.0f * pscale;
    const GLfloat length = outer - inner;

    dispatch_apply(mnParticles, m_DQueue, ^(size_t i) {
        simd::float3 nrpos    = mpGenerator[eNBodyRandIntervalLenIsTwo]->nrand();
        simd::float3 rpos     = mpGenerator[eNBodyRandIntervalLenIsOne]->rand();
        simd::float3 position = nrpos * (inner + (length * rpos));

        mpPosition[eAxisX][i] = position.x;
        mpPosition[eAxisY][i] = position.y;
        mpPosition[eAxisZ][i] = position.z;

        mpMass[i] = 1.0f;

        simd::float3 axis = m_Axis;

        GLfloat scalar = simd::dot(nrpos, axis);

        if((1.0f - scalar) < 1.0e-6)
        {
            axis.xy = nrpos.yx;

            axis = simd::normalize(axis);
        } // if

        simd::float3 velocity =
        {
            mpPosition[eAxisX][i],
            mpPosition[eAxisY][i],
            mpPosition[eAxisZ][i]
        };

        velocity = vscale * simd::cross(velocity, axis);

        mpVelocity[eAxisX][i] = velocity.x;
        mpVelocity[eAxisY][i] = velocity.y;
        mpVelocity[eAxisZ][i] = velocity.z;
    });
} // configShell

void URDS::configMWM31()
{
    Data::Galaxy galaxy(mnParticles);

    if(galaxy.rows())
    {
        // The Milky-Way (MW) seems to be on a collision course with our
        // neighbour spiral galaxy Andromeda (M31)

        GLfloat pscale = m_Scale[0];
        GLfloat vscale = pscale * m_Scale[1];
        GLfloat mscale = pscale * pscale * pscale;

        GLint numPoints = 0;

        simd::float3 position = 0.0f;
        simd::float3 velocity = 0.0f;

        size_t i = 0;

        while(!galaxy.eof())
        {
            numPoints++;

            std::vector<float> vec = galaxy.floats();

            mpMass[i] = mscale * vec[0];

            position  = {vec[1], vec[2], vec[3]};
            position *= pscale;

            mpPosition[eAxisX][i] = position.x;
            mpPosition[eAxisY][i] = position.y;
            mpPosition[eAxisZ][i] = position.z;

            velocity  = {vec[4], vec[5], vec[6]};
            velocity *= vscale;

            mpVelocity[eAxisX][i] = velocity.x;
            mpVelocity[eAxisY][i] = velocity.y;
            mpVelocity[eAxisZ][i] = velocity.z;

            i++;
        } // while
    } // if
} // configMWM31

#pragma mark -
#pragma mark Public - Interfaces

URDS::URDS(const Properties& rProperties)
: URDB::URDB(rProperties)
{
    mnCount   = GLfloat(mnParticles);
    mnBCScale = mnCount / 1024.0f;
} // Constructor

URDS::~URDS()
{
    mnCount   = 0.0f;
    mnBCScale = 0.0f;
    mpMass    = nullptr;

    mpPosition[eAxisX] = nullptr;
    mpPosition[eAxisY] = nullptr;
    mpPosition[eAxisZ] = nullptr;

    mpVelocity[eAxisX] = nullptr;
    mpVelocity[eAxisY] = nullptr;
    mpVelocity[eAxisZ] = nullptr;
} // Destructor

bool URDS::operator()(Split* pSplit)
{
    bool bSuccess = pSplit != nullptr;

    if(bSuccess)
    {
        mpMass = pSplit->mass();

        mpPosition[eAxisX] = pSplit->position(eAxisX);
        mpPosition[eAxisY] = pSplit->position(eAxisY);
        mpPosition[eAxisZ] = pSplit->position(eAxisZ);

        mpVelocity[eAxisX] = pSplit->velocity(eAxisX);
        mpVelocity[eAxisY] = pSplit->velocity(eAxisY);
        mpVelocity[eAxisZ] = pSplit->velocity(eAxisZ);

        switch(mnConfig)
        {
            case NBody::eConfigShell:
                configShell();
                break;

            case NBody::eConfigMWM31:
                configMWM31();
                break;

            case NBody::eConfigExpand:
                configExpand();
                break;

            case NBody::eConfigRandom:
            default:
                configRandom();
                break;
        } // switch
    } // if

    return bSuccess;
} // operator()
```

[Next](Sources-Model-NBody-Simulation-Core-Data-Random-Packed-NBodySimulationDataURDP.m.md)[Previous](Sources-Model-NBody-Simulation-Core-Data-Random-Split-NBodySimulationDataURDS.h.md)

