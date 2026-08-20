---
title: SceneKit slides for WWDC 2014
apple_id: TP40014551
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2014-10-16'
source_url: https://developer.apple.com/library/archive/samplecode/SceneKitWWDC2014/Listings/Scene_Kit_Session_WWDC_2014_Resources_Shaders_ParticleSystem_vsh.html
archived_at: '2026-07-18T03:23:13.929662Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [SceneKit slides for WWDC 2014](SceneKit%20slides%20for%20WWDC%202014.md)


[Next](Scene%20Kit%20Session%20WWDC%202014-Resources-Shaders-NodeDelegate.vsh.md)[Previous](Scene%20Kit%20Session%20WWDC%202014-Resources-Shaders-SceneDelegate.vsh.md)

# Scene Kit Session WWDC 2014/Resources/Shaders/ParticleSystem.vsh

```
#version 120

attribute vec4 a_position;
attribute vec3 a_velocity;
attribute vec2 a_angleAndLife;

uniform mat4 u_mv;

varying vec3 v_params; // angle, scale, life
varying vec4 v_position;
varying vec3 v_velocity;

void main()
{
    gl_Position = u_mv * vec4(a_position.xyz, 1.0);
    v_params = vec3(a_angleAndLife.x, a_position.w, a_angleAndLife.y);
    v_velocity = mat3(u_mv) * a_velocity;
}
```

[Next](Scene%20Kit%20Session%20WWDC%202014-Resources-Shaders-NodeDelegate.vsh.md)[Previous](Scene%20Kit%20Session%20WWDC%202014-Resources-Shaders-SceneDelegate.vsh.md)

