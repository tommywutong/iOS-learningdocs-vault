---
title: DeferredShading
apple_id: DTS40010088
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2015-07-08'
source_url: https://developer.apple.com/library/archive/samplecode/DeferredShading/Listings/passthrough_vs.html
archived_at: '2026-07-18T03:06:12.244692Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [DeferredShading](DeferredShading.md)


[Next](matrixUtil.h.md)[Previous](matrixUtil.c.md)

# passthrough.vs

```
/*
 Copyright (C) 2015 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 The application delegate.
 */

#version 150

in vec4 inPosition;
in vec3 inTexcoord;

out vec3 texCoord;

void main()
{
    gl_Position = inPosition;
    texCoord = inTexcoord;
}
```

[Next](matrixUtil.h.md)[Previous](matrixUtil.c.md)

