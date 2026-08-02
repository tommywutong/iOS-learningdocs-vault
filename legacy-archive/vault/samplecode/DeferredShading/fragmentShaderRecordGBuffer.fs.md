---
title: DeferredShading
apple_id: DTS40010088
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2015-07-08'
source_url: https://developer.apple.com/library/archive/samplecode/DeferredShading/Listings/fragmentShaderRecordGBuffer_fs.html
archived_at: '2026-07-18T03:06:11.727398Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [DeferredShading](DeferredShading.md)


[Next](teapot.h.md)[Previous](renderer.h.md)

# fragmentShaderRecordGBuffer.fs

```
/*
 Copyright (C) 2015 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 The application delegate.
 */

#version 150

in vec3 normal, position;
in vec4 frontColor;

out vec4 fragColor;
out vec3 fragPosition;
out vec2 fragNormal;

void main()
{
    vec3 n = normalize(normal);
    fragPosition = position.xyz;
    fragColor =  frontColor;
    fragNormal = n.xy;
}
```

[Next](teapot.h.md)[Previous](renderer.h.md)

