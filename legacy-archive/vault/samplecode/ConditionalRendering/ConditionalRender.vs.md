---
title: ConditionalRendering
apple_id: DTS40010087
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenGL
published: '2014-06-17'
source_url: https://developer.apple.com/library/archive/samplecode/ConditionalRendering/Listings/ConditionalRender_vs.html
archived_at: '2026-07-18T03:04:13.567730Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [ConditionalRendering](ConditionalRendering.md)


[Next](ConditionalRenderingAppDelegate.h.md)[Previous](ConditionalRender.fs.md)

# ConditionalRender.vs

```
#version 150

in vec3 attribPosition;
in vec3 attribNormal;

uniform float scale;
uniform mat4 modelTransformMatrix;
uniform mat4 cameraMatrix;
uniform mat4 projectionMatrix;
uniform vec4 color;

flat out vec3 normal;
out vec4 eyePos;
out vec4 primaryColor;

void main() {
    mat4 scaleMatrix = mat4(scale);
    scaleMatrix[3].w = 1.0;
    mat4 transform = cameraMatrix * modelTransformMatrix * scaleMatrix;
    mat3 normalTransform = mat3(transform[0].xyz, transform[1].xyz, transform[2].xyz);
    // normal
    normal = normalize(transform * vec4(attribNormal, 0.0)).xyz;
    // position
    eyePos = transform * vec4(attribPosition, 1.0);
    gl_Position = projectionMatrix * eyePos;
    // color
    primaryColor = color;
}
```

[Next](ConditionalRenderingAppDelegate.h.md)[Previous](ConditionalRender.fs.md)

