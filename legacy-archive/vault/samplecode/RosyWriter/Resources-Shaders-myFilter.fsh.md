---
title: RosyWriter
apple_id: DTS40011110
resource_type: Sample Code
platform: iOS
topic: Audio, Video, & Visual Effects
technology: AVFoundation
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/RosyWriter/Listings/Resources_Shaders_myFilter_fsh.html
archived_at: '2026-07-18T03:22:22.050249Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [RosyWriter](RosyWriter.md)


[Next](ReadMe.txt.md)[Previous](Resources-Shaders-myFilter.vsh.md)

# Resources/Shaders/myFilter.fsh

```

precision mediump float;

varying mediump vec2 coordinate;
uniform sampler2D videoframe;

void main()
{
    vec4 color = texture2D(videoframe, coordinate);
    gl_FragColor.bgra = vec4(color.b, 0.0 * color.g, color.r, color.a);
}
```

[Next](ReadMe.txt.md)[Previous](Resources-Shaders-myFilter.vsh.md)

