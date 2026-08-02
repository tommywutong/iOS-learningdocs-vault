---
title: SceneKit slides for WWDC 2014
apple_id: TP40014551
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2014-10-16'
source_url: https://developer.apple.com/library/archive/samplecode/SceneKitWWDC2014/Listings/Scene_Kit_Session_WWDC_2014_Resources_Shaders_NodeDelegate_vsh.html
archived_at: '2026-07-18T03:23:13.860739Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [SceneKit slides for WWDC 2014](SceneKit%20slides%20for%20WWDC%202014.md)


[Next](Scene%20Kit%20Session%20WWDC%202014-Resources-Shaders-CustomProgram.fsh.md)[Previous](Scene%20Kit%20Session%20WWDC%202014-Resources-Shaders-ParticleSystem.vsh.md)

# Scene Kit Session WWDC 2014/Resources/Shaders/NodeDelegate.vsh

```
attribute vec4 a_position;
attribute vec2 a_angleAndLife;

uniform mat4 u_mvp;

varying vec2 v_angleAndLife;

void main() {
    gl_Position = u_mvp * a_position;
    v_angleAndLife = a_angleAndLife;
}
```

[Next](Scene%20Kit%20Session%20WWDC%202014-Resources-Shaders-CustomProgram.fsh.md)[Previous](Scene%20Kit%20Session%20WWDC%202014-Resources-Shaders-ParticleSystem.vsh.md)

