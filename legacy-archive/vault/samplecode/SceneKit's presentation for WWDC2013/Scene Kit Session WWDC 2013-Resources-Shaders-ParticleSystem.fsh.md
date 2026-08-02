---
title: SceneKit's presentation for WWDC2013
apple_id: DTS40013423
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: SceneKit
published: '2014-01-07'
source_url: https://developer.apple.com/library/archive/samplecode/SceneKit_Slides_WWDC2013/Listings/Scene_Kit_Session_WWDC_2013_Resources_Shaders_ParticleSystem_fsh.html
archived_at: '2026-07-18T03:23:19.741769Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [SceneKit's presentation for WWDC2013](Scene%20Kit%27s%20presentation%20for%20WWDC2013.md)


[Next](Scene%20Kit%20Session%20WWDC%202013-Resources-Shaders-ParticleSystem.vsh.md)[Previous](Scene%20Kit%20Session%20WWDC%202013-Resources-Shaders-NodeDelegate.vsh.md)

# Scene Kit Session WWDC 2013/Resources/Shaders/ParticleSystem.fsh

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

[Next](Scene%20Kit%20Session%20WWDC%202013-Resources-Shaders-ParticleSystem.vsh.md)[Previous](Scene%20Kit%20Session%20WWDC%202013-Resources-Shaders-NodeDelegate.vsh.md)

