---
title: Deep Image Display with OpenGL
apple_id: TP40016622
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenGL
published: '2015-12-10'
source_url: https://developer.apple.com/library/archive/samplecode/DeepImageDisplayWithOpenGL/Listings/Sources_Quad2D_fs.html
archived_at: '2026-07-18T03:06:08.761364Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Deep Image Display with OpenGL](Deep%20Image%20Display%20with%20OpenGL.md)


[Next](Sources-IOSurface2D.h.md)[Previous](Sources-NSTextFile.h.md)

# Sources/Quad2D.fs

```
/*
 Copyright (C) 2015 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 A quad fragment shader for texture 2D.
 */

#version 410 core

in  vec2 fragTexCoord;
out vec4 fragColor;

uniform sampler2D tex;

void main()
{
    fragColor = texture(tex, fragTexCoord);
}
```

[Next](Sources-IOSurface2D.h.md)[Previous](Sources-NSTextFile.h.md)

