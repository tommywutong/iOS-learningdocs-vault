---
title: OpenCL N-Body Simulation
apple_id: TP40016610
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenCL
published: '2015-12-10'
source_url: https://developer.apple.com/library/archive/samplecode/OpenCL_NBody_Simulation/Listings/Sources_Model_HUD_Button_HUDButton_h.html
archived_at: '2026-07-18T03:17:37.446034Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [OpenCL N-Body Simulation](OpenCL%20N-Body%20Simulation.md)


[Next](Sources-Model-HUD-Meter-Timer-HUDMeterTimer.h.md)[Previous](Sources-Model-HUD-Button-HUDButton.mm.md)

# Sources/Model/HUD/Button/HUDButton.h

```objc
/*
 <codex>
 <abstract>
 Utility class for generating a button in an OpenGL view.
 </abstract>
 </codex>
 */


#ifndef _HUD_BUTTON_H_
#define _HUD_BUTTON_H_

#import <string>

#import "GLUQuad.h"
#import "GLUText.h"

#ifdef __cplusplus

namespace HUD
{
    namespace Button
    {
        typedef std::string Label;
        typedef CGPoint     Position;
        typedef CGRect      Bounds;

        enum Tracking
        {
            eNothing,
            ePressed,
            eUnpressed,
        };

        class Image
        {
        public:
            Image(const Bounds& frame,
                  const CGFloat& size = 24.0f);

            Image(const Bounds& frame,
                  const CGFloat& size,
                  const bool& italic,
                  const Label& label);

            virtual ~Image();

            bool setLabel(const Label& label);

            void draw(const bool& selected,
                      const Position& position,
                      const Bounds& bounds);

        private:
            bool          mbIsItalic;
            GLuint        m_Texture[2];
            GLdouble      mnSize;
            GLsizei       mnWidth;
            GLsizei       mnHeight;
            Label         m_Label;
            GLU::QuadRef  mpQuad;
            GLU::Text    *mpText;
        }; // Image
    } // Button
} // HUD

#endif

#endif
```

[Next](Sources-Model-HUD-Meter-Timer-HUDMeterTimer.h.md)[Previous](Sources-Model-HUD-Button-HUDButton.mm.md)

