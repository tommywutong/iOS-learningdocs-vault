---
title: OpenCL_OceanWave
apple_id: DTS40009447
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenCL
published: '2011-04-13'
source_url: https://developer.apple.com/library/archive/samplecode/OpenCL_OceanWave/Listings/ocean_simulator_cpp.html
archived_at: '2026-07-18T03:17:50.215049Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [OpenCL_OceanWave](OpenCLOceanWave.md)


[Next](oceansimulator.h.md)[Previous](oceanrenderer.h.md)

Current information on this Developer Library topic can be found here:

- [Performance > Multiprocessing](https://developer.apple.com/referencelibrary/Performance/idxMultiprocessing-date.html)

# ocean_simulator.cpp

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


#include "ocean_simulator.h"
#include "data_loader.h"

#include <OpenGL/OpenGL.h>
#include <OpenCL/opencl.h>
#include <GLUT/glut.h>
#include <OpenGL/gl.h>

////////////////////////////////////////////////////////////////////////////////////////////////////

#define SEPARATOR ("-------------------------------------------------------------------------------\n")
int USE_GL_ATTACHMENTS = 1;

////////////////////////////////////////////////////////////////////////////////////////////////////

static const float inv_cps = 1.0f / CLOCKS_PER_SEC;
static const float PI = 3.14159265358979f;

////////////////////////////////////////////////////////////////////////////////////////////////////

static void notify_callback(const char *errinfo, const void *private_info, size_t cb, void *user_data)
{
    printf( "%s\n", errinfo );
}

static cl_int GetVirtualScreenCountForCGLContext(CGLContextObj cgl, unsigned int *vs_count) {

   CGLPixelFormatObj pf;
   CGLError cgl_err;
   GLint count = 0;

   // Get the current pixel format
   pf = CGLGetPixelFormat(cgl);
   if(!pf)
     return CL_INVALID_GL_CONTEXT_APPLE;

   // Get the CGL virtual screen count
   cgl_err = CGLDescribePixelFormat(pf, 0, kCGLPFAVirtualScreenCount, &count);
   if(cgl_err || !count)
     return CL_INVALID_GL_CONTEXT_APPLE;

   *vs_count = count;
   return CL_SUCCESS;
}

////////////////////////////////////////////////////////////////////////////////////////////////////

static int Log2(int n)
{
    int i = 0;
    int num = 1;
    for (i = 0; num < n; i++)
        num *= 2;
    return i;
}
////////////////////////////////////////////////////////////////////////////////////////////////////

const float g = 9.81f;
const float A = .00000775f;

float2 RandomNormalComplex()
{
    float x1, x2, w, y1, y2;
    w = 2.0f;

    do
    {
        x1 = 2.0f * rand() / (float) RAND_MAX - 1.0f;
        x2 = 2.0f * rand() / (float) RAND_MAX - 1.0f;
        w = x1 * x1 + x2 * x2;
    }
    while ( w >= 1.0f );

    w = sqrt( (-2.0f * log( w ) ) / w );
    y1 = x1 * w;
    y2 = x2 * w;

    return float2(y1, y2);
}

////////////////////////////////////////////////////////////////////////////////////////////////////

float PhillipsSpectrum(
    const float kx, 
    const float ky, 
    const float WindVel, 
    const float WindDir)
{
    float wDir = WindDir * PI / 180.0f;
    float L = WindVel * WindVel / g;
    float w = L / 75.0f;
    float ksq = kx * kx + ky * ky;
    float kWindDir = kx * cos(wDir) + ky * sin(wDir);
    float ph = A * exp(-1.0f / (L * L * ksq)) * (kWindDir * kWindDir) / (ksq * ksq * ksq);
    float dampFac = exp(-ksq * w * w);
    if (kWindDir < 0.0f)
        ph *= 0.1f;
    return ph*dampFac;
}

void InitialSpectrum(
    float4 *h0Wg,  
    const int N, 
    const float WX, 
    const float WY, 
    const float WindVel, 
    const float WindDir)
{
    float multiplier;
    float2 amplitude;
    float kx, ky;
    float W;

    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            kx = (-N / 2.0f + i) * (2 * PI / WX);
            ky = (-N / 2.0f + j) * (2 * PI / WY);
            W = sqrt(g * sqrt(kx * kx + ky * ky));
            if ((i == N / 2) && (j == N / 2))
                multiplier = 0.0f;
            else
                multiplier = sqrt(PhillipsSpectrum(kx, ky, WindVel, WindDir));
            amplitude = RandomNormalComplex();
            h0Wg[i*N+j] = float4(amplitude[0] * multiplier, amplitude[1] * multiplier, W, 0.0f);
        }
    }
}

////////////////////////////////////////////////////////////////////////////////////////////////////

OceanSimulator::OceanSimulator(
    const int n, 
    const float Wx, 
    const float Wy, 
    const int w, 
    const int h,
    const float speed,
    const float direction)
{
    N = n;
    m = Log2(N);
    WX = Wx;
    WY = Wy;
    width = w;
    height = h;
    wind_direction = direction;
    wind_speed = speed;
    time_step = 0.0f;
}

int OceanSimulator::step(float dt)
{
    time_step += dt;
    updateFourierCoefficients();
    inverseFastFourierTransform();
    return 0;
}

void 
OceanSimulator::setWindDirection(float v)
{
    wind_direction = v;
   initializeWaveSpectrum();
}

void 
OceanSimulator::setWindSpeed(float v)
{
    wind_speed = v;
    initializeWaveSpectrum();
}

////////////////////////////////////////////////////////////////////////////////////////////////////

int OceanSimulatorCPU::setup(unsigned int bufferId)
{
    m_bufferId = bufferId;

    hf0Wg_cpu                   = (float4*) malloc(N * N * sizeof(float4));
    ht_cpu.realp                = (float*) malloc(N * N * sizeof(float));
    ht_cpu.imagp                = (float*) malloc(N * N * sizeof(float));
    nx_cpu.realp                = (float*) malloc(N * N * sizeof(float));
    nx_cpu.imagp                = (float*) malloc(N * N * sizeof(float));
    ny_cpu.realp                = (float*) malloc(N * N * sizeof(float));
    ny_cpu.imagp                = (float*) malloc(N * N * sizeof(float));
    setup_cpu                   = vDSP_create_fftsetup(m, FFT_RADIX2);

    initializeWaveSpectrum();

    return 0;
}

int OceanSimulatorCPU::initializeWaveSpectrum()
{
    float4 *h0Wg = (float4 *) malloc(N * N * sizeof(float4));
    InitialSpectrum(h0Wg,  N, WX, WY, wind_speed, wind_direction);
    memcpy(hf0Wg_cpu, h0Wg, N*N*sizeof(float4));
    free(h0Wg);
    return 0;
}

int OceanSimulatorCPU::updateFourierCoefficients()
{

    int i, j, mi, mj, index;
    float wt, cs, sn, h1r, h1i, h2r, h2i, hor, hoi;
    float2 H1, H2, temp, temp2;
    float kx, ky;

    for (i = 0; i < N; i++)
    {
        for (j = 0; j < N; j++)
        {
            int ii = (i + N/2) % N;
            int jj = (j + N/2) % N;
            int indexo = ii*N + jj;
            index = i * N + j;
            mi = (N - i) % N;
            mj = (N - j) % N;
            float4 h0Wg1 = hf0Wg_cpu[index];
            float4 h0Wg2 = hf0Wg_cpu[mi*N+mj];
            wt = h0Wg1[2] * time_step;
            cs = cos(wt);
            sn = sin(wt);
            H1 = float2(h0Wg1[0], h0Wg1[1]);
            H2 = float2(h0Wg2[0], h0Wg2[1]);
            h1r = H1[0];
            h1i = H1[1];
            h2r = H2[0];
            h2i = H2[1];

            hor = h1r * cs - h1i * sn + h2r * cs - h2i * sn;
            hoi = h1r * sn + h1i * cs - h2r * sn - h2i * cs;
            temp = float2(hor, hoi);
            kx = (2.0f * PI / WX) * ((float) i - (float) N / 2.0f);
            ky = (2.0f * PI / WY) * ((float) j - (float) N / 2.0f);         

            temp2 = float2(temp[1], -temp[0]);
            ht_cpu.realp[indexo] = temp[0];
            ht_cpu.imagp[indexo] = temp[1];
            float2 temp3 = temp2 * kx;
            float2 temp4 = temp2 * ky;
            nx_cpu.realp[indexo] = temp3[0];
            nx_cpu.imagp[indexo] = temp3[1];
            ny_cpu.realp[indexo] = temp4[0];
            ny_cpu.imagp[indexo] = temp4[1];
        }
    }

    return 0;
}

int OceanSimulatorCPU::inverseFastFourierTransform()
{
    vDSP_fft2d_zip(setup_cpu, &ht_cpu, 1, 0, m, m, FFT_INVERSE);
    vDSP_fft2d_zip(setup_cpu, &nx_cpu, 1, 0, m, m, FFT_INVERSE);
    vDSP_fft2d_zip(setup_cpu, &ny_cpu, 1, 0, m, m, FFT_INVERSE);
    return 0;
}

void OceanSimulatorCPU::getBuffer(float2 *data)
{
    for(int i = 0; i < N*N; i++) 
    {
        data[i]         = make_float2(ht_cpu.realp[i], ht_cpu.imagp[i]);
        data[i + N*N]   = make_float2(nx_cpu.realp[i], nx_cpu.imagp[i]);
        data[i + 2*N*N] = make_float2(ny_cpu.realp[i], ny_cpu.imagp[i]);
    }
}


////////////////////////////////////////////////////////////////////////////////////////////////////

OceanSimulatorGPU::~OceanSimulatorGPU()
{

}

int OceanSimulatorGPU::setup(unsigned int bufferId)
{
    size_t              returned_size;
    int                 err;

    int arg = 0;

    global_size[0] = N;
    global_size[1] = N;

    local_size[0] = 16;
    local_size[1] = 16;

    if(USE_GL_ATTACHMENTS) {
        printf(SEPARATOR);

        CGLContextObj kCGLContext = CGLGetCurrentContext();
        CGLShareGroupObj share_group = CGLGetShareGroup(kCGLContext);
        cl_context_properties properties[] = { CL_CONTEXT_PROPERTY_USE_CGL_SHAREGROUP_APPLE, (cl_context_properties)share_group, 0 };
        compute_context_gpu = clCreateContext(properties, 0, 0, notify_callback, 0, 0);
        if(!compute_context_gpu)
            return -2;      

        unsigned int screen_count;
        GetVirtualScreenCountForCGLContext(kCGLContext, &screen_count);

        if(screen_count > 1) {

            printf("Multiple GPUs found\n");

            cl_device_id compute_device   = NULL;
            cl_device_id rendering_device = NULL;
            compute_device_gpu            = NULL;

            int compute_virtual_screen   = 0;
            int rendering_virtual_screen = 0;

            if(CGLSetVirtualScreen(kCGLContext, compute_virtual_screen) != kCGLNoError)
            {
                printf("Failed to set virtual screen %d\n", compute_virtual_screen);
                return -1;
            }

            err = clGetGLContextInfoAPPLE(compute_context_gpu, kCGLContext, CL_CGL_DEVICE_FOR_CURRENT_VIRTUAL_SCREEN_APPLE, sizeof( cl_device_id ), &compute_device, NULL);
            if( err != CL_SUCCESS || !compute_device )
            {
                printf("Unable to get CL_CGL_DEVICE_FOR_CURRENT_VIRTUAL_SCREEN_APPLE list from context: %d", err );
                return -1;
            }

            if(CGLSetVirtualScreen(kCGLContext, rendering_virtual_screen) != kCGLNoError)
            {
                printf("Failed to set virtual screen %d\n", rendering_virtual_screen);
                return -1;
            }

            err = clGetGLContextInfoAPPLE(compute_context_gpu, kCGLContext, CL_CGL_DEVICE_FOR_CURRENT_VIRTUAL_SCREEN_APPLE, sizeof( cl_device_id ), &rendering_device, NULL);
            if( err != CL_SUCCESS || !rendering_device )
            {
                printf("Unable to get CL_CGL_DEVICE_FOR_CURRENT_VIRTUAL_SCREEN_APPLE list from context: %d", err );
                return -1;
            }           

            char device_name[100];
            char device_vendor[100];
            char device_version[100];

            err  = clGetDeviceInfo( compute_device, CL_DEVICE_NAME,    sizeof( device_name ),    device_name,    NULL );
            err |= clGetDeviceInfo( compute_device, CL_DEVICE_VENDOR,  sizeof( device_vendor ),  device_vendor,  NULL );
            err |= clGetDeviceInfo( compute_device, CL_DEVICE_VERSION, sizeof( device_version ), device_version, NULL );
            if( err )
            {
                printf("Unable to get device info for compute device: %d", err );
                return -1;
            }

            printf("Using device[%d] for compute: %s %s %s\n", compute_virtual_screen, device_vendor, device_name, device_version);

            err  = clGetDeviceInfo( rendering_device, CL_DEVICE_NAME,    sizeof( device_name ),    device_name,    NULL );
            err |= clGetDeviceInfo( rendering_device, CL_DEVICE_VENDOR,  sizeof( device_vendor ),  device_vendor,  NULL );
            err |= clGetDeviceInfo( rendering_device, CL_DEVICE_VERSION, sizeof( device_version ), device_version, NULL );
            if( err )
            {
                printf("Unable to get device info for rendering device: %d", err );
                return -1;
            }

            printf("Using device[%d] for rendering: %s %s %s\n", rendering_virtual_screen, device_vendor, device_name, device_version);

            compute_device_gpu = compute_device;
        }
        else {

            compute_device_gpu = NULL;          
            err = clGetGLContextInfoAPPLE(compute_context_gpu, kCGLContext, 
                                        CL_CGL_DEVICE_FOR_CURRENT_VIRTUAL_SCREEN_APPLE, 
                                        sizeof( cl_device_id ), &compute_device_gpu, NULL);
            if( err != CL_SUCCESS || !compute_device_gpu )
            {
                printf("Unable to get CL_CGL_DEVICE_FOR_CURRENT_VIRTUAL_SCREEN_APPLE list from context: %d", err );
                return -1;
            }
        }   
    }
    else {
        err = clGetDeviceIDs(NULL, CL_DEVICE_TYPE_GPU, 1, &compute_device_gpu, NULL);
        if (err != CL_SUCCESS)
        {
            printf("Error: Failed to locate compute device!\n");
            return EXIT_FAILURE;
        }

        compute_context_gpu = clCreateContext(0, 1, &compute_device_gpu, notify_callback, NULL, &err);
        if (!compute_context_gpu)
        {
            printf("Error: Failed to create a compute context!\n");
            return EXIT_FAILURE;
        }
    }

    compute_commands_gpu = clCreateCommandQueue(compute_context_gpu, compute_device_gpu, 0, &err);
    if (!compute_commands_gpu)
    {
        printf("Error: Failed to create a command queue!\n");
        return EXIT_FAILURE;
    }

    // Report the device vendor and device name
    // 
    cl_char vendor_name[1024] = {0};
    cl_char device_name[1024] = {0};
    err = clGetDeviceInfo(compute_device_gpu, CL_DEVICE_VENDOR, sizeof(vendor_name), vendor_name, &returned_size);
    err|= clGetDeviceInfo(compute_device_gpu, CL_DEVICE_NAME, sizeof(device_name), device_name, &returned_size);
    if (err != CL_SUCCESS)
    {
        printf("Error: Failed to retrieve device info!\n");
        return EXIT_FAILURE;
    }

    printf(SEPARATOR);
    printf("Connecting to %s %s...\n", vendor_name, device_name);

    h0 = clCreateBuffer(compute_context_gpu, CL_MEM_READ_WRITE, sizeof(float4)*N*N, NULL, &err);
    if(!h0)
    {
        printf("Failed to create h0! %d\n", err);
        return EXIT_FAILURE;
    }


    if(USE_GL_ATTACHMENTS) {

        ht = clCreateFromGLBuffer(compute_context_gpu, CL_MEM_READ_WRITE, bufferId, &err);
        if (!ht || err != CL_SUCCESS)
        {
            printf("Failed to create ht! %d\n", err);
            return EXIT_FAILURE;
        }
    }
    else {

        ht = clCreateBuffer(compute_context_gpu, CL_MEM_READ_WRITE, sizeof(float2)*N*N*3, NULL, &err);
        if(!ht)
        {
            printf("Failed to create ht! %d\n", err);
            return EXIT_FAILURE;
        }
    }

    size_t src_len = 0;;
    char* source = 0;
    LoadTextFromFile("compute_kernels.cl", &source, &src_len);
    compute_program_gpu = clCreateProgramWithSource(compute_context_gpu, 1, (const char **) & source, NULL, &err);
    if (!compute_program_gpu || err != CL_SUCCESS)
    {
        printf("Error: Failed to create compute program! %d\n", err);
        return EXIT_FAILURE;
    }

    printf(SEPARATOR);
    printf("Building compute program...\n");
    err = clBuildProgram(compute_program_gpu, 0, NULL, NULL, NULL, NULL);
    if (err != CL_SUCCESS)
    {
        size_t len;
        char buffer[2048];

        printf("Error: Failed to build program executable!\n");
        clGetProgramBuildInfo(compute_program_gpu, compute_device_gpu, CL_PROGRAM_BUILD_LOG, sizeof(buffer), buffer, &len);
        printf("%s\n", buffer);
        return EXIT_FAILURE;
    }

    printf(SEPARATOR);
    printf("Building compute kernels...\n");

    kernel_advanceintime_gpu = clCreateKernel(compute_program_gpu, "advanceintime", &err);

    if (!kernel_advanceintime_gpu)
    {
        printf("Failed to create kernels!\n");
        return -1;
    }  

    float twoPiOverWX = 2.0f * M_PI / WX;
    float twoPiOverWY = 2.0f * M_PI / WY;
    int m = (int) log2(N);

    if(USE_GL_ATTACHMENTS) {
        err = CL_SUCCESS;
        err |= clEnqueueAcquireGLObjects(compute_commands_gpu, 1, &ht, 0, NULL, NULL);
        if (err != CL_SUCCESS)
        {
            printf("Failed to acquire OpenGL objects!\n");
            return -1;
        }
    }

    float2 *zero = (float2 *) malloc(sizeof(float2)*N*N*3);
    memset(zero, 0, sizeof(float2)*N*N*3);
    err = clEnqueueWriteBuffer(compute_commands_gpu, ht, CL_TRUE, 0, sizeof(float2)*N*N*3, zero, 0, NULL, NULL);
    if (err != CL_SUCCESS)
        return -1;  
    free(zero);

    initializeWaveSpectrum();

    arg = 0;
    err = CL_SUCCESS;
    err |= clSetKernelArg(kernel_advanceintime_gpu, arg++, sizeof(cl_mem), &h0);
    err |= clSetKernelArg(kernel_advanceintime_gpu, arg++, sizeof(cl_mem), &ht);
    err |= clSetKernelArg(kernel_advanceintime_gpu, arg++, sizeof(float),  &twoPiOverWX);
    err |= clSetKernelArg(kernel_advanceintime_gpu, arg++, sizeof(float),  &twoPiOverWY);
    err |= clSetKernelArg(kernel_advanceintime_gpu, arg++, sizeof(int),    &N);
    err |= clSetKernelArg(kernel_advanceintime_gpu, arg++, sizeof(int),    &m);
    err |= clSetKernelArg(kernel_advanceintime_gpu, arg++, sizeof(float),  &time_step);
    if (err != CL_SUCCESS)
    {
        printf("Failed to set kernel arguments!\n");
        return -1;
    }

    if(USE_GL_ATTACHMENTS) {
        err = clEnqueueReleaseGLObjects(compute_commands_gpu, 1, &ht, 0, NULL, NULL);
        if(err != CL_SUCCESS)
        {
            printf("Failed to release OpenGL object!\n");
            return -1;
        }
    }   

    clFFT_Dim3 NN = (clFFT_Dim3) { N, N, 1 };
    plan = clFFT_CreatePlan(compute_context_gpu, NN, clFFT_2D, clFFT_InterleavedComplexFormat, &err);
    if(!plan || err)
    {
        printf("Failed to create fft plan!\n");
        return -1;
    }

    if(USE_GL_ATTACHMENTS) {
        height_buffer = NULL;
        normalX       = NULL;
        normalY       = NULL;
        data          = NULL;
    }
    else {
        height_buffer = (float *) malloc(sizeof(float)*N*N);
        normalX       = (float *) malloc(sizeof(float)*N*N);
        normalY       = (float *) malloc(sizeof(float)*N*N);
        data          = (float *) malloc(sizeof(float2)*N*N);
    }

    return 0;
}

int OceanSimulatorGPU::initializeWaveSpectrum()
{
    float4 *h0Wg = (float4 *) malloc(N * N * sizeof(float4));
    InitialSpectrum(h0Wg,  N, WX, WY, wind_speed, wind_direction);

    int err = clEnqueueWriteBuffer(compute_commands_gpu, h0, CL_TRUE, 0, sizeof(float4)*N*N, h0Wg, 0, NULL, NULL);
    if (err != CL_SUCCESS)
        return -1;

    free(h0Wg);
    return 0;
}

int OceanSimulatorGPU::updateFourierCoefficients()
{
    int          err;

    if(USE_GL_ATTACHMENTS) {
        err = CL_SUCCESS;
        err |= clEnqueueAcquireGLObjects(compute_commands_gpu, 1, &ht, 0, NULL, NULL);
        if (err != CL_SUCCESS)
        {
            printf("Failed to acquire OpenGL objects!\n");
            return -1;
        }
    }   

    err = CL_SUCCESS;
    err |= clSetKernelArg(kernel_advanceintime_gpu, 6, sizeof(float), &time_step);
    if (err != CL_SUCCESS)
    {
        printf("Failed to set kernel arguments!\n");
        return -1;
    }

    err = clEnqueueNDRangeKernel(compute_commands_gpu, kernel_advanceintime_gpu, 2, NULL, global_size, local_size, 0, NULL, NULL);
    if (err != CL_SUCCESS)
    {
        printf("Failed to enqueue kernel! %d\n", err);
        return EXIT_FAILURE;
    }

    return 0;
}

void OceanSimulatorGPU::getBuffer(float2 *data)
{
    int err = clEnqueueReadBuffer(compute_commands_gpu, ht, CL_TRUE, 0, sizeof(float2)*3*N*N, data, 0, NULL, NULL);
    if(err)
        printf("failed to read");
}

int OceanSimulatorGPU::inverseFastFourierTransform()
{
    int err = clFFT_ExecuteInterleaved(compute_commands_gpu, plan, 3, clFFT_Inverse, ht, ht, 0, NULL, NULL);

    if(USE_GL_ATTACHMENTS) {

        err = clEnqueueReleaseGLObjects(compute_commands_gpu, 1, &ht, 0, NULL, NULL);
        if(err != CL_SUCCESS)
        {
            printf("Failed to release OpenGL object!\n");
            return -1;
        }
    }   

    err = clFinish(compute_commands_gpu);

    return err;
}


float* OceanSimulatorGPU::getHeightBuffer(void)
{
    int err = clEnqueueReadBuffer(compute_commands_gpu, ht, CL_TRUE, 0, sizeof(float2)*N*N, data, 0, NULL, NULL);
    if(err)
        printf("failed to read");   

    int i;
    for(i = 0; i < N*N; i++)
        height_buffer[i] = data[2*i];

    return height_buffer;   
}

float* OceanSimulatorGPU::getNormalXBuffer(void)
{
    int err = clEnqueueReadBuffer(compute_commands_gpu, ht, CL_TRUE, N*N*sizeof(float2), sizeof(float2)*N*N, data, 0, NULL, NULL);
    if(err)
        printf("failed to read");   

    int i;
    for(i = 0; i < N*N; i++)
        normalX[i] = data[2*i];

    return normalX; 
}

float* OceanSimulatorGPU::getNormalYBuffer(void)
{
    int err = clEnqueueReadBuffer(compute_commands_gpu, ht, CL_TRUE, 2*N*N*sizeof(float2), sizeof(float2)*N*N, data, 0, NULL, NULL);
    if(err)
        printf("failed to read");   

    int i;
    for(i = 0; i < N*N; i++)
        normalY[i] = data[2*i];

    return normalY; 
}
```

[Next](oceansimulator.h.md)[Previous](oceanrenderer.h.md)

