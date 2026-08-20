---
title: GL3 Text
apple_id: DTS40013069
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenGL
published: '2014-10-16'
source_url: https://developer.apple.com/library/archive/samplecode/GL3_Text/Listings/Sources_Toolkits_OpenGL_Texture_GLUTexture_h.html
archived_at: '2026-07-18T03:09:48.947290Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [GL3 Text](GL3%20Text.md)


[Next](Sources-Toolkits-OpenGL-Texture-GLUTexture.mm.md)[Previous](Sources-Toolkits-OpenGL-Text-GLUText.mm.md)

# Sources/Toolkits/OpenGL/Texture/GLUTexture.h

```objc
/*
     File: GLUTexture.h
 Abstract: 
 Utility toolkit for generating an OpenGL textures from strings.

  Version: 1.2

 Disclaimer: IMPORTANT:  This Apple software is supplied to you by Apple
 Inc. ("Apple") in consideration of your agreement to the following
 terms, and your use, installation, modification or redistribution of
 this Apple software constitutes acceptance of these terms.  If you do
 not agree with these terms, please do not use, install, modify or
 redistribute this Apple software.

 In consideration of your agreement to abide by the following terms, and
 subject to these terms, Apple grants you a personal, non-exclusive
 license, under Apple's copyrights in this original Apple software (the
 "Apple Software"), to use, reproduce, modify and redistribute the Apple
 Software, with or without modifications, in source and/or binary forms;
 provided that if you redistribute the Apple Software in its entirety and
 without modifications, you must retain this notice and the following
 text and disclaimers in all such redistributions of the Apple Software.
 Neither the name, trademarks, service marks or logos of Apple Inc. may
 be used to endorse or promote products derived from the Apple Software
 without specific prior written permission from Apple.  Except as
 expressly stated in this notice, no other rights or licenses, express or
 implied, are granted by Apple herein, including but not limited to any
 patent rights that may be infringed by your derivative works or by other
 works in which the Apple Software may be incorporated.

 The Apple Software is provided by Apple on an "AS IS" basis.  APPLE
 MAKES NO WARRANTIES, EXPRESS OR IMPLIED, INCLUDING WITHOUT LIMITATION
 THE IMPLIED WARRANTIES OF NON-INFRINGEMENT, MERCHANTABILITY AND FITNESS
 FOR A PARTICULAR PURPOSE, REGARDING THE APPLE SOFTWARE OR ITS USE AND
 OPERATION ALONE OR IN COMBINATION WITH YOUR PRODUCTS.

 IN NO EVENT SHALL APPLE BE LIABLE FOR ANY SPECIAL, INDIRECT, INCIDENTAL
 OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
 SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
 INTERRUPTION) ARISING IN ANY WAY OUT OF THE USE, REPRODUCTION,
 MODIFICATION AND/OR DISTRIBUTION OF THE APPLE SOFTWARE, HOWEVER CAUSED
 AND WHETHER UNDER THEORY OF CONTRACT, TORT (INCLUDING NEGLIGENCE),
 STRICT LIABILITY OR OTHERWISE, EVEN IF APPLE HAS BEEN ADVISED OF THE
 POSSIBILITY OF SUCH DAMAGE.

 Copyright (C) 2014 Apple Inc. All Rights Reserved.

 */

// MacOS X

#ifndef _GL_UTILITIES_TEXTURE_H_
#define _GL_UTILITIES_TEXTURE_H_

// Mac OS X frameworks
#import <Cocoa/Cocoa.h>
#import <OpenGL/OpenGL.h>

// OpenGL container types
#import "GLUContainers.h"

#ifdef __cplusplus

namespace GLU
{
    // Generate a texture from a c-string, using a font, at a size,
    // with an alignment and a color
    GLuint Texture2DCreateFromString(const GLchar * const pString,
                                     const GLchar * const pFontName,
                                     const CGFloat& rFontSize,
                                     const CTTextAlignment& rAlignment,
                                     const CGFloat * const pColor,
                                     NSSize& rSize);

    // Generate a texture from a stl string, using a font, at a size,
    // with an alignment and a color
    GLuint Texture2DCreateFromString(const String& rString,
                                     const String& rFontName,
                                     const CGFloat& rFontSize,
                                     const CTTextAlignment& rAlignment,
                                     const CGFloat * const pColor,
                                     NSSize& rSize);

    // Generate a texture from a core foundation string, using a font,
    // at a size, with an alignment and a color
    GLuint Texture2DCreateFromString(CFStringRef pString,
                                     CFStringRef pFontName,
                                     const CGFloat& rFontSize,
                                     const CTTextAlignment& rAlignment,
                                     const CGFloat * const pColor,
                                     NSSize& rSize);

    // Generate a texture from a core foundation attributed string
    GLuint Texture2DCreateFromString(CFAttributedStringRef pAttrString,
                                     const CFRange& rRange,
                                     NSSize& rSize);
} // GLU

#endif

#endif
```

[Next](Sources-Toolkits-OpenGL-Texture-GLUTexture.mm.md)[Previous](Sources-Toolkits-OpenGL-Text-GLUText.mm.md)

