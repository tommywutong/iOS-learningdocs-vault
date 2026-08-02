---
title: DeferredShading
apple_id: DTS40010088
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2015-07-08'
source_url: https://developer.apple.com/library/archive/samplecode/DeferredShading/Listings/vertexShaderTransform_vs.html
archived_at: '2026-07-18T03:06:13.889177Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [DeferredShading](DeferredShading.md)


[Next](LICENSE.txt.md)[Previous](DeferredShadingAppDelegate.h.md)

# vertexShaderTransform.vs

```
/*
 Copyright (C) 2015 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 The application delegate.
 */

#version 150

uniform mat4 projectionMatrix;
uniform mat4 cameraMatrix;
uniform mat4 orientationMatrix;
uniform vec4 color;

in vec3 inNormal;
in vec4 inPosition;

out vec3 normal, position;
out vec4 frontColor;


void main() {
    mat4 mv = cameraMatrix * orientationMatrix;
    normal = vec3(mv * vec4(inNormal, 0.0));
    position = vec3(mv * inPosition);
    gl_Position = projectionMatrix * mv * inPosition;
    frontColor = color;
}
```

[Next](LICENSE.txt.md)[Previous](DeferredShadingAppDelegate.h.md)

