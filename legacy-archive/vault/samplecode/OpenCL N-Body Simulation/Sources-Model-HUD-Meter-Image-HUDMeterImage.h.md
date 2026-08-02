---
title: OpenCL N-Body Simulation
apple_id: TP40016610
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenCL
published: '2015-12-10'
source_url: https://developer.apple.com/library/archive/samplecode/OpenCL_NBody_Simulation/Listings/Sources_Model_HUD_Meter_Image_HUDMeterImage_h.html
archived_at: '2026-07-18T03:17:37.615268Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [OpenCL N-Body Simulation](OpenCL%20N-Body%20Simulation.md)


[Next](Sources-Model-NBody-Engine-NBodyEngine.h.md)[Previous](Sources-Model-HUD-Meter-Image-HUDMeterImage.mm.md)

# Sources/Model/HUD/Meter/Image/HUDMeterImage.h

```objc
/*
 <codex>
 <abstract>
 Utility class for generating and manging an OpenGl based 2D meter.
 </abstract>
 </codex>
 */

#ifndef _HUD_METER_IMAGE_H_
#define _HUD_METER_IMAGE_H_

#import <string>
#import <unordered_map>

#import <OpenGL/OpenGL.h>

#import "GLUQuad.h"
#import "GLUText.h"

#ifdef __cplusplus

namespace HUD
{
    namespace Meter
    {
        typedef std::string String;

        typedef std::unordered_map<String, GLU::Text *>  Hash;

        class Image
        {
        public:
            Image(const GLsizei& w,
                  const GLsizei& h,
                  const size_t& max,
                  const String& legend);

            virtual ~Image();

            void reset();
            void update();

            void draw(const GLfloat& x,
                      const GLfloat& y);

            void setTarget(const GLdouble& target);

            const GLdouble target() const;

        private:
            GLuint        m_Texture[3];
            GLsizei       mnWidth;
            GLsizei       mnHeight;
            size_t        mnMax;
            GLdouble      mnLimit;
            GLdouble      mnValue;
            GLdouble      mnSmooth;
            CGRect        m_Bounds[3];
            String        m_Legend;
            Hash          m_Hash;
            GLU::Text*    mpLegend;
            GLU::QuadRef  mpQuad;
        }; // Image
    } // Meter
} // HUD

#endif

#endif
```

[Next](Sources-Model-NBody-Engine-NBodyEngine.h.md)[Previous](Sources-Model-HUD-Meter-Image-HUDMeterImage.mm.md)

