---
title: SceneKit slides for WWDC 2014
apple_id: TP40014551
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2014-10-16'
source_url: https://developer.apple.com/library/archive/samplecode/SceneKitWWDC2014/Listings/Scene_Kit_Session_WWDC_2014_Resources_Shaders_CustomProgram_fsh.html
archived_at: '2026-07-18T03:23:13.753386Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [SceneKit slides for WWDC 2014](SceneKit%20slides%20for%20WWDC%202014.md)


[Next](Scene%20Kit%20Session%20WWDC%202014-Resources-Shaders-CustomProgram.vsh.md)[Previous](Scene%20Kit%20Session%20WWDC%202014-Resources-Shaders-NodeDelegate.vsh.md)

# Scene Kit Session WWDC 2014/Resources/Shaders/CustomProgram.fsh

```
varying vec2 v_uv;
varying float v_color;

void main(void) {
    const float sinPi4 = 0.7071;

    float feather = 0.3;

    // display a diamond shape
    float fade = pow(abs(v_uv.x) + abs(v_uv.y), feather);

    // rotate the texture coordinates by 45 degrees to add a smaller offset diamond
    vec2 uv45 = vec2(v_uv.x * sinPi4 - v_uv.y * sinPi4,
                    v_uv.y * sinPi4 + v_uv.x * sinPi4);
    fade *= pow(abs(uv45.x) + abs(uv45.y), feather * 0.4);

    float col = v_color * max(1. - fade, 0.);
    gl_FragColor = vec4(col, col, col, col);
}
```

[Next](Scene%20Kit%20Session%20WWDC%202014-Resources-Shaders-CustomProgram.vsh.md)[Previous](Scene%20Kit%20Session%20WWDC%202014-Resources-Shaders-NodeDelegate.vsh.md)

