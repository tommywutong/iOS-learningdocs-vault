---
title: OpenCL N-Body Simulation
apple_id: TP40016610
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenCL
published: '2015-12-10'
source_url: https://developer.apple.com/library/archive/samplecode/OpenCL_NBody_Simulation/Listings/Sources_Model_NBody_Visualizer_NBodySimulationVisualizer_h.html
archived_at: '2026-07-18T03:17:41.891326Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [OpenCL N-Body Simulation](OpenCL%20N-Body%20Simulation.md)


[Next](Sources-Model-NBody-Visualizer-NBodySimulationVisualizer.mm.md)[Previous](Sources-Model-NBody-Engine-NBodyEngine.mm.md)

# Sources/Model/NBody/Visualizer/NBodySimulationVisualizer.h

```objc
/*
 <codex>
 <abstract>
 A Visualizer mediator object for managing of rendering n-particles to an OpenGL view.
 </abstract>
 </codex>
 */

#ifndef _NBODY_SIMULATION_VISUALIZER_H_
#define _NBODY_SIMULATION_VISUALIZER_H_

#import <Cocoa/Cocoa.h>
#import <OpenGL/OpenGL.h>
#import <simd/simd.h>

#import "GLUGaussian.h"
#import "GLUProgram.h"
#import "GLUTexture.h"

#import "NBodySimulationProperties.h"

#ifdef __cplusplus

namespace NBody
{
    namespace Simulation
    {
        class Visualizer
        {
        public:
            Visualizer(const Properties& rProperties);

            virtual ~Visualizer();

            void reset(const GLuint& nDemo);

            void draw(const GLfloat *pPosition);

            const bool isValid() const;

            const simd::float3& eye() const;

            void stopRotation();
            void toggleRotation();

            void toggleEarthView();

            void setFrame(const CGSize& rFrame);

            void setIsResetting(const bool& bReset);
            void setShowEarthView(const bool& bShowView);

            void setRotation(const CGPoint& rRotation);
            void setRotationChange(const GLfloat& nDelta);
            void setRotationSpeed(const GLfloat& nSpeed);

            void setTimeScale(const GLfloat& nScale);

            void setStarSize(const GLfloat& nSize);
            void setStarScale(const GLfloat& nScale);

            void setViewDistance(const GLfloat& nDistance);
            void setViewRotation(const CGPoint& rRotation);
            void setViewTime(const GLfloat& nTime);
            void setViewZoom(const GLfloat& nZoom);
            void setViewZoomSpeed(const GLfloat& nSpeed);

            bool setProperties(const GLuint& nCount,
                               const Properties * const pProperties);

        public:
            simd::float3 m_Center;
            simd::float3 m_Up;

        private:
            bool buffer(const GLuint& nCount);
            bool textures(CFStringRef pName, CFStringRef pExt, const GLint& nTexRes = 32);
            bool program(CFStringRef pName);

            bool acquire(const Properties& rProperties);

            void lookAt(const GLfloat *pPosition);
            void projection();

            void render(const GLfloat *pPosition);
            void update();

            void advance(const GLuint& nDemo);

        private:
            bool  m_Flag[4];

            simd::float3 m_Eye;

            simd::float4x4 m_ModelView;
            simd::float4x4 m_Projection;

            CGPoint m_ViewRotation;
            CGPoint m_Rotation;
            CGSize  m_Frame;

            GLsizei  m_Bounds[2];
            GLfloat  m_Property[9];
            GLuint   m_Graphic[5];
            GLuint   mnActiveDemo;
            int64_t  mnCount;

            Properties*  mpProperties;

            GLU::Program*  mpProgram;
            GLU::Gaussian* mpGausssian;
            GLU::Texture*  mpTexture;
        }; // Visualizer
    } // SImulation
} // NBody

#endif

#endif
```

[Next](Sources-Model-NBody-Visualizer-NBodySimulationVisualizer.mm.md)[Previous](Sources-Model-NBody-Engine-NBodyEngine.mm.md)

