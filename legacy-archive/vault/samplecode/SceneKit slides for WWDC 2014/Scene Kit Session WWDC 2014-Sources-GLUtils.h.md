---
title: SceneKit slides for WWDC 2014
apple_id: TP40014551
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2014-10-16'
source_url: https://developer.apple.com/library/archive/samplecode/SceneKitWWDC2014/Listings/Scene_Kit_Session_WWDC_2014_Sources_GLUtils_h.html
archived_at: '2026-07-18T03:23:14.732974Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [SceneKit slides for WWDC 2014](SceneKit%20slides%20for%20WWDC%202014.md)


[Next](Scene%20Kit%20Session%20WWDC%202014-Sources-AAPLView.m.md)[Previous](Scene%20Kit%20Session%20WWDC%202014-Sources-Slides-AAPLSlideDaeOnOSX.m.md)

# Scene Kit Session WWDC 2014/Sources/GLUtils.h

```objc
/*
 Copyright (C) 2014-2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 This file contains some OpenGL utilities
 */

#import <OpenGL/gl.h>
#import <OpenGL/glext.h>

typedef struct {
    GLuint index;
    const char *name;
} AAPLAttribLocation;

// Load, build and link a GLSL program
GLuint AAPLCreateProgramWithNameAndAttributeLocations(NSString *shaderName, AAPLAttribLocation *attribLocations);

// Bind an OpenGL texture
int AAPLBindSampler(int stage, GLint location, GLuint texture, GLenum target);

// Unbind an OpenGL texture
void AAPLUnbindSampler(int stage, GLenum target);
```

[Next](Scene%20Kit%20Session%20WWDC%202014-Sources-AAPLView.m.md)[Previous](Scene%20Kit%20Session%20WWDC%202014-Sources-Slides-AAPLSlideDaeOnOSX.m.md)

