---
title: GL3 Text
apple_id: DTS40013069
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenGL
published: '2014-10-16'
source_url: https://developer.apple.com/library/archive/samplecode/GL3_Text/Listings/Sources_Toolkits_OpenGL_Math_Transforms_GLMTransforms_h.html
archived_at: '2026-07-18T03:09:47.576022Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [GL3 Text](GL3%20Text.md)


[Next](Sources-Toolkits-OpenGL-Math-Transforms-GLMTransforms.mm.md)[Previous](Sources-Toolkits-OpenGL-Math-Constants-GLMConstants.mm.md)

# Sources/Toolkits/OpenGL/Math/Transforms/GLMTransforms.h

```objc
/*
     File: GLMTransforms.h
 Abstract: 
 Utility methods for linear transformations of projective geometry.

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

#ifndef _OPENGL_MATH_TRANSFORMS_H_
#define _OPENGL_MATH_TRANSFORMS_H_

#import <simd/simd.h>
#import <OpenGL/OpenGL.h>

#ifdef __cplusplus

namespace GLM
{
    void uniform(const GLint& location,
                 const bool& transpose,
                 const simd::float4x4& M);

    simd::float4x4 scale(const GLfloat& x,
                         const GLfloat& y,
                         const GLfloat& z);

    simd::float4x4 scale(const simd::float3& s);

    simd::float4x4 translate(const GLfloat& x,
                             const GLfloat& y,
                             const GLfloat& z);

    simd::float4x4 translate(const simd::float3& t);

    simd::float4x4 rotate(const GLfloat& angle,
                          const GLfloat& x,
                          const GLfloat& y,
                          const GLfloat& z);

    simd::float4x4 rotate(const GLfloat& angle,
                          const simd::float3& u);

    simd::float4x4 rotate(const simd::float4& r);

    simd::float4x4 frustum(const GLfloat& left,
                           const GLfloat& right,
                           const GLfloat& bottom,
                           const GLfloat& top,
                           const GLfloat& near,
                           const GLfloat& far);

    simd::float4x4 frustum(const GLfloat& fovy,
                           const GLfloat& width,
                           const GLfloat& heigth,
                           const GLfloat& near,
                           const GLfloat& far);

    simd::float4x4 frustum(const GLfloat& fovy,
                           const GLfloat& aspect,
                           const GLfloat& near,
                           const GLfloat& far);

    simd::float4x4 lookAt(const GLfloat * const pEye,
                          const GLfloat * const pCenter,
                          const GLfloat * const pUp);

    simd::float4x4 lookAt(const simd::float3& eye,
                          const simd::float3& center,
                          const simd::float3& up);

    simd::float4x4 perspective(const GLfloat& fovy,
                               const GLfloat& aspect,
                               const GLfloat& near,
                               const GLfloat& far);

    simd::float4x4 perspective(const GLfloat& fovy,
                               const GLfloat& width,
                               const GLfloat& height,
                               const GLfloat& near,
                               const GLfloat& far);

    simd::float4x4 projection(const GLfloat& fovy,
                              const GLfloat& aspect,
                              const GLfloat& near,
                              const GLfloat& far);

    simd::float4x4 projection(const GLfloat& fovy,
                              const GLfloat& width,
                              const GLfloat& height,
                              const GLfloat& near,
                              const GLfloat& far);

    simd::float4x4 ortho(const GLfloat& left,
                         const GLfloat& right,
                         const GLfloat& bottom,
                         const GLfloat& top,
                         const GLfloat& near,
                         const GLfloat& far);

    simd::float4x4 ortho(const GLfloat& left,
                         const GLfloat& right,
                         const GLfloat& bottom,
                         const GLfloat& top);

    simd::float4x4 ortho(const simd::float3& origin,
                         const simd::float3& size);
} // GLM

#endif

#endif
```

[Next](Sources-Toolkits-OpenGL-Math-Transforms-GLMTransforms.mm.md)[Previous](Sources-Toolkits-OpenGL-Math-Constants-GLMConstants.mm.md)

