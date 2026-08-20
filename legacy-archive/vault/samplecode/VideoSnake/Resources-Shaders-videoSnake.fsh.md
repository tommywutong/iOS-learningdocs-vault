---
title: VideoSnake
apple_id: DTS40012327
resource_type: Sample Code
platform: iOS
topic: Audio, Video, & Visual Effects
technology: AVFoundation
published: '2016-09-28'
source_url: https://developer.apple.com/library/archive/samplecode/VideoSnake/Listings/Resources_Shaders_videoSnake_fsh.html
archived_at: '2026-07-18T03:27:55.266079Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [VideoSnake](VideoSnake.md)


[Next](ReadMe.txt.md)[Previous](Resources-Shaders-videoSnake.vsh.md)

# Resources/Shaders/videoSnake.fsh

```
/*
 <codex>
 <abstract>Fragment shader.</abstract>
 </codex>
 */

precision mediump float;

varying mediump vec2 coordinate;
uniform sampler2D videoframe;
uniform mediump vec4 backgroundcolor;

void main()
{
    if (coordinate.x >= 0.99 || coordinate.x <= 0.01 ||
        coordinate.y >= 0.99 || coordinate.y <= 0.01)
    {
        gl_FragColor = backgroundcolor;
    }
    else
    {
        gl_FragColor = texture2D(videoframe, coordinate);
    }
}
```

[Next](ReadMe.txt.md)[Previous](Resources-Shaders-videoSnake.vsh.md)

