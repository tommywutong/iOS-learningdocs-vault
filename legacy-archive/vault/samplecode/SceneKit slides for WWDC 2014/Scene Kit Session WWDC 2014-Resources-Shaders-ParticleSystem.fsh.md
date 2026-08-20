---
title: SceneKit slides for WWDC 2014
apple_id: TP40014551
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2014-10-16'
source_url: https://developer.apple.com/library/archive/samplecode/SceneKitWWDC2014/Listings/Scene_Kit_Session_WWDC_2014_Resources_Shaders_ParticleSystem_fsh.html
archived_at: '2026-07-18T03:23:13.887313Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [SceneKit slides for WWDC 2014](SceneKit%20slides%20for%20WWDC%202014.md)


[Next](Scene%20Kit%20Session%20WWDC%202014-Resources-Shaders-NodeDelegate.fsh.md)[Previous](Scene%20Kit%20Session%20WWDC%202014-Resources-Shaders-SceneDelegate.fsh.md)

# Scene Kit Session WWDC 2014/Resources/Shaders/ParticleSystem.fsh

```
uniform sampler2D u_tex;
uniform sampler2D u_ramp;

varying vec3 v_uv;

void main(void) {
    vec4 tex = texture2D(u_tex, v_uv.xy);
    vec4 col = texture2D(u_ramp, v_uv.zx);
    gl_FragColor = tex * col;
}
```

[Next](Scene%20Kit%20Session%20WWDC%202014-Resources-Shaders-NodeDelegate.fsh.md)[Previous](Scene%20Kit%20Session%20WWDC%202014-Resources-Shaders-SceneDelegate.fsh.md)

