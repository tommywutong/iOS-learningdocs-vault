---
title: SceneKit's presentation for WWDC2013
apple_id: DTS40013423
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: SceneKit
published: '2014-01-07'
source_url: https://developer.apple.com/library/archive/samplecode/SceneKit_Slides_WWDC2013/Listings/Scene_Kit_Session_WWDC_2013_Resources_Shaders_NodeDelegate_vsh.html
archived_at: '2026-07-18T03:23:19.693049Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [SceneKit's presentation for WWDC2013](Scene%20Kit%27s%20presentation%20for%20WWDC2013.md)


[Next](Scene%20Kit%20Session%20WWDC%202013-Resources-Shaders-ParticleSystem.fsh.md)[Previous](Scene%20Kit%20Session%20WWDC%202013-Resources-Shaders-NodeDelegate.fsh.md)

# Scene Kit Session WWDC 2013/Resources/Shaders/NodeDelegate.vsh

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

[Next](Scene%20Kit%20Session%20WWDC%202013-Resources-Shaders-ParticleSystem.fsh.md)[Previous](Scene%20Kit%20Session%20WWDC%202013-Resources-Shaders-NodeDelegate.fsh.md)

