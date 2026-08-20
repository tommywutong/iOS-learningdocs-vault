---
title: OpenCL_OceanWave
apple_id: DTS40009447
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenCL
published: '2011-04-13'
source_url: https://developer.apple.com/library/archive/samplecode/OpenCL_OceanWave/Listings/ocean_simulator_h.html
archived_at: '2026-07-18T03:17:50.449903Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [OpenCL_OceanWave](OpenCLOceanWave.md)


[Next](Document%20Revision%20History.md)[Previous](oceansimulator.cpp.md)

Current information on this Developer Library topic can be found here:

- [Performance > Multiprocessing](https://developer.apple.com/referencelibrary/Performance/idxMultiprocessing-date.html)

# ocean_simulator.h

```c
// Version:    <1.0>
//
// Disclaimer: IMPORTANT:  This Apple software is supplied to you by Apple Inc. ("Apple")
//             in consideration of your agreement to the following terms, and your use,
//             installation, modification or redistribution of this Apple software
//             constitutes acceptance of these terms.  If you do not agree with these
//             terms, please do not use, install, modify or redistribute this Apple
//             software.
//
//             In consideration of your agreement to abide by the following terms, and
//             subject to these terms, Apple grants you a personal, non - exclusive
//             license, under Apple's copyrights in this original Apple software ( the
//             "Apple Software" ), to use, reproduce, modify and redistribute the Apple
//             Software, with or without modifications, in source and / or binary forms;
//             provided that if you redistribute the Apple Software in its entirety and
//             without modifications, you must retain this notice and the following text
//             and disclaimers in all such redistributions of the Apple Software. Neither
//             the name, trademarks, service marks or logos of Apple Inc. may be used to
//             endorse or promote products derived from the Apple Software without specific
//             prior written permission from Apple.  Except as expressly stated in this
//             notice, no other rights or licenses, express or implied, are granted by
//             Apple herein, including but not limited to any patent rights that may be
//             infringed by your derivative works or by other works in which the Apple
//             Software may be incorporated.
//
//             The Apple Software is provided by Apple on an "AS IS" basis.  APPLE MAKES NO
//             WARRANTIES, EXPRESS OR IMPLIED, INCLUDING WITHOUT LIMITATION THE IMPLIED
//             WARRANTIES OF NON - INFRINGEMENT, MERCHANTABILITY AND FITNESS FOR A
//             PARTICULAR PURPOSE, REGARDING THE APPLE SOFTWARE OR ITS USE AND OPERATION
//             ALONE OR IN COMBINATION WITH YOUR PRODUCTS.
//
//             IN NO EVENT SHALL APPLE BE LIABLE FOR ANY SPECIAL, INDIRECT, INCIDENTAL OR
//             CONSEQUENTIAL DAMAGES ( INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
//             SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
//             INTERRUPTION ) ARISING IN ANY WAY OUT OF THE USE, REPRODUCTION, MODIFICATION
//             AND / OR DISTRIBUTION OF THE APPLE SOFTWARE, HOWEVER CAUSED AND WHETHER
//             UNDER THEORY OF CONTRACT, TORT ( INCLUDING NEGLIGENCE ), STRICT LIABILITY OR
//             OTHERWISE, EVEN IF APPLE HAS BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
//
// Copyright ( C ) 2008 Apple Inc. All Rights Reserved.
//
////////////////////////////////////////////////////////////////////////////////////////////////////


#ifndef __OCEAN_SIMULATOR__
#define __OCEAN_SIMULATOR__

////////////////////////////////////////////////////////////////////////////////////////////////////

#include "compute_engine.h"
#include "compute_types.h"
#include "texture.h"
#include "shader.h"

#include <OpenGL/gl.h>
#include <GLUT/glut.h>
#include <OpenCL/opencl.h>
#include <OpenCL/cl_gl.h>
#include "clFFT.h"

#include <time.h>
#include <stdio.h>
#include <math.h>
#include <iostream>
#include <fstream>
#include <vecLib/vDSP.h>
#include <vecLib/vecLib.h>

////////////////////////////////////////////////////////////////////////////////////////////////////

class OceanSimulator
{

public:

    OceanSimulator(
        const int n, 
        const float Wx, 
        const float Wy, 
        const int w = 500, 
        const int h = 500,
        const float speed = 12.0f,
        const float dir = 85.0f);

    virtual ~OceanSimulator() {} 

    void setWindDirection(float v);
    void setWindSpeed(float v);

    float getWindDirection(void)    { return wind_direction; }
    float getWindSpeed(void)        { return wind_speed; }

    virtual int setup(unsigned int bufferId) = 0;
    virtual int step(float dt);

    virtual int initializeWaveSpectrum() = 0;
    virtual int updateFourierCoefficients() = 0;
    virtual int inverseFastFourierTransform() = 0;

    virtual float* getHeightBuffer(void)  { return 0; }
    virtual float* getNormalXBuffer(void) { return 0; }
    virtual float* getNormalYBuffer(void) { return 0; }
    virtual void getBuffer(float2 *data) { return; }

protected:

    int N, m;
    int width;
    int height;
    float WX;
    float WY;
    float time_step;
    float wind_direction;
    float wind_speed;

};

////////////////////////////////////////////////////////////////////////////////////////////////////

class OceanSimulatorCPU : public OceanSimulator
{

public:

    OceanSimulatorCPU(
        const int n, 
        const float wx, 
        const float wy, 
        const int width, 
        const int height,
        const float speed,
        const float direction)
    : 
        OceanSimulator(n, wx, wy, width, height, speed, direction)
    {
        // EMPTY!
    };

    virtual ~OceanSimulatorCPU() {} 

    virtual int setup(unsigned int bufferId);
    virtual int initializeWaveSpectrum();
    virtual int updateFourierCoefficients();
    virtual int inverseFastFourierTransform();

    virtual float* getHeightBuffer(void)  { return ht_cpu.realp; }
    virtual float* getNormalXBuffer(void) { return nx_cpu.realp; }
    virtual float* getNormalYBuffer(void) { return ny_cpu.realp; }

    void getBuffer(float2 *data);

protected:

    unsigned int m_bufferId;

    int curr_threads_cpu;
    COMPLEX_SPLIT ht_cpu;
    COMPLEX_SPLIT nx_cpu;
    COMPLEX_SPLIT ny_cpu;
    float4 *hf0Wg_cpu;
    FFTSetup setup_cpu;
};

////////////////////////////////////////////////////////////////////////////////////////////////////

class OceanSimulatorGPU : public OceanSimulator
{

public:

    OceanSimulatorGPU(
        const int n, 
        const float wx, 
        const float wy, 
        const int width, 
        const int height,
        const float speed,
        const float direction)
    : 
        OceanSimulator(n, wx, wy, width, height, speed, direction)
    {
        // EMPTY!
    };

    virtual ~OceanSimulatorGPU();

    virtual int setup(unsigned int bufferId);
    virtual int initializeWaveSpectrum();
    virtual int updateFourierCoefficients();
    virtual int inverseFastFourierTransform();
    void getBuffer(float2 *data);

    virtual float* getHeightBuffer(void);
    virtual float* getNormalXBuffer(void);
    virtual float* getNormalYBuffer(void);

protected:

    size_t global_size[2];
    size_t local_size[2];
    cl_command_queue compute_commands_gpu;
    cl_device_id compute_device_gpu;
    cl_context compute_context_gpu;
    cl_program compute_program_gpu;
    cl_kernel kernel_advanceintime_gpu;
    float *height_buffer;
    float *normalX;
    float *normalY;
    float *data;

    clFFT_Plan  plan;

    cl_mem h0;
    cl_mem ht;
};

#endif
```

[Next](Document%20Revision%20History.md)[Previous](oceansimulator.cpp.md)

