---
title: OpenCL N-Body Simulation
apple_id: TP40016610
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenCL
published: '2015-12-10'
source_url: https://developer.apple.com/library/archive/samplecode/OpenCL_NBody_Simulation/Listings/Sources_Model_OpenGL_Utilities_Text_GLUText_h.html
archived_at: '2026-07-18T03:17:43.245140Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [OpenCL N-Body Simulation](OpenCL%20N-Body%20Simulation.md)


[Next](Sources-Model-OpenGL-Utilities-Text-GLUText.mm.md)[Previous](Sources-Model-OpenGL-Utilities-Quad-GLUQuad.mm.md)

# Sources/Model/OpenGL/Utilities/Text/GLUText.h

```objc
/*
 <codex>
 <abstract>
 Utility methods for generating OpenGL texture from a string.
 </abstract>
 </codex>
 */

#ifndef _OPENGL_UTILITY_TEXT_H_
#define _OPENGL_UTILITY_TEXT_H_

#import <string>

#import <Cocoa/Cocoa.h>
#import <OpenGL/OpenGL.h>

#import "CTFrame.h"
#import "GLcontainers.h"

#ifdef __cplusplus

namespace GLU
{
    class Text
    {
    public:
        // Create a texture with bounds derived from the text size.
        Text(const GLstring& rText,
             const GLstring& rFont,
             const GLfloat& nFontSize,
             const CGPoint& rOrigin,
             const CTTextAlignment& nTextAlign = kCTTextAlignmentCenter);

        // Create a texture with bounds derived from the input width and height.
        Text(const GLstring& rText,
             const GLstring& rFont,
             const GLfloat& nFontSize,
             const GLsizei& nWidth,
             const GLsizei& nHeight,
             const CTTextAlignment& nTextAlign = kCTTextAlignmentCenter);

        // Create a texture with bounds derived from the text size using
        // helvetica bold or helvetica bold oblique font.
        Text(const GLstring& rText,
             const CGFloat& nFontSize,
             const bool& bIsItalic,
             const CGPoint& rOrigin,
             const CTTextAlignment& nTextAlign = kCTTextAlignmentCenter);

        // Create a texture with bounds derived from input width and height,
        // and using helvetica bold or helvetica bold oblique font.
        Text(const GLstring& rText,
             const CGFloat& nFontSize,
             const bool& bIsItalic,
             const GLsizei& nWidth,
             const GLsizei& nHeight,
             const CTTextAlignment& nTextAlign = kCTTextAlignmentCenter);

        virtual ~Text();

        const GLuint&  texture() const;
        const CGRect&  bounds()  const;
        const CFRange& range()   const;

    private:
        CGContextRef create(const GLsizei& nWidth,
                            const GLsizei& nHeight);

        CGContextRef create(const CGSize& rSize);

        GLuint create(CGContextRef pContext);

        GLuint create(const GLstring& rText,
                      const GLstring& rFont,
                      const GLfloat& nFontSize,
                      const CGPoint& rOrigin,
                      const CTTextAlignment& nTextAlign);

        GLuint create(const GLstring& rText,
                      const GLstring& rFont,
                      const GLfloat& nFontSize,
                      const GLsizei& nWidth,
                      const GLsizei& nHeight,
                      const CTTextAlignment& nTextAlign);

    private:
        GLuint   mnTexture;
        CGRect   m_Bounds;
        CFRange  m_Range;
    }; // Text
} // GLU

#endif

#endif
```

[Next](Sources-Model-OpenGL-Utilities-Text-GLUText.mm.md)[Previous](Sources-Model-OpenGL-Utilities-Quad-GLUQuad.mm.md)

