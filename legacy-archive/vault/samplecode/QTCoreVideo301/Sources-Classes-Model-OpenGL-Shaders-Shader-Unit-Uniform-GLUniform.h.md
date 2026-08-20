---
title: QTCoreVideo301
apple_id: DTS40007785
resource_type: Sample Code
platform: macOS
topic: Audio, Video, & Visual Effects
technology: QuartzCore
published: '2013-07-18'
source_url: https://developer.apple.com/library/archive/samplecode/QTCoreVideo301/Listings/Sources_Classes_Model_OpenGL_Shaders_Shader_Unit_Uniform_GLUniform_h.html
archived_at: '2026-07-18T03:20:45.993677Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [QTCoreVideo301](QTCoreVideo301.md)


[Next](Sources-Classes-Model-OpenGL-Shaders-Shader-Unit-Uniform-GLUniform.mm.md)[Previous](Sources-Classes-Model-OpenGL-Shaders-Shader-Unit-Constants-GLSLUnitDictTypes.h.md)

# Sources/Classes/Model/OpenGL/Shaders/Shader/Unit/Uniform/GLUniform.h

```objc
/*
     File: GLUniform.h
 Abstract: 
 Accessors for uniforms.

  Version: 2.0

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

 Copyright (C) 2013 Apple Inc. All Rights Reserved.

 */

#ifndef _GL_UNIFORM_H_
#define _GL_UNIFORM_H_

#import <Cocoa/Cocoa.h>

#ifdef __cplusplus
extern "C" {
#endif

    void GLUniformSet1i(NSDictionary *pUniform);
    void GLUniformSet2i(NSDictionary *pUniform);
    void GLUniformSet3i(NSDictionary *pUniform);
    void GLUniformSet4i(NSDictionary *pUniform);

    void GLUniformSet1iv(NSDictionary *pUniform);
    void GLUniformSet2iv(NSDictionary *pUniform);
    void GLUniformSet3iv(NSDictionary *pUniform);
    void GLUniformSet4iv(NSDictionary *pUniform);

    void GLUniformSet1f(NSDictionary *pUniform);
    void GLUniformSet2f(NSDictionary *pUniform);
    void GLUniformSet3f(NSDictionary *pUniform);
    void GLUniformSet4f(NSDictionary *pUniform);

    void GLUniformSet1fv(NSDictionary *pUniform);
    void GLUniformSet2fv(NSDictionary *pUniform);
    void GLUniformSet3fv(NSDictionary *pUniform);
    void GLUniformSet4fv(NSDictionary *pUniform);

    void GLUniformSet2x2fv(NSDictionary *pUniform);
    void GLUniformSet3x3fv(NSDictionary *pUniform);
    void GLUniformSet4x4fv(NSDictionary *pUniform);

#ifdef __cplusplus
}
#endif

#endif
```

[Next](Sources-Classes-Model-OpenGL-Shaders-Shader-Unit-Uniform-GLUniform.mm.md)[Previous](Sources-Classes-Model-OpenGL-Shaders-Shader-Unit-Constants-GLSLUnitDictTypes.h.md)

