---
title: Deep Image Display with OpenGL
apple_id: TP40016622
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenGL
published: '2015-12-10'
source_url: https://developer.apple.com/library/archive/samplecode/DeepImageDisplayWithOpenGL/Listings/Sources_Quad2D_vs.html
archived_at: '2026-07-18T03:06:08.813337Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Deep Image Display with OpenGL](Deep%20Image%20Display%20with%20OpenGL.md)


[Next](Sources-NSBitmap.mm.md)[Previous](Sources-GLProgram.h.md)

# Sources/Quad2D.vs

```
/*
 Copyright (C) 2015 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 A quad vertex shader for texture 2D.
 */

#version 410 core

layout(location = 0) in vec2 vertex;
layout(location = 1) in vec2 texCoord;

out vec2 fragTexCoord;

void main()
{
    gl_Position  = vec4(vertex, 0.0, 1.0);
    fragTexCoord = texCoord;
}
```

[Next](Sources-NSBitmap.mm.md)[Previous](Sources-GLProgram.h.md)

