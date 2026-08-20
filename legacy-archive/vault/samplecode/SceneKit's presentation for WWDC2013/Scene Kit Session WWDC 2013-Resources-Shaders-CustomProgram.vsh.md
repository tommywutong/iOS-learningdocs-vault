---
title: SceneKit's presentation for WWDC2013
apple_id: DTS40013423
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: SceneKit
published: '2014-01-07'
source_url: https://developer.apple.com/library/archive/samplecode/SceneKit_Slides_WWDC2013/Listings/Scene_Kit_Session_WWDC_2013_Resources_Shaders_CustomProgram_vsh.html
archived_at: '2026-07-18T03:23:19.608749Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [SceneKit's presentation for WWDC2013](Scene%20Kit%27s%20presentation%20for%20WWDC2013.md)


[Next](Scene%20Kit%20Session%20WWDC%202013-Resources-Shaders-NodeDelegate.fsh.md)[Previous](Scene%20Kit%20Session%20WWDC%202013-Resources-Shaders-CustomProgram.fsh.md)

# Scene Kit Session WWDC 2013/Resources/Shaders/CustomProgram.vsh

```
attribute vec4 a_srcPos;   // source position in the geometry
attribute vec4 a_dstPos;   // destination position in the geometry
attribute vec2 a_texcoord; // texture coordinates in the geometry

uniform mat4 u_mv;    // ModelView transform
uniform mat4 u_proj;  // Projection transform
uniform float factor; // morph factor
uniform float time;

varying vec2 v_uv;     // sprite texture coordinates
varying float v_color; // sprite color

void main()
{
    // Billboard sprite scale
    float scale = 0.4;

    // Billboard sprite angular speed
    float angularSpeed = 5.0;

    // Morph the position between the source position (a_vertices) and the
    // destination position (a_normals) based on the "factor" uniform,
    // then transform it in view space.
    vec4 vsPos = u_mv * mix(a_srcPos, a_dstPos, factor);

    // Billboard sprite expansion, based on the texcoord cardinal values
    vsPos.xy += vec2(a_texcoord.x * scale, a_texcoord.y * scale);

    // Project the position
    gl_Position = u_proj * vsPos;

    // Rotate the UVs based on time (and offset based on the source position in the geometry, to avoid aligning all the sprites)
    float angle = angularSpeed * time + (a_srcPos.x + a_srcPos.y);
    float sn = sin(angle);
    float cs = cos(angle);
    v_uv = vec2( a_texcoord.x * cs - a_texcoord.y * sn, a_texcoord.y * cs + a_texcoord.x * sn);

    // Colorize the sprite based on the source position in the geometry
    v_color = pow(1. - abs(a_srcPos.y) / 7., 1.5);
}
```

[Next](Scene%20Kit%20Session%20WWDC%202013-Resources-Shaders-NodeDelegate.fsh.md)[Previous](Scene%20Kit%20Session%20WWDC%202013-Resources-Shaders-CustomProgram.fsh.md)

