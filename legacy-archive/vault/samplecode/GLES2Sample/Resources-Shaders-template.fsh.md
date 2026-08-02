---
title: GLES2Sample
apple_id: DTS40009188
resource_type: Sample Code
platform: iOS
topic: Graphics & Animation
technology: OpenGLES
published: '2010-07-07'
source_url: https://developer.apple.com/library/archive/samplecode/GLES2Sample/Listings/Resources_Shaders_template_fsh.html
archived_at: '2026-07-18T03:10:00.990436Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [GLES2Sample](GLES2Sample.md)


[Next](Resources-Shaders-template.vsh.md)[Previous](Classes-Shaders.m.md)

# Resources/Shaders/template.fsh

```
#ifdef GL_ES
// define default precision for float, vec, mat.
precision highp float;
#endif

varying vec4 colorVarying;

void main()
{
    gl_FragColor = colorVarying;
}
```

[Next](Resources-Shaders-template.vsh.md)[Previous](Classes-Shaders.m.md)

