---
title: ConditionalRendering
apple_id: DTS40010087
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenGL
published: '2014-06-17'
source_url: https://developer.apple.com/library/archive/samplecode/ConditionalRendering/Listings/color_vs.html
archived_at: '2026-07-18T03:04:14.438064Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [ConditionalRendering](ConditionalRendering.md)


[Next](ConditionalRender.fs.md)[Previous](color.fs.md)

# color.vs

```
#version 150

in vec4 inVertex;
out vec4 color;

uniform mat4 MVP;
uniform vec4 constantColor;

void main()
{
    gl_Position = MVP * inVertex;
    color = constantColor;
}
```

[Next](ConditionalRender.fs.md)[Previous](color.fs.md)

