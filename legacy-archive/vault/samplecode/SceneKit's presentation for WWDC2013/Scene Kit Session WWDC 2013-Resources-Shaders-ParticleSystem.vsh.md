---
title: SceneKit's presentation for WWDC2013
apple_id: DTS40013423
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: SceneKit
published: '2014-01-07'
source_url: https://developer.apple.com/library/archive/samplecode/SceneKit_Slides_WWDC2013/Listings/Scene_Kit_Session_WWDC_2013_Resources_Shaders_ParticleSystem_vsh.html
archived_at: '2026-07-18T03:23:19.780156Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [SceneKit's presentation for WWDC2013](Scene%20Kit%27s%20presentation%20for%20WWDC2013.md)


[Next](Scene%20Kit%20Session%20WWDC%202013-Resources-Shaders-SceneDelegate.fsh.md)[Previous](Scene%20Kit%20Session%20WWDC%202013-Resources-Shaders-ParticleSystem.fsh.md)

# Scene Kit Session WWDC 2013/Resources/Shaders/ParticleSystem.vsh

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

[Next](Scene%20Kit%20Session%20WWDC%202013-Resources-Shaders-SceneDelegate.fsh.md)[Previous](Scene%20Kit%20Session%20WWDC%202013-Resources-Shaders-ParticleSystem.fsh.md)

