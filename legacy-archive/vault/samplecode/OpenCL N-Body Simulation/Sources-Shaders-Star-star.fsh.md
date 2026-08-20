---
title: OpenCL N-Body Simulation
apple_id: TP40016610
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenCL
published: '2015-12-10'
source_url: https://developer.apple.com/library/archive/samplecode/OpenCL_NBody_Simulation/Listings/Sources_Shaders_Star_star_fsh.html
archived_at: '2026-07-18T03:17:43.701269Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [OpenCL N-Body Simulation](OpenCL%20N-Body%20Simulation.md)


[Next](Sources-Shaders-Star-star.vsh.md)[Previous](Sources-Other-main.m.md)

# Sources/Shaders/Star/star.fsh

```
/*
 <codex>
 <abstract>
 Fragment shader for stars.
 </abstract>
 </codex>
 */

void main()
{
    float d = distance(vec2(0.5, 0.5), gl_TexCoord[0].st);
    float s = clamp(1.0 - 2.0 * d, 0.0, 1.0);
    float t = cos(0.5 * 3.1415 * s);
    float c = 1.0 - pow(t, 0.25);

    gl_FragColor = vec4(c, c, c, 1.0) * gl_Color;
}
```

[Next](Sources-Shaders-Star-star.vsh.md)[Previous](Sources-Other-main.m.md)

