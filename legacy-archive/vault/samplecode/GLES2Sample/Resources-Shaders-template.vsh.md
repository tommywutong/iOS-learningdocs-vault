---
title: GLES2Sample
apple_id: DTS40009188
resource_type: Sample Code
platform: iOS
topic: Graphics & Animation
technology: OpenGLES
published: '2010-07-07'
source_url: https://developer.apple.com/library/archive/samplecode/GLES2Sample/Listings/Resources_Shaders_template_vsh.html
archived_at: '2026-07-18T03:10:01.099815Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [GLES2Sample](GLES2Sample.md)


[Next](Document%20Revision%20History.md)[Previous](Resources-Shaders-template.fsh.md)

# Resources/Shaders/template.vsh

```
attribute vec4 position;
attribute vec4 color;

uniform mat4 modelViewProjectionMatrix;

varying vec4 colorVarying;

void main()
{
    gl_Position = modelViewProjectionMatrix * position;
    colorVarying = color;
}
```

[Next](Document%20Revision%20History.md)[Previous](Resources-Shaders-template.fsh.md)

