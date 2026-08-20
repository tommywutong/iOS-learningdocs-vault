---
title: OpenCL_OceanWave
apple_id: DTS40009447
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenCL
published: '2011-04-13'
source_url: https://developer.apple.com/library/archive/samplecode/OpenCL_OceanWave/Listings/ocean_renderer_cpp.html
archived_at: '2026-07-18T03:17:50.028506Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [OpenCL_OceanWave](OpenCLOceanWave.md)


[Next](oceanrenderer.h.md)[Previous](fft-fftsetup.cpp.md)

Current information on this Developer Library topic can be found here:

- [Performance > Multiprocessing](https://developer.apple.com/referencelibrary/Performance/idxMultiprocessing-date.html)

# ocean_renderer.cpp

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


#include "ocean_renderer.h"
#include "data_loader.h"

#include <OpenGL/OpenGL.h>
#include <OpenCL/opencl.h>
#include <GLUT/glut.h>

#define BUFFER_OFFSET(i) ((char*)NULL + (i))

////////////////////////////////////////////////////////////////////////////////////////////////////

#define SEPARATOR ("-------------------------------------------------------------------------------\n")
extern int USE_GL_ATTACHMENTS;

////////////////////////////////////////////////////////////////////////////////////////////////////

static const float inv_cps = 1.0f / CLOCKS_PER_SEC;

static float xangle = 60.0f * 3.14159f / 180.0f;
static float zheight = 20.0f;
static float choppyFac = 0.0f;
static float zscale = 1.0f;

static const float PI = 3.14159265358979;

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

OceanRenderer::OceanRenderer(
    const int n, 
    const float Wx, 
    const float Wy, 
    const int numtex, 
    const int w, 
    const int h)
{
    N = n;
    m = Log2(N);
    WX = Wx;
    WY = Wy;
    width = w;
    height = h;
    exposure = 20.0f;
    sun_angle = 300.0f;
}

OceanRenderer::~OceanRenderer()
{
    glDeleteBuffersARB(1, &buffer);
    free(debugData);
}

void OceanRenderer::setup(void)
{
    debugData = (float *) malloc(4*2*N*N*sizeof(float));
    memset(debugData, 0x0, 4*2*N*N*sizeof(float));

    glClearColor(0.0f, 0.0f, 0.0f, 0.0f);
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
    glEnable(GL_DEPTH_TEST);
    glEnable(GL_TEXTURE_2D);
    glHint(GL_PERSPECTIVE_CORRECTION_HINT, GL_NICEST);
    glColor3f(1.0f, 1.0f, 1.0f);
    glShadeModel(GL_SMOOTH);
    glEnable(GL_MULTISAMPLE_ARB);

    glViewport(0, 0, width, height);
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    gluPerspective(45.0f, 1.0f, 1.0f, 30000.0f);
    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();

    int tri_per_strip = 2 * (N - 1);
    triangle_count = tri_per_strip * (N - 1);
    GLuint *index_buffer = (GLuint *) calloc(3 * triangle_count, sizeof(GLuint));
    float *texcoord_buffer = (float *) calloc(2 * N * N, sizeof(float));

    int count = 0;
    for (int i = 0; i < (N - 1); i++ )
    {
        for (int j = 0; j < (N - 1); j++)
        {
            GLuint ind0 =  i * (GLuint)N + j;
            GLuint ind1 =  (i + 1) * (GLuint)N + j;
            GLuint ind2 =  i * (GLuint)N + (j + 1);
            GLuint ind3 =  (i + 1) * (GLuint)N + (j + 1);
            index_buffer[count++] = ind0;
            index_buffer[count++] = ind1;
            index_buffer[count++] = ind2;
            index_buffer[count++] = ind1;
            index_buffer[count++] = ind2;
            index_buffer[count++] = ind3;
        }
    }

    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            int index = i * N + j;
            texcoord_buffer[2*index]   = (float) i / (float) N;
            texcoord_buffer[2*index+1] = (float) j / (float) N;
        }
    }

    glGenBuffersARB(1, &buffer);
    glGenBuffersARB(1, &indexBuffer);

    glEnableClientState(GL_VERTEX_ARRAY);
    glEnableClientState(GL_TEXTURE_COORD_ARRAY);
    glEnableClientState(GL_INDEX_ARRAY);

    glBindBufferARB(GL_ARRAY_BUFFER_ARB, buffer);

    glBufferDataARB(GL_ARRAY_BUFFER_ARB, 4*2*N*N*sizeof(float), debugData, USE_GL_ATTACHMENTS ? GL_STATIC_DRAW : GL_DYNAMIC_DRAW);
    glBufferSubDataARB(GL_ARRAY_BUFFER_ARB, 6*N*N*sizeof(float), 2*N*N*sizeof(float), texcoord_buffer);

    glVertexPointer(2, GL_FLOAT, 0, 0);
    glTexCoordPointer(2, GL_FLOAT, 0, BUFFER_OFFSET(6*N*N*sizeof(float)));
    glBindBufferARB(GL_ARRAY_BUFFER_ARB, 0);

    glBindBufferARB(GL_ELEMENT_ARRAY_BUFFER_ARB, indexBuffer);
    glBufferDataARB(GL_ELEMENT_ARRAY_BUFFER_ARB, 3*triangle_count*sizeof(unsigned int), index_buffer, GL_STATIC_DRAW_ARB);
    glBindBufferARB(GL_ELEMENT_ARRAY_BUFFER_ARB, 0);

    if(index_buffer) free(index_buffer);
    if(texcoord_buffer) free(texcoord_buffer);

    ocean_shader.loadAndCompile("ocean.vert", "ocean.frag");
    ocean_shader.setUniform4f("WaveConstants", make_float4(WX, WY, choppyFac, zscale));
    ocean_shader.setUniform4f("CameraPosition", camera_position);
    ocean_shader.setUniform1f("Exposure", exposure);
    ocean_shader.setUniform1f("SunAngle", sun_angle);

    GLuint nxIndex = ocean_shader.getVertexAttribLocation("Nx");
    GLuint nyIndex = ocean_shader.getVertexAttribLocation("Ny");
    glEnableVertexAttribArrayARB(nxIndex);
    glEnableVertexAttribArrayARB(nyIndex);  
    glBindBufferARB(GL_ARRAY_BUFFER_ARB, buffer);
    glVertexAttribPointer(nxIndex, 2, GL_FLOAT, GL_FALSE, 0, BUFFER_OFFSET(2*N*N*sizeof(float)));
    glVertexAttribPointer(nyIndex, 2, GL_FLOAT, GL_FALSE, 0, BUFFER_OFFSET(4*N*N*sizeof(float)));
    glBindBufferARB(GL_ARRAY_BUFFER_ARB, 0);

    sky_shader.loadAndCompile("sky.vert", "sky.frag");
    sky_shader.setUniform4f("CameraPosition", camera_position);
    sky_shader.setUniform1f("Exposure", exposure);
    sky_shader.setUniform1f("SunAngle", sun_angle);
}

void OceanRenderer::renderHorizon()
{    
    glDisable(GL_DEPTH_TEST);

    glMatrixMode(GL_MODELVIEW);
    glPushMatrix();
    glLoadIdentity();

    sky_shader.setUniform4f("CameraPosition", camera_position);
    sky_shader.setUniform1f("Exposure", exposure);
    sky_shader.setUniform1f("SunAngle", sun_angle);
    sky_shader.enable();

    glColor4f(1.0f, 1.0f, 1.0f, 1.0f);
    glBegin(GL_QUADS);
    glVertex4f(-1.0f, -1.0f, 1.0f, 1.0f);
    glVertex4f( 1.0f, -1.0f, 1.0f, 1.0f);
    glVertex4f( 1.0f,  1.0f, 1.0f, 1.0f);
    glVertex4f(-1.0f,  1.0f, 1.0f, 1.0f);
    glEnd();

    sky_shader.disable();    

    glPopMatrix();
    glEnable(GL_DEPTH_TEST);

}

void OceanRenderer::renderWaterSurface()
{
    static const float FogColor[4] = { 0.85f, 0.85f, 0.85f, 1.0f };

    glFogfv(GL_FOG_COLOR, FogColor);    
    glFogi(GL_FOG_MODE, GL_EXP2);
    glFogf(GL_FOG_DENSITY, 0.01f);
    glEnable(GL_FOG);

    ocean_shader.setUniform4f("CameraPosition", camera_position);
    ocean_shader.setUniform1f("Exposure", exposure);
    ocean_shader.setUniform1f("SunAngle", sun_angle);
    ocean_shader.enable();
    GLuint nxIndex = ocean_shader.getVertexAttribLocation("Nx");
    GLuint nyIndex = ocean_shader.getVertexAttribLocation("Ny");    

    glBindBufferARB(GL_ARRAY_BUFFER_ARB, buffer);
    glVertexPointer(2, GL_FLOAT, 0, 0);
    glTexCoordPointer(2, GL_FLOAT, 0, BUFFER_OFFSET(6*N*N*sizeof(float)));
    glVertexAttribPointer(nxIndex, 2, GL_FLOAT, GL_FALSE, 0, BUFFER_OFFSET(2*N*N*sizeof(float)));
    glVertexAttribPointer(nyIndex, 2, GL_FLOAT, GL_FALSE, 0, BUFFER_OFFSET(4*N*N*sizeof(float)));

    glBindBufferARB(GL_ELEMENT_ARRAY_BUFFER_ARB, indexBuffer);
    glDrawElements(GL_TRIANGLES, 3*triangle_count, GL_UNSIGNED_INT, 0);
    glBindBuffer(GL_ARRAY_BUFFER_ARB, 0);

    ocean_shader.disable();

    glDisable(GL_FOG);
}

void OceanRenderer::render()
{
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

    renderHorizon();

    glMatrixMode(GL_MODELVIEW);
    glPushMatrix();
    {
        glRotatef(-xangle*180.0 / PI, 0.0f, 0.0f, 0.0f);
        glTranslatef(-0.5f*WX, 0.0f, -zheight / cos(xangle) - 12.0f);
        renderWaterSurface();
    }    
    glPopMatrix();
    glutSwapBuffers();

}

void OceanRenderer::resize(int w, int h)
{
    width = w;
    height = h;
    glViewport(0, 0, width, height);
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    gluPerspective(45, 1.0f, 1, 30000);
    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();
    render();
}


void OceanRenderer::updateVertexPositions(
    const float* ht_cpu_f)
{
    if(ht_cpu_f)
    {
        glBindBufferARB(GL_ARRAY_BUFFER_ARB, buffer);
        float2 *vert1 = (float2 *) glMapBufferARB(GL_ARRAY_BUFFER_ARB, GL_READ_WRITE_ARB);
        for (int i = 0; i < N*N; i++) 
        {
            vert1[i] = float2(ht_cpu_f[i], 0.0f);
        }
        glUnmapBufferARB(GL_ARRAY_BUFFER_ARB);
        glBindBuffer(GL_ARRAY_BUFFER_ARB, 0);
    }
}


void OceanRenderer::updateVertexNormals(
    const float* nx_cpu_f, 
    const float* ny_cpu_f)
{
    if(nx_cpu_f && ny_cpu_f)
    {
        glBindBufferARB(GL_ARRAY_BUFFER_ARB, buffer);
        float2 *norm1 = (float2 *) glMapBufferARB(GL_ARRAY_BUFFER_ARB, GL_READ_WRITE_ARB);
        for (int i = 0; i < N*N; i++)
        {
            norm1[i + N*N]   = float2(nx_cpu_f[i], 0.0f);
            norm1[i + 2*N*N] = float2(ny_cpu_f[i], 0.0f);
        }
        glUnmapBufferARB(GL_ARRAY_BUFFER_ARB);
        glBindBuffer(GL_ARRAY_BUFFER_ARB, 0);
    }
}

void OceanRenderer::debugPrintOut(int flag)
{
    glBindBufferARB(GL_ARRAY_BUFFER_ARB, buffer);
//  float2 *vert = (float2 *) glMapBufferARB(GL_ARRAY_BUFFER_ARB, GL_READ_ONLY_ARB);
    glGetBufferSubDataARB(GL_ARRAY_BUFFER_ARB, 0, 3*2*N*N*sizeof(float), debugData);
    if(flag)
    {
        printf("%f\n", debugData[100]);
        printf("%f\n", debugData[200]);
        printf("%f\n", debugData[300]);
        printf("\n\n");
    }    
   // glUnmapBufferARB(GL_ARRAY_BUFFER_ARB);
    glBindBuffer(GL_ARRAY_BUFFER_ARB, 0);
}


void OceanRenderer::resetBufferData(void)
{
    size_t size = 3*2*N*N*sizeof(float);
    memset(debugData, 0x0, size);
    glBindBufferARB(GL_ARRAY_BUFFER_ARB, buffer);
    glBufferSubDataARB(GL_ARRAY_BUFFER_ARB, 0, size, debugData);
    glBindBuffer(GL_ARRAY_BUFFER_ARB, 0);
}
```

[Next](oceanrenderer.h.md)[Previous](fft-fftsetup.cpp.md)

