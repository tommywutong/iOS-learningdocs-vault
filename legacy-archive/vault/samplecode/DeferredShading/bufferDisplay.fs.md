---
title: DeferredShading
apple_id: DTS40010088
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2015-07-08'
source_url: https://developer.apple.com/library/archive/samplecode/DeferredShading/Listings/bufferDisplay_fs.html
archived_at: '2026-07-18T03:06:11.621845Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [DeferredShading](DeferredShading.md)


[Next](matrixUtil.c.md)[Previous](deferredLighting.fs.md)

# bufferDisplay.fs

```
/*
 Copyright (C) 2015 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 The application delegate.
 */

#version 150

uniform sampler2D displayTex;

in vec3 texCoord;
out vec4 fragColor;

void main()
{
    // Retrieve a color from the texture for the resulting fragment
    fragColor = texture(displayTex, texCoord.st);
}
```

[Next](matrixUtil.c.md)[Previous](deferredLighting.fs.md)

