---
title: OpenCL_OceanWave
apple_id: DTS40009447
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenCL
published: '2011-04-13'
source_url: https://developer.apple.com/library/archive/samplecode/OpenCL_OceanWave/Listings/main_cpp.html
archived_at: '2026-07-18T03:17:49.872564Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [OpenCL_OceanWave](OpenCLOceanWave.md)


[Next](common-aabb.h.md)[Previous](ReadMe.txt.md)

Current information on this Developer Library topic can be found here:

- [Performance > Multiprocessing](https://developer.apple.com/referencelibrary/Performance/idxMultiprocessing-date.html)

# main.cpp

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

#include <stdlib.h>
#include <GLUT/glut.h>
#include <OpenGL/gl.h>
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <iostream>
#include <fstream>
#include <time.h>
#include <math.h>

#include "timing.h"
#include "camera.h"
#include "ocean_simulator.h"
#include "ocean_renderer.h"

extern int USE_GL_ATTACHMENTS;

////////////////////////////////////////////////////////////////////////////////////////////////////

static OceanSimulatorGPU *SimulatorGPU  = 0;
static OceanSimulatorCPU *SimulatorCPU  = 0;
static OceanSimulator *Simulator        = 0;
static OceanRenderer *Renderer          = 0;
static Camera MainCamera;

////////////////////////////////////////////////////////////////////////////////////////////////////

static int Width                        = 512;
static int Height                       = 512;
static double TimeElapsed               = 0;
static float TimeDelta                  = 0;
static uint FrameCount                  = 0;
static uint ReportStatsInterval         = 100;
static bool Paused                      = false;
static bool Update                      = false;

static float ShadowTextColor[4]         = { 0.0f, 0.0f, 0.0f, 1.0f };
static float HighlightTextColor[4]      = { 0.9f, 0.9f, 0.9f, 1.0f };
static uint TextOffset[2]               = { 25, 25 };

static uint ShowStats                   = 1;
static char StatsString[512]            = "\0";
static uint ShowInfo                    = 1;
static char InfoString[512]             = "\0";

static float CameraFov                  = 45.0f;
static float CameraFarClip              = 1000.0f;
static float CameraNearClip             = 0.1f;

static float3 CameraPosition            = make_float3(0.0f, -42.0f, 0.0f);
static float3 CameraRotation            = make_float3(-25.0f, 180.0f, 0.0f);
const float CameraInertia               = 0.5f;

////////////////////////////////////////////////////////////////////////////////////////////////////

static void DrawString(float x, float y, float color[4], char *buffer)
{
    unsigned int uiLen, i;

    glPushAttrib(GL_LIGHTING_BIT);
    glDisable(GL_LIGHTING);

    glRasterPos2f(x, y);
    glColor3f(color[0], color[1], color[2]);
    uiLen = (unsigned int) strlen(buffer);
    for (i = 0; i < uiLen; i++)
    {
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, buffer[i]);
    }
    glPopAttrib();
}

static void DrawText(float x, float y, int light, char *format, ...)
{
    va_list args;
    char buffer[256];
    GLint iVP[4];
    GLint iMatrixMode;

    va_start(args, format);
    vsprintf(buffer, format, args);
    va_end(args);

    glPushAttrib(GL_LIGHTING_BIT);
    glDisable(GL_LIGHTING);
    glDisable(GL_BLEND);

    glGetIntegerv(GL_VIEWPORT, iVP);
    glViewport(0, 0, Width, Height);
    glGetIntegerv(GL_MATRIX_MODE, &iMatrixMode);

    glMatrixMode(GL_PROJECTION);
    glPushMatrix();
    glLoadIdentity();

    glMatrixMode(GL_MODELVIEW);
    glPushMatrix();
    glLoadIdentity();

    glScalef(2.0f / Width, -2.0f / Height, 1.0f);
    glTranslatef(-Width / 2.0f, -Height / 2.0f, 0.0f);

    if(light)
    {
        glColor4fv(ShadowTextColor);
        DrawString(x-0, y-0, ShadowTextColor, buffer);

        glColor4fv(HighlightTextColor);
        DrawString(x-2, y-2, HighlightTextColor, buffer);
    }
    else
    {
        glColor4fv(HighlightTextColor);
        DrawString(x-0, y-0, HighlightTextColor, buffer);

        glColor4fv(ShadowTextColor);
        DrawString(x-2, y-2, ShadowTextColor, buffer);   
    }

    glPopMatrix();
    glMatrixMode(GL_PROJECTION);

    glPopMatrix();
    glMatrixMode(iMatrixMode);

    glPopAttrib();
    glViewport(iVP[0], iVP[1], iVP[2], iVP[3]);
}

static void
ReportInfo(void)
{
    if(ShowStats)
    {
        int iX = 20;
        int iY = 20;

        DrawText(iX - 1, Height - iY - 1, 0, StatsString);
        DrawText(iX - 2, Height - iY - 2, 0, StatsString);
        DrawText(iX, Height - iY, 1, StatsString);
     }

    if(ShowInfo)
    {
        int iX = TextOffset[0];
        int iY = Height - TextOffset[1];

        DrawText(Width - iX - 1 - strlen(InfoString) * 10, Height - iY - 1, 0, InfoString);
        DrawText(Width - iX - 2 - strlen(InfoString) * 10, Height - iY - 2, 0, InfoString);
        DrawText(Width - iX - strlen(InfoString) * 10, Height - iY, 1, InfoString);

        ShowInfo = (ShowInfo > 200) ? 0 : ShowInfo + 1;
    }
}

static void 
ReportStats(
    uint64_t uiStartTime, uint64_t uiEndTime)
{
    TimeElapsed += SubtractTime(uiEndTime, uiStartTime);

    if(TimeElapsed && FrameCount && FrameCount > ReportStatsInterval) 
    {
        double fMs = (TimeElapsed * 1000.0 / (double) FrameCount);
        double fFps = 1.0 / (fMs / 1000.0);

        sprintf(StatsString, "[%s] Compute: %3.2f ms  Display: %3.2f fps\n", 
                (Simulator == SimulatorGPU) ? "GPU" : "CPU", fMs, fFps);

        glutSetWindowTitle(StatsString);

        FrameCount = 0;
        TimeElapsed = 0;
    }    
}

int Initialize(
    int n, 
    float wx, float wy, 
    int textures, 
    int width, int height,
    float speed, float direction)
{
    Renderer = new OceanRenderer(n, wx, wy, textures, width, height);    
    Renderer->setup();
    Renderer->setExposure(20.0f);
    Renderer->setSunAngle(600.0f);

    SimulatorGPU = new OceanSimulatorGPU(n, wx, wy, width, height, speed, direction); 
    Simulator = SimulatorGPU;
    int err = Simulator->setup(Renderer->getBufferId());
    if(err)
    {
        printf("Failed to initialize CL\n");
        return err;
    }

    MainCamera.setInertia(1.0f);
    MainCamera.setFovInDegrees(CameraFov);
    MainCamera.setNearClip(CameraNearClip);
    MainCamera.setFarClip(CameraFarClip);
    MainCamera.setPosition(CameraPosition);
    MainCamera.setViewport(Width, Height);
    MainCamera.pitch(CameraRotation.x);
    MainCamera.yaw(CameraRotation.y);
    MainCamera.update();

    MainCamera.setInertia(CameraInertia);
    MainCamera.setPosition(CameraPosition);
    MainCamera.update();

    return 0;

}

void Shutdown()
{
    if(Renderer)
        delete Renderer;
    Renderer = 0;

    if(Simulator)
        delete Simulator;
    Simulator = 0;        

    exit(0);

}

void Render(void)
{
    FrameCount++;
    MainCamera.update();

    glFlush();      

    uint64_t start = GetCurrentTime();
    if(Simulator)
    {
        if(!Paused || Update) {
            Simulator->step(0.1f);
        }
    }
    if(Renderer)
    {
        if(Simulator == SimulatorCPU || !USE_GL_ATTACHMENTS)
        {
            Renderer->updateVertexPositions(Simulator->getHeightBuffer());
            Renderer->updateVertexNormals(Simulator->getNormalXBuffer(), Simulator->getNormalYBuffer());
        }

        MainCamera.enable();
        Renderer->render();
        MainCamera.disable();
    }
    ReportInfo();

    glutSwapBuffers();
    uint64_t end = GetCurrentTime();
    TimeDelta = (float)SubtractTime(end, start);

    ReportStats(start, end);
    Update = false;

}

void Resize(int w, int h)
{
    Width = w;
    Height = h;
    if(Renderer)
        Renderer->resize(w, h);
}

void Keyboard(unsigned char key, int x, int y)
{
    switch(key)
    {
        case ' ':
            Paused = !Paused;
            break;

        case '_':
        case '-':
            Simulator->setWindSpeed(Simulator->getWindSpeed() * (1.1f));
            sprintf(InfoString, "WindSpeed = %f\n", Simulator->getWindSpeed());
            ShowInfo = 1;
            break;

        case '+':
        case '=':
            if(Simulator->getWindSpeed() > 1.0f)
                Simulator->setWindSpeed(Simulator->getWindSpeed() * (1.0f / 1.1f));
            sprintf(InfoString, "WindSpeed = %f\n", Simulator->getWindSpeed());
            ShowInfo = 1;
            break;

        case '0':
            Simulator->setWindDirection(Simulator->getWindDirection() * (1.1f));
            sprintf(InfoString, "WindDirection = %f\n", Simulator->getWindDirection());
            ShowInfo = 1;
            break;

        case '9':
            Simulator->setWindDirection(Simulator->getWindDirection() * (1.0f / 1.1f));
            sprintf(InfoString, "WindDirection = %f\n", Simulator->getWindDirection());
            ShowInfo = 1;
            break;

        case ']':
            Renderer->setExposure(Renderer->getExposure() * (1.1f));
            sprintf(InfoString, "Exposure = %f\n", Renderer->getExposure());
            ShowInfo = 1;
            break;

        case '[':
            Renderer->setExposure(Renderer->getExposure() * (1.0f / 1.1f));
            sprintf(InfoString, "Exposure = %f\n", Renderer->getExposure());
            ShowInfo = 1;
            break;

        case 'p':
            Renderer->setSunAngle(Renderer->getSunAngle() * (1.1f));
            ShowInfo = 1;
            break;

        case 'o':
            Renderer->setSunAngle(Renderer->getSunAngle() * (1.0f / 1.1f));
            ShowInfo = 1;
            break;

        case 27:
        case 'q':
            Shutdown();
            break;

        case 'f':
            glutFullScreen();
            break;

    };

    Update = true;
}

/////////////////////////////////////////////////////////////////////////////

int main(int argc, char** argv)
{   
    float speed = 10.0f;
    float direction = 85.0f;

    int n = 512;
    float wx = 100.0f;
    float wy = 100.0f;
    int textures = 1;

    glutInit(&argc, argv);
    glutInitDisplayMode (GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE );
    glutInitWindowPosition (50, 0);
    glutInitWindowSize(Width, Height);
    glutCreateWindow ("");

    CGLContextObj kCGLContext = CGLGetCurrentContext();
    if(CGLSetVirtualScreen(kCGLContext, 0) != kCGLNoError)
    {
        printf("Failed to set virtual screen 0\n");
        return -1;
    }

    int err = Initialize(n, wx, wy, textures, Width, Height, speed, direction);
    if(err)
        return err;
    atexit(Shutdown);
    printf("Starting event loop...\n");

    glutDisplayFunc(Render);
    glutIdleFunc(Render);
    glutReshapeFunc(Resize);
    glutKeyboardFunc(Keyboard);
    glutMainLoop();

    return 0;
}
```

[Next](common-aabb.h.md)[Previous](ReadMe.txt.md)

