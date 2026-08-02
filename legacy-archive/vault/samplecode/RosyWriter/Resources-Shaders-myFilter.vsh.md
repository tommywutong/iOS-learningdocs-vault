---
title: RosyWriter
apple_id: DTS40011110
resource_type: Sample Code
platform: iOS
topic: Audio, Video, & Visual Effects
technology: AVFoundation
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/RosyWriter/Listings/Resources_Shaders_myFilter_vsh.html
archived_at: '2026-07-18T03:22:22.097755Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [RosyWriter](RosyWriter.md)


[Next](Resources-Shaders-myFilter.fsh.md)[Previous](Classes-RosyWriterCapturePipeline.m.md)

# Resources/Shaders/myFilter.vsh

```

attribute vec4 position;
attribute mediump vec4 texturecoordinate;
varying mediump vec2 coordinate;

void main()
{
    gl_Position = position;
    coordinate = texturecoordinate.xy;
}
```

[Next](Resources-Shaders-myFilter.fsh.md)[Previous](Classes-RosyWriterCapturePipeline.m.md)

