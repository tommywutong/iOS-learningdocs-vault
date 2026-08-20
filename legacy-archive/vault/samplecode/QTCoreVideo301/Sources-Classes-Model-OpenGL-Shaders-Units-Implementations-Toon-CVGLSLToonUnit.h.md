---
title: QTCoreVideo301
apple_id: DTS40007785
resource_type: Sample Code
platform: macOS
topic: Audio, Video, & Visual Effects
technology: QuartzCore
published: '2013-07-18'
source_url: https://developer.apple.com/library/archive/samplecode/QTCoreVideo301/Listings/Sources_Classes_Model_OpenGL_Shaders_Units_Implementations_Toon_CVGLSLToonUnit_h.html
archived_at: '2026-07-18T03:20:48.565503Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [QTCoreVideo301](QTCoreVideo301.md)


[Next](Sources-Classes-Model-OpenGL-Shaders-Units-Implementations-Toon-CVGLSLToonUnit.m.md)[Previous](Sources-Classes-Model-OpenGL-Shaders-Units-Implementations-Sky-CVGLSLSkyUnit.m.md)

# Sources/Classes/Model/OpenGL/Shaders/Units/Implementations/Toon/CVGLSLToonUnit.h

```objc
/*
     File: CVGLSLToonUnit.h
 Abstract: 
 Utility toolkit for GLSL toon shader.

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

// Required Includes

#import <Cocoa/Cocoa.h>
#import <OpenGL/OpenGL.h>

#import "GLUniformDictionary.h"

#import "CVGLSLUnit.h"

// The OpenGL Toon Shaders

@interface CVGLSLToonUnit : CVGLSLUnit
{
@private
    GLfloat               m_Values[2];
    GLUniformDictionary  *mpUniforms;
} // GLSLToonUnit

+ (id) unit;

+ (id) unitInAppBundle:(NSString *)theName;

+ (id) unitWithDictionary:(NSDictionary *)theDictionary;

- (void) execute:(CVOpenGLTextureRef)theVideo
            flag:(const BOOL)theFlag
          values:(const GLfloat *)theValues;

@end
```

[Next](Sources-Classes-Model-OpenGL-Shaders-Units-Implementations-Toon-CVGLSLToonUnit.m.md)[Previous](Sources-Classes-Model-OpenGL-Shaders-Units-Implementations-Sky-CVGLSLSkyUnit.m.md)

