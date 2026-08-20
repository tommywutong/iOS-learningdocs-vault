---
title: VideoSnake
apple_id: DTS40012327
resource_type: Sample Code
platform: iOS
topic: Audio, Video, & Visual Effects
technology: AVFoundation
published: '2016-09-28'
source_url: https://developer.apple.com/library/archive/samplecode/VideoSnake/Listings/Resources_Shaders_videoSnake_vsh.html
archived_at: '2026-07-18T03:27:55.310993Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [VideoSnake](VideoSnake.md)


[Next](Resources-Shaders-videoSnake.fsh.md)[Previous](Classes-matrix.c.md)

# Resources/Shaders/videoSnake.vsh

```
/*
 <codex>
 <abstract>Vertex shader.</abstract>
 </codex>
 */

attribute vec4 position;
attribute mediump vec4 texturecoordinate;

uniform mat4 amodelview;
uniform mat4 aprojection;

varying mediump vec2 coordinate;

void main()
{
    gl_Position = aprojection * amodelview * position;
    coordinate = texturecoordinate.xy;
}
```

[Next](Resources-Shaders-videoSnake.fsh.md)[Previous](Classes-matrix.c.md)

