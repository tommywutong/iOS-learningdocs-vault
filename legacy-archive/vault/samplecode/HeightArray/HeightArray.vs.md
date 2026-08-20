---
title: HeightArray
apple_id: DTS40010103
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenGL
published: '2014-06-17'
source_url: https://developer.apple.com/library/archive/samplecode/HeightArray/Listings/HeightArray_vs.html
archived_at: '2026-07-18T03:11:47.801434Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [HeightArray](HeightArray.md)


[Next](HeightArrayAppDelegate.h.md)[Previous](HeightArray.fs.md)

# HeightArray.vs

```
#version 150

in vec3 attribPosition;
in vec3 attribTexCoord;
in vec3 attribNormal;

uniform mat4 cameraMatrix;
uniform mat4 textureMatrix;
uniform mat4 projectionMatrix;

out vec3 normal;
out vec3 texCoord; //3D texture coordinates to index into a 2D texture array

void main()
{
    normal = vec3(cameraMatrix * vec4(attribNormal, 0.0));
    gl_Position = projectionMatrix * cameraMatrix * vec4(attribPosition, 1.0);
    texCoord = vec3(textureMatrix * vec4(attribTexCoord, 1.0));
}
```

[Next](HeightArrayAppDelegate.h.md)[Previous](HeightArray.fs.md)

