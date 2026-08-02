---
title: OpenCL N-Body Simulation
apple_id: TP40016610
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenCL
published: '2015-12-10'
source_url: https://developer.apple.com/library/archive/samplecode/OpenCL_NBody_Simulation/Listings/Sources_Model_Foundation_Frame_CTFrame_h.html
archived_at: '2026-07-18T03:17:36.926868Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [OpenCL N-Body Simulation](OpenCL%20N-Body%20Simulation.md)


[Next](Sources-Model-Foundation-Frame-CTFrame.mm.md)[Previous](Sources-Model-Foundation-Files-NSFile.mm.md)

# Sources/Model/Foundation/Frame/CTFrame.h

```objc
/*
 <codex>
 <abstract>
 Utility calss for generating frames from attributed strings.
 </abstract>
 </codex>
 */

#ifndef _CORE_TEXT_FRAME_H_
#define _CORE_TEXT_FRAME_H_

#import <string>

#import <Cocoa/Cocoa.h>
#import <OpenGL/OpenGL.h>

#ifdef __cplusplus

namespace CT
{
    class Frame
    {
    public:
        // Create a frame with bounds derived from the text size.
        Frame(const std::string& rText,
              const std::string& rFont,
              const GLfloat& nFontSize,
              const CGPoint& rOrigin,
              const CTTextAlignment& nTextAlign = kCTTextAlignmentCenter);

        // Create a frame with bounds derived from the input width and height.
        Frame(const std::string& rText,
              const std::string& rFont,
              const GLfloat& nFontSize,
              const GLsizei& nWidth,
              const GLsizei& nHeight,
              const CTTextAlignment& nTextAlign = kCTTextAlignmentCenter);

        // Create a frame with bounds derived from the text size using
        // helvetica bold or helvetica bold oblique font.
        Frame(const std::string& rText,
              const CGFloat& nFontSize,
              const bool& bIsItalic,
              const CGPoint& rOrigin,
              const CTTextAlignment& nTextAlign = kCTTextAlignmentCenter);

        // Create a frame with bounds derived from input width and height,
        // and using helvetica bold or helvetica bold oblique font.
        Frame(const std::string& rText,
              const CGFloat& nFontSize,
              const bool& bIsItalic,
              const GLsizei& nWidth,
              const GLsizei& nHeight,
              const CTTextAlignment& nTextAlign = kCTTextAlignmentCenter);

        virtual ~Frame();

        const CGRect&  bounds() const;
        const CFRange& range()  const;

        void draw(CGContextRef pContext);

    private:
        void defaults();

        CTFramesetterRef create(const std::string& rText,
                                const std::string& rFont,
                                const GLfloat& nFontSize,
                                const CTTextAlignment& nTextAlign);

        CTFrameRef create(CTFramesetterRef pFrameSetter);

        CTFrameRef create(const CGPoint& rOrigin,
                          const CGSize& rSize,
                          CTFramesetterRef pFrameSetter);

        CTFrameRef create(const GLsizei& nWidth,
                          const GLsizei& nHeight,
                          CTFramesetterRef pFrameSetter);

        CTFrameRef create(const std::string& rText,
                          const std::string& rFont,
                          const GLfloat& nFontSize,
                          const CGPoint& rOrigin,
                          const CTTextAlignment& nTextAlign);

        CTFrameRef create(const std::string& rText,
                          const std::string& rFont,
                          const GLfloat& nFontSize,
                          const GLsizei& nWidth,
                          const GLsizei& nHeight,
                          const CTTextAlignment& nTextAlign);

    private:
        CTFrameRef mpFrame;
        CFRange    m_Range;
        CGRect     m_Bounds;
    }; // Frame
} // CT

#endif

#endif
```

[Next](Sources-Model-Foundation-Frame-CTFrame.mm.md)[Previous](Sources-Model-Foundation-Files-NSFile.mm.md)

