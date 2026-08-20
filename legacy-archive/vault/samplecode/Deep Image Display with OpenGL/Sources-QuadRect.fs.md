---
title: Deep Image Display with OpenGL
apple_id: TP40016622
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenGL
published: '2015-12-10'
source_url: https://developer.apple.com/library/archive/samplecode/DeepImageDisplayWithOpenGL/Listings/Sources_QuadRect_fs.html
archived_at: '2026-07-18T03:06:08.844270Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Deep Image Display with OpenGL](Deep%20Image%20Display%20with%20OpenGL.md)


[Next](Sources-CGImageCopy.mm.md)[Previous](Sources-GLView.mm.md)

# Sources/QuadRect.fs

```
/*
 Copyright (C) 2015 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 A quad fragment shader for texture rectangle.
 */

#version 410 core

in  vec2 fragTexCoord;
out vec4 fragColor;

uniform sampler2DRect tex;

void main()
{
    fragColor = texture(tex, fragTexCoord);
}
```

[Next](Sources-CGImageCopy.mm.md)[Previous](Sources-GLView.mm.md)

